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

#include "absl/status/statusor.h"
#include "buf/validate/internal/message_factory.h"
#include "buf/validate/internal/rules.h"
#include "buf/validate/validate.pb.h"
#include "eval/public/cel_expression.h"
#include "google/protobuf/arena.h"
#include "google/protobuf/descriptor.h"

namespace buf::validate::internal {

using Rules = absl::StatusOr<std::vector<std::unique_ptr<ValidationRules>>>;

Rules NewMessageRules(
    std::unique_ptr<MessageFactory>& messageFactory,
    bool allowUnknownFields,
    google::protobuf::Arena* arena,
    google::api::expr::runtime::CelExpressionBuilder& builder,
    const google::protobuf::Descriptor* descriptor);

absl::StatusOr<std::unique_ptr<MessageValidationRules>> BuildMessageRules(
    google::api::expr::runtime::CelExpressionBuilder& builder, const MessageRules& rules);

} // namespace buf::validate::internal