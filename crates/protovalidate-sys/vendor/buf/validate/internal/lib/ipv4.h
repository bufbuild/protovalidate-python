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

#include <cstdint>
#include <optional>
#include <string_view>

namespace buf::validate::internal::lib {

struct IPv4Address {
  static const size_t bits_count = 32;
  uint32_t bits;
};

struct IPv4Prefix : public IPv4Address {
  uint8_t prefixLength;

  // Returns the bits of the subnet mask, e.g. the bits that are 1 correspond to
  // the routing prefix and the bits that are 0 correspond to the host ID.
  [[nodiscard]] constexpr uint32_t mask() const {
    if (prefixLength == 0) {
      // Shifting a uint32_t by >= 32 is undefined behavior.
      // On x86, the right operand is truncated to 5 bits.
      // For some reason, this isn't an issue on GCC/Linux even though the
      // assembler output looks like it should exhibit the same issue. Not sure
      // why that is.
      return 0;
    }
    return ~0UL << (bits_count - prefixLength);
  }
};

static inline bool operator==(const IPv4Address& a, const IPv4Address& b) {
  return a.bits == b.bits;
}

static inline bool operator==(const IPv4Prefix& a, const IPv4Prefix& b) {
  return a.bits == b.bits && a.prefixLength == b.prefixLength;
}

std::optional<IPv4Address> parseIPv4Address(std::string_view str);

std::optional<IPv4Prefix> parseIPv4Prefix(std::string_view str);

} // namespace buf::validate::internal::lib
