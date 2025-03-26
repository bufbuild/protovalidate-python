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

import unittest

from protovalidate.internal.extra_func import Ipv4, Uri


class TestFunc(unittest.TestCase):
    def test_ninf(self):
        uri = Uri("https://foo%c3x%96")
        is_it = uri.uri()
        self.assertFalse(is_it)

    def test_is_ip(self):
        v4 = Ipv4("127.0.0.1").address()
        self.assertTrue(v4)
