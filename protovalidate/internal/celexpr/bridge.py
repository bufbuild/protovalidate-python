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

"""Bridges protobuf-py messages into google.protobuf for cel-expr-python."""

from __future__ import annotations

import typing

from google.protobuf import descriptor_pb2 as google_descriptor_pb2
from google.protobuf import descriptor_pool as google_descriptor_pool
from google.protobuf import message as google_message
from google.protobuf import message_factory as google_message_factory
from protobuf import DescFile, DescMessage

if typing.TYPE_CHECKING:
    import protobuf


class GoogleBridge:
    """Lazily mirrors protobuf-py descriptors into google's pool and bridges
    protobuf-py message values to google dynamic messages."""

    def __init__(self) -> None:
        self._pool: google_descriptor_pool.DescriptorPool = google_descriptor_pool.Default()
        self._mirrored: set[str] = set()
        self._classes: dict[str, type[google_message.Message]] = {}

    def _mirror_file(self, desc_file: DescFile) -> None:
        """Registers a protobuf-py DescFile (and its transitive deps) into the
        google pool, dependencies first, skipping files already present."""
        if desc_file.name in self._mirrored:
            return
        self._mirrored.add(desc_file.name)
        for dep in desc_file.dependencies:
            self._mirror_file(dep)
        try:
            self._pool.FindFileByName(desc_file.name)
        except KeyError:
            proto = google_descriptor_pb2.FileDescriptorProto.FromString(desc_file.proto.to_binary())
            self._pool.Add(proto)

    def google_class(self, desc: DescMessage) -> type[google_message.Message]:
        """The google message class mirroring a protobuf-py DescMessage."""
        cls = self._classes.get(desc.type_name)
        if cls is None:
            self._mirror_file(desc.file)
            google_desc = self._pool.FindMessageTypeByName(desc.type_name)
            cls = google_message_factory.GetMessageClass(google_desc)
            self._classes[desc.type_name] = cls
        return cls

    def to_google(self, msg: protobuf.Message) -> google_message.Message:
        """Re-creates a protobuf-py message as a google.protobuf message."""
        bridged = self.google_class(type(msg).desc())()
        bridged.ParseFromString(msg.to_binary())
        return bridged
