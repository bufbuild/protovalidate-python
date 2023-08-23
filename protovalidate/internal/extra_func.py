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

import math
from ipaddress import IPv4Address, IPv6Address, ip_address
from urllib import parse as urlparse

import celpy  # type: ignore
from celpy import celtypes  # type: ignore

from protovalidate.internal import string_format


def _validate_hostname(host):
    if not host:
        return False
    if len(host) > 253:
        return False

    if host[-1] == ".":
        host = host[:-1]

    for part in host.split("."):
        if len(part) == 0 or len(part) > 63:
            return False

        # Host names cannot begin or end with hyphens
        if part[0] == "-" or part[-1] == "-":
            return False
        for r in part:
            if (r < "A" or r > "Z") and (r < "a" or r > "z") and (r < "0" or r > "9") and r != "-":
                return False
    return True


def validate_email(addr):
    if "<" in addr and ">" in addr:
        addr = addr.split("<")[1].split(">")[0]

    if len(addr) > 254:
        return False

    parts = addr.split("@")
    if len(parts) != 2:
        return False
    if len(parts[0]) > 64:
        return False
    return _validate_hostname(parts[1])


def is_ip(val: celtypes.Value, version: celtypes.Value | None = None) -> celpy.Result:
    if not isinstance(val, (celtypes.BytesType, celtypes.StringType)):
        msg = "invalid argument, expected string or bytes"
        raise celpy.EvalError(msg)
    try:
        if version is None:
            ip_address(val)
        elif version == 4:
            IPv4Address(val)
        elif version == 6:
            IPv6Address(val)
        else:
            msg = "invalid argument, expected 4 or 6"
            raise celpy.EvalError(msg)
        return celtypes.BoolType(True)
    except ValueError:
        return celtypes.BoolType(False)


def is_email(string: celtypes.Value) -> celpy.Result:
    if not isinstance(string, celtypes.StringType):
        msg = "invalid argument, expected string"
        raise celpy.EvalError(msg)
    return celtypes.BoolType(validate_email(string))


def is_uri(string: celtypes.Value) -> celpy.Result:
    url = urlparse.urlparse(string)
    if not all([url.scheme, url.netloc, url.path]):
        return celtypes.BoolType(False)
    return celtypes.BoolType(True)


def is_uri_ref(string: celtypes.Value) -> celpy.Result:
    url = urlparse.urlparse(string)
    if not all([url.scheme, url.path]) and url.fragment:
        return celtypes.BoolType(False)
    return celtypes.BoolType(True)


def is_hostname(string: celtypes.Value) -> celpy.Result:
    if not isinstance(string, celtypes.StringType):
        msg = "invalid argument, expected string"
        raise celpy.EvalError(msg)
    return celtypes.BoolType(_validate_hostname(string))


def is_nan(val: celtypes.Value) -> celpy.Result:
    if not isinstance(val, celtypes.DoubleType):
        msg = "invalid argument, expected double"
        raise celpy.EvalError(msg)
    return celtypes.BoolType(math.isnan(val))


def is_inf(val: celtypes.Value, sign: None | celtypes.Value = None) -> celpy.Result:
    if not isinstance(val, celtypes.DoubleType):
        msg = "invalid argument, expected double"
        raise celpy.EvalError(msg)
    if sign is None:
        return celtypes.BoolType(math.isinf(val))

    if not isinstance(sign, celtypes.IntType):
        msg = "invalid argument, expected int"
        raise celpy.EvalError(msg)
    if sign > 0:
        return celtypes.BoolType(math.isinf(val) and val > 0)
    elif sign < 0:
        return celtypes.BoolType(math.isinf(val) and val < 0)
    else:
        return celtypes.BoolType(math.isinf(val))


def unique(val: celtypes.Value) -> celpy.Result:
    if not isinstance(val, celtypes.ListType):
        msg = "invalid argument, expected list"
        raise celpy.EvalError(msg)
    return celtypes.BoolType(len(val) == len(set(val)))


def make_extra_funcs(locale: str) -> dict[str, celpy.CELFunction]:
    string_fmt = string_format.StringFormat(locale)
    return {
        # Missing standard functions
        "format": string_fmt.format,
        # protovalidate specific functions
        "isNan": is_nan,
        "isInf": is_inf,
        "isIp": is_ip,
        "isEmail": is_email,
        "isUri": is_uri,
        "isUriRef": is_uri_ref,
        "isHostname": is_hostname,
        "unique": unique,
    }


EXTRA_FUNCS = make_extra_funcs("en_US")
