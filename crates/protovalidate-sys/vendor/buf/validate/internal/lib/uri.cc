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

#include "buf/validate/internal/lib/uri.h"

#include <array>
#include <cstdint>

#include "buf/validate/internal/lib/parser_common.h"

namespace buf::validate::internal::lib {

namespace {

struct UriParser : ParserCommon {
  using Unreserved = ConcatRanges<
      Alpha, //
      Num, //
      Char<'-'>, //
      Char<'_'>, //
      Char<'.'>, //
      Char<'~'>>;

  using SubDelims = ConcatRanges<
      Char<'!'>, //
      Char<'$'>, //
      Char<'&'>, //
      Char<'\''>, //
      Char<'('>, //
      Char<')'>, //
      Char<'*'>, //
      Char<'+'>, //
      Char<','>, //
      Char<';'>, //
      Char<'='>>;

  bool validateUri() { return consumeUri() && str.empty(); }

  bool consumeUri() {
    auto start = str;
    if (!(consumeScheme() && consume<Char<':'>>() && consumeHierPart())) {
      str = start;
      return false;
    }
    if (consume<Char<'?'>>() && !consumeQuery()) {
      str = start;
      return false;
    }
    if (consume<Char<'#'>>() && !consumeFragment()) {
      str = start;
      return false;
    }
    return true;
  }

  bool consumeHierPart() {
    auto start = str;
    if (consumeSequence<'/', '/'>() && consumeAuthority() && consumePathAbempty()) {
      return true;
    }
    str = start;
    return consumePathAbsolute() || consumePathRootless() || consumePathEmpty();
  }

  bool validateUriReference() { return (consumeUri() || consumeRelativeRef()) && str.empty(); }

  bool consumeRelativeRef() {
    auto start = str;
    if (!consumeRelativePart()) {
      return false;
    }
    if (consume<Char<'?'>>() && !consumeQuery()) {
      str = start;
      return false;
    }
    if (consume<Char<'#'>>() && !consumeFragment()) {
      str = start;
      return false;
    }
    return true;
  }

  bool consumeRelativePart() {
    auto start = str;
    if (consumeSequence<'/', '/'>() && consumeAuthority() && consumePathAbempty()) {
      return true;
    }
    str = start;
    return consumePathAbsolute() || consumePathNoscheme() || consumePathEmpty();
  }

  bool consumeScheme() {
    auto start = str;
    if (consume<Alpha>()) {
      while (consume<ConcatRanges<AlphaNum, Char<'+'>, Char<'-'>, Char<'.'>>>()) {
        // continue
      }
      if (!str.empty() && str[0] == ':') {
        return true;
      }
    }
    str = start;
    return false;
  }

  bool consumeAuthority() {
    auto start = str;
    if (consumeUserInfo() && !consume<Char<'@'>>()) {
      str = start;
      return false;
    }
    if (!consumeHost()) {
      str = start;
      return false;
    }
    if (consume<Char<':'>>() && !consumePort()) {
      str = start;
      return false;
    }
    if (!this->isAuthorityEnd()) {
      str = start;
      return false;
    }
    return true;
  }

  bool isAuthorityEnd() {
    return str.empty() || //
        str[0] == '?' || //
        str[0] == '#' || //
        str[0] == '/';
  }

  bool consumeUserInfo() {
    auto start = str;
    for (;;) {
      if (consume<ConcatRanges<Unreserved, SubDelims, Char<':'>>>() || consumePercentEncoded()) {
        continue;
      }
      if (!str.empty() && str[0] == '@') {
        return true;
      }
      str = start;
      return false;
    }
  }

  bool consumeHost() {
    if (!str.empty() && str[0] == '[' && consumeIPLiteral()) {
      return true;
    }
    return consumeRegName();
  }

  bool consumePort() {
    auto start = str;
    for (;;) {
      if (consume<Num>()) {
        continue;
      }
      if (isAuthorityEnd()) {
        return true;
      }
      str = start;
      return false;
    }
  }

  bool consumeIPLiteral() {
    auto start = str;
    if (consume<Char<'['>>()) {
      auto j = str;
      if (consumeIPv6Address() && consume<Char<']'>>()) {
        return true;
      }
      str = j;
      if (consumeIPVFuture() && consume<Char<']'>>()) {
        return true;
      }
    }
    str = start;
    return false;
  }

  bool consumeIPv6Address() {
    // These is a simplified IPv6 parser, since we don't care about prefixes or
    // the actual values. See ipv6.cc for more details and comments.
    const size_t hexadecatets_count = 8;
    int index = 0;
    bool doubleColonFound = false;
    while (index < hexadecatets_count) {
      if ((doubleColonFound || index == hexadecatets_count - 2) &&
          str.length() >= std::char_traits<char>::length("0.0.0.0") && str[0] != ':' &&
          (str[1] == '.' || str[2] == '.' || str[3] == '.')) {
        uint8_t _;
        return parseDecimalOctet(_) && consume<Char<'.'>>() && //
            parseDecimalOctet(_) && consume<Char<'.'>>() && //
            parseDecimalOctet(_) && consume<Char<'.'>>() && //
            parseDecimalOctet(_);
      } else if (uint16_t _; parseHexadecimalHexadecatet(_)) {
        index++;
      } else if (consumeSequence<':', ':'>()) {
        if (consume<Char<':'>>() || index++ > hexadecatets_count - 1 || doubleColonFound) {
          return false;
        }
        doubleColonFound = true;
      } else if (consume<Char<':'>>()) {
        if (index == 0 || str.empty()) {
          return false;
        }
        continue;
      } else {
        break;
      }
    }
    return (doubleColonFound || index == hexadecatets_count) &&
        (!consumeSequence<'%', '2', '5'>() || consumeZoneId());
  }

  bool consumeZoneId() {
    auto start = str;
    while (consume<Unreserved>() || consumePercentEncodedUTF8CodePoint()) {
      // continue
    }
    return start != str;
  }

  bool consumeIPVFuture() {
    auto start = str;
    if (consume<Char<'v'>>() && consume<HexDigit>()) {
      while (consume<HexDigit>()) {
        // continue
      }
      if (consume<Char<'.'>>()) {
        int j = 0;
        while (consume<ConcatRanges<Unreserved, SubDelims, Char<':'>>>()) {
          j++;
        }
        if (j >= 1) {
          return true;
        }
      }
    }
    str = start;
    return false;
  }

  bool consumeRegName() {
    auto start = str;
    for (;;) {
      if (consume<ConcatRanges<Unreserved, SubDelims>>() || consumePercentEncodedUTF8CodePoint()) {
        continue;
      }
      if (!str.empty() && str[0] == ':') {
        return true;
      }
      if (isAuthorityEnd()) {
        return true;
      }
      str = start;
      return false;
    }
  }

  bool isPathEnd() { return str.empty() || str[0] == '?' || str[0] == '#'; }

  bool consumePathAbempty() {
    auto start = str;
    while (consume<Char<'/'>>() && consumeSegment()) {
      // continue
    }
    if (isPathEnd()) {
      return true;
    }
    str = start;
    return false;
  }

  bool consumePathAbsolute() {
    auto start = str;
    if (consume<Char<'/'>>()) {
      if (consumeSegmentNz()) {
        while (consume<Char<'/'>>() && consumeSegment()) {
          // continue
        }
      }
      if (isPathEnd()) {
        return true;
      }
    }
    str = start;
    return false;
  }

  bool consumePathNoscheme() {
    auto start = str;
    if (consumeSegmentNzNc()) {
      while (consume<Char<'/'>>() && consumeSegment()) {
        // continue
      }
      if (isPathEnd()) {
        return true;
      }
    }
    str = start;
    return false;
  }

  bool consumePathRootless() {
    auto start = str;
    if (consumeSegmentNz()) {
      while (consume<Char<'/'>>() && consumeSegment()) {
        // continue
      }
      if (isPathEnd()) {
        return true;
      }
    }
    str = start;
    return false;
  }

  bool consumePathEmpty() { return isPathEnd(); }

  bool consumeSegment() {
    while (consumePChar()) {
      // continue
    }
    return true;
  }

  bool consumeSegmentNz() {
    if (!consumePChar()) {
      return false;
    }
    return consumeSegment();
  }

  bool consumeSegmentNzNc() {
    auto start = str;
    while (consume<ConcatRanges<Unreserved, SubDelims, Char<'@'>>>() || consumePercentEncoded()) {
      // continue
    }
    return str != start;
  }

  template <typename... T>
  bool consumePChar() {
    return consume<ConcatRanges<Unreserved, SubDelims, Char<':'>, Char<'@'>, T...>>() ||
        consumePercentEncoded();
  }

  bool consumeQuery() {
    auto start = str;
    for (;;) {
      if (consumePChar<Char<'/'>, Char<'?'>>()) {
        continue;
      }
      if (str.empty() || str[0] == '#') {
        return true;
      }
      str = start;
      return false;
    }
  }

  bool consumeFragment() {
    auto start = str;
    for (;;) {
      if (consumePChar<Char<'/'>, Char<'?'>>()) {
        continue;
      }
      if (str.empty()) {
        return true;
      }
      str = start;
      return false;
    }
  }

  bool consumePercentEncoded() {
    auto start = str;
    if (consume<Char<'%'>>() && consume<HexDigit>() && consume<HexDigit>()) {
      return true;
    }
    str = start;
    return false;
  }

  bool parsePercentEncoded(uint8_t& outputValue) {
    auto start = str;
    if (!consume<Char<'%'>>()) {
      return false;
    }
    if (parseHexadecimalNumber<uint8_t, 0xff, 2>(outputValue)) {
      return true;
    }
    str = start;
    return false;
  }

  bool consumePercentEncodedUTF8CodePoint() {
    auto start = str;
    std::array<uint8_t, 4> b;
    int size;

    // Handle prefix byte
    if (!parsePercentEncoded(b[0])) {
      return false;
    }
    if (b[0] <= 0x7f) {
      return true;
    } else if (0xc2 <= b[0] && b[0] <= 0xdf) {
      size = 2;
    } else if (0xe0 <= b[0] && b[0] <= 0xef) {
      size = 3;
    } else if (0xf0 <= b[0] && b[0] <= 0xf4) {
      size = 4;
    } else {
      // Invalid prefix byte.
      str = start;
      return false;
    }

    // Remaining bytes must be percent coded; parse them.
    for (int i = 1; i < size; i++) {
      if (!parsePercentEncoded(b[i]) || (b[i] & 0b1100'0000) != 0b1000'0000) {
        str = start;
        return false;
      }
    }

    // Check for invalid conditions.
    if ((b[0] == 0xe0 && b[1] < 0xa0) || // Overlong encoding (3-byte)
        (b[0] == 0xf0 && b[1] < 0x90) || // Overlong encoding (4-byte)
        (b[0] == 0xf4 && b[1] > 0x90) // Sequence larger than U+10FFFF
    ) {
      str = start;
      return false;
    }

    return true;
  }
};

} // namespace

bool validateUri(std::string_view str) {
  UriParser parser{str};
  return parser.validateUri();
}

bool validateUriReference(std::string_view str) {
  UriParser parser{str};
  return parser.validateUriReference();
}

} // namespace buf::validate::internal::lib
