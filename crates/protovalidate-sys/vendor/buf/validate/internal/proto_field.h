// Copyright 2023-2026 Buf Technologies, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#pragma once

#include <string_view>

#include "absl/status/status.h"
#include "buf/validate/validate.pb.h"
#include "google/protobuf/arena.h"
#include "google/protobuf/message.h"

namespace buf::validate::internal {

/// ProtoField represents a field value. This may be a scalar field on a message, a repeated or map
/// field on a message, or an item within a repeated or map field on a message.
class ProtoField {
 public:
  /// Constructs a new ProtoField representing the field specified by descriptor under the provided
  /// message. The provided descriptor should be contained by the provided message, although the
  /// field need not be present. If the field is a repeated or map field, index may be specified to
  /// point to a specific index; otherwise, the sentinel value -1 (default) should be provided.
  ProtoField(
      const google::protobuf::Message* message,
      const google::protobuf::FieldDescriptor* descriptor,
      int index = -1)
      : message_{message}, descriptor_{descriptor}, index_{index} {}

  [[nodiscard]] const google::protobuf::Message* message() const { return message_; }

  [[nodiscard]] const google::protobuf::FieldDescriptor* descriptor() const { return descriptor_; }

  [[nodiscard]] int index() const { return index_; }

  /// Returns true if this ProtoField instance refers to a repeated or map field, rather than a
  /// singular value.
  [[nodiscard]] bool is_repeated() const { return descriptor_->is_repeated() && index_ == -1; }

  /// If this ProtoField references a repeated field, returns the number of items in the repeated
  /// field. Otherwise, always returns zero.
  [[nodiscard]] int size() const {
    if (!is_repeated()) {
      return 0;
    }
    return message_->GetReflection()->FieldSize(*message_, descriptor_);
  }

  /// If this ProtoField references a repeated field, and the provided index is a valid index into
  /// this repeated field, returns a ProtoField referencing the specific item at the provided index.
  [[nodiscard]] absl::optional<ProtoField> at(int index) const {
    if (index < 0 || !is_repeated() ||
        index >= message_->GetReflection()->FieldSize(*message_, descriptor_)) {
      return absl::nullopt;
    }
    return ProtoField{message_, descriptor_, index};
  }

  using Value = absl::variant<
      absl::monostate,
      int64_t,
      uint64_t,
      double,
      bool,
      std::string,
      const google::protobuf::Message*>;

  /// Returns a variant representing the value of this ProtoField, if this field references a
  /// singular value. If is_repeated() returns true, you must instead call at(...) to get a specific
  /// item within the repeated field or map; this method will return the monostate value otherwise.
  [[nodiscard]] Value variant() const {
    if (is_repeated()) {
      return absl::monostate{};
    }
    if (!descriptor_->is_repeated() &&
        !message_->GetReflection()->HasField(*message_, descriptor_)) {
      return absl::monostate{};
    }
    switch (descriptor_->cpp_type()) {
      case google::protobuf::FieldDescriptor::CPPTYPE_INT32:
        if (index_ != -1) {
          return static_cast<int64_t>(
              message_->GetReflection()->GetRepeatedInt32(*message_, descriptor_, index_));
        }
        return static_cast<int64_t>(message_->GetReflection()->GetInt32(*message_, descriptor_));
      case google::protobuf::FieldDescriptor::CPPTYPE_INT64:
        if (index_ != -1) {
          return message_->GetReflection()->GetRepeatedInt64(*message_, descriptor_, index_);
        }
        return message_->GetReflection()->GetInt64(*message_, descriptor_);
      case google::protobuf::FieldDescriptor::CPPTYPE_ENUM:
        if (index_ != -1) {
          return static_cast<int64_t>(
              message_->GetReflection()->GetRepeatedEnumValue(*message_, descriptor_, index_));
        }
        return static_cast<int64_t>(
            message_->GetReflection()->GetEnumValue(*message_, descriptor_));
      case google::protobuf::FieldDescriptor::CPPTYPE_UINT32:
        if (index_ != -1) {
          return static_cast<uint64_t>(
              message_->GetReflection()->GetRepeatedUInt32(*message_, descriptor_, index_));
        }
        return static_cast<uint64_t>(message_->GetReflection()->GetUInt32(*message_, descriptor_));
      case google::protobuf::FieldDescriptor::CPPTYPE_UINT64:
        if (index_ != -1) {
          return message_->GetReflection()->GetRepeatedUInt64(*message_, descriptor_, index_);
        }
        return message_->GetReflection()->GetUInt64(*message_, descriptor_);
      case google::protobuf::FieldDescriptor::CPPTYPE_FLOAT:
        if (index_ != -1) {
          return static_cast<double>(
              message_->GetReflection()->GetRepeatedFloat(*message_, descriptor_, index_));
        }
        return static_cast<double>(message_->GetReflection()->GetFloat(*message_, descriptor_));
      case google::protobuf::FieldDescriptor::CPPTYPE_DOUBLE:
        if (index_ != -1) {
          return message_->GetReflection()->GetRepeatedDouble(*message_, descriptor_, index_);
        }
        return message_->GetReflection()->GetDouble(*message_, descriptor_);
      case google::protobuf::FieldDescriptor::CPPTYPE_BOOL:
        if (index_ != -1) {
          return message_->GetReflection()->GetRepeatedBool(*message_, descriptor_, index_);
        }
        return message_->GetReflection()->GetBool(*message_, descriptor_);
      case google::protobuf::FieldDescriptor::CPPTYPE_STRING:
        if (index_ != -1) {
          return message_->GetReflection()->GetRepeatedString(*message_, descriptor_, index_);
        }
        return message_->GetReflection()->GetString(*message_, descriptor_);
      case google::protobuf::FieldDescriptor::CPPTYPE_MESSAGE:
        if (index_ != -1) {
          return &message_->GetReflection()->GetRepeatedMessage(*message_, descriptor_, index_);
        }
        return &message_->GetReflection()->GetMessage(*message_, descriptor_);
    }
    return absl::monostate{};
  }

 private:
  const google::protobuf::Message* message_;
  const google::protobuf::FieldDescriptor* descriptor_;
  int index_;
};

} // namespace buf::validate::internal
