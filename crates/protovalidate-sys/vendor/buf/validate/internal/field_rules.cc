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

#include "buf/validate/internal/field_rules.h"

#include "buf/validate/internal/cel_rules.h"
#include "google/protobuf/any.pb.h"

namespace buf::validate::internal {
absl::StatusOr<std::unique_ptr<FieldValidationRules>> NewFieldRules(
    std::unique_ptr<MessageFactory>& messageFactory,
    bool allowUnknownFields,
    google::protobuf::Arena* arena,
    google::api::expr::runtime::CelExpressionBuilder& builder,
    const google::protobuf::FieldDescriptor* field,
    const FieldRules& fieldLvl) {
  if (fieldLvl.ignore() == IGNORE_ALWAYS) {
    return nullptr;
  }
  absl::StatusOr<std::unique_ptr<FieldValidationRules>> rules_or;
  switch (fieldLvl.type_case()) {
    case FieldRules::kBool:
      rules_or = NewScalarFieldRules(
          messageFactory,
          allowUnknownFields,
          arena,
          builder,
          field,
          fieldLvl,
          fieldLvl.bool_(),
          google::protobuf::FieldDescriptor::TYPE_BOOL,
          "google.protobuf.BoolValue");
      break;
    case FieldRules::kFloat:
      rules_or = NewScalarFieldRules(
          messageFactory,
          allowUnknownFields,
          arena,
          builder,
          field,
          fieldLvl,
          fieldLvl.float_(),
          google::protobuf::FieldDescriptor::TYPE_FLOAT,
          "google.protobuf.FloatValue");
      break;
    case FieldRules::kDouble:
      rules_or = NewScalarFieldRules(
          messageFactory,
          allowUnknownFields,
          arena,
          builder,
          field,
          fieldLvl,
          fieldLvl.double_(),
          google::protobuf::FieldDescriptor::TYPE_DOUBLE,
          "google.protobuf.DoubleValue");
      break;
    case FieldRules::kInt32:
      rules_or = NewScalarFieldRules(
          messageFactory,
          allowUnknownFields,
          arena,
          builder,
          field,
          fieldLvl,
          fieldLvl.int32(),
          google::protobuf::FieldDescriptor::TYPE_INT32,
          "google.protobuf.Int32Value");
      break;
    case FieldRules::kInt64:
      rules_or = NewScalarFieldRules(
          messageFactory,
          allowUnknownFields,
          arena,
          builder,
          field,
          fieldLvl,
          fieldLvl.int64(),
          google::protobuf::FieldDescriptor::TYPE_INT64,
          "google.protobuf.Int64Value");
      break;
    case FieldRules::kUint32:
      rules_or = NewScalarFieldRules(
          messageFactory,
          allowUnknownFields,
          arena,
          builder,
          field,
          fieldLvl,
          fieldLvl.uint32(),
          google::protobuf::FieldDescriptor::TYPE_UINT32,
          "google.protobuf.UInt32Value");
      break;
    case FieldRules::kUint64:
      rules_or = NewScalarFieldRules(
          messageFactory,
          allowUnknownFields,
          arena,
          builder,
          field,
          fieldLvl,
          fieldLvl.uint64(),
          google::protobuf::FieldDescriptor::TYPE_UINT64,
          "google.protobuf.UInt64Value");
      break;
    case FieldRules::kSint32:
      rules_or = NewScalarFieldRules(
          messageFactory,
          allowUnknownFields,
          arena,
          builder,
          field,
          fieldLvl,
          fieldLvl.sint32(),
          google::protobuf::FieldDescriptor::TYPE_SINT32);
      break;
    case FieldRules::kSint64:
      rules_or = NewScalarFieldRules(
          messageFactory,
          allowUnknownFields,
          arena,
          builder,
          field,
          fieldLvl,
          fieldLvl.sint64(),
          google::protobuf::FieldDescriptor::TYPE_SINT64);
      break;
    case FieldRules::kFixed32:
      rules_or = NewScalarFieldRules(
          messageFactory,
          allowUnknownFields,
          arena,
          builder,
          field,
          fieldLvl,
          fieldLvl.fixed32(),
          google::protobuf::FieldDescriptor::TYPE_FIXED32);
      break;
    case FieldRules::kFixed64:
      rules_or = NewScalarFieldRules(
          messageFactory,
          allowUnknownFields,
          arena,
          builder,
          field,
          fieldLvl,
          fieldLvl.fixed64(),
          google::protobuf::FieldDescriptor::TYPE_FIXED64);
      break;
    case FieldRules::kSfixed32:
      rules_or = NewScalarFieldRules(
          messageFactory,
          allowUnknownFields,
          arena,
          builder,
          field,
          fieldLvl,
          fieldLvl.sfixed32(),
          google::protobuf::FieldDescriptor::TYPE_SFIXED32);
      break;
    case FieldRules::kSfixed64:
      rules_or = NewScalarFieldRules(
          messageFactory,
          allowUnknownFields,
          arena,
          builder,
          field,
          fieldLvl,
          fieldLvl.sfixed64(),
          google::protobuf::FieldDescriptor::TYPE_SFIXED64);
      break;
    case FieldRules::kString:
      rules_or = NewScalarFieldRules(
          messageFactory,
          allowUnknownFields,
          arena,
          builder,
          field,
          fieldLvl,
          fieldLvl.string(),
          google::protobuf::FieldDescriptor::TYPE_STRING,
          "google.protobuf.StringValue");
      break;
    case FieldRules::kBytes:
      rules_or = NewScalarFieldRules(
          messageFactory,
          allowUnknownFields,
          arena,
          builder,
          field,
          fieldLvl,
          fieldLvl.bytes(),
          google::protobuf::FieldDescriptor::TYPE_BYTES,
          "google.protobuf.BytesValue");
      break;
    case FieldRules::kEnum: {
      rules_or = std::make_unique<EnumValidationRules>(field, fieldLvl);
      auto status = BuildScalarFieldRules(
          *rules_or.value(),
          messageFactory,
          allowUnknownFields,
          arena,
          builder,
          field,
          fieldLvl,
          fieldLvl.enum_(),
          google::protobuf::FieldDescriptor::TYPE_ENUM);
      if (!status.ok()) {
        rules_or = status;
      }
      break;
    }
    case FieldRules::kDuration:
      if (field->cpp_type() != google::protobuf::FieldDescriptor::CPPTYPE_MESSAGE ||
          field->message_type()->full_name() !=
              google::protobuf::Duration::descriptor()->full_name()) {
        return absl::InvalidArgumentError("duration field validator on non-duration field");
      } else {
        auto result = std::make_unique<FieldValidationRules>(field, fieldLvl);
        auto status = BuildCelRules(
            messageFactory, allowUnknownFields, arena, builder, fieldLvl.duration(), *result);
        if (!status.ok()) {
          rules_or = status;
        } else {
          rules_or = std::move(result);
        }
      }
      break;
    case FieldRules::kFieldMask:
      if (field->cpp_type() != google::protobuf::FieldDescriptor::CPPTYPE_MESSAGE ||
          field->message_type()->full_name() !=
              google::protobuf::FieldMask::descriptor()->full_name()) {
        return absl::InvalidArgumentError("field_mask field validator on non-field_mask field");
      } else {
        auto result = std::make_unique<FieldValidationRules>(field, fieldLvl);
        auto status = BuildCelRules(
            messageFactory, allowUnknownFields, arena, builder, fieldLvl.field_mask(), *result);
        if (!status.ok()) {
          rules_or = status;
        } else {
          rules_or = std::move(result);
        }
      }
      break;
    case FieldRules::kTimestamp:
      if (field->cpp_type() != google::protobuf::FieldDescriptor::CPPTYPE_MESSAGE ||
          field->message_type()->full_name() !=
              google::protobuf::Timestamp::descriptor()->full_name()) {
        return absl::InvalidArgumentError("timestamp field validator on non-timestamp field");
      } else {
        auto result = std::make_unique<FieldValidationRules>(field, fieldLvl);
        auto status = BuildCelRules(
            messageFactory, allowUnknownFields, arena, builder, fieldLvl.timestamp(), *result);
        if (!status.ok()) {
          rules_or = status;
        } else {
          rules_or = std::move(result);
        }
      }
      break;
    case FieldRules::kRepeated:
      if (!field->is_repeated()) {
        return absl::InvalidArgumentError("repeated field validator on non-repeated field");
      } else if (field->is_map()) {
        return absl::InvalidArgumentError("repeated field validator on map field");
      } else {
        std::unique_ptr<FieldValidationRules> items;
        if (fieldLvl.repeated().has_items()) {
          auto items_or = NewFieldRules(
              messageFactory,
              allowUnknownFields,
              arena,
              builder,
              field,
              fieldLvl.repeated().items());
          if (!items_or.ok()) {
            return items_or.status();
          }
          items = std::move(items_or).value();
        }
        auto result = std::make_unique<RepeatedValidationRules>(field, fieldLvl, std::move(items));
        auto status = BuildCelRules(
            messageFactory, allowUnknownFields, arena, builder, fieldLvl.repeated(), *result);
        if (!status.ok()) {
          rules_or = status;
        } else {
          rules_or = std::move(result);
        }
      }
      break;
    case FieldRules::kMap:
      if (!field->is_map()) {
        return absl::InvalidArgumentError("map field validator on non-map field");
      } else {
        auto keyRulesOr = NewFieldRules(
            messageFactory,
            allowUnknownFields,
            arena,
            builder,
            field->message_type()->field(0),
            fieldLvl.map().keys());
        if (!keyRulesOr.ok()) {
          return keyRulesOr.status();
        }
        auto valueRulesOr = NewFieldRules(
            messageFactory,
            allowUnknownFields,
            arena,
            builder,
            field->message_type()->field(1),
            fieldLvl.map().values());
        if (!valueRulesOr.ok()) {
          return valueRulesOr.status();
        }
        auto result = std::make_unique<MapValidationRules>(
            field, fieldLvl, std::move(keyRulesOr).value(), std::move(valueRulesOr).value());
        auto status = BuildCelRules(
            messageFactory, allowUnknownFields, arena, builder, fieldLvl.map(), *result);
        if (!status.ok()) {
          rules_or = status;
        } else {
          rules_or = std::move(result);
        }
      }
      break;
    case FieldRules::kAny:
      if (field->cpp_type() != google::protobuf::FieldDescriptor::CPPTYPE_MESSAGE ||
          field->message_type()->full_name() != google::protobuf::Any::descriptor()->full_name()) {
        return absl::InvalidArgumentError("any field validator on non-any field");
      } else {
        auto result = std::make_unique<FieldValidationRules>(field, fieldLvl, &fieldLvl.any());
        auto status = BuildCelRules(
            messageFactory, allowUnknownFields, arena, builder, fieldLvl.any(), *result);
        if (!status.ok()) {
          rules_or = status;
        } else {
          rules_or = std::move(result);
        }
      }
      break;
    case FieldRules::TYPE_NOT_SET:
      rules_or = std::make_unique<FieldValidationRules>(field, fieldLvl);
      break;
    default:
      return absl::InvalidArgumentError(
          absl::StrFormat("unknown field validator type %d", fieldLvl.type_case()));
  }
  if (rules_or.ok()) {
    for (int i = 0; i < fieldLvl.cel_expression_size(); i++) {
      const auto& expr = fieldLvl.cel_expression(i);
      FieldPathElement celElement =
          staticFieldPathElement<FieldRules, FieldRules::kCelExpressionFieldNumber>();
      celElement.set_index(i);
      FieldPath rulePath;
      *rulePath.mutable_elements()->Add() = celElement;
      auto status = rules_or.value()->Add(builder, expr, rulePath, nullptr);
      if (!status.ok()) {
        return status;
      }
    }
    for (int i = 0; i < fieldLvl.cel_size(); i++) {
      const auto& rule = fieldLvl.cel(i);
      FieldPathElement celElement =
          staticFieldPathElement<FieldRules, FieldRules::kCelFieldNumber>();
      celElement.set_index(i);
      FieldPath rulePath;
      *rulePath.mutable_elements()->Add() = celElement;
      auto status = rules_or.value()->Add(builder, rule, rulePath, nullptr);
      if (!status.ok()) {
        return status;
      }
    }
  }
  return rules_or;
}

} // namespace buf::validate::internal
