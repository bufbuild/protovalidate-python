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

#pragma once

#include <bitset>
#include <cstdint>
#include <optional>
#include <string_view>

namespace buf::validate::internal::lib {

struct IPv6Address {
  static const size_t bits_count = 128;
  std::bitset<bits_count> bits;
};

struct IPv6Prefix : public IPv6Address {
  uint8_t prefixLength;

  // Returns the bits of the subnet mask, e.g. the bits that are 1 correspond to
  // the routing prefix and the bits that are 0 correspond to the host ID.
  [[nodiscard]] std::bitset<bits_count> mask() const {
    return std::bitset<bits_count>{}.set() << (bits_count - prefixLength);
  }
};

static inline bool operator==(const IPv6Address& a, const IPv6Address& b) {
  return a.bits == b.bits;
}

static inline bool operator==(const IPv6Prefix& a, const IPv6Prefix& b) {
  return a.bits == b.bits && a.prefixLength == b.prefixLength;
}

std::optional<IPv6Address> parseIPv6Address(std::string_view str);

std::optional<IPv6Prefix> parseIPv6Prefix(std::string_view str);

} // namespace buf::validate::internal::lib
