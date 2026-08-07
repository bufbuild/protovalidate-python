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

#include "absl/status/status.h"
#include "absl/strings/escaping.h"
#include "buf/validate/internal/proto_field.h"
#include "buf/validate/validate.pb.h"
#include "eval/public/cel_value.h"
#include "google/protobuf/arena.h"
#include "google/protobuf/message.h"

namespace buf::validate::internal {
inline std::string fieldPathString(const FieldPath& path);

/// RuleViolation is a wrapper for the protobuf Violation that provides additional in-memory
/// information, specifically, references to the in-memory values for the field and rule.
class RuleViolation {
  friend struct RuleContext;

 public:
  RuleViolation(
      Violation proto,
      const absl::optional<ProtoField>& fieldValue,
      const absl::optional<ProtoField>& ruleValue)
      : proto_{std::move(proto)}, fieldValue_{fieldValue}, ruleValue_{ruleValue} {}

  [[nodiscard]] const Violation& proto() const { return proto_; }
  [[nodiscard]] absl::optional<ProtoField> field_value() const { return fieldValue_; }
  [[nodiscard]] absl::optional<ProtoField> rule_value() const { return ruleValue_; }

 private:
  Violation proto_;
  absl::optional<ProtoField> fieldValue_;
  absl::optional<ProtoField> ruleValue_;
};

struct RuleContext {
  RuleContext() : failFast(false), arena(nullptr) {}
  RuleContext(const RuleContext&) = delete;
  void operator=(const RuleContext&) = delete;

  bool failFast;
  google::protobuf::Arena* arena;
  std::vector<RuleViolation> violations;

  [[nodiscard]] bool shouldReturn(const absl::Status& status) const {
    return !status.ok() || (failFast && !violations.empty());
  }

  void appendFieldPathElement(const FieldPathElement& element, int start) {
    for (int i = start; i < violations.size(); i++) {
      *violations[i].proto_.mutable_field()->mutable_elements()->Add() = element;
    }
  }

  void appendRulePathElement(std::initializer_list<FieldPathElement> suffix, int start) {
    for (int i = start; i < violations.size(); i++) {
      auto* elements = violations[i].proto_.mutable_rule()->mutable_elements();
      std::copy(suffix.begin(), suffix.end(), RepeatedPtrFieldBackInserter(elements));
    }
  }

  void setFieldValue(ProtoField field, int start) {
    for (int i = start; i < violations.size(); i++) {
      violations[i].fieldValue_ = field;
    }
  }

  void setRuleValue(ProtoField rule, int start) {
    for (int i = start; i < violations.size(); i++) {
      violations[i].ruleValue_ = rule;
    }
  }

  void setForKey(int start) {
    for (int i = start; i < violations.size(); i++) {
      violations[i].proto_.set_for_key(true);
    }
  }

  void finalize() {
    for (RuleViolation& violation : violations) {
      if (violation.proto().has_field()) {
        std::reverse(
            violation.proto_.mutable_field()->mutable_elements()->begin(),
            violation.proto_.mutable_field()->mutable_elements()->end());
      }
      if (violation.proto().has_rule()) {
        std::reverse(
            violation.proto_.mutable_rule()->mutable_elements()->begin(),
            violation.proto_.mutable_rule()->mutable_elements()->end());
      }
    }
  }
};

class ValidationRules {
 public:
  ValidationRules() = default;
  virtual ~ValidationRules() = default;

  ValidationRules(const ValidationRules&) = delete;
  void operator=(const ValidationRules&) = delete;

  virtual absl::Status Validate(
      RuleContext& ctx, const google::protobuf::Message& message) const = 0;
};

inline std::string fieldPathString(const FieldPath& path) {
  std::string result;
  for (const FieldPathElement& element : path.elements()) {
    if (!result.empty()) {
      result += '.';
    }
    switch (element.subscript_case()) {
      case FieldPathElement::kIndex:
        absl::StrAppend(&result, element.field_name(), "[", std::to_string(element.index()), "]");
        break;
      case FieldPathElement::kBoolKey:
        absl::StrAppend(&result, element.field_name(), element.bool_key() ? "[true]" : "[false]");
        break;
      case FieldPathElement::kIntKey:
        absl::StrAppend(&result, element.field_name(), "[", std::to_string(element.int_key()), "]");
        break;
      case FieldPathElement::kUintKey:
        absl::StrAppend(
            &result, element.field_name(), "[", std::to_string(element.uint_key()), "]");
        break;
      case FieldPathElement::kStringKey:
        absl::StrAppend(
            &result, element.field_name(), "[\"", absl::CEscape(element.string_key()), "\"]");
        break;
      case FieldPathElement::SUBSCRIPT_NOT_SET:
        absl::StrAppend(&result, element.field_name());
    }
  }
  return result;
}

} // namespace buf::validate::internal
