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

import datetime
import math
import re
from decimal import Decimal


class StringFormat:
    """An implementation of string.format() in CEL."""

    def __init__(self):
        self.fmt = None

    def format(self, fmt: str, args: list) -> str:
        # printf style formatting
        i = 0
        j = 0
        result = ""
        while i < len(fmt):
            if fmt[i] != "%":
                result += fmt[i]
                i += 1
                continue

            if i + 1 < len(fmt) and fmt[i + 1] == "%":
                result += "%"
                i += 2
                continue
            if j >= len(args):
                msg = f"index {j} out of range"
                raise ValueError(msg)
            arg = args[j]
            j += 1
            i += 1
            if i >= len(fmt):
                msg = "format() incomplete format specifier"
                raise ValueError(msg)
            precision = 6
            if fmt[i] == ".":
                i += 1
                precision = 0
                while i < len(fmt) and fmt[i].isdigit():
                    precision = precision * 10 + int(fmt[i])
                    i += 1
            if i >= len(fmt):
                msg = "format() incomplete format specifier"
                raise ValueError(msg)
            if fmt[i] == "f":
                result += self.__format_float(arg, precision)
            elif fmt[i] == "e":
                result += self.__format_exponential(arg, precision)
            elif fmt[i] == "d":
                result += self.__format_int(arg)
            elif fmt[i] == "s":
                result += self.__format_string(arg)
            elif fmt[i] == "x":
                result += self.__format_hex(arg)
            elif fmt[i] == "X":
                result += self.__format_hex(arg).upper()
            elif fmt[i] == "o":
                result += self.__format_oct(arg)
            elif fmt[i] == "b":
                result += self.__format_bin(arg)
            else:
                msg = f'could not parse formatting clause: unrecognized formatting clause "{fmt[i]}"'
                raise ValueError(msg)
            i += 1
        if j < len(args):
            msg = "format() too many arguments for format string"
            raise ValueError(msg)

        return result

    def __validate_number(self, arg: float | int) -> str | None:
        if math.isnan(arg):
            return "NaN"
        if math.isinf(arg):
            if arg < 0:
                return "-Infinity"
            return "Infinity"
        return None

    def __format_float(self, arg, precision: int) -> str:
        if isinstance(arg, float):
            result = self.__validate_number(arg)
            if result is not None:
                return result
            return f"{arg:.{precision}f}"
        msg = (
            "error during formatting: fixed-point clause can only be used on doubles, was given "
            f"{self.__type_str(type(arg))}"
        )
        raise ValueError(msg)

    def __format_exponential(self, arg, precision: int) -> str:
        if isinstance(arg, float):
            result = self.__validate_number(arg)
            if result is not None:
                return result
            return f"{arg:.{precision}e}"
        msg = (
            "error during formatting: scientific clause can only be used on doubles, was given "
            f"{self.__type_str(type(arg))}"
        )
        raise ValueError(msg)

    def __format_int(self, arg) -> str:
        # bool is a subclass of int in Python, so check bool first
        if isinstance(arg, bool):
            msg = (
                "error during formatting: decimal clause can only be used on integers, was given "
                f"{self.__type_str(type(arg))}"
            )
            raise ValueError(msg)
        if isinstance(arg, int | float):
            result = self.__validate_number(arg)
            if result is not None:
                return result
            return f"{int(arg)}"
        msg = (
            "error during formatting: decimal clause can only be used on integers, was given "
            f"{self.__type_str(type(arg))}"
        )
        raise ValueError(msg)

    def __format_hex(self, arg) -> str:
        if isinstance(arg, bool):
            msg = (
                "error during formatting: only integers, byte buffers, and strings can be formatted as hex, "
                f"was given {self.__type_str(type(arg))}"
            )
            raise ValueError(msg)
        if isinstance(arg, int):
            return f"{arg:x}"
        if isinstance(arg, bytes | bytearray):
            return arg.hex()
        if isinstance(arg, str):
            return arg.encode("utf-8").hex()
        msg = (
            "error during formatting: only integers, byte buffers, and strings can be formatted as hex, was given "
            f"{self.__type_str(type(arg))}"
        )
        raise ValueError(msg)

    def __format_oct(self, arg) -> str:
        if isinstance(arg, bool):
            msg = (
                "error during formatting: octal clause can only be used on integers, was given "
                f"{self.__type_str(type(arg))}"
            )
            raise ValueError(msg)
        if isinstance(arg, int):
            return f"{arg:o}"
        msg = (
            "error during formatting: octal clause can only be used on integers, was given "
            f"{self.__type_str(type(arg))}"
        )
        raise ValueError(msg)

    def __format_bin(self, arg) -> str:
        if isinstance(arg, bool):
            return f"{int(arg):b}"
        if isinstance(arg, int):
            return f"{arg:b}"
        msg = (
            "error during formatting: only integers and bools can be formatted as binary, was given "
            f"{self.__type_str(type(arg))}"
        )
        raise ValueError(msg)

    def __format_string(self, arg) -> str:
        if arg is None:
            return "null"
        if isinstance(arg, bool):
            # True -> "true", False -> "false"
            return str(arg).lower()
        if isinstance(arg, bytes | bytearray):
            decoded = arg.decode("utf-8", errors="replace")
            # Collapse any contiguous replacement characters into one
            return re.sub("\ufffd+", "\ufffd", decoded)
        if isinstance(arg, float):
            result = self.__validate_number(arg)
            if result is not None:
                return result
            return f"{arg:g}"
        if isinstance(arg, datetime.timedelta):
            return self.__format_duration(arg)
        if isinstance(arg, int):
            result = self.__validate_number(arg)
            if result is not None:
                return result
            return f"{arg}"
        if isinstance(arg, list):
            return self.__format_list(arg)
        if isinstance(arg, dict):
            return self.__format_map(arg)
        if isinstance(arg, str):
            return arg
        if isinstance(arg, datetime.datetime):
            return self.__format_timestamp(arg)
        return "unknown"

    def __format_list(self, arg: list) -> str:
        return "[" + ", ".join(self.__format_string(val) for val in arg) + "]"

    def __format_map(self, arg: dict) -> str:
        m = {self.__format_string(k): self.__format_string(v) for k, v in arg.items()}
        return "{" + ", ".join(key + ": " + val for key, val in sorted(m.items())) + "}"

    def __format_duration(self, arg: datetime.timedelta) -> str:
        total_seconds = Decimal(arg.days * 86400 + arg.seconds) + Decimal(arg.microseconds) / Decimal(1_000_000)
        return f"{total_seconds:f}s"

    def __format_timestamp(self, arg: datetime.datetime) -> str:
        # Format as ISO 8601 with Z suffix, using millisecond precision if needed.
        if arg.microsecond != 0:
            base = arg.isoformat(timespec="milliseconds")
        else:
            base = arg.isoformat(timespec="seconds")
        return base.removesuffix("+00:00") + "Z"

    def __type_str(self, arg: type) -> str:
        if arg is type(None):
            return "null_type"
        if arg is bool:
            return "bool"
        if arg is bytes or arg is bytearray:
            return "bytes"
        if arg is float:
            return "double"
        if arg is datetime.timedelta:
            return "google.protobuf.Duration"
        if arg is int:
            return "int"
        if arg is list:
            return "list"
        if arg is dict:
            return "map"
        if arg is str:
            return "string"
        if arg is datetime.datetime:
            return "google.protobuf.Timestamp"
        return "unknown"
