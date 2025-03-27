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
import typing
from urllib import parse as urlparse

import celpy
from celpy import celtypes

from protovalidate.internal import string_format

# See https://html.spec.whatwg.org/multipage/input.html#valid-e-mail-address
_email_regex = re.compile(
    r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
)


def is_ip(val: celtypes.Value, ver: typing.Optional[celtypes.Value] = None) -> celpy.Result:
    """Validate whether a given string is a valid IP address according to an optional IP version.

    IPv4 addresses are expected in the dotted decimal format, for example "192.168.5.21".
    IPv6 addresses are expected in their text representation, for example "::1" or "2001:0DB8:ABCD:0012::0".

    Both formats are well-defined in the internet standard RFC 3986. Zone
    identifiers for IPv6 addresses (for example "fe80::a%en1") are supported.

    Args:
        val (celTypes.Value): The string to validate.
        version (typing.Optional[celtypes.Value]): An optional version to use for validating the IP address.
            Passing None for a version of 0 means either 4 or 6.
            Passing a version other than 0, 4, or 6 always returns False.

    Returns:
        True if the string is an IPv4 or IPv6 address, optionally limited to a specific version.

    Raises:
        celpy.CELEvalError: If val is not an instance of celtypes.StringType or
                            if version is not an instance of celtypes.IntType and is not None.
    """

    if not isinstance(val, celtypes.StringType):
        msg = "invalid argument, expected string"
        raise celpy.CELEvalError(msg)
    if not isinstance(ver, celtypes.IntType) and ver is not None:
        msg = "invalid argument, expected int"
        raise celpy.CELEvalError(msg)

    if ver is None:
        version = 0
    else:
        version = ver

    return celtypes.BoolType(_is_ip(val, version))


def _is_ip(string: str, version: int) -> bool:
    """Internal implementation"""
    valid = False
    if version == 6:
        valid = Ipv6(string).address()
    elif version == 4:
        valid = Ipv4(string).address()
    elif version == 0:
        valid = Ipv4(string).address() or Ipv6(string).address()

    return valid


def is_ip_prefix(val: celtypes.Value, *args) -> celpy.Result:
    if not isinstance(val, celtypes.StringType):
        msg = "invalid argument, expected string or bytes"
        raise celpy.CELEvalError(msg)
    version = 0
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

    return celtypes.BoolType(_is_ip_prefix(val, version, strict=strict))


def _is_ip_prefix(string: str, version: int, *, strict=False) -> bool:
    """Internal implementation"""
    valid = False
    if version == 6:
        v6 = Ipv6(string)
        valid = v6.address_prefix() and (not strict or v6.is_prefix_only())
    elif version == 4:
        v4 = Ipv4(string)
        valid = v4.address_prefix() and (not strict or v4.is_prefix_only())
    elif version == 0:
        valid = _is_ip_prefix(string, 6, strict=strict) or _is_ip_prefix(string, 4, strict=strict)

    return valid


def is_email(string: celtypes.Value) -> celpy.Result:
    """Return true if the string is an email address, for example "foo@example.com".

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
    """Return true if the string is a URI, for example "https://example.com/foo/bar?baz=quux#frag".

    URI is defined in the internet standard RFC 3986.
    Zone Identifiers in IPv6 address literals are supported (RFC 6874).

    """
    if not isinstance(string, celtypes.StringType):
        msg = "invalid argument, expected string"
        raise celpy.CELEvalError(msg)
    valid = Uri(str(string)).uri()
    return celtypes.BoolType(valid)


def is_uri_ref(string: celtypes.Value) -> celpy.Result:
    """Return true if the string is a URI Reference - a URI such as "https://example.com/foo/bar?baz=quux#frag" or
    a Relative Reference such as "./foo/bar?query".

    URI, URI Reference, and Relative Reference are defined in the internet standard RFC 3986.
    Zone Identifiers in IPv6 address literals are supported (RFC 6874).

    """
    if not isinstance(string, celtypes.StringType):
        msg = "invalid argument, expected string"
        raise celpy.CELEvalError(msg)
    valid = Uri(str(string)).uri_reference()
    return celtypes.BoolType(valid)


def is_hostname(val: celtypes.Value) -> celpy.Result:
    if not isinstance(val, celtypes.StringType):
        msg = "invalid argument, expected string"
        raise celpy.CELEvalError(msg)
    return celtypes.BoolType(_is_hostname(val))


def _is_hostname(val: str) -> bool:
    if len(val) > 253:
        return False

    if val.endswith(val.lower()):
        string = val[0 : len(val) - 1]
    else:
        string = val

    all_digits = False
    parts = string.lower().split(sep=".")

    # split hostname on '.' and validate each part
    for part in parts:
        all_digits = True

        # if part is empty, longer than 63 chars, or starts/ends with '-', it is invalid
        part_len = len(part)

        if part_len == 0 or part_len > 63 or part.startswith("-") or part.endswith("-"):
            return False

        for c in part:
            # if the character is not a-z, 0-9, or '-', it is invalid
            if (c < "a" or c > "z") and (c < "0" or c > "9") and c != "-":
                return False

            all_digits = all_digits and c >= "0" and c <= "9"

    # the last part cannot be all numbers
    return not all_digits


def _is_port(val: str) -> bool:
    if len(val) == 0:
        return False

    for c in val:
        if c < "0" or c > "9":
            return False

    try:
        return int(val) <= 65535

    except ValueError:
        # Error converting to number
        return False


def is_host_and_port(string: celtypes.Value, port_required: celtypes.Value) -> celpy.Result:
    if not isinstance(string, celtypes.StringType):
        msg = "invalid argument, expected string"
        raise celpy.CELEvalError(msg)
    if not isinstance(port_required, celtypes.BoolType):
        msg = "invalid argument, expected bool"
        raise celpy.CELEvalError(msg)
    return celtypes.BoolType(_is_host_and_port(string, port_required=bool(port_required)))


def _is_host_and_port(val: str, *, port_required=False) -> bool:
    if len(val) == 0:
        return False

    split_idx = val.rfind(":")
    if val[0] == "[":
        end = val.rfind("]")
        end_plus = end + 1

        if end_plus == len(val):
            return not port_required and _is_ip(val[1:end], 6)
        elif end_plus == split_idx:
            return _is_ip(val[1:end], 6) and _is_port(val[split_idx + 1 :])
        else:
            # malformed
            return False

    if split_idx < 0:
        return not port_required and (_is_hostname(val) or _is_ip(val, 4))

    host = val[0:split_idx]
    port = val[split_idx + 1 :]

    return (_is_hostname(host) or _is_ip(host, 4)) and _is_port(port)


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


class Ipv4:
    """a class"""

    _string: str
    _index: int
    _octets: bytearray
    _prefix_len: int

    def __init__(self, string: str):
        """ipv4

        Args:
        """

        super().__init__()
        self._string = string
        self._index = 0
        self._octets = bytearray()
        self._prefix_len = 0

    def address(self) -> bool:
        """Parses an IPv4 Address in dotted decimal notation."""
        return self.__address_part() and self._index == len(self._string)

    def address_prefix(self) -> bool:
        """Parses an IPv4 Address prefix."""
        return (
            self.__address_part() and self.__take("/") and self.__prefix_length() and self._index == len(self._string)
        )

    def get_bits(self) -> int:
        """Get the bits of an address parsed through address() or address_prefix()

        Returns:
            The 32-bit value if address was parsed successfully. 0 if not successful.
        """
        if len(self._octets) != 4:
            return 0

        return (self._octets[0] << 24) | (self._octets[1] << 16) | (self._octets[2] << 8) | self._octets[3]

    def is_prefix_only(self) -> bool:
        """Determines TODO

        Behavior is undefined if address_prefix() has not been called before or has returned false.

        Returns:
            True if all bits to the right of the prefix-length are all zeros. False otherwise.
        """
        bits = self.get_bits()

        mask: int
        if self._prefix_len == 32:
            mask = 0xFFFFFFFF
        else:
            mask = ~(0xFFFFFFFF >> self._prefix_len)

        masked = bits & mask

        return bits == masked

    def __prefix_length(self) -> bool:
        start = self._index

        while True:
            if self._index >= len(self._string) or not self.__digit():
                break

            if self._index - start > 2:
                # max prefix-length is 32 bits, so anything more than 2 digits is invalid
                return False

        string = self._string[start : self._index]
        if len(string) == 0:
            # too short
            return False

        if len(string) > 1 and string[0] == "0":
            # bad leading 0
            return False

        try:
            value = int(string)

            if value > 32:
                # max 32 bits
                return False

            self._prefix_len = value

            return True

        except ValueError:
            # Error converting to number
            return False

    def __address_part(self) -> bool:
        start = self._index

        if (
            self.__dec_octet()
            and self.__take(".")
            and self.__dec_octet()
            and self.__take(".")
            and self.__dec_octet()
            and self.__take(".")
            and self.__dec_octet()
        ):
            return True

        self._index = start

        return False

    def __dec_octet(self) -> bool:
        start = self._index

        while True:
            if self._index >= len(self._string) or not self.__digit():
                break

            if self._index - start > 3:
                # decimal octet can be three characters at most
                return False

        string = self._string[start : self._index]

        if len(string) == 0:
            # too short
            return False

        if len(string) > 1 and string[0] == "0":
            # bad leading 0
            return False

        try:
            value = int(string)

            if value > 255:
                return False

            self._octets.append(value)

            return True

        except ValueError:
            # Error converting to number
            return False

    def __digit(self) -> bool:
        """Reports whether the current position is a digit.

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


class Ipv6:
    """a class"""

    _string: str
    _index: int
    _pieces: list[int]
    _double_colon_at: int
    _double_colon_seen: bool
    _dotted_raw: str
    _dotted_addr: typing.Optional[Ipv4]
    _zone_id_found: bool
    _prefix_len: int

    def __init__(self, string: str):
        """ipv6

        Args:

        Attributes:
            _string (str): The string to parse.
            _index (int): The index.
            _pieces (list[int]): 16-bit pieces found.
            _double_colon_at (bool): Number of 16-bit pieces found when double colon was found.
            _double_colon_seen (bool): Whether a double colon has been seen in string.
            _dotted_raw (str): Dotted notation for right-most 32 bits.
            _dotted_addr (typing.Optional[Ipv4]): Dotted notation successfully parsed as Ipv4.
            _zone_id_found (bool): Whether a zone ID has been found in string.
            _prefix_len (int): 0 - 128
        """

        super().__init__()
        self._string = string
        self._index = 0
        self._pieces = []
        self._double_colon_at = -1
        self._double_colon_seen = False
        self._dotted_raw = ""
        self._dotted_addr = None
        self._zone_id_found = False

    def get_bits(self) -> int:
        """Get the bits of an address parsed through address() or address_prefix() as a 128-bit integer.

        Returns:
            The 128-bit value if address was parsed successfully. 0 if no address was parsed successfully.
        """

        p16 = self._pieces

        # Handle dotted decimal, add to p16
        if self._dotted_addr is not None:
            # Right-most 32 bits
            dotted32 = self._dotted_addr.get_bits()
            # High 16 bits
            p16.append(dotted32 >> 16)
            # Low 16 bits
            p16.append(dotted32)

        # Handle double colon, fill pieces with 0
        if self._double_colon_seen:
            while True:
                if len(p16) >= 8:
                    break

                # Delete 0 entries at pos, insert a 0
                p16.insert(self._double_colon_at, 0x00000000)

        if len(p16) != 8:
            return 0

        return (
            p16[0] << 112
            | p16[1] << 96
            | p16[2] << 80
            | p16[3] << 64
            | p16[4] << 48
            | p16[5] << 32
            | p16[6] << 16
            | p16[7]
        )

    def is_prefix_only(self) -> bool:
        """Determine whether string is an ipv6 prefix only.

        Behavior is undefined if address_prefix() has not been called before.

        Returns:
            True if all bits to the right of the prefix-length are all zeros. False otherwise.
        """
        bits = self.get_bits()
        mask: int
        if self._prefix_len >= 128:
            mask = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        elif self._prefix_len < 0:
            mask = 0x00000000000000000000000000000000
        else:
            mask = ~(0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF >> self._prefix_len)

        masked = bits & mask
        if bits != masked:
            return False

        return True

    def address(self) -> bool:
        """Parse an IPv6 Address following RFC 4291, with optional zone id following RFC 4007."""

        return self.__address_part() and self._index == len(self._string)

    def address_prefix(self) -> bool:
        """Parse an IPv6 Address Prefix following RFC 4291. Zone id is not permitted."""

        return (
            self.__address_part()
            and not self._zone_id_found
            and self.__take("/")
            and self.__prefix_length()
            and self._index == len(self._string)
        )

    def __prefix_length(self) -> bool:
        start = self._index

        while True:
            if self._index >= len(self._string) or not self.__digit():
                break

            if self._index - start > 3:
                return False

        string = self._string[start : self._index]

        if len(string) == 0:
            # too short
            return False

        if len(string) > 1 and string[0] == "0":
            # bad leading 0
            return False

        try:
            value = int(string)

            if value > 128:
                # max 128 bits
                return False

            self._prefix_len = value

            return True

        except ValueError:
            # Error converting to number
            return False

    def __address_part(self) -> bool:
        """Store the dotted notation for right-most 32 bits in dottedRaw / dottedAddr if found."""

        while True:
            if self._index >= len(self._string):
                break

            # dotted notation for right-most 32 bits, e.g. 0:0:0:0:0:ffff:192.1.56.10
            if self._double_colon_seen or (len(self._pieces) == 6 and self.__dotted()):
                dotted = Ipv4(self._dotted_raw)

                if dotted.address():
                    self._dotted_addr = dotted
                    return True

                return False

            if self.__h16():
                continue

            if self.__take(":"):
                if self.__take(":"):
                    if self._double_colon_seen:
                        return False

                    self._double_colon_seen = True
                    self._double_colon_at = len(self._pieces)

                    if self.__take(":"):
                        return False

                continue

            if self._string[self._index] == "%" and not self.__zone_id():
                return False

            break

        return self._double_colon_seen or len(self._pieces) == 8

    def __zone_id(self) -> bool:
        """Determine whether string contains a zoneID.

        Method parses the rule from RFC 6874:

        ZoneID = 1*( unreserved / pct-encoded )

        There is no definition for the character set allowed in the zone identifier.
        RFC 4007 permits basically any non-null string.
        """

        start = self._index

        if self.__take("%"):
            if len(self._string) - self._index > 0:
                # permit any non-null string
                self._index = len(self._string)
                self._zone_id_found = True

                return True

        self._index = start
        self._zone_id_found = False

        return False

    def __dotted(self) -> bool:
        """Determine whether string contains a dotted address.

        Method parses the rule:

        1*3DIGIT "." 1*3DIGIT "." 1*3DIGIT "." 1*3DIGIT

        Stores match in _dotted_raw.
        """

        start = self._index
        self._dotted_raw = ""

        while True:
            if self._index < len(self._string) and (self.__digit() or self.__take(".")):
                continue

            break

        if self._index - start >= 7:
            self._dotted_raw = self._string[start : self._index]
            return True

        self._index = start

        return False

    def __h16(self) -> bool:
        """Determine whether string contains an h16.

        Method parses the rule:

        h16 = 1*4HEXDIG

        Stores 16-bit value in _pieces.
        """

        start = self._index

        while True:
            if self._index >= len(self._string) or not self.__hex_dig():
                break

        string = self._string[start : self._index]

        if len(string) == 0:
            # too short
            return False

        if len(string) > 4:
            # too long
            return False

        try:
            value = int(string, 16)

            self._pieces.append(value)

            return True

        except ValueError:
            # Error converting to number
            return False

        return True

    def __hex_dig(self) -> bool:
        """Report whether the current position is a hex digit.

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

    def __digit(self) -> bool:
        """Report whether the current position is a digit.

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


class Uri:
    """Uri is a class used to parse a given string to determine if it is a valid URI or URI reference."""

    _string: str
    _index: int
    _pct_encoded_found: bool

    def __init__(self, string: str):
        """Initialize a URI validation class with a given string."""
        super().__init__()
        self._string = string
        self._index = 0

    def uri(self) -> bool:
        """Determine whether string is a valid URI.

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
        """Determine whether string is a valid URI reference.

        Method parses the rule:

            URI-reference = URI / relative-ref

        """
        return self.uri() or self.__relative_ref()

    def __hier_part(self) -> bool:
        """Determine whether string contains a valid hier-part.

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

        return self.__path_absolute() or self.__path_rootless() or self.__path_empty()

    def __relative_ref(self) -> bool:
        """Determine whether string contains a valid relative reference.

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
        """Determine whether string contains a valid relative part.

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
        """Determine whether string contains a valid scheme.

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
        """Determine whether string contains a valid authority.

        Method parses the rule:

            authority = [ userinfo "@" ] host [ ":" port ]

        Lead by double slash ("") and terminated by "/", "?", "#", or end of URI.

        """
        start = self._index
        if self.__userinfo():
            if not self.__take("@"):
                self._index = start
                return False

        if not self.__host():
            self._index = start
            return False

        if self.__take(":"):
            if not self.__port():
                self._index = start
                return False

        if not self.__is_authority_end():
            self._index = start
            return False

        return True

    def __is_authority_end(self) -> bool:
        """Report whether the current position is the end of the authority.

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
        """Determine whether string contains a valid userinfo.

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
        """Verify that string is correctly percent-encoded."""
        try:
            # unquote defaults to 'UTF-8' encoding.
            urlparse.unquote(string, errors="strict")
        except UnicodeError:
            return False

        return True

    def __host(self) -> bool:
        """Determine whether string contains a valid host.

        Method parses the rule:

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
        """Determine whether string contains a valid port.

        Method parses the rule:

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
        """Determine whether string contains a valid port.

        Method parses the rule from RFC 6874:

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
        """Determine whether string contains a valid ipv6 address.

        Method parses the rule "IPv6address".

        Relies on the implementation of _is_ip.

        """
        start = self._index
        while self.__hex_dig() or self.__take(":"):
            pass

        if _is_ip(self._string[start : self._index], 6):
            return True

        self._index = start
        return False

    def __ipv6_addrz(self) -> bool:
        """Determine whether string contains a valid IPv6addrz.

        Method parses the rule from RFC 6874:

            IPv6addrz = IPv6address "%25" ZoneID

        """
        start = self._index
        if self.__ipv6_address() and self.__take("%") and self.__take("2") and self.__take("5") and self.__zone_id():
            return True

        self._index = start

        return False

    def __zone_id(self) -> bool:
        """Determine whether string contains a valid zone ID.

        Method parses the rule from RFC 6874:

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
        """Determine whether string contains a valid ipvFuture.

        Method parses the rule:

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
        """Determine whether string contains a valid reg-name.

        Method parses the rule:

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
        """Determine whether the current index has reached the end of path.

        > The path is terminated by the first question mark ("?") or
        > number sign ("#") character, or by the end of the URI.

        """
        return self._index >= len(self._string) or self._string[self._index] == "?" or self._string[self._index] == "#"

    def __path_abempty(self) -> bool:
        """Determine whether string contains a path-abempty.

        Method parses the rule:

            path-abempty = *( "/" segment )

        Terminated by end of path: "?", "#", or end of URI.

        """
        start = self._index
        while self.__take("/") and self.__segment():
            pass

        if self.__is_path_end():
            return True

        self._index = start

        return False

    def __path_absolute(self) -> bool:
        """Determine whether string contains a path-absolute.

        Method parses the rule:

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
        """Determine whether string contains a path-noscheme.

        Method parses the rule:

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
        """Determine whether string contains a path-rootless.

        Method parses the rule:

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
        """Determine whether string contains a path-empty.

        Method parses the rule:

            path-empty = 0<pchar>

        Terminated by end of path: "?", "#", or end of URI.

        """
        return self.__is_path_end()

    def __segment(self) -> bool:
        """Determine whether string contains a segment.

        Method parses the rule:

            segment = *pchar

        """
        while self.__pchar():
            pass

        return True

    def __segment_nz(self) -> bool:
        """Determine whether string contains a segment-nz.

        Method parses the rule:

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
        """Determine whether string contains a segment-nz-nc.

        Method parses the rule:

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
        """Report whether the current position is a pchar.

        Method parses the rule:

            pchar = unreserved / pct-encoded / sub-delims / ":" / "@"

        """
        return (
            self.__unreserved() or self.__pct_encoded() or self.__sub_delims() or self.__take(":") or self.__take("@")
        )

    def __query(self) -> bool:
        """Determine whether string contains a valid query.

        Method parses the rule:

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
        """Determine whether string contains a valid fragment.

        Method parses the rule:

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
        """Determine whether string contains a valid percent encoding.

        Method parses the rule:

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
        """Report whether the current position is an unreserved character.

        Method parses the rule:

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
        """Report whether the current position is a sub-delim.

        Method parses the rule:

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
        """Report whether the current position is an alpha character.

        Method parses the rule:

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
        """Report whether the current position is a digit.

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
        """Report whether the current position is a hex digit.

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
