# Copyright 2023-2026 Buf Technologies, Inc.
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

import random
from collections.abc import Callable, Iterator

import pytest
from google.protobuf.message import Message
from google.protobuf.wrappers_pb2 import (
    BoolValue,
    BytesValue,
    DoubleValue,
    FloatValue,
    Int32Value,
    Int64Value,
    StringValue,
    UInt32Value,
    UInt64Value,
)
from pytest_benchmark.fixture import BenchmarkFixture

import protovalidate

from .gen.bench.v1.bench_pb2 import (
    BenchComplexSchema,
    BenchEnum,
    BenchMap,
    BenchRepeatedBytesUnique,
    BenchRepeatedMessage,
    BenchRepeatedScalar,
    BenchRepeatedScalarUnique,
    BenchScalar,
)
from .gen.bench.v1.native_pb2 import BenchGT, MultiRule, StringMatching, WrapperTesting
from .gen.bench.v1.native_pb2 import TestByteMatching as ByteMatching


def gen_bytes(n: int, salt: int) -> bytes:
    return bytes((i + salt) & 0xFF for i in range(n))


words = [
    "alpha",
    "bravo",
    "charlie",
    "delta",
    "echo",
    "foxtrot",
    "golf",
    "hotel",
    "india",
    "juliet",
]


# Fix the random seed for repeatable data in complex messages
@pytest.fixture(autouse=True, scope="module")
def random_seed() -> Iterator[None]:
    random.seed(1)
    yield
    random.seed(None)


# ruff: noqa: S311 # Allow pseudorandom
def gen_complex(depth: int) -> BenchComplexSchema:
    m = BenchComplexSchema(
        s1=random.choice(words),
        s2=random.choice(words),
        i32=random.randint(1, 100),
        i64=random.randint(1, 999),
        u32=random.randint(1, 100),
        u64=random.randint(1, 1000),
        si32=random.randint(1, 100),
        si64=random.randint(1, 999),
        f32=random.randint(1, 100),
        f64=random.randint(1, 999),
        sf32=random.randint(1, 100),
        sf64=random.randint(1, 999),
        fl=random.randint(1, 100),
        db=random.randint(1, 100),
        bl=True,
        by=gen_bytes(8, 7),
        nested=BenchScalar(x=random.randint(1, 100)),
        rep_str=[random.choice(words) for _ in range(3)],
        rep_i32=[random.randint(1, 100) for _ in range(2)],
        rep_bytes=[gen_bytes(3, i) for i in range(1, 4)],
        rep_msg=[BenchScalar(x=random.randint(1, 100)) for _ in range(2)],
        map_str_str={"a": "1", "b": "2", "c": "3"},
        map_i32_i64={1: 10, 2: 20, 3: 30},
        map_u64_bool={1: True, 2: False},
        map_str_bytes={"k": gen_bytes(2, 0)},
        map_str_msg={"a": BenchScalar(x=random.randint(1, 100)), "b": BenchScalar(x=random.randint(1, 100))},
        map_i64_msg={1: BenchScalar(x=random.randint(1, 100)), 2: BenchScalar(x=random.randint(1, 100))},
        enum_field=BenchEnum.BENCH_ENUM_ONE,
        oneof_str=random.choice(words),
    )
    if depth > 0:
        m.self_ref.CopyFrom(gen_complex(depth - 1))
    return m


validator = protovalidate.Validator()


# Use lambda factories to allow random seed fixture to apply before computing
cases = [
    pytest.param(lambda: BenchScalar(x=42), id="scalar"),
    pytest.param(lambda: BenchRepeatedScalar(x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), id="repeated_scalar"),
    pytest.param(lambda: BenchRepeatedMessage(x=[BenchScalar(x=i + 1) for i in range(10)]), id="repeated_message"),
    pytest.param(
        lambda: BenchRepeatedScalarUnique(x=[1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8]), id="repeated_unique_scalar"
    ),
    pytest.param(
        lambda: BenchRepeatedBytesUnique(x=[gen_bytes(4, i + 1) for i in range(8)]), id="repeated_unique_bytes"
    ),
    pytest.param(
        lambda: BenchMap(entries={"k1": "v1", "k2": "v2", "k3": "v3", "k4": "v4", "k5": "v5", "k6": "v6", "k7": "v7"}),
        id="map",
    ),
    pytest.param(lambda: gen_complex(1), id="complex_schema"),
    pytest.param(
        lambda: BenchGT(
            gt=50,
            gte=50,
            lt=50,
            lte=50,
            gtltin=50,
            gtltein=50,
            # gtltex, gtlteex, gteltex, gtelteex have unsatisfiable rules (lt < gt);
            # Go's bench leaves them at zero which is treated as unset for proto3 scalars
            # by the rules engine — protovalidate skips fields with rules.required=false
            # unset zero values. Keeping them at 0 mirrors Go's fixture.
            gteltin=50,
            gteltein=50,
            const=10,
            constgt=10,
            in_test=3,
            not_in_test=4,
        ),
        id="int32_gt",
    ),
    pytest.param(
        lambda: ByteMatching(
            # 16-byte buffers; bytes.ip accepts 4 or 16 bytes (v4/v6 raw), bytes.ipv4
            # requires 4 bytes, bytes.ipv6 requires 16, bytes.uuid requires 16.
            ip_addr=gen_bytes(16, 1),
            ipv4_addr=gen_bytes(4, 2),
            ipv6_addr=gen_bytes(16, 3),
            uuid=gen_bytes(16, 4),
        ),
        id="bytes_matching",
    ),
    pytest.param(
        lambda: StringMatching(
            hostname="example.com",
            host_and_port="example.com:8080",
            email="user@example.com",
            uuid="00112233-4455-6677-8899-aabbccddeeff",
        ),
        id="string_matching",
    ),
    pytest.param(
        lambda: WrapperTesting(
            i32=Int32Value(value=11),
            d=DoubleValue(value=11),
            f=FloatValue(value=11),
            i64=Int64Value(value=11),
            u64=UInt64Value(value=11),
            u32=UInt32Value(value=11),
            b=BoolValue(value=True),
            s=StringValue(value="hello"),
            bs=BytesValue(value=gen_bytes(5, 0)),
        ),
        id="wrapper_testing",
    ),
    pytest.param(lambda: MultiRule(many=1), id="multi_rule_error"),
    pytest.param(lambda: MultiRule(many=10), id="multi_rule_no_error"),
]


@pytest.mark.parametrize("message_factory", cases)
def test_benchmark(message_factory: Callable[[], Message], benchmark: BenchmarkFixture):
    message = message_factory()
    benchmark(validator.collect_violations, message)
