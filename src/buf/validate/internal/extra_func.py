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

import celpy
from celpy import celtypes
from buf.validate.internal import string_format
from urllib import parse as urlparse
from ipaddress import IPv4Address, IPv6Address, ip_address
from validate_email import validate_email


def _validateHostName(host):
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
            if (
                (r < "A" or r > "Z")
                and (r < "a" or r > "z")
                and (r < "0" or r > "9")
                and r != "-"
            ):
                return False
    return True


def _validateEmail(addr):
    if "<" in addr and ">" in addr:
        addr = addr.split("<")[1].split(">")[0]

    if not validate_email(addr):
        return False

    if len(addr) > 254:
        return False

    parts = addr.split("@")
    if len(parts) != 2:
        return False
    if len(parts[0]) > 64:
        return False
    return _validateHostName(parts[1])


def is_ip(val: celtypes.Value, version: celtypes.Value | None = None) -> celpy.Result:
    if not isinstance(val, (celtypes.BytesType, celtypes.StringType)):
        raise celpy.EvalError("invalid argument, expected string or bytes")
    try:
        if version is None:
            ip_address(val)
        elif version == 4:
            IPv4Address(val)
        elif version == 6:
            IPv6Address(val)
        else:
            raise celpy.EvalError("invalid argument, expected 4 or 6")
        return celtypes.BoolType(True)
    except ValueError:
        return celtypes.BoolType(False)


def is_email(string: celtypes.Value) -> celpy.Result:
    if not isinstance(string, celtypes.StringType):
        raise celpy.EvalError("invalid argument, expected string")
    return celtypes.BoolType(_validateEmail(string))


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
        raise celpy.EvalError("invalid argument, expected string")
    return celtypes.BoolType(_validateHostName(string))


def unique(val: celtypes.Value) -> celpy.Result:
    if not isinstance(val, celtypes.ListType):
        raise celpy.EvalError("invalid argument, expected list")
    return celtypes.BoolType(len(val) == len(set(val)))


def make_extra_funcs(locale: str) -> dict[str, celpy.CELFunction]:
    string_fmt = string_format.StringFormat(locale)
    return {
        "format": string_fmt.format,
        "isIp": is_ip,
        "isEmail": is_email,
        "isUri": is_uri,
        "isUriRef": is_uri_ref,
        "isHostname": is_hostname,
        "unique": unique,
    }


EXTRA_FUNCS = make_extra_funcs("en_US")
