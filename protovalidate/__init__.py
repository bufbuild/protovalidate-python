# Copyright 2023 Buf Technologies, Inc.
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

from protovalidate import validator

Validator = validator.Validator
CompilationError = validator.CompilationError
ValidationError = validator.ValidationError
Violations = validator.Violations

_validator = Validator()
validate = _validator.validate
collect_violations = _validator.collect_violations

__all__ = ["Validator", "CompilationError", "ValidationError", "Violations", "validate", "collect_violations"]
