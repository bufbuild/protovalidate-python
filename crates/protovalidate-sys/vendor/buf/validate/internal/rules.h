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

#include <string>
#include <string_view>
#include <utility>

#include "buf/validate/internal/cel_validation_rules.h"
#include "buf/validate/validate.pb.h"
#include "google/protobuf/arena.h"
#include "google/protobuf/descriptor.h"
#include "google/protobuf/message.h"

namespace buf::validate::internal {

class MessageValidationRules final : public CelValidationRules {
 public:
  MessageValidationRules() = default;

  absl::Status Validate(RuleContext& ctx, const google::protobuf::Message& message) const override;
};

class FieldValidationRules : public CelValidationRules {
 public:
  FieldValidationRules(
      const google::protobuf::FieldDescriptor* desc,
      const FieldRules& field,
      const AnyRules* anyRules = nullptr)
      : fieldRules_(field),
        field_(desc),
        mapEntryField_(desc->containing_type()->options().map_entry()),
        ignoreEmpty_(
            field.ignore() == IGNORE_IF_ZERO_VALUE ||
            (desc->has_presence() && !mapEntryField_)),
        required_(field.required()),
        anyRules_(anyRules) {}

  absl::Status Validate(RuleContext& ctx, const google::protobuf::Message& message) const override;

  absl::Status ValidateAny(
      RuleContext& ctx, const ProtoField& field, const google::protobuf::Message& anyMsg) const;

  [[nodiscard]] const AnyRules* getAnyRules() const { return anyRules_; }

  [[nodiscard]] bool getIgnoreEmpty() const { return ignoreEmpty_; }

 protected:
  const FieldRules& fieldRules_;
  const google::protobuf::FieldDescriptor* field_ = nullptr;
  bool mapEntryField_ = false;
  bool ignoreEmpty_ = false;
  bool required_ = false;
  const AnyRules* anyRules_ = nullptr;
};

class EnumValidationRules : public FieldValidationRules {
  using Base = FieldValidationRules;

 public:
  EnumValidationRules(const google::protobuf::FieldDescriptor* desc, const FieldRules& field)
      : Base(desc, field), definedOnly_(field.enum_().defined_only()) {}

  absl::Status Validate(RuleContext& ctx, const google::protobuf::Message& message) const override;

 private:
  bool definedOnly_;
};

class RepeatedValidationRules : public FieldValidationRules {
  using Base = FieldValidationRules;

 public:
  RepeatedValidationRules(
      const google::protobuf::FieldDescriptor* desc,
      const FieldRules& field,
      std::unique_ptr<FieldValidationRules> itemRules)
      : Base(desc, field), itemRules_(std::move(itemRules)) {}

  absl::Status Validate(RuleContext& ctx, const google::protobuf::Message& message) const override;

 private:
  std::unique_ptr<FieldValidationRules> itemRules_;
};

class MapValidationRules : public FieldValidationRules {
  using Base = FieldValidationRules;

 public:
  MapValidationRules(
      const google::protobuf::FieldDescriptor* desc,
      const FieldRules& field,
      std::unique_ptr<FieldValidationRules> keyRules,
      std::unique_ptr<FieldValidationRules> valueRules)
      : Base(desc, field), keyRules_(std::move(keyRules)), valueRules_(std::move(valueRules)) {}

  absl::Status Validate(RuleContext& ctx, const google::protobuf::Message& message) const override;

 private:
  std::unique_ptr<FieldValidationRules> keyRules_;
  std::unique_ptr<FieldValidationRules> valueRules_;
};

// A set of rules that share the same 'rule' value.
class OneofValidationRules : public ValidationRules {
  using Base = ValidationRules;

 public:
  OneofValidationRules(const google::protobuf::OneofDescriptor* desc, const OneofRules& oneof)
      : oneof_(desc), required_(oneof.required()) {}

  absl::Status Validate(RuleContext& ctx, const google::protobuf::Message& message) const override;

 private:
  const google::protobuf::OneofDescriptor* oneof_ = nullptr;
  bool required_ = false;
};

class MessageOneofValidationRules : public ValidationRules {
  using Base = ValidationRules;

public:
  MessageOneofValidationRules(const std::vector<const google::protobuf::FieldDescriptor*> fields, const bool required)
      : fields_(fields), required_(required) {}

  absl::Status Validate(RuleContext& ctx, const google::protobuf::Message& message) const override;

private:
  const std::vector<const google::protobuf::FieldDescriptor*> fields_;
  bool required_ = false;
  std::string field_names_() const;
};

// Creates a new expression builder suitable for creating rules.
absl::StatusOr<std::unique_ptr<google::api::expr::runtime::CelExpressionBuilder>> NewRuleBuilder(
    google::protobuf::Arena* arena);

inline auto fieldPathElement(const google::protobuf::FieldDescriptor* fieldDescriptor)
    -> FieldPathElement {
  FieldPathElement element;
  element.set_field_number(fieldDescriptor->number());
  element.set_field_type(
      static_cast<::google::protobuf::FieldDescriptorProto_Type>(fieldDescriptor->type()));
  if (fieldDescriptor->is_extension()) {
    *element.mutable_field_name() = absl::StrCat("[", fieldDescriptor->full_name(), "]");
  } else {
    *element.mutable_field_name() = fieldDescriptor->name();
  }
  return element;
}

template <typename ProtoMessage, int number>
auto staticFieldPathElement() -> FieldPathElement {
  // This is thread-safe: C++11 guarantees static local initialization to be done only once and is
  // synchronized automatically.
  static const FieldPathElement element =
      fieldPathElement(ProtoMessage::descriptor()->FindFieldByNumber(number));
  return element;
}

inline auto oneofPathElement(const google::protobuf::OneofDescriptor& oneofDescriptor)
    -> FieldPathElement {
  FieldPathElement element;
  *element.mutable_field_name() = oneofDescriptor.name();
  return element;
}

inline absl::Status setPathElementMapKey(
    FieldPathElement* element,
    const google::protobuf::Message& message,
    const google::protobuf::FieldDescriptor* keyField,
    const google::protobuf::FieldDescriptor* valueField) {
  using Type = google::protobuf::FieldDescriptor::Type;
  element->set_key_type(
      static_cast<::google::protobuf::FieldDescriptorProto_Type>(keyField->type()));
  element->set_value_type(
      static_cast<::google::protobuf::FieldDescriptorProto_Type>(valueField->type()));
  switch (keyField->type()) {
    case Type::TYPE_BOOL:
      element->set_bool_key(message.GetReflection()->GetBool(message, keyField));
      break;
    case Type::TYPE_INT32:
    case Type::TYPE_SFIXED32:
    case Type::TYPE_SINT32:
      element->set_int_key(message.GetReflection()->GetInt32(message, keyField));
      break;
    case Type::TYPE_INT64:
    case Type::TYPE_SFIXED64:
    case Type::TYPE_SINT64:
      element->set_int_key(message.GetReflection()->GetInt64(message, keyField));
      break;
    case Type::TYPE_UINT32:
    case Type::TYPE_FIXED32:
      element->set_uint_key(message.GetReflection()->GetUInt32(message, keyField));
      break;
    case Type::TYPE_UINT64:
    case Type::TYPE_FIXED64:
      element->set_uint_key(message.GetReflection()->GetUInt64(message, keyField));
      break;
    case Type::TYPE_STRING:
      *element->mutable_string_key() = message.GetReflection()->GetString(message, keyField);
      break;
    default:
      return absl::InternalError(absl::StrCat("unexpected map key type ", keyField->type_name()));
  }
  return {};
}

} // namespace buf::validate::internal
