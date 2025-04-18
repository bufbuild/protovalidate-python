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
# source: buf/validate/conformance/cases/required_field_proto3.proto
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
    'buf/validate/conformance/cases/required_field_proto3.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:buf/validate/conformance/cases/required_field_proto3.proto\x12\x1e\x62uf.validate.conformance.cases\x1a\x1b\x62uf/validate/validate.proto\"0\n\x14RequiredProto3Scalar\x12\x18\n\x03val\x18\x01 \x01(\tB\x06\xbaH\x03\xc8\x01\x01R\x03val\"?\n RequiredProto3ScalarIgnoreAlways\x12\x1b\n\x03val\x18\x01 \x01(\tB\t\xbaH\x06\xc8\x01\x01\xd8\x01\x03R\x03val\"E\n\x1cRequiredProto3OptionalScalar\x12\x1d\n\x03val\x18\x01 \x01(\tB\x06\xbaH\x03\xc8\x01\x01H\x00R\x03val\x88\x01\x01\x42\x06\n\x04_val\"T\n(RequiredProto3OptionalScalarIgnoreAlways\x12 \n\x03val\x18\x01 \x01(\tB\t\xbaH\x06\xc8\x01\x01\xd8\x01\x03H\x00R\x03val\x88\x01\x01\x42\x06\n\x04_val\"\x85\x01\n\x15RequiredProto3Message\x12S\n\x03val\x18\x01 \x01(\x0b\x32\x39.buf.validate.conformance.cases.RequiredProto3Message.MsgB\x06\xbaH\x03\xc8\x01\x01R\x03val\x1a\x17\n\x03Msg\x12\x10\n\x03val\x18\x01 \x01(\tR\x03val\"\xa0\x01\n!RequiredProto3MessageIgnoreAlways\x12\x62\n\x03val\x18\x01 \x01(\x0b\x32\x45.buf.validate.conformance.cases.RequiredProto3MessageIgnoreAlways.MsgB\t\xbaH\x06\xc8\x01\x01\xd8\x01\x03R\x03val\x1a\x17\n\x03Msg\x12\x10\n\x03val\x18\x01 \x01(\tR\x03val\"D\n\x13RequiredProto3OneOf\x12\x16\n\x01\x61\x18\x01 \x01(\tB\x06\xbaH\x03\xc8\x01\x01H\x00R\x01\x61\x12\x0e\n\x01\x62\x18\x02 \x01(\tH\x00R\x01\x62\x42\x05\n\x03val\"S\n\x1fRequiredProto3OneOfIgnoreAlways\x12\x19\n\x01\x61\x18\x01 \x01(\tB\t\xbaH\x06\xc8\x01\x01\xd8\x01\x03H\x00R\x01\x61\x12\x0e\n\x01\x62\x18\x02 \x01(\tH\x00R\x01\x62\x42\x05\n\x03val\"2\n\x16RequiredProto3Repeated\x12\x18\n\x03val\x18\x01 \x03(\tB\x06\xbaH\x03\xc8\x01\x01R\x03val\"A\n\"RequiredProto3RepeatedIgnoreAlways\x12\x1b\n\x03val\x18\x01 \x03(\tB\t\xbaH\x06\xc8\x01\x01\xd8\x01\x03R\x03val\"\xa1\x01\n\x11RequiredProto3Map\x12T\n\x03val\x18\x01 \x03(\x0b\x32:.buf.validate.conformance.cases.RequiredProto3Map.ValEntryB\x06\xbaH\x03\xc8\x01\x01R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\xbc\x01\n\x1dRequiredProto3MapIgnoreAlways\x12\x63\n\x03val\x18\x01 \x03(\x0b\x32\x46.buf.validate.conformance.cases.RequiredProto3MapIgnoreAlways.ValEntryB\t\xbaH\x06\xc8\x01\x01\xd8\x01\x03R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'buf.validate.conformance.cases.required_field_proto3_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_REQUIREDPROTO3SCALAR'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDPROTO3SCALAR'].fields_by_name['val']._serialized_options = b'\272H\003\310\001\001'
  _globals['_REQUIREDPROTO3SCALARIGNOREALWAYS'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDPROTO3SCALARIGNOREALWAYS'].fields_by_name['val']._serialized_options = b'\272H\006\310\001\001\330\001\003'
  _globals['_REQUIREDPROTO3OPTIONALSCALAR'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDPROTO3OPTIONALSCALAR'].fields_by_name['val']._serialized_options = b'\272H\003\310\001\001'
  _globals['_REQUIREDPROTO3OPTIONALSCALARIGNOREALWAYS'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDPROTO3OPTIONALSCALARIGNOREALWAYS'].fields_by_name['val']._serialized_options = b'\272H\006\310\001\001\330\001\003'
  _globals['_REQUIREDPROTO3MESSAGE'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDPROTO3MESSAGE'].fields_by_name['val']._serialized_options = b'\272H\003\310\001\001'
  _globals['_REQUIREDPROTO3MESSAGEIGNOREALWAYS'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDPROTO3MESSAGEIGNOREALWAYS'].fields_by_name['val']._serialized_options = b'\272H\006\310\001\001\330\001\003'
  _globals['_REQUIREDPROTO3ONEOF'].fields_by_name['a']._loaded_options = None
  _globals['_REQUIREDPROTO3ONEOF'].fields_by_name['a']._serialized_options = b'\272H\003\310\001\001'
  _globals['_REQUIREDPROTO3ONEOFIGNOREALWAYS'].fields_by_name['a']._loaded_options = None
  _globals['_REQUIREDPROTO3ONEOFIGNOREALWAYS'].fields_by_name['a']._serialized_options = b'\272H\006\310\001\001\330\001\003'
  _globals['_REQUIREDPROTO3REPEATED'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDPROTO3REPEATED'].fields_by_name['val']._serialized_options = b'\272H\003\310\001\001'
  _globals['_REQUIREDPROTO3REPEATEDIGNOREALWAYS'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDPROTO3REPEATEDIGNOREALWAYS'].fields_by_name['val']._serialized_options = b'\272H\006\310\001\001\330\001\003'
  _globals['_REQUIREDPROTO3MAP_VALENTRY']._loaded_options = None
  _globals['_REQUIREDPROTO3MAP_VALENTRY']._serialized_options = b'8\001'
  _globals['_REQUIREDPROTO3MAP'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDPROTO3MAP'].fields_by_name['val']._serialized_options = b'\272H\003\310\001\001'
  _globals['_REQUIREDPROTO3MAPIGNOREALWAYS_VALENTRY']._loaded_options = None
  _globals['_REQUIREDPROTO3MAPIGNOREALWAYS_VALENTRY']._serialized_options = b'8\001'
  _globals['_REQUIREDPROTO3MAPIGNOREALWAYS'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDPROTO3MAPIGNOREALWAYS'].fields_by_name['val']._serialized_options = b'\272H\006\310\001\001\330\001\003'
  _globals['_REQUIREDPROTO3SCALAR']._serialized_start=123
  _globals['_REQUIREDPROTO3SCALAR']._serialized_end=171
  _globals['_REQUIREDPROTO3SCALARIGNOREALWAYS']._serialized_start=173
  _globals['_REQUIREDPROTO3SCALARIGNOREALWAYS']._serialized_end=236
  _globals['_REQUIREDPROTO3OPTIONALSCALAR']._serialized_start=238
  _globals['_REQUIREDPROTO3OPTIONALSCALAR']._serialized_end=307
  _globals['_REQUIREDPROTO3OPTIONALSCALARIGNOREALWAYS']._serialized_start=309
  _globals['_REQUIREDPROTO3OPTIONALSCALARIGNOREALWAYS']._serialized_end=393
  _globals['_REQUIREDPROTO3MESSAGE']._serialized_start=396
  _globals['_REQUIREDPROTO3MESSAGE']._serialized_end=529
  _globals['_REQUIREDPROTO3MESSAGE_MSG']._serialized_start=506
  _globals['_REQUIREDPROTO3MESSAGE_MSG']._serialized_end=529
  _globals['_REQUIREDPROTO3MESSAGEIGNOREALWAYS']._serialized_start=532
  _globals['_REQUIREDPROTO3MESSAGEIGNOREALWAYS']._serialized_end=692
  _globals['_REQUIREDPROTO3MESSAGEIGNOREALWAYS_MSG']._serialized_start=506
  _globals['_REQUIREDPROTO3MESSAGEIGNOREALWAYS_MSG']._serialized_end=529
  _globals['_REQUIREDPROTO3ONEOF']._serialized_start=694
  _globals['_REQUIREDPROTO3ONEOF']._serialized_end=762
  _globals['_REQUIREDPROTO3ONEOFIGNOREALWAYS']._serialized_start=764
  _globals['_REQUIREDPROTO3ONEOFIGNOREALWAYS']._serialized_end=847
  _globals['_REQUIREDPROTO3REPEATED']._serialized_start=849
  _globals['_REQUIREDPROTO3REPEATED']._serialized_end=899
  _globals['_REQUIREDPROTO3REPEATEDIGNOREALWAYS']._serialized_start=901
  _globals['_REQUIREDPROTO3REPEATEDIGNOREALWAYS']._serialized_end=966
  _globals['_REQUIREDPROTO3MAP']._serialized_start=969
  _globals['_REQUIREDPROTO3MAP']._serialized_end=1130
  _globals['_REQUIREDPROTO3MAP_VALENTRY']._serialized_start=1076
  _globals['_REQUIREDPROTO3MAP_VALENTRY']._serialized_end=1130
  _globals['_REQUIREDPROTO3MAPIGNOREALWAYS']._serialized_start=1133
  _globals['_REQUIREDPROTO3MAPIGNOREALWAYS']._serialized_end=1321
  _globals['_REQUIREDPROTO3MAPIGNOREALWAYS_VALENTRY']._serialized_start=1076
  _globals['_REQUIREDPROTO3MAPIGNOREALWAYS_VALENTRY']._serialized_end=1130
# @@protoc_insertion_point(module_scope)
