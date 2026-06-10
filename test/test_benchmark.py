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

"""Benchmarks for CEL rule evaluation, by rule category.

Run with `uv run poe bench`. This file only touches the public protovalidate
API, so the same file produces comparable numbers on any branch (e.g. to
compare CEL backends, check out the baseline branch, drop this file in, and
run it there).

Each benchmark measures steady-state `collect_violations` on a shared
`Validator`, so per-message-type compilation is warmed up by the calibration
phase and the numbers reflect rule evaluation, not compilation.
"""

import time

from google.protobuf import any_pb2, duration_pb2, timestamp_pb2

import protovalidate
from buf.validate.conformance.cases import (
    kitchen_sink_pb2,
    numbers_pb2,
    repeated_pb2,
    strings_pb2,
    wkt_timestamp_pb2,
)

_validator = protovalidate.Validator()


def _run(benchmark, msg, *, expected_violations: int = 0):
    violations = benchmark(_validator.collect_violations, msg)
    assert len(violations) == expected_violations


def test_int64_range_valid(benchmark):
    _run(benchmark, numbers_pb2.Int64GTELTE(val=200))


def test_int64_range_invalid(benchmark):
    _run(benchmark, numbers_pb2.Int64GTELTE(val=300), expected_violations=1)


def test_string_len_valid(benchmark):
    _run(benchmark, strings_pb2.StringLen(val="foo"))


def test_string_email_valid(benchmark):
    _run(benchmark, strings_pb2.StringEmail(val="foo@example.com"))


def test_string_pattern_valid(benchmark):
    _run(benchmark, strings_pb2.StringPattern(val="Foo123"))


def test_repeated_unique_valid(benchmark):
    _run(benchmark, repeated_pb2.RepeatedUnique(val=["a", "b", "c", "d", "e"]))


def test_timestamp_gt_now_valid(benchmark):
    ts = timestamp_pb2.Timestamp()
    ts.FromSeconds(int(time.time()) + 3600)
    _run(benchmark, wkt_timestamp_pb2.TimestampGTNow(val=ts))


def _kitchen_sink_msg() -> kitchen_sink_pb2.KitchenSinkMessage:
    inner = duration_pb2.Duration(seconds=1)
    any_val = any_pb2.Any()
    any_val.Pack(inner)
    return kitchen_sink_pb2.KitchenSinkMessage(
        val=kitchen_sink_pb2.ComplexTestMsg(
            const="abcd",
            int_const=5,
            bool_const=False,
            float_val={"value": 1.0},
            dur_val=duration_pb2.Duration(seconds=3),
            ts_val=timestamp_pb2.Timestamp(seconds=100),
            float_const=7.0,
            double_in=123,
            enum_const=kitchen_sink_pb2.COMPLEX_TEST_ENUM_TWO,
            any_val=any_val,
            rep_ts_val=[timestamp_pb2.Timestamp(nanos=2000000)],
            map_val={-1: "a", -2: "b"},
            bytes_val=b"\x00\x99",
            x="oneof",
        )
    )


def test_kitchen_sink_valid(benchmark):
    _run(benchmark, _kitchen_sink_msg())
