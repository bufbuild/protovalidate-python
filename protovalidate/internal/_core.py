# Copyright 2023-2026 Buf Technologies, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Backend-agnostic rule-engine primitives shared by both CEL backends."""

import abc
import typing

from protovalidate._gen.buf.validate import validate_pb


class CompilationError(Exception):
    pass


class Violation:
    """A singular rule violation."""

    field_value: typing.Any
    rule_value: typing.Any

    def __init__(
        self,
        *,
        field_value: typing.Any = None,
        rule_value: typing.Any = None,
        field: validate_pb.FieldPath | None = None,
        rule: validate_pb.FieldPath | None = None,
        rule_id: str = "",
        message: str = "",
        for_key: bool = False,
    ):
        self.field_value = field_value
        self.rule_value = rule_value
        self._field_elements: list[validate_pb.FieldPathElement] = list(field.elements) if field is not None else []
        self._rule_elements: list[validate_pb.FieldPathElement] = list(rule.elements) if rule is not None else []
        self._rule_id = rule_id
        self._message = message
        self._for_key = for_key

    def append_field_element(self, element: validate_pb.FieldPathElement) -> None:
        self._field_elements.append(element)

    def extend_rule_elements(self, elements: list[validate_pb.FieldPathElement]) -> None:
        self._rule_elements.extend(elements)

    def finalize_paths(self) -> None:
        self._field_elements.reverse()
        self._rule_elements.reverse()

    @property
    def proto(self) -> validate_pb.Violation:
        kwargs: dict[str, typing.Any] = {
            "rule_id": self._rule_id,
            "message": self._message,
            "for_key": self._for_key,
        }
        if self._field_elements:
            kwargs["field"] = validate_pb.FieldPath(elements=list(self._field_elements))
        if self._rule_elements:
            kwargs["rule"] = validate_pb.FieldPath(elements=list(self._rule_elements))
        return validate_pb.Violation(**kwargs)


class RuleContext:
    """The state associated with a single rule evaluation."""

    _violations: list[Violation]

    def __init__(self, *, fail_fast: bool = False):
        self._fail_fast = fail_fast
        self._violations = []

    @property
    def violations(self) -> list[Violation]:
        return self._violations

    def add(self, violation: Violation):
        self._violations.append(violation)

    def add_errors(self, other_ctx: "RuleContext"):
        self._violations.extend(other_ctx.violations)

    def add_field_path_element(self, element: validate_pb.FieldPathElement):
        for violation in self._violations:
            violation.append_field_element(element)

    def add_rule_path_elements(self, elements: list[validate_pb.FieldPathElement]):
        for violation in self._violations:
            violation.extend_rule_elements(elements)

    @property
    def done(self) -> bool:
        return self._fail_fast and self.has_errors()

    def has_errors(self) -> bool:
        return len(self._violations) > 0

    def sub_context(self) -> "RuleContext":
        return RuleContext(fail_fast=self._fail_fast)


class Rules(abc.ABC):
    """The rules associated with a single 'rules' message."""

    @abc.abstractmethod
    def validate(self, ctx: RuleContext, message: typing.Any) -> None:
        """Validate the message against the rules in this rule."""
        ...
