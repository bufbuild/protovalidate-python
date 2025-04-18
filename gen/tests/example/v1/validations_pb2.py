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

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: tests/example/v1/validations.proto
# Protobuf Python Version: 5.29.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    3,
    '',
    'tests/example/v1/validations.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"tests/example/v1/validations.proto\x12\x10tests.example.v1\x1a\x1b\x62uf/validate/validate.proto\x1a\x1fgoogle/protobuf/timestamp.proto\")\n\x0c\x44oubleFinite\x12\x19\n\x03val\x18\x01 \x01(\x01\x42\x07\xbaH\x04\x12\x02@\x01R\x03val\";\n\x0eSFixed64ExLTGT\x12)\n\x03val\x18\x01 \x01(\x10\x42\x17\xbaH\x14\x62\x12\x11\x00\x00\x00\x00\x00\x00\x00\x00!\n\x00\x00\x00\x00\x00\x00\x00R\x03val\")\n\x0cTestOneofMsg\x12\x19\n\x03val\x18\x01 \x01(\x08\x42\x07\xbaH\x04j\x02\x08\x01R\x03val\"q\n\x05Oneof\x12\x1a\n\x01x\x18\x01 \x01(\tB\n\xbaH\x07r\x05:\x03\x66ooH\x00R\x01x\x12\x17\n\x01y\x18\x02 \x01(\x05\x42\x07\xbaH\x04\x1a\x02 \x00H\x00R\x01y\x12.\n\x01z\x18\x03 \x01(\x0b\x32\x1e.tests.example.v1.TestOneofMsgH\x00R\x01zB\x03\n\x01o\"H\n\x0eTimestampGTNow\x12\x36\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xbaH\x05\xb2\x01\x02@\x01R\x03val\"\x87\x01\n\tMapMinMax\x12\x42\n\x03val\x18\x01 \x03(\x0b\x32$.tests.example.v1.MapMinMax.ValEntryB\n\xbaH\x07\x9a\x01\x04\x08\x02\x10\x04R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x08R\x05value:\x02\x38\x01\"\x85\x01\n\x07MapKeys\x12\x42\n\x03val\x18\x01 \x03(\x0b\x32\".tests.example.v1.MapKeys.ValEntryB\x0c\xbaH\t\x9a\x01\x06\"\x04\x42\x02\x10\x00R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\x12R\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\"\n\x05\x45mbed\x12\x19\n\x03val\x18\x01 \x01(\x03\x42\x07\xbaH\x04\"\x02 \x00R\x03val\"K\n\x11RepeatedEmbedSkip\x12\x36\n\x03val\x18\x01 \x03(\x0b\x32\x17.tests.example.v1.EmbedB\x0b\xbaH\x08\x92\x01\x05\"\x03\xd8\x01\x03R\x03valB\x8a\x01\n\x14\x63om.tests.example.v1B\x10ValidationsProtoP\x01\xa2\x02\x03TEX\xaa\x02\x10Tests.Example.V1\xca\x02\x10Tests\\Example\\V1\xe2\x02\x1cTests\\Example\\V1\\GPBMetadata\xea\x02\x12Tests::Example::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tests.example.v1.validations_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.tests.example.v1B\020ValidationsProtoP\001\242\002\003TEX\252\002\020Tests.Example.V1\312\002\020Tests\\Example\\V1\342\002\034Tests\\Example\\V1\\GPBMetadata\352\002\022Tests::Example::V1'
  _globals['_DOUBLEFINITE'].fields_by_name['val']._loaded_options = None
  _globals['_DOUBLEFINITE'].fields_by_name['val']._serialized_options = b'\272H\004\022\002@\001'
  _globals['_SFIXED64EXLTGT'].fields_by_name['val']._loaded_options = None
  _globals['_SFIXED64EXLTGT'].fields_by_name['val']._serialized_options = b'\272H\024b\022\021\000\000\000\000\000\000\000\000!\n\000\000\000\000\000\000\000'
  _globals['_TESTONEOFMSG'].fields_by_name['val']._loaded_options = None
  _globals['_TESTONEOFMSG'].fields_by_name['val']._serialized_options = b'\272H\004j\002\010\001'
  _globals['_ONEOF'].fields_by_name['x']._loaded_options = None
  _globals['_ONEOF'].fields_by_name['x']._serialized_options = b'\272H\007r\005:\003foo'
  _globals['_ONEOF'].fields_by_name['y']._loaded_options = None
  _globals['_ONEOF'].fields_by_name['y']._serialized_options = b'\272H\004\032\002 \000'
  _globals['_TIMESTAMPGTNOW'].fields_by_name['val']._loaded_options = None
  _globals['_TIMESTAMPGTNOW'].fields_by_name['val']._serialized_options = b'\272H\005\262\001\002@\001'
  _globals['_MAPMINMAX_VALENTRY']._loaded_options = None
  _globals['_MAPMINMAX_VALENTRY']._serialized_options = b'8\001'
  _globals['_MAPMINMAX'].fields_by_name['val']._loaded_options = None
  _globals['_MAPMINMAX'].fields_by_name['val']._serialized_options = b'\272H\007\232\001\004\010\002\020\004'
  _globals['_MAPKEYS_VALENTRY']._loaded_options = None
  _globals['_MAPKEYS_VALENTRY']._serialized_options = b'8\001'
  _globals['_MAPKEYS'].fields_by_name['val']._loaded_options = None
  _globals['_MAPKEYS'].fields_by_name['val']._serialized_options = b'\272H\t\232\001\006\"\004B\002\020\000'
  _globals['_EMBED'].fields_by_name['val']._loaded_options = None
  _globals['_EMBED'].fields_by_name['val']._serialized_options = b'\272H\004\"\002 \000'
  _globals['_REPEATEDEMBEDSKIP'].fields_by_name['val']._loaded_options = None
  _globals['_REPEATEDEMBEDSKIP'].fields_by_name['val']._serialized_options = b'\272H\010\222\001\005\"\003\330\001\003'
  _globals['_DOUBLEFINITE']._serialized_start=118
  _globals['_DOUBLEFINITE']._serialized_end=159
  _globals['_SFIXED64EXLTGT']._serialized_start=161
  _globals['_SFIXED64EXLTGT']._serialized_end=220
  _globals['_TESTONEOFMSG']._serialized_start=222
  _globals['_TESTONEOFMSG']._serialized_end=263
  _globals['_ONEOF']._serialized_start=265
  _globals['_ONEOF']._serialized_end=378
  _globals['_TIMESTAMPGTNOW']._serialized_start=380
  _globals['_TIMESTAMPGTNOW']._serialized_end=452
  _globals['_MAPMINMAX']._serialized_start=455
  _globals['_MAPMINMAX']._serialized_end=590
  _globals['_MAPMINMAX_VALENTRY']._serialized_start=536
  _globals['_MAPMINMAX_VALENTRY']._serialized_end=590
  _globals['_MAPKEYS']._serialized_start=593
  _globals['_MAPKEYS']._serialized_end=726
  _globals['_MAPKEYS_VALENTRY']._serialized_start=672
  _globals['_MAPKEYS_VALENTRY']._serialized_end=726
  _globals['_EMBED']._serialized_start=728
  _globals['_EMBED']._serialized_end=762
  _globals['_REPEATEDEMBEDSKIP']._serialized_start=764
  _globals['_REPEATEDEMBEDSKIP']._serialized_end=839
# @@protoc_insertion_point(module_scope)
