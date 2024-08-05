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
import typing
from email.utils import parseaddr
from ipaddress import IPv4Address, IPv4Network, IPv6Address, IPv6Network, ip_address, ip_network
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

    all_digits = True
    for part in host.split("."):
        if len(part) == 0 or len(part) > 63:
            return False

        # Host names cannot begin or end with hyphens
        if part[0] == "-" or part[-1] == "-":
            return False
        all_digits = True
        for r in part:
            if (r < "A" or r > "Z") and (r < "a" or r > "z") and (r < "0" or r > "9") and r != "-":
                return False
            all_digits = all_digits and "0" <= r <= "9"
    return not all_digits


def validate_email(addr):
    parts = parseaddr(addr)
    if addr != parts[1]:
        return False

    addr = parts[1]
    if len(addr) > 254:
        return False

    parts = addr.split("@")
    if len(parts) != 2:
        return False
    if len(parts[0]) > 64:
        return False
    return _validate_hostname(parts[1])


def validate_host_and_port(string: str, *, port_required: bool) -> bool:
    if not string:
        return False

    split_idx = string.rfind(":")
    if string[0] == "[":
        end = string.find("]")
        after_end = end + 1
        if after_end == len(string):  # no port
            return not port_required and validate_ip(string[1:end], 6)
        if after_end == split_idx:  # port
            return validate_ip(string[1:end]) and validate_port(string[split_idx + 1 :])
        return False  # malformed

    if split_idx == -1:
        return not port_required and (_validate_hostname(string) or validate_ip(string, 4))

    host = string[:split_idx]
    port = string[split_idx + 1 :]
    return (_validate_hostname(host) or validate_ip(host, 4)) and validate_port(port)


def validate_port(val: str) -> bool:
    try:
        port = int(val)
        return port <= 65535
    except ValueError:
        return False


def validate_ip(val: typing.Union[str, bytes], version: typing.Optional[int] = None) -> bool:
    try:
        if version is None:
            ip_address(val)
        elif version == 4:
            IPv4Address(val)
        elif version == 6:
            IPv6Address(val)
        else:
            msg = "invalid argument, expected 4 or 6"
            raise celpy.CELEvalError(msg)
        return True
    except ValueError:
        return False


def is_ip(val: celtypes.Value, version: typing.Optional[celtypes.Value] = None) -> celpy.Result:
    if not isinstance(val, (celtypes.BytesType, celtypes.StringType)):
        msg = "invalid argument, expected string or bytes"
        raise celpy.CELEvalError(msg)
    if not isinstance(version, celtypes.IntType) and version is not None:
        msg = "invalid argument, expected int"
        raise celpy.CELEvalError(msg)
    return celtypes.BoolType(validate_ip(val, version))


def is_ip_prefix(val: celtypes.Value, *args) -> celpy.Result:
    if not isinstance(val, (celtypes.BytesType, celtypes.StringType)):
        msg = "invalid argument, expected string or bytes"
        raise celpy.CELEvalError(msg)
    version = None
    strict = celtypes.BoolType(False)
    if len(args) == 1 and isinstance(args[0], celtypes.BoolType):
        strict = args[0]
    elif len(args) == 1 and isinstance(args[0], celtypes.IntType):
        version = args[0]
    elif len(args) == 1 and (not isinstance(args[0], celtypes.BoolType) or not isinstance(args[0], celtypes.IntType)):
        msg = "invalid argument, expected bool or int"
        raise celpy.CELEvalError(msg)
    elif len(args) == 2 and isinstance(args[0], celtypes.IntType) and isinstance(args[1], celtypes.BoolType):
        version = args[0]
        strict = args[1]
    elif len(args) == 2 and (not isinstance(args[0], celtypes.IntType) or not isinstance(args[1], celtypes.BoolType)):
        msg = "invalid argument, expected int and bool"
        raise celpy.CELEvalError(msg)
    try:
        if version is None:
            ip_network(val, strict=strict)
        elif version == 4:
            IPv4Network(val, strict=strict)
        elif version == 6:
            IPv6Network(val, strict=strict)
        else:
            msg = "invalid argument, expected 4 or 6"
            raise celpy.CELEvalError(msg)
        return celtypes.BoolType(True)
    except ValueError:
        return celtypes.BoolType(False)


def is_email(string: celtypes.Value) -> celpy.Result:
    if not isinstance(string, celtypes.StringType):
        msg = "invalid argument, expected string"
        raise celpy.CELEvalError(msg)
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
        raise celpy.CELEvalError(msg)
    return celtypes.BoolType(_validate_hostname(string))


def is_host_and_port(string: celtypes.Value, port_required: celtypes.Value) -> celpy.Result:
    if not isinstance(string, celtypes.StringType):
        msg = "invalid argument, expected string"
        raise celpy.CELEvalError(msg)
    if not isinstance(port_required, celtypes.BoolType):
        msg = "invalid argument, expected bool"
        raise celpy.CELEvalError(msg)
    return celtypes.BoolType(validate_host_and_port(string, port_required=bool(port_required)))


def is_nan(val: celtypes.Value) -> celpy.Result:
    if not isinstance(val, celtypes.DoubleType):
        msg = "invalid argument, expected double"
        raise celpy.CELEvalError(msg)
    return celtypes.BoolType(math.isnan(val))


def is_inf(val: celtypes.Value, sign: typing.Optional[celtypes.Value] = None) -> celpy.Result:
    if not isinstance(val, celtypes.DoubleType):
        msg = "invalid argument, expected double"
        raise celpy.CELEvalError(msg)
    if sign is None:
        return celtypes.BoolType(math.isinf(val))

    if not isinstance(sign, celtypes.IntType):
        msg = "invalid argument, expected int"
        raise celpy.CELEvalError(msg)
    if sign > 0:
        return celtypes.BoolType(math.isinf(val) and val > 0)
    elif sign < 0:
        return celtypes.BoolType(math.isinf(val) and val < 0)
    else:
        return celtypes.BoolType(math.isinf(val))


def unique(val: celtypes.Value) -> celpy.Result:
    if not isinstance(val, celtypes.ListType):
        msg = "invalid argument, expected list"
        raise celpy.CELEvalError(msg)
    return celtypes.BoolType(len(val) == len(set(val)))


def make_extra_funcs(locale: str) -> typing.Dict[str, celpy.CELFunction]:
    string_fmt = string_format.StringFormat(locale)
    return {
        # Missing standard functions
        "format": string_fmt.format,
        # protovalidate specific functions
        "isNan": is_nan,
        "isInf": is_inf,
        "isIp": is_ip,
        "isIpPrefix": is_ip_prefix,
        "isEmail": is_email,
        "isUri": is_uri,
        "isUriRef": is_uri_ref,
        "isHostname": is_hostname,
        "isHostAndPort": is_host_and_port,
        "unique": unique,
    }


EXTRA_FUNCS = make_extra_funcs("en_US")
