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

#include "buf/validate/conformance/harness/harness.pb.h"
#include "buf/validate/validator.h"
#include "google/protobuf/dynamic_message.h"

namespace buf::validate::conformance {

class TestRunner {
 public:
  explicit TestRunner(
      const google::protobuf::DescriptorPool* descriptorPool =
          google::protobuf::DescriptorPool::generated_pool())
      : descriptorPool_(descriptorPool), validatorFactory_(ValidatorFactory::New().value()) {
    validatorFactory_->SetMessageFactory(&messageFactory_, descriptorPool_);
    validatorFactory_->SetAllowUnknownFields(false);
  }

  harness::TestConformanceResponse runTest(const harness::TestConformanceRequest& request);
  harness::TestResult runTestCase(
      const google::protobuf::Descriptor* desc, const google::protobuf::Any& dyn);
  harness::TestResult runTestCase(const google::protobuf::Message& message);

 private:
  google::protobuf::DynamicMessageFactory messageFactory_;
  const google::protobuf::DescriptorPool* descriptorPool_;
  std::unique_ptr<ValidatorFactory> validatorFactory_;
  google::protobuf::Arena arena_;
};

} // namespace buf::validate::conformance