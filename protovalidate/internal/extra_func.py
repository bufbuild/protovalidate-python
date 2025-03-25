# Copyright 2023-2025 Buf Technologies, Inc.
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
import re
import sys
import typing
from ipaddress import IPv4Address, IPv4Network, IPv6Address, IPv6Network, ip_address, ip_network
from urllib import parse as urlparse

import celpy
from celpy import celtypes

from protovalidate.internal import string_format

# See https://html.spec.whatwg.org/multipage/input.html#valid-e-mail-address
_email_regex = re.compile(
    r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
)


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
            ip_network(val, strict=bool(strict))
        elif version == 4:
            IPv4Network(val, strict=bool(strict))
        elif version == 6:
            IPv6Network(val, strict=bool(strict))
        else:
            msg = "invalid argument, expected 4 or 6"
            raise celpy.CELEvalError(msg)
        return celtypes.BoolType(True)
    except ValueError:
        return celtypes.BoolType(False)


def is_email(string: celtypes.Value) -> celpy.Result:
    """Returns true if the string is an email address, for example "foo@example.com".

    Conforms to the definition for a valid email address from the HTML standard.
    Note that this standard willfully deviates from RFC 5322, which allows many
    unexpected forms of email addresses and will easily match a typographical
    error.
    """

    if not isinstance(string, celtypes.StringType):
        msg = "invalid argument, expected string"
        raise celpy.CELEvalError(msg)
    m = _email_regex.match(string) is not None
    return celtypes.BoolType(m)


def is_uri(string: celtypes.Value) -> celpy.Result:
    valid = Uri(str(string)).uri()
    return celtypes.BoolType(valid)


def is_uri_ref(string: celtypes.Value) -> celpy.Result:
    valid = Uri(str(string)).uri_reference()
    return celtypes.BoolType(valid)


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


class Uri:
    _string: str
    _index: int
    _pct_encoded_found: bool

    def log(self, string: str):
        print("index is {} -- {}".format(self._index, string), file=sys.stderr)

    def __init__(self, string: str):
        super().__init__()
        self._string = string
        self._index = 0

    def uri(self) -> bool:
        """Determines whether string is a valid URI.

        Method parses the rule:
        URI = scheme ":" hier-part [ "?" query ] [ "#" fragment ]
        """
        start = self._index
        if not (self.__scheme() and self.__take(":") and self.__hier_part()):
            self._index = start
            return False

        if self.__take("?") and not self.__query():
            return False

        if self.__take("#") and not self.__fragment():
            return False

        if self._index != len(self._string):
            self._index = start
            return False

        return True

    def uri_reference(self) -> bool:
        """Determines whether string is a valid URI reference.

        Method parses the rule:
        URI-reference = URI / relative-ref
        """
        return self.uri() or self.__relative_ref()

    def __hier_part(self) -> bool:
        """Determines whether string contains a valid hier-part.

        Method parses the rule:

        hier-part = "//" authority path-abempty.
                  / path-absolute
                  / path-rootless
                  / path-empty
        """
        start = self._index
        if self.__take("/") and self.__take("/") and self.__authority() and self.__path_abempty():
            return True

        self._index = start

        self.log("made it here, which is bad")

        return self.__path_absolute() or self.__path_rootless() or self.__path_empty()

    def __relative_ref(self) -> bool:
        """Determines whether string contains a valid relative reference.

        Method parses the rule:

        relative-ref = relative-part [ "?" query ] [ "#" fragment ]
        """
        start = self._index
        if not self.__relative_part():
            return False

        if self.__take("?") and not self.__query():
            self._index = start
            return False

        if self.__take("#") and not self.__fragment():
            self._index = start
            return False

        if self._index != len(self._string):
            self._index = start
            return False

        return True

    def __relative_part(self) -> bool:
        """Determines whether string contains a valid relative part.

        Method parses the rule:

        relative-part = "//" authority path-abempty
                      / path-absolute
                      / path-noscheme
                      / path-empty
        """

        start = self._index
        if self.__take("/") and self.__take("/") and self.__authority() and self.__path_abempty():
            return True

        self._index = start

        return self.__path_absolute() or self.__path_noscheme() or self.__path_empty()

    def __scheme(self) -> bool:
        """Determines whether string contains a valid scheme.

        Method parses the rule:

        scheme = ALPHA *( ALPHA / DIGIT / "+" / "-" / "." )

        Terminated by ":".
        """

        start = self._index
        if self.__alpha():
            while self.__alpha() or self.__digit() or self.__take("+") or self.__take("-") or self.__take("."):
                pass

            if self._string[self._index] == ":":
                return True

        self._index = start
        return False

    def __authority(self) -> bool:
        """Determines whether string contains a valid authority.

        Method parses the rule:

        authority = [ userinfo "@" ] host [ ":" port ]

        Lead by double slash ("") and terminated by "/", "?", "#", or end of URI.
        """

        start = self._index
        if self.__userinfo():
            if not self.__take("@"):
                self._index = start
                self.log("done with userinfo")
                return False

        self.log("checking host")
        if not self.__host():
            self._index = start
            self.log("not a host")
            return False

        if self.__take(":"):
            if not self.__port():
                self._index = start
                return False

        self.log("is auth end check")
        if not self.__is_authority_end():
            self.log("not a auth end")
            self._index = start
            return False

        self.log("we passed")
        return True

    def __is_authority_end(self) -> bool:
        """Reports whether the current position is the end of the authority.

        The authority component [...] is terminated by the next slash ("/"),
        question mark ("?"), or number sign ("#") character, or by the
        end of the URI.
        """

        return (
            self._index >= len(self._string)
            or self._string[self._index] == "?"
            or self._string[self._index] == "#"
            or self._string[self._index] == "/"
        )

    def __userinfo(self) -> bool:
        """Determines whether string contains a valid userinfo.

        Method parses the rule:

        userinfo = *( unreserved / pct-encoded / sub-delims / ":" )

        Terminated by "@" in authority.
        """
        start = self._index
        while True:
            if self.__unreserved() or self.__pct_encoded() or self.__sub_delims() or self.__take(":"):
                continue

            if self._index < len(self._string):
                if self._string[self._index] == "@":
                    return True

            self._index = start
            return False

    def __check_host_pct_encoded(self, string: str) -> bool:
        """Verifies that string is correctly percent-encoded"""
        try:
            # unquote defaults to 'UTF-8' encoding.
            urlparse.unquote(string, errors="strict")
        except UnicodeError:
            return False

        return True

    def __host(self) -> bool:
        """Determines whether string contains a valid host.

        host parses the rule:

        host = IP-literal / IPv4address / reg-name.
        """
        if self._index >= len(self._string):
            return False

        start = self._index
        self._pct_encoded_found = False

        # Note: IPv4address is a subset of reg-name
        if (self._string[self._index] == "[" and self.__ip_literal()) or self.__reg_name():
            if self._pct_encoded_found:
                raw_host = self._string[start : self._index]
                # RFC 3986:
                # > URI producing applications must not use percent-encoding in host
                # > unless it is used to represent a UTF-8 character sequence.
                if not self.__check_host_pct_encoded(raw_host):
                    return False

            return True

        return False

    def __port(self) -> bool:
        """Determines whether string contains a valid port.

        host parses the rule:

        port = *DIGIT

        Terminated by end of authority.
        """
        start = self._index
        while True:
            if self.__digit():
                continue

            if self.__is_authority_end():
                return True

            self._index = start
            return False

    def __ip_literal(self) -> bool:
        """Determines whether string contains a valid port.

        ip_literal parses the rule from RFC 6874:

        IP-literal = "[" ( IPv6address / IPv6addrz / IPvFuture  ) "]"
        """

        start = self._index

        if self.__take("["):
            curr_idx = self._index
            if self.__ipv6_address() and self.__take("]"):
                return True

            self._index = curr_idx

            if self.__ipv6_addrz() and self.__take("]"):
                return True

            self._index = curr_idx

            if self.__ip_vfuture() and self.__take("]"):
                return True

        self._index = start
        return False

    def __ipv6_address(self) -> bool:
        """Determines whether string contains a valid ipv6 address.

        Method parses the rule "IPv6address".

        Relies on the implementation of is_ip.
        """
        start = self._index
        while self.__hex_dig() or self.__take(":"):
            pass

        if validate_ip(self._string[start : self._index], 6):
            return True

        self._index = start
        return False

    def __ipv6_addrz(self) -> bool:
        """Determines whether string contains a valid IPv6addrz.

        RFC 6874:

        IPv6addrz = IPv6address "%25" ZoneID
        """
        start = self._index
        if self.__ipv6_address() and self.__take("%") and self.__take("2") and self.__take("5") and self.__zone_id():
            return True

        self._index = start

        return False

    def __zone_id(self) -> bool:
        """Determines whether string contains a valid zone ID.

        RFC 6874:

        ZoneID = 1*( unreserved / pct-encoded )
        """

        start = self._index
        while self.__unreserved() or self.__pct_encoded():
            pass

        if self._index - start > 0:
            return True

        self._index = start

        return False

    def __ip_vfuture(self) -> bool:
        """Determines whether string contains a valid ipvFuture.

        IPvFuture  = "v" 1*HEXDIG "." 1*( unreserved / sub-delims / ":" )
        """
        start = self._index

        if self.__take("v") and self.__hex_dig():
            while self.__hex_dig():
                pass

            if self.__take("."):
                j = 0
                while self.__unreserved() or self.__sub_delims() or self.__take(":"):
                    j += 1

                if j >= 1:
                    return True

        self._index = start

        return False

    def __reg_name(self) -> bool:
        """Determines whether string contains a valid reg-name.

        reg-name = *( unreserved / pct-encoded / sub-delims )

        Terminates on start of port (":") or end of authority.
        """
        start = self._index
        while True:
            if self.__unreserved() or self.__pct_encoded() or self.__sub_delims():
                continue

            if self.__is_authority_end():
                # End of authority
                return True

            if self._string[self._index] == ":":
                return True

            self._index = start

            return False

    def __is_path_end(self) -> bool:
        """Determines whether the current index has reached the end of path.

        > The path is terminated by the first question mark ("?") or
        > number sign ("#") character, or by the end of the URI.
        """
        return self._index >= len(self._string) or self._string[self._index] == "?" or self._string[self._index] == "#"

    def __path_abempty(self) -> bool:
        """Determines whether string contains a path-abempty.

        path-abempty = *( "/" segment )

        Terminated by end of path: "?", "#", or end of URI.
        """
        start = self._index
        while self.__take("/") and self.__segment():
            pass

        self.log("done with segment loop")
        if self.__is_path_end():
            return True

        self._index = start

        return False

    def __path_absolute(self) -> bool:
        """Determines whether string contains a path-absolute.

        path-absolute = "/" [ segment-nz *( "/" segment ) ]

        Terminated by end of path: "?", "#", or end of URI.
        """
        start = self._index

        if self.__take("/"):
            if self.__segment_nz():
                while self.__take("/") and self.__segment():
                    pass

            if self.__is_path_end():
                return True

        self._index = start

        return False

    def __path_noscheme(self) -> bool:
        """Determines whether string contains a path-noscheme.

        path-noscheme = segment-nz-nc *( "/" segment )

        Terminated by end of path: "?", "#", or end of URI.
        """

        start = self._index
        if self.__segment_nz_nc():
            while self.__take("/") and self.__segment():
                pass

            if self.__is_path_end():
                return True

        self._index = start

        return True

    def __path_rootless(self) -> bool:
        """Determines whether string contains a path-rootless.

        path-rootless = segment-nz *( "/" segment )

        Terminated by end of path: "?", "#", or end of URI.
        """
        start = self._index

        if self.__segment_nz():
            while self.__take("/") and self.__segment():
                pass

            if self.__is_path_end():
                return True

        self._index = start

        return True

    def __path_empty(self) -> bool:
        """Determines whether string contains a path-empty.

        path-empty = 0<pchar>

        Terminated by end of path: "?", "#", or end of URI.
        """
        return self.__is_path_end()

    def __segment(self) -> bool:
        """Determines whether string contains a segment.

        segment = *pchar
        """

        while self.__pchar():
            pass

        return True

    def __segment_nz(self) -> bool:
        """Determines whether string contains a segment-nz.

        segment-nz = 1*pchar
        """
        start = self._index

        if self.__pchar():
            while self.__pchar():
                pass

            return True

        self._index = start

        return False

    def __segment_nz_nc(self) -> bool:
        """Determines whether string contains a segment-nz-nc.

        segment-nz-nc = 1*( unreserved / pct-encoded / sub-delims / "@" )
                      ; non-zero-length segment without any colon ":"
        """

        start = self._index

        while self.__unreserved() or self.__pct_encoded() or self.__sub_delims() or self.__take("@"):
            pass

        if self._index - start > 0:
            return True

        self._index = start

        return False

    def __pchar(self) -> bool:
        """Determines whether the character at the current index is a pchar.

        pchar = unreserved / pct-encoded / sub-delims / ":" / "@"
        """
        return (
            self.__unreserved() or self.__pct_encoded() or self.__sub_delims() or self.__take(":") or self.__take("@")
        )

    def __query(self) -> bool:
        """Determines whether string contains a valid query.

        query = *( pchar / "/" / "?" )

        Terminated by "#" or end of URI.
        """

        start = self._index

        while True:
            if self.__pchar() or self.__take("/") or self.__take("?"):
                continue

            if self._index == len(self._string) or self._string[self._index] == "#":
                return True

            self._index = start

            return False

    def __fragment(self) -> bool:
        """Determines whether string contains a valid fragment.

        fragment = *( pchar / "/" / "?" )

        Terminated by end of URI.
        """

        start = self._index

        while True:
            if self.__pchar() or self.__take("/") or self.__take("?"):
                continue

            if self._index == len(self._string):
                return True

            self._index = start

            return False

    def __pct_encoded(self) -> bool:
        """Determines whether string contains a valid percent encoding.

        pct-encoded = "%" HEXDIG HEXDIG

        Sets `_pct_encoded_found` to true if a valid triplet was found
        """
        start = self._index

        if self.__take("%") and self.__hex_dig() and self.__hex_dig():
            self._pct_encoded_found = True
            return True

        self._index = start

        return False

    def __unreserved(self) -> bool:
        """Determines whether the character at the current index is unreserved.

        unreserved = ALPHA / DIGIT / "-" / "." / "_" / "~"
        """
        return (
            self.__alpha()
            or self.__digit()
            or self.__take("-")
            or self.__take("_")
            or self.__take(".")
            or self.__take("~")
        )

    def __sub_delims(self) -> bool:
        """Determines whether the character at the current index is a sub-delim.

        sub-delims  = "!" / "$" / "&" / "'" / "(" / ")"
                    / "*" / "+" / "," / ";" / "="
        """
        return (
            self.__take("!")
            or self.__take("$")
            or self.__take("&")
            or self.__take("'")
            or self.__take("(")
            or self.__take(")")
            or self.__take("*")
            or self.__take("+")
            or self.__take(",")
            or self.__take(";")
            or self.__take("=")
        )

    def __alpha(self) -> bool:
        """Determines whether the character at the current index is an alpha char.

        alpha parses the rule:

        ALPHA =  %x41-5A / %x61-7A ; A-Z / a-z
        """

        if self._index >= len(self._string):
            return False

        c = self._string[self._index]
        if ("A" <= c <= "Z") or ("a" <= c <= "z"):
            self._index += 1
            return True

        return False

    def __digit(self) -> bool:
        """Determines whether the character at the current index is a digit.

        Method parses the rule:

        DIGIT = %x30-39  ; 0-9
        """

        if self._index >= len(self._string):
            return False

        c = self._string[self._index]
        if "0" <= c <= "9":
            self._index += 1
            return True

        return False

    def __hex_dig(self) -> bool:
        """Determines whether the character at the current index is a hex digit.

        Method parses the rule:

        HEXDIG =  DIGIT / "A" / "B" / "C" / "D" / "E" / "F"
        """

        if self._index >= len(self._string):
            return False

        c = self._string[self._index]

        if ("0" <= c <= "9") or ("a" <= c <= "f") or ("A" <= c <= "F") or ("0" <= c <= "9"):
            self._index += 1

            return True

        return False

    def __take(self, char: str) -> bool:
        """Take the given char at the current index.

        If char is at the current index, increment the index.

        Returns:
            True if char is at the current index. False if char is not at the
            current index or the end of string has been reached.
        """

        if self._index >= len(self._string):
            return False

        if self._string[self._index] == char:
            self._index += 1
            return True

        return False


def make_extra_funcs(locale: str) -> dict[str, celpy.CELFunction]:
    # TODO(#257): Fix types and add tests for StringFormat.
    # For now, ignoring the type.
    string_fmt = string_format.StringFormat(locale)  # type: ignore
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
