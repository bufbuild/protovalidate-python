# Copyright (c) 2023-2026 Buf Technologies, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import typing

from google.protobuf import descriptor as google_descriptor
from google.protobuf import message as google_message
from protobuf import Message
from protobuf.wkt import FileDescriptorProto, FileDescriptorSet


class LegacyMessageConverter:
    """Copies google.protobuf messages into protobuf-py dynamic messages."""

    def __init__(self) -> None:
        self._types: dict[google_descriptor.Descriptor, type[Message]] = {}

    def normalize(self, msg: Message | google_message.Message) -> Message:
        """Normalize an input Protobuf message to a protobuf.Message.

        protobuf.Message is returned as-is, otherwise google.protobuf.Message is
        copied into a protobuf.Message of the same type.
        """
        if isinstance(msg, Message):
            return msg
        # Normalize upb descriptor type
        desc = typing.cast(google_descriptor.Descriptor, msg.DESCRIPTOR)
        cls = self._types.get(desc)
        if cls is None:
            cls = _message_class(desc)
            self._types[desc] = cls
        return cls.from_binary(msg.SerializeToString())


def _message_class(desc: google_descriptor.Descriptor) -> type[Message]:
    files: dict[str, FileDescriptorProto] = {}
    _collect_files(desc.file, files)
    registry = FileDescriptorSet(file=list(files.values())).to_registry()
    result = registry.message(desc.full_name)
    # The collected files declare the descriptor's type.
    assert result is not None  # noqa: S101
    return result.type


def _collect_files(file: google_descriptor.FileDescriptor, out: dict[str, FileDescriptorProto]) -> None:
    if file.name in out:
        return
    for dep in file.dependencies:
        _collect_files(dep, out)
    out[file.name] = FileDescriptorProto.from_binary(file.serialized_pb)
