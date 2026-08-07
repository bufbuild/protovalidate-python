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

#include "buf/validate/internal/rules.h"

#include "absl/status/statusor.h"
#include "buf/validate/internal/extra_func.h"
#include "eval/public/builtin_func_registrar.h"
#include "eval/public/cel_expr_builder_factory.h"
#include "eval/public/cel_value.h"
#include "eval/public/containers/field_access.h"
#include "eval/public/containers/field_backed_list_impl.h"
#include "eval/public/containers/field_backed_map_impl.h"
#include "eval/public/string_extension_func_registrar.h"
#include "eval/public/structs/cel_proto_wrapper.h"
#include "google/protobuf/dynamic_message.h"
#include "google/protobuf/util/message_differencer.h"

namespace buf::validate::internal {
namespace cel = google::api::expr;
namespace {

bool isEmptyItem(cel::runtime::CelValue item) {
  switch (item.type()) {
    case ::cel::Kind::kBool:
      return !item.BoolOrDie();
    case ::cel::Kind::kInt:
      return item.Int64OrDie() == 0;
    case ::cel::Kind::kUint:
      return item.Uint64OrDie() == 0;
    case ::cel::Kind::kDouble:
      return item.DoubleOrDie() == 0;
    case ::cel::Kind::kString:
      return item.StringOrDie().value().empty();
    case ::cel::Kind::kBytes:
      return item.BytesOrDie().value().empty();
    default:
      return false;
  }
}

} // namespace

absl::StatusOr<std::unique_ptr<google::api::expr::runtime::CelExpressionBuilder>> NewRuleBuilder(
    google::protobuf::Arena* arena) {
  cel::runtime::InterpreterOptions options;
  options.enable_qualified_type_identifiers = true;
  options.enable_timestamp_duration_overflow_errors = true;
  options.enable_heterogeneous_equality = true;
  options.enable_empty_wrapper_null_unboxing = true;
  options.enable_regex_precompilation = true;
  options.constant_folding = true;
  options.constant_arena = arena;

  std::unique_ptr<cel::runtime::CelExpressionBuilder> builder =
      cel::runtime::CreateCelExpressionBuilder(options);
  auto register_status = cel::runtime::RegisterBuiltinFunctions(builder->GetRegistry(), options);
  if (!register_status.ok()) {
    return register_status;
  }
  register_status = cel::runtime::RegisterStringExtensionFunctions(builder->GetRegistry());
  if (!register_status.ok()) {
    return register_status;
  }
  register_status = RegisterExtraFuncs(*builder->GetRegistry(), arena);
  if (!register_status.ok()) {
    return register_status;
  }
  return builder;
}

absl::Status MessageValidationRules::Validate(
    RuleContext& ctx, const google::protobuf::Message& message) const {
  google::api::expr::runtime::Activation activation;
  activation.InsertValue("this", cel::runtime::CelProtoWrapper::CreateMessage(&message, ctx.arena));
  return ValidateCel(ctx, activation);
}

absl::Status FieldValidationRules::Validate(
    RuleContext& ctx, const google::protobuf::Message& message) const {
  static const google::protobuf::FieldDescriptor* requiredField =
      FieldRules::descriptor()->FindFieldByNumber(FieldRules::kRequiredFieldNumber);
  google::api::expr::runtime::Activation activation;
  cel::runtime::CelValue result;
  std::string subPath;
  if (field_->is_map()) {
    result = cel::runtime::CelValue::CreateMap(
        google::protobuf::Arena::Create<cel::runtime::FieldBackedMapImpl>(
            ctx.arena, &message, field_, ctx.arena));
    if (result.MapOrDie()->size() == 0) {
      if (ignoreEmpty_) {
        return absl::OkStatus();
      } else if (required_) {
        Violation violation;
        *violation.mutable_rule_id() = "required";
        *violation.mutable_message() = "value is required";
        *violation.mutable_field()->mutable_elements()->Add() = fieldPathElement(field_);
        *violation.mutable_rule()->mutable_elements()->Add() =
            staticFieldPathElement<FieldRules, FieldRules::kRequiredFieldNumber>();
        ctx.violations.emplace_back(
            std::move(violation),
            ProtoField{&message, field_},
            ProtoField{&fieldRules_, requiredField});
        return absl::OkStatus();
      }
    }
  } else if (field_->is_repeated()) {
    result = cel::runtime::CelValue::CreateList(
        google::protobuf::Arena::Create<cel::runtime::FieldBackedListImpl>(
            ctx.arena, &message, field_, ctx.arena));
    if (result.ListOrDie()->size() == 0) {
      if (ignoreEmpty_) {
        return absl::OkStatus();
      } else if (required_) {
        Violation violation;
        *violation.mutable_rule_id() = "required";
        *violation.mutable_message() = "value is required";
        *violation.mutable_field()->mutable_elements()->Add() = fieldPathElement(field_);
        *violation.mutable_rule()->mutable_elements()->Add() =
            staticFieldPathElement<FieldRules, FieldRules::kRequiredFieldNumber>();
        ctx.violations.emplace_back(
            std::move(violation),
            ProtoField{&message, field_},
            ProtoField{&fieldRules_, requiredField});
        return absl::OkStatus();
      }
    }
  } else {
    if (!message.GetReflection()->HasField(message, field_)) {
      if (required_) {
        Violation violation;
        *violation.mutable_rule_id() = "required";
        *violation.mutable_message() = "value is required";
        *violation.mutable_field()->mutable_elements()->Add() = fieldPathElement(field_);
        *violation.mutable_rule()->mutable_elements()->Add() =
            staticFieldPathElement<FieldRules, FieldRules::kRequiredFieldNumber>();
        ctx.violations.emplace_back(
            std::move(violation),
            ProtoField{&message, field_},
            ProtoField{&fieldRules_, requiredField});
        return absl::OkStatus();
      } else if (ignoreEmpty_) {
        return absl::OkStatus();
      }
    }

    if (anyRules_ != nullptr &&
        field_->cpp_type() == google::protobuf::FieldDescriptor::CPPTYPE_MESSAGE) {
      const auto& anyMsg = message.GetReflection()->GetMessage(message, field_);
      auto status = ValidateAny(ctx, ProtoField{&message, field_}, anyMsg);
      if (!status.ok()) {
        return status;
      }
    }

    auto status = cel::runtime::CreateValueFromSingleField(&message, field_, ctx.arena, &result);
    if (!status.ok()) {
      return status;
    }

  }
  activation.InsertValue("this", result);
  int pos = ctx.violations.size();
  auto status = ValidateCel(ctx, activation);
  if (!status.ok()) {
    return status;
  }
  if (ctx.violations.size() > pos) {
    auto element = fieldPathElement(field_);
    ctx.appendFieldPathElement(element, pos);
    ctx.setFieldValue(ProtoField{&message, field_}, pos);
  }
  return status;
}

absl::Status EnumValidationRules::Validate(
    RuleContext& ctx, const google::protobuf::Message& message) const {
  static const google::protobuf::FieldDescriptor* definedOnlyField =
      EnumRules::descriptor()->FindFieldByNumber(EnumRules::kDefinedOnlyFieldNumber);
  if (auto status = Base::Validate(ctx, message); ctx.shouldReturn(status)) {
    return status;
  }
  if (definedOnly_) {
    auto value = message.GetReflection()->GetEnumValue(message, field_);
    if (field_->enum_type()->FindValueByNumber(value) == nullptr) {
      Violation violation;
      *violation.mutable_rule_id() = "enum.defined_only";
      *violation.mutable_message() = "value must be one of the defined enum values";
      *violation.mutable_field()->mutable_elements()->Add() = fieldPathElement(field_);
      *violation.mutable_rule()->mutable_elements()->Add() = fieldPathElement(
          EnumRules::descriptor()->FindFieldByNumber(EnumRules::kDefinedOnlyFieldNumber));
      *violation.mutable_rule()->mutable_elements()->Add() = fieldPathElement(
          FieldRules::descriptor()->FindFieldByNumber(FieldRules::kEnumFieldNumber));
      ctx.violations.emplace_back(
          std::move(violation),
          ProtoField{&message, field_},
          ProtoField{&fieldRules_.enum_(), definedOnlyField});
    }
  }
  return absl::OkStatus();
}

absl::Status RepeatedValidationRules::Validate(
    RuleContext& ctx, const google::protobuf::Message& message) const {
  auto status = Base::Validate(ctx, message);
  if (ctx.shouldReturn(status) || itemRules_ == nullptr) {
    return status;
  }
  // Validate each item.
  auto& list = *google::protobuf::Arena::Create<cel::runtime::FieldBackedListImpl>(
      ctx.arena, &message, field_, ctx.arena);
  for (int i = 0; i < list.size(); i++) {
    auto item = list[i];
    if (itemRules_->getIgnoreEmpty() && isEmptyItem(item)) {
      continue;
    }
    cel::runtime::Activation activation;
    activation.InsertValue("this", item);
    int pos = ctx.violations.size();
    status = itemRules_->ValidateCel(ctx, activation);
    if (itemRules_->getAnyRules() != nullptr) {
      const auto& anyMsg = message.GetReflection()->GetRepeatedMessage(message, field_, i);
      status = itemRules_->ValidateAny(ctx, ProtoField{&message, field_, i}, anyMsg);
    }
    if (ctx.violations.size() > pos) {
      FieldPathElement element = fieldPathElement(field_);
      element.set_index(i);
      ctx.appendFieldPathElement(element, pos);
      ctx.appendRulePathElement(
          {
              fieldPathElement(
                  RepeatedRules::descriptor()->FindFieldByNumber(RepeatedRules::kItemsFieldNumber)),
              fieldPathElement(
                  FieldRules::descriptor()->FindFieldByNumber(FieldRules::kRepeatedFieldNumber)),
          },
          pos);
      ctx.setFieldValue(ProtoField{&message, field_, i}, pos);
    }
    if (ctx.shouldReturn(status)) {
      return status;
    }
  }
  return absl::OkStatus();
}

absl::Status MapValidationRules::Validate(
    RuleContext& ctx, const google::protobuf::Message& message) const {
  auto status = Base::Validate(ctx, message);
  if (!status.ok() || (keyRules_ == nullptr && valueRules_ == nullptr)) {
    return status;
  }
  cel::runtime::FieldBackedMapImpl mapVal(&message, field_, ctx.arena);
  cel::runtime::Activation activation;
  const auto* keyField = field_->message_type()->FindFieldByName("key");
  const auto* valueField = field_->message_type()->FindFieldByName("value");
  auto keys_or = mapVal.ListKeys();
  if (!keys_or.ok()) {
    return keys_or.status();
  }
  const auto& keys = *std::move(keys_or).value();
  for (int i = 0; i < mapVal.size(); i++) {
    const auto& elemMsg = message.GetReflection()->GetRepeatedMessage(message, field_, i);
    int pos = ctx.violations.size();
    auto key = keys[i];
    if (keyRules_ != nullptr) {
      if (!keyRules_->getIgnoreEmpty() || !isEmptyItem(key)) {
        activation.InsertValue("this", key);
        status = keyRules_->ValidateCel(ctx, activation);
        if (!status.ok()) {
          return status;
        }
        if (ctx.violations.size() > pos) {
          ctx.appendRulePathElement(
              {
                  fieldPathElement(
                      MapRules::descriptor()->FindFieldByNumber(MapRules::kKeysFieldNumber)),
                  fieldPathElement(
                      FieldRules::descriptor()->FindFieldByNumber(FieldRules::kMapFieldNumber)),
              },
              pos);
          ctx.setFieldValue(ProtoField{&elemMsg, keyField}, pos);
          ctx.setForKey(pos);
        }
        activation.RemoveValueEntry("this");
      }
    }
    if (valueRules_ != nullptr) {
      auto value = *mapVal[key];
      if (!valueRules_->getIgnoreEmpty() || !isEmptyItem(value)) {
        activation.InsertValue("this", value);
        int valuePos = ctx.violations.size();
        status = valueRules_->ValidateCel(ctx, activation);
        if (!status.ok()) {
          return status;
        }
        if (ctx.violations.size() > valuePos) {
          ctx.appendRulePathElement(
              {
                  fieldPathElement(
                      MapRules::descriptor()->FindFieldByNumber(MapRules::kValuesFieldNumber)),
                  fieldPathElement(
                      FieldRules::descriptor()->FindFieldByNumber(FieldRules::kMapFieldNumber)),
              },
              valuePos);
          ctx.setFieldValue(ProtoField{&elemMsg, valueField}, pos);
        }
        activation.RemoveValueEntry("this");
      }
    }
    if (ctx.violations.size() > pos) {
      FieldPathElement element = fieldPathElement(field_);
      if (auto status = setPathElementMapKey(&element, elemMsg, keyField, valueField);
          !status.ok()) {
        return status;
      }
      ctx.appendFieldPathElement(element, pos);
      if (ctx.failFast) {
        return absl::OkStatus();
      }
    }
  }
  return absl::OkStatus();
}

absl::Status FieldValidationRules::ValidateAny(
    RuleContext& ctx, const ProtoField& field, const google::protobuf::Message& anyMsg) const {
  static const google::protobuf::FieldDescriptor* anyInField =
      AnyRules::descriptor()->FindFieldByNumber(AnyRules::kInFieldNumber);
  static const google::protobuf::FieldDescriptor* anyNotInField =
      AnyRules::descriptor()->FindFieldByNumber(AnyRules::kNotInFieldNumber);
  const auto* typeUriField = anyMsg.GetDescriptor()->FindFieldByName("type_url");
  if (typeUriField == nullptr ||
      typeUriField->type() != google::protobuf::FieldDescriptor::TYPE_STRING) {
    return absl::InvalidArgumentError("expected Any");
  }
  const auto& typeUri = anyMsg.GetReflection()->GetString(anyMsg, typeUriField);
  if (anyRules_->in_size() > 0) {
    // Must be in the list of allowed types.
    bool found = false;
    for (const auto& allowed : anyRules_->in()) {
      if (allowed == typeUri) {
        found = true;
        break;
      }
    }
    if (!found) {
      Violation violation;
      *violation.mutable_rule_id() = "any.in";
      *violation.mutable_message() = "type URL must be in the allow list";
      if (field.index() == -1) {
        *violation.mutable_field()->mutable_elements()->Add() =
            fieldPathElement(field.descriptor());
      }
      *violation.mutable_rule()->mutable_elements()->Add() =
          staticFieldPathElement<AnyRules, AnyRules::kInFieldNumber>();
      *violation.mutable_rule()->mutable_elements()->Add() =
          staticFieldPathElement<FieldRules, FieldRules::kAnyFieldNumber>();
      ctx.violations.emplace_back(
          std::move(violation), field, ProtoField{&fieldRules_.any(), anyInField});
    }
  }
  for (const auto& block : anyRules_->not_in()) {
    if (block == typeUri) {
      Violation violation;
      *violation.mutable_rule_id() = "any.not_in";
      *violation.mutable_message() = "type URL must not be in the block list";
      if (field.index() == -1) {
        *violation.mutable_field()->mutable_elements()->Add() =
            fieldPathElement(field.descriptor());
      }
      *violation.mutable_rule()->mutable_elements()->Add() =
          staticFieldPathElement<AnyRules, AnyRules::kNotInFieldNumber>();
      *violation.mutable_rule()->mutable_elements()->Add() =
          staticFieldPathElement<FieldRules, FieldRules::kAnyFieldNumber>();
      ctx.violations.emplace_back(
          std::move(violation), field, ProtoField{&fieldRules_.any(), anyNotInField});
      break;
    }
  }
  return absl::OkStatus();
}

absl::Status OneofValidationRules::Validate(
    buf::validate::internal::RuleContext& ctx, const google::protobuf::Message& message) const {
  if (required_) {
    if (!message.GetReflection()->HasOneof(message, oneof_)) {
      Violation violation;
      *violation.mutable_rule_id() = "required";
      *violation.mutable_message() = "exactly one field is required in oneof";
      *violation.mutable_field()->mutable_elements()->Add() = oneofPathElement(*oneof_);
      ctx.violations.emplace_back(std::move(violation), absl::nullopt, absl::nullopt);
    }
  }
  return absl::OkStatus();
}

absl::Status MessageOneofValidationRules::Validate(
    RuleContext& ctx, const google::protobuf::Message& message) const {
  int has_count = 0;
  for (const auto& fdesc : fields_) {
    if (message.GetReflection()->HasField(message, fdesc)) {
      has_count++;
    }
  }
  if (has_count > 1) {
    Violation violation;
    *violation.mutable_rule_id() = "message.oneof";
    *violation.mutable_message() = absl::StrCat("only one of ", field_names_(), " can be set");
    ctx.violations.emplace_back(std::move(violation), absl::nullopt, absl::nullopt);
  }
  if (required_ && has_count == 0) {
    Violation violation;
    *violation.mutable_rule_id() = "message.oneof";
    *violation.mutable_message() = absl::StrCat("one of ", field_names_(), " must be set");
    ctx.violations.emplace_back(std::move(violation), absl::nullopt, absl::nullopt);
  }
  return absl::OkStatus();
}

std::string MessageOneofValidationRules::field_names_() const {
  return absl::StrJoin(fields_, ", ", [](std::string* out, const google::protobuf::FieldDescriptor *fdesc) {
    absl::StrAppend(out, fdesc->name());
  });
}

} // namespace buf::validate::internal
