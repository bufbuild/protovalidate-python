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
# source: buf/validate/conformance/cases/ignore_empty_proto2.proto
# Protobuf Python Version: 6.30.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    1,
    '',
    'buf/validate/conformance/cases/ignore_empty_proto2.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8buf/validate/conformance/cases/ignore_empty_proto2.proto\x12\x1e\x62uf.validate.conformance.cases\x1a\x1b\x62uf/validate/validate.proto\"?\n\x1fIgnoreEmptyProto2ScalarOptional\x12\x1c\n\x03val\x18\x01 \x01(\x05\x42\n\xbaH\x07\x1a\x02 \x00\xd8\x01\x01R\x03val\"N\n*IgnoreEmptyProto2ScalarOptionalWithDefault\x12 \n\x03val\x18\x01 \x01(\x05:\x02\x34\x32\x42\n\xbaH\x07\x1a\x02 \x00\xd8\x01\x01R\x03val\"?\n\x1fIgnoreEmptyProto2ScalarRequired\x12\x1c\n\x03val\x18\x01 \x02(\x05\x42\n\xbaH\x07\x1a\x02 \x00\xd8\x01\x01R\x03val\"\xc7\x01\n\x18IgnoreEmptyProto2Message\x12\x91\x01\n\x03val\x18\x01 \x01(\x0b\x32<.buf.validate.conformance.cases.IgnoreEmptyProto2Message.MsgBA\xbaH>\xba\x01\x38\n\x1bignore_empty.proto2.message\x12\x06\x66oobar\x1a\x11this.val == \'foo\'\xd8\x01\x01R\x03val\x1a\x17\n\x03Msg\x12\x10\n\x03val\x18\x01 \x01(\tR\x03val\"=\n\x16IgnoreEmptyProto2Oneof\x12\x1e\n\x03val\x18\x01 \x01(\x05\x42\n\xbaH\x07\x1a\x02 \x00\xd8\x01\x01H\x00R\x03valB\x03\n\x01o\":\n\x19IgnoreEmptyProto2Repeated\x12\x1d\n\x03val\x18\x01 \x03(\x05\x42\x0b\xbaH\x08\x92\x01\x02\x08\x03\xd8\x01\x01R\x03val\"\xac\x01\n\x14IgnoreEmptyProto2Map\x12\\\n\x03val\x18\x01 \x03(\x0b\x32=.buf.validate.conformance.cases.IgnoreEmptyProto2Map.ValEntryB\x0b\xbaH\x08\x9a\x01\x02\x08\x03\xd8\x01\x01R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\x05R\x03key\x12\x14\n\x05value\x18\x02 \x01(\x05R\x05value:\x02\x38\x01\x42\xd8\x01\n\"com.buf.validate.conformance.casesB\x16IgnoreEmptyProto2ProtoP\x01\xa2\x02\x04\x42VCC\xaa\x02\x1e\x42uf.Validate.Conformance.Cases\xca\x02\x1e\x42uf\\Validate\\Conformance\\Cases\xe2\x02*Buf\\Validate\\Conformance\\Cases\\GPBMetadata\xea\x02!Buf::Validate::Conformance::Cases')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'buf.validate.conformance.cases.ignore_empty_proto2_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.buf.validate.conformance.casesB\026IgnoreEmptyProto2ProtoP\001\242\002\004BVCC\252\002\036Buf.Validate.Conformance.Cases\312\002\036Buf\\Validate\\Conformance\\Cases\342\002*Buf\\Validate\\Conformance\\Cases\\GPBMetadata\352\002!Buf::Validate::Conformance::Cases'
  _globals['_IGNOREEMPTYPROTO2SCALAROPTIONAL'].fields_by_name['val']._loaded_options = None
  _globals['_IGNOREEMPTYPROTO2SCALAROPTIONAL'].fields_by_name['val']._serialized_options = b'\272H\007\032\002 \000\330\001\001'
  _globals['_IGNOREEMPTYPROTO2SCALAROPTIONALWITHDEFAULT'].fields_by_name['val']._loaded_options = None
  _globals['_IGNOREEMPTYPROTO2SCALAROPTIONALWITHDEFAULT'].fields_by_name['val']._serialized_options = b'\272H\007\032\002 \000\330\001\001'
  _globals['_IGNOREEMPTYPROTO2SCALARREQUIRED'].fields_by_name['val']._loaded_options = None
  _globals['_IGNOREEMPTYPROTO2SCALARREQUIRED'].fields_by_name['val']._serialized_options = b'\272H\007\032\002 \000\330\001\001'
  _globals['_IGNOREEMPTYPROTO2MESSAGE'].fields_by_name['val']._loaded_options = None
  _globals['_IGNOREEMPTYPROTO2MESSAGE'].fields_by_name['val']._serialized_options = b'\272H>\272\0018\n\033ignore_empty.proto2.message\022\006foobar\032\021this.val == \'foo\'\330\001\001'
  _globals['_IGNOREEMPTYPROTO2ONEOF'].fields_by_name['val']._loaded_options = None
  _globals['_IGNOREEMPTYPROTO2ONEOF'].fields_by_name['val']._serialized_options = b'\272H\007\032\002 \000\330\001\001'
  _globals['_IGNOREEMPTYPROTO2REPEATED'].fields_by_name['val']._loaded_options = None
  _globals['_IGNOREEMPTYPROTO2REPEATED'].fields_by_name['val']._serialized_options = b'\272H\010\222\001\002\010\003\330\001\001'
  _globals['_IGNOREEMPTYPROTO2MAP_VALENTRY']._loaded_options = None
  _globals['_IGNOREEMPTYPROTO2MAP_VALENTRY']._serialized_options = b'8\001'
  _globals['_IGNOREEMPTYPROTO2MAP'].fields_by_name['val']._loaded_options = None
  _globals['_IGNOREEMPTYPROTO2MAP'].fields_by_name['val']._serialized_options = b'\272H\010\232\001\002\010\003\330\001\001'
  _globals['_IGNOREEMPTYPROTO2SCALAROPTIONAL']._serialized_start=121
  _globals['_IGNOREEMPTYPROTO2SCALAROPTIONAL']._serialized_end=184
  _globals['_IGNOREEMPTYPROTO2SCALAROPTIONALWITHDEFAULT']._serialized_start=186
  _globals['_IGNOREEMPTYPROTO2SCALAROPTIONALWITHDEFAULT']._serialized_end=264
  _globals['_IGNOREEMPTYPROTO2SCALARREQUIRED']._serialized_start=266
  _globals['_IGNOREEMPTYPROTO2SCALARREQUIRED']._serialized_end=329
  _globals['_IGNOREEMPTYPROTO2MESSAGE']._serialized_start=332
  _globals['_IGNOREEMPTYPROTO2MESSAGE']._serialized_end=531
  _globals['_IGNOREEMPTYPROTO2MESSAGE_MSG']._serialized_start=508
  _globals['_IGNOREEMPTYPROTO2MESSAGE_MSG']._serialized_end=531
  _globals['_IGNOREEMPTYPROTO2ONEOF']._serialized_start=533
  _globals['_IGNOREEMPTYPROTO2ONEOF']._serialized_end=594
  _globals['_IGNOREEMPTYPROTO2REPEATED']._serialized_start=596
  _globals['_IGNOREEMPTYPROTO2REPEATED']._serialized_end=654
  _globals['_IGNOREEMPTYPROTO2MAP']._serialized_start=657
  _globals['_IGNOREEMPTYPROTO2MAP']._serialized_end=829
  _globals['_IGNOREEMPTYPROTO2MAP_VALENTRY']._serialized_start=775
  _globals['_IGNOREEMPTYPROTO2MAP_VALENTRY']._serialized_end=829
# @@protoc_insertion_point(module_scope)
