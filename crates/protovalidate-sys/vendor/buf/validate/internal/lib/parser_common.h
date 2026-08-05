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

#include <algorithm>
#include <string_view>
#include <type_traits>
#include <utility>
#include <cstdint>

namespace buf::validate::internal::lib {

namespace {

// These helper templates enable constructing arbitrary character ranges at
// compile-time.

template <char add, std::size_t... n>
constexpr auto charSeqFromIndices(std::index_sequence<n...> /*unused*/) {
  return std::integer_sequence<char, static_cast<char>(add + n)...>{};
}

template <char start, char end>
struct MakeCharRange {
  static constexpr size_t size = static_cast<size_t>(end) - static_cast<size_t>(start) + 1;
  using indices = std::make_integer_sequence<size_t, size>;
  using type = decltype(charSeqFromIndices<start>(indices{}));
};

template <char start, char end>
using CharRange = typename MakeCharRange<start, end>::type;

template <char n>
using Char = typename MakeCharRange<n, n>::type;

template <typename seq1, typename seq2>
struct MakeConcatRangesImpl;

template <char... cs1, char... cs2>
struct MakeConcatRangesImpl<
    std::integer_sequence<char, cs1...>,
    std::integer_sequence<char, cs2...>> {
  using type = typename std::integer_sequence<char, cs1..., cs2...>;
};

template <typename head, typename... tail>
struct MakeConcatRanges {
  using type = typename MakeConcatRangesImpl<head, typename MakeConcatRanges<tail...>::type>::type;
};

template <typename n>
struct MakeConcatRanges<n> {
  using type = n;
};

template <typename head, typename... tail>
using ConcatRanges = typename MakeConcatRanges<head, tail...>::type;

// Minimal test suite to ensure that our template machinery does what we expect.
static_assert(
    std::is_same_v<ConcatRanges<CharRange<'a', 'c'>>, std::integer_sequence<char, 'a', 'b', 'c'>>);
static_assert(std::is_same_v<
              ConcatRanges<CharRange<'a', 'c'>, CharRange<'0', '2'>>,
              std::integer_sequence<char, 'a', 'b', 'c', '0', '1', '2'>>);
static_assert(std::is_same_v<
              ConcatRanges<CharRange<'a', 'b'>, CharRange<'0', '1'>, CharRange<'4', '5'>>,
              std::integer_sequence<char, 'a', 'b', '0', '1', '4', '5'>>);

// Common character ranges
using Num = CharRange<'0', '9'>;
using Alpha = ConcatRanges<CharRange<'a', 'z'>, CharRange<'A', 'Z'>>;
using AlphaNum = ConcatRanges<Alpha, Num>;
using HexDigit = ConcatRanges<Num, CharRange<'a', 'f'>, CharRange<'A', 'F'>>;

// Helper functions for parsing decimal and hexadecimal digits.
constexpr unsigned calculateDecimalDigits(unsigned value) {
  unsigned i = 0;
  for (; value != 0; i++) {
    value /= 10;
  }
  return std::max(1U, i);
}

constexpr unsigned calculateHexadecimalDigits(unsigned value) {
  unsigned i = 0;
  for (; value != 0; i++) {
    value >>= 4;
  }
  return std::max(1U, i);
}

bool decimalDigitValue(char c, int& outputValue) {
  if ('0' <= c && c <= '9') {
    outputValue = c - '0';
    return true;
  }
  return false;
}

bool hexadecimalDigitValue(char c, int& outputValue) {
  if ('0' <= c && c <= '9') {
    outputValue = c - '0';
    return true;
  } else if ('a' <= c && c <= 'f') {
    outputValue = c - 'a' + 10;
    return true;
  } else if ('A' <= c && c <= 'F') {
    outputValue = c - 'A' + 10;
    return true;
  }
  return false;
}

struct ParserCommon {
  std::string_view str;

  ParserCommon(std::string_view str) : str{str} {}

  template <char head, char... tail>
  bool charMatchRange(char value) {
    if (value == head) {
      return true;
    }
    if constexpr (sizeof...(tail) > 0) {
      return charMatchRange<tail...>(value);
    }
    return false;
  }

  template <char... c>
  bool charMatchRangeSeqRange(char value, std::integer_sequence<char, c...> /*unused*/) {
    return charMatchRange<c...>(value);
  }

  template <typename seq>
  bool consume() {
    if (str.empty() || !charMatchRangeSeqRange(str[0], seq{})) {
      return false;
    }
    str = str.substr(1);
    return true;
  }

  template <char head, char... tail>
  bool sequenceMatch(int i = 0) {
    if (str[i] != head) {
      return false;
    }
    if constexpr (sizeof...(tail) > 0) {
      return sequenceMatch<tail...>(i + 1);
    }
    return true;
  }

  template <char... c>
  bool consumeSequence() {
    if (str.length() < sizeof...(c) || !sequenceMatch<c...>()) {
      return false;
    }
    str = str.substr(sizeof...(c));
    return true;
  }

  /**
   * Consumes an unsigned decimal number, storing the value in outputValue.
   * Leading zeros are disallowed.
   */
  template <typename T, T maxValue>
  bool parseDecimalNumber(T& outputValue) {
    constexpr unsigned maxDigits = calculateDecimalDigits(static_cast<unsigned>(maxValue));
    int digitValue;
    if (str.empty() || !decimalDigitValue(str[0], digitValue)) {
      // Invalid: too short
      return false;
    }
    int i = 1;
    unsigned value = digitValue;
    if (str.length() > i && decimalDigitValue(str[i], digitValue)) {
      if (value == 0) {
        // Invalid: leading zero
        return false;
      }
      do {
        i++;
        value *= 10U;
        value += digitValue;
      } while (i <= maxDigits && str.length() > i && decimalDigitValue(str[i], digitValue));
    }
    if (i > maxDigits || value > maxValue) {
      // Invalid: out of range
      return false;
    }
    str = str.substr(i);
    outputValue = static_cast<T>(value);
    return true;
  }

  /**
   * Consumes an unsigned hexadecimal number, storing the value in outputValue.
   */
  template <typename T, T maxValue, int minDigits = 1>
  bool parseHexadecimalNumber(T& outputValue) {
    constexpr unsigned maxDigits = calculateHexadecimalDigits(static_cast<unsigned>(maxValue));
    int digitValue;
    int i = 0;
    if (str.empty() || !hexadecimalDigitValue(str[i++], digitValue)) {
      // Invalid: too short
      return false;
    }
    unsigned value = digitValue;
    while (i <= maxDigits && str.length() > i && hexadecimalDigitValue(str[i], digitValue)) {
      i++;
      value <<= 4U;
      value += digitValue;
    }
    if (i > maxDigits || value > maxValue) {
      // Invalid: out of range
      return false;
    }
    if (i < minDigits) {
      // Invalid: not enough digits.
      return false;
    }
    str = str.substr(i);
    outputValue = static_cast<T>(value);
    return true;
  }

  /**
   * Consumes a decimal octet (0-255) with no leading zeroes.
   */
  bool parseDecimalOctet(uint8_t& outputValue) {
    return parseDecimalNumber<uint8_t, 255U>(outputValue);
  }

  /**
   * Consumes a hexadecimal hexadecatet (0x0 - 0xffff).
   */
  bool parseHexadecimalHexadecatet(uint16_t& outputValue) {
    return parseHexadecimalNumber<uint16_t, 0xffffU>(outputValue);
  }
};

} // namespace

} // namespace buf::validate::internal::lib
