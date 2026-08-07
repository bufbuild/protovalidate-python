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

#include "google/protobuf/descriptor.h"
#include "google/protobuf/message.h"

namespace buf::validate::internal {

struct MessageFactory {
 public:
  MessageFactory(
      google::protobuf::MessageFactory* messageFactory,
      const google::protobuf::DescriptorPool* descriptorPool)
      : messageFactory_(messageFactory), descriptorPool_(descriptorPool) {}

  google::protobuf::MessageFactory* messageFactory() { return messageFactory_; }

  const google::protobuf::DescriptorPool* descriptorPool() { return descriptorPool_; }

 private:
  google::protobuf::MessageFactory* messageFactory_;
  const google::protobuf::DescriptorPool* descriptorPool_;
};

bool Reparse(
    MessageFactory& messageFactory,
    const google::protobuf::Message& from,
    google::protobuf::Message* to);

} // namespace buf::validate::internal
