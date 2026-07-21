# Copyright (c) 2023-2026 Buf Technologies, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""celpy registration for protovalidate's custom CEL functions."""

from __future__ import annotations

import functools
import typing

import celpy
import re2
from celpy import celtypes

from protovalidate import _funcs, _string_format
from protovalidate._rules import MessageType

if typing.TYPE_CHECKING:
    from collections.abc import Callable


def _to_py(value: object) -> object:
    """Convert a celpy celtypes value to a plain Python type for func evaluation.

    Most celtypes subclass their builtin, so this would be a no-op — except
    ``celtypes.BoolType`` subclasses ``int`` (``bool`` cannot be subclassed), so
    ``isinstance(x, bool)`` is ``False`` for a celpy bool. Normalizing here lets
    the shared functions discriminate ``bool`` from ``int`` arguments correctly.
    """
    if isinstance(value, celtypes.BoolType):
        return bool(value)
    if isinstance(value, celtypes.DoubleType):
        return float(value)
    if isinstance(value, celtypes.IntType | celtypes.UintType):
        return int(value)
    if isinstance(value, celtypes.StringType):
        return str(value)
    if isinstance(value, celtypes.BytesType):
        return bytes(value)
    if isinstance(value, celtypes.ListType):
        return [_to_py(v) for v in value]
    if isinstance(value, celtypes.MapType):
        return {_to_py(k): _to_py(v) for k, v in value.items()}
    return value


def _wrap(fn: Callable[..., object]) -> celpy.CELFunction:
    """Adapt a plain Python func result to celpy."""

    @functools.wraps(fn)
    def wrapper(*args: celtypes.Value) -> celpy.Result:
        try:
            result = fn(*[_to_py(arg) for arg in args])
        except ValueError as ex:
            raise celpy.CELEvalError(str(ex)) from ex
        if isinstance(result, bool):
            return celtypes.BoolType(result)
        if isinstance(result, str):
            return celtypes.StringType(result)
        return typing.cast("celpy.Result", result)

    return wrapper


def cel_get_field(message: celtypes.Value, field_name: celtypes.Value) -> celpy.Result:
    if not isinstance(message, MessageType):
        msg = "invalid argument, expected message"
        raise celpy.CELEvalError(msg)
    if not isinstance(field_name, celtypes.StringType):
        msg = "invalid argument, expected string"
        raise celpy.CELEvalError(msg)
    field = message.get_field(field_name)
    if not field:
        msg = f"no such field: {field_name}"
        raise celpy.CELEvalError(msg)
    return message.convert_field(field)


def cel_unique(val: celtypes.Value) -> celpy.Result:
    if not isinstance(val, celtypes.ListType | list):
        msg = "invalid argument, expected list"
        raise celpy.CELEvalError(msg)
    seen: set[celtypes.Value] = set()
    for item in val:
        if item in seen:
            return celtypes.BoolType(False)  # noqa: FBT003
        seen.add(item)
    return celtypes.BoolType(True)  # noqa: FBT003


def cel_matches(text: str, pattern: str) -> celpy.Result:
    try:
        m = re2.search(pattern, text)
    except re2.error as ex:
        return celpy.CELEvalError("match error", ex.__class__, ex.args)

    return celtypes.BoolType(m is not None)


def make_extra_funcs() -> dict[str, celpy.CELFunction]:
    string_fmt = _string_format.StringFormat()
    return {
        # Missing standard functions
        "format": string_fmt.format,
        # Overridden standard functions
        "matches": cel_matches,
        # protovalidate specific functions
        "getField": cel_get_field,
        "isNan": _wrap(_funcs.cel_is_nan),
        "isInf": _wrap(_funcs.cel_is_inf),
        "isIp": _wrap(_funcs.cel_is_ip),
        "isIpPrefix": _wrap(_funcs.cel_is_ip_prefix),
        "isEmail": _wrap(_funcs.cel_is_email),
        "isUri": _wrap(_funcs.cel_is_uri),
        "isUriRef": _wrap(_funcs.cel_is_uri_ref),
        "isHostname": _wrap(_funcs.cel_is_hostname),
        "isHostAndPort": _wrap(_funcs.cel_is_host_and_port),
        "unique": cel_unique,
    }
