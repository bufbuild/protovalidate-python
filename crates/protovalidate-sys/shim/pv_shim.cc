// Copyright (c) 2023-2026 Buf Technologies, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include "pv_shim.h"

#include <cstdlib>
#include <cstring>
#include <memory>
#include <string>
#include <utility>

#include "absl/status/status.h"
#include "absl/strings/str_cat.h"
#include "absl/strings/string_view.h"
#include "absl/status/statusor.h"
#include "buf/validate/validator.h"
#include "google/protobuf/arena.h"
#include "google/protobuf/descriptor.h"
#include "google/protobuf/descriptor.pb.h"
#include "google/protobuf/dynamic_message.h"
#include "google/protobuf/message.h"

namespace {

// Collects BuildFile errors so they reach the caller instead of being logged.
// Without one, protobuf writes descriptor errors to ABSL_LOG(ERROR) and
// BuildFile just returns null, which makes bad descriptors hard to diagnose
// from Python.
class StringErrorCollector : public google::protobuf::DescriptorPool::ErrorCollector {
 public:
  void RecordError(absl::string_view filename, absl::string_view element_name,
                   const google::protobuf::Message* descriptor,
                   ErrorLocation location, absl::string_view message) override {
    if (!text_.empty()) text_ += "; ";
    absl::StrAppend(&text_, filename, ": ", element_name, ": ", message);
  }

  const std::string& text() const { return text_; }

 private:
  std::string text_;
};

char* CopyCString(const std::string& value) {
  char* out = static_cast<char*>(std::malloc(value.size() + 1));
  if (out == nullptr) return nullptr;
  std::memcpy(out, value.data(), value.size() + 1);
  return out;
}

void SetError(char** error, const std::string& message) {
  if (error != nullptr) *error = CopyCString(message);
}

// Mirrors the mapping protovalidate-cc's own conformance runner uses, in
// buf/validate/conformance/runner.cc: InvalidArgument means a rule failed while
// being evaluated, FailedPrecondition means it could not be compiled. Having
// these the wrong way round makes conformance report compilation errors where
// it expects runtime errors.
int ClassifyStatus(const absl::Status& status) {
  switch (status.code()) {
    case absl::StatusCode::kInvalidArgument:
      return PV_ERR_RUNTIME;
    case absl::StatusCode::kFailedPrecondition:
      return PV_ERR_COMPILATION;
    default:
      return PV_ERR_UNEXPECTED;
  }
}

}  // namespace

// The pool is an overlay on the descriptors compiled into this extension
// (well-known types plus buf.validate), so the rule extensions protovalidate-cc
// reads always match the C++ types it was built against, and user files are
// only consulted for names the underlay does not define.
//
// Files are added with BuildFile rather than by feeding a DescriptorDatabase.
// A database-backed pool would be the more usual choice, but protobuf requires
// that such a database not be mutated during the pool's lifetime -- "changes to
// the content of the DescriptorDatabase may not be reflected in subsequent
// lookups" -- and this engine learns about descriptors incrementally, as Python
// encounters new message types. BuildFile on an overlay pool is the supported
// way to add files after construction; it is what python-protobuf's own
// DescriptorPool.Add does.
//
// The consequence for callers: a file's imports must be added before the file
// itself, since BuildFile resolves dependencies eagerly.
struct pv_engine {
  pv_engine()
      : pool(google::protobuf::DescriptorPool::generated_pool()),
        message_factory(&pool) {}

  google::protobuf::DescriptorPool pool;
  google::protobuf::DynamicMessageFactory message_factory;
  std::unique_ptr<buf::validate::ValidatorFactory> validator_factory;
};

extern "C" {

pv_engine* pv_engine_new(char** error) {
  auto engine = std::make_unique<pv_engine>();
  auto factory = buf::validate::ValidatorFactory::New();
  if (!factory.ok()) {
    SetError(error, std::string(factory.status().message()));
    return nullptr;
  }
  engine->validator_factory = std::move(*factory);
  engine->validator_factory->SetMessageFactory(&engine->message_factory,
                                               &engine->pool);
  return engine.release();
}

void pv_engine_free(pv_engine* engine) { delete engine; }

int pv_engine_add_file(pv_engine* engine, const uint8_t* file_descriptor_proto,
                       size_t len, char** error) {
  google::protobuf::FileDescriptorProto proto;
  if (!proto.ParseFromArray(file_descriptor_proto, static_cast<int>(len))) {
    SetError(error, "could not parse FileDescriptorProto");
    return PV_ERR_ARGUMENT;
  }
  // Already known, either from the linked-in descriptors or a previous add.
  // Callers may re-send descriptors without tracking what we have seen.
  if (engine->pool.FindFileByName(proto.name()) != nullptr) return PV_OK;

  StringErrorCollector collector;
  if (engine->pool.BuildFileCollectingErrors(proto, &collector) == nullptr) {
    std::string message = "could not add " + proto.name() + " to descriptor pool";
    if (!collector.text().empty()) message += ": " + collector.text();
    SetError(error, message);
    return PV_ERR_ARGUMENT;
  }
  return PV_OK;
}

int pv_engine_validate(pv_engine* engine, const char* type_name,
                       size_t type_name_len, const uint8_t* payload,
                       size_t payload_len, int fail_fast, uint8_t** out,
                       size_t* out_len, char** error) {
  absl::string_view name(type_name, type_name_len);
  const google::protobuf::Descriptor* descriptor =
      engine->pool.FindMessageTypeByName(name);
  if (descriptor == nullptr) {
    SetError(error, absl::StrCat("unknown message type: ", name));
    return PV_ERR_ARGUMENT;
  }

  google::protobuf::Arena arena;
  google::protobuf::Message* message =
      engine->message_factory.GetPrototype(descriptor)->New(&arena);
  if (!message->ParseFromArray(payload, static_cast<int>(payload_len))) {
    SetError(error, absl::StrCat("could not parse payload as ", name));
    return PV_ERR_ARGUMENT;
  }

  auto validator =
      engine->validator_factory->NewValidator(&arena, fail_fast != 0);
  auto result = validator.Validate(*message);
  if (!result.ok()) {
    SetError(error, std::string(result.status().message()));
    return ClassifyStatus(result.status());
  }

  // Serialized straight into the output buffer; the +1 keeps the allocation
  // nonzero (and the pointer meaningful) when there are no violations.
  size_t size = result->proto().ByteSizeLong();
  uint8_t* buffer = static_cast<uint8_t*>(std::malloc(size + 1));
  if (buffer == nullptr) {
    SetError(error, "out of memory");
    return PV_ERR_RUNTIME;
  }
  if (!result->proto().SerializeToArray(buffer, static_cast<int>(size))) {
    std::free(buffer);
    SetError(error, "could not serialize violations");
    return PV_ERR_RUNTIME;
  }
  *out = buffer;
  *out_len = size;
  return PV_OK;
}

void pv_free(void* ptr) { std::free(ptr); }

}  // extern "C"
