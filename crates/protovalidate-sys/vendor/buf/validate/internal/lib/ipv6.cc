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

#include "buf/validate/internal/lib/ipv6.h"

#include <array>
#include <cstdint>

#include "buf/validate/internal/lib/parser_common.h"

namespace buf::validate::internal::lib {

namespace {

struct IPv6Parser : ParserCommon, public IPv6Prefix {
  static const size_t hexadecatets_count = 8;

  bool consumeZoneId() {
    if (str.empty()) {
      return false;
    }
    do {
      if (str[0] == '\0') {
        return false;
      }
      str = str.substr(1);
    } while (!str.empty());
    return true;
  }

  bool checkDotted() {
    // The dotted segment can't be smaller than the smallest possible address
    // (e.g. single digits in each octet)
    constexpr int minLength = std::char_traits<char>::length("0.0.0.0");
    if (str.length() < minLength) {
      return false;
    }
    return str[0] != ':' && (str[1] == '.' || str[2] == '.' || str[3] == '.');
  }

  bool parseDotted() {
    std::array<uint8_t, 4> octets;
    if (!parseDecimalOctet(octets[0]) || !consume<Char<'.'>>() || //
        !parseDecimalOctet(octets[1]) || !consume<Char<'.'>>() || //
        !parseDecimalOctet(octets[2]) || !consume<Char<'.'>>() || //
        !parseDecimalOctet(octets[3])) {
      return false;
    }
    bits |= static_cast<uint32_t>(octets[0]) << 24;
    bits |= static_cast<uint32_t>(octets[1]) << 16;
    bits |= static_cast<uint32_t>(octets[2]) << 8;
    bits |= static_cast<uint32_t>(octets[3]);
    return true;
  }

  bool consumePrefixLength() { return parseDecimalNumber<uint8_t, bits_count>(prefixLength); }

  bool parseAddressPart() {
    std::bitset<bits_count> b;
    int index = 0;
    bool doubleColonFound = false;
    uint16_t value;
    while (index < hexadecatets_count) {
      if ((doubleColonFound || index == hexadecatets_count - 2) && checkDotted()) {
        if (!parseDotted()) {
          return false;
        }
        b <<= 32;
        index += 2;
        break;
      } else if (parseHexadecimalHexadecatet(value)) {
        b <<= 16;
        b |= value;
        index++;
      } else if (consumeSequence<':', ':'>()) {
        if (consume<Char<':'>>()) {
          return false;
        }
        if (index > hexadecatets_count - 1 || doubleColonFound) {
          return false;
        }
        bits |= b << ((hexadecatets_count - index) << 4);
        b.reset();
        doubleColonFound = true;
        // This ensures that we can't have more than 7 hexadecatets when there's
        // a double-colon, even though we don't actually process a hexadecatet.
        index++;
      } else if (consume<Char<':'>>()) {
        if (index == 0 || str.empty()) {
          // Can not start or end on a single colon.
          return false;
        }
        continue;
      } else {
        // Unable to match anything: this is the end.
        break;
      }
    }
    bits |= b;
    // The parsed result is valid if we've either seen the double colon, or the
    // length is exactly 8 hexadecatets.
    return doubleColonFound || index == hexadecatets_count;
  }

  bool parseAddress() {
    return parseAddressPart() && (!consume<Char<'%'>>() || consumeZoneId()) && str.empty();
  }

  bool parsePrefix() {
    return parseAddressPart() && consume<Char<'/'>>() && consumePrefixLength() && str.empty();
  }
};

} // namespace

std::optional<IPv6Address> parseIPv6Address(std::string_view str) {
  IPv6Parser address{str};
  if (!address.parseAddress()) {
    return std::nullopt;
  }
  return address;
}

std::optional<IPv6Prefix> parseIPv6Prefix(std::string_view str) {
  IPv6Parser prefix{str};
  if (!prefix.parsePrefix()) {
    return std::nullopt;
  }
  return prefix;
}

} // namespace buf::validate::internal::lib
