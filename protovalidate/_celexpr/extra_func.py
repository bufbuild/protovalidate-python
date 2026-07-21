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

"""cel-expr-python registration for protovalidate's custom CEL functions."""

from __future__ import annotations

from cel_expr_python import cel
from google.protobuf import (
    descriptor as google_descriptor,
    message as google_message,
    wrappers_pb2 as google_wrappers_pb2,
)

from protovalidate import _funcs

from ._utils import is_repeated


def cel_get_field(message: object, field_name: object) -> object:
    if not isinstance(message, google_message.Message):
        msg = "invalid argument, expected message"
        raise TypeError(msg)
    if not isinstance(field_name, str):
        msg = "invalid argument, expected string"
        raise TypeError(msg)
    if field_name not in message.DESCRIPTOR.fields_by_name:
        msg = f"no such field: {field_name}"
        raise ValueError(msg)
    field = message.DESCRIPTOR.fields_by_name[field_name]
    value = getattr(message, field.name)
    if field.message_type is not None and field.message_type.GetOptions().map_entry:
        return dict(value)
    if is_repeated(field):
        return list(value)
    if field.type == google_descriptor.FieldDescriptor.TYPE_BYTES:
        # Route bytes through BytesValue so the value is owned by the runtime;
        # raw Python bytes returns are corrupted by a runtime conversion bug.
        return google_wrappers_pb2.BytesValue(value=value)
    return value


def cel_unique(val: object) -> bool:
    if not isinstance(val, list):
        msg = "invalid argument, expected list"
        raise TypeError(msg)
    # Track seen values keyed by (type, value) so that distinct CEL types that
    # are equal in Python (notably bool vs int: ``True == 1``) are not treated
    # as duplicates, and so that bytes are never confused with strings.
    seen: set = set()
    for item in val:
        # The runtime hands bytes values to Python as (unhashable) bytearrays.
        hashable = bytes(item) if isinstance(item, bytearray) else item
        key = (type(hashable), hashable)
        if key in seen:
            return False
        seen.add(key)
    return True


def _bytes_starts_with(value: object, prefix: object) -> bool:
    return bytes(value).startswith(bytes(prefix))  # ty: ignore[invalid-argument-type]


def _bytes_ends_with(value: object, suffix: object) -> bool:
    return bytes(value).endswith(bytes(suffix))  # ty: ignore[invalid-argument-type]


def _bytes_contains(value: object, sub: object) -> bool:
    return bytes(sub) in bytes(value)  # ty: ignore[invalid-argument-type]


def make_extension() -> cel.CelExtension:
    """Build the CEL extension with protovalidate's custom functions.

    ``matches`` is not registered: the cel-cpp runtime already evaluates it
    with RE2, which is the engine the protovalidate spec requires. ``format``
    comes from the bundled strings extension. The bytes overloads of
    ``startsWith``/``endsWith``/``contains`` are protovalidate additions to
    the standard string-only functions.
    """
    _b, _s, _i, _d, _l, _dyn = (
        cel.Type.BOOL,
        cel.Type.STRING,
        cel.Type.INT,
        cel.Type.DOUBLE,
        cel.Type.LIST,
        cel.Type.DYN,
    )
    return cel.CelExtension(
        "protovalidate",
        [
            cel.FunctionDecl(
                "getField",
                [cel.Overload("get_field", _dyn, [_dyn, _s], impl=cel_get_field)],
            ),
            cel.FunctionDecl(
                "isNan",
                [
                    cel.Overload(
                        "double_is_nan",
                        _b,
                        [_d],
                        is_member=True,
                        impl=_funcs.cel_is_nan,
                    )
                ],
            ),
            cel.FunctionDecl(
                "isInf",
                [
                    cel.Overload(
                        "double_is_inf",
                        _b,
                        [_d],
                        is_member=True,
                        impl=_funcs.cel_is_inf,
                    ),
                    cel.Overload(
                        "double_int_is_inf",
                        _b,
                        [_d, _i],
                        is_member=True,
                        impl=_funcs.cel_is_inf,
                    ),
                ],
            ),
            cel.FunctionDecl(
                "isIp",
                [
                    cel.Overload(
                        "string_is_ip", _b, [_s], is_member=True, impl=_funcs.cel_is_ip
                    ),
                    cel.Overload(
                        "string_int_is_ip",
                        _b,
                        [_s, _i],
                        is_member=True,
                        impl=_funcs.cel_is_ip,
                    ),
                ],
            ),
            cel.FunctionDecl(
                "isIpPrefix",
                [
                    cel.Overload(
                        "string_is_ip_prefix",
                        _b,
                        [_s],
                        is_member=True,
                        impl=_funcs.cel_is_ip_prefix,
                    ),
                    cel.Overload(
                        "string_int_is_ip_prefix",
                        _b,
                        [_s, _i],
                        is_member=True,
                        impl=_funcs.cel_is_ip_prefix,
                    ),
                    cel.Overload(
                        "string_bool_is_ip_prefix",
                        _b,
                        [_s, _b],
                        is_member=True,
                        impl=_funcs.cel_is_ip_prefix,
                    ),
                    cel.Overload(
                        "string_int_bool_is_ip_prefix",
                        _b,
                        [_s, _i, _b],
                        is_member=True,
                        impl=_funcs.cel_is_ip_prefix,
                    ),
                ],
            ),
            cel.FunctionDecl(
                "isEmail",
                [
                    cel.Overload(
                        "string_is_email",
                        _b,
                        [_s],
                        is_member=True,
                        impl=_funcs.cel_is_email,
                    )
                ],
            ),
            cel.FunctionDecl(
                "isUri",
                [
                    cel.Overload(
                        "string_is_uri",
                        _b,
                        [_s],
                        is_member=True,
                        impl=_funcs.cel_is_uri,
                    )
                ],
            ),
            cel.FunctionDecl(
                "isUriRef",
                [
                    cel.Overload(
                        "string_is_uri_ref",
                        _b,
                        [_s],
                        is_member=True,
                        impl=_funcs.cel_is_uri_ref,
                    )
                ],
            ),
            cel.FunctionDecl(
                "isHostname",
                [
                    cel.Overload(
                        "string_is_hostname",
                        _b,
                        [_s],
                        is_member=True,
                        impl=_funcs.cel_is_hostname,
                    )
                ],
            ),
            cel.FunctionDecl(
                "isHostAndPort",
                [
                    cel.Overload(
                        "string_bool_is_host_and_port",
                        _b,
                        [_s, _b],
                        is_member=True,
                        impl=_funcs.cel_is_host_and_port,
                    )
                ],
            ),
            cel.FunctionDecl(
                "unique",
                [
                    cel.Overload(
                        "list_unique", _b, [_l], is_member=True, impl=cel_unique
                    )
                ],
            ),
            cel.FunctionDecl(
                "startsWith",
                [
                    cel.Overload(
                        "bytes_starts_with",
                        _b,
                        [cel.Type.BYTES, cel.Type.BYTES],
                        is_member=True,
                        impl=_bytes_starts_with,
                    )
                ],
            ),
            cel.FunctionDecl(
                "endsWith",
                [
                    cel.Overload(
                        "bytes_ends_with",
                        _b,
                        [cel.Type.BYTES, cel.Type.BYTES],
                        is_member=True,
                        impl=_bytes_ends_with,
                    )
                ],
            ),
            cel.FunctionDecl(
                "contains",
                [
                    cel.Overload(
                        "bytes_contains",
                        _b,
                        [cel.Type.BYTES, cel.Type.BYTES],
                        is_member=True,
                        impl=_bytes_contains,
                    )
                ],
            ),
        ],
    )
