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
# source: buf/validate/conformance/cases/required_field_proto2.proto
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
    'buf/validate/conformance/cases/required_field_proto2.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:buf/validate/conformance/cases/required_field_proto2.proto\x12\x1e\x62uf.validate.conformance.cases\x1a\x1b\x62uf/validate/validate.proto\"8\n\x1cRequiredProto2ScalarOptional\x12\x18\n\x03val\x18\x01 \x01(\tB\x06\xbaH\x03\xc8\x01\x01R\x03val\"G\n(RequiredProto2ScalarOptionalIgnoreAlways\x12\x1b\n\x03val\x18\x01 \x01(\tB\t\xbaH\x06\xc8\x01\x01\xd8\x01\x03R\x03val\"D\n#RequiredProto2ScalarOptionalDefault\x12\x1d\n\x03val\x18\x01 \x01(\t:\x03\x66ooB\x06\xbaH\x03\xc8\x01\x01R\x03val\"S\n/RequiredProto2ScalarOptionalDefaultIgnoreAlways\x12 \n\x03val\x18\x01 \x01(\t:\x03\x66ooB\t\xbaH\x06\xc8\x01\x01\xd8\x01\x03R\x03val\"8\n\x1cRequiredProto2ScalarRequired\x12\x18\n\x03val\x18\x01 \x02(\tB\x06\xbaH\x03\xc8\x01\x01R\x03val\"\x85\x01\n\x15RequiredProto2Message\x12S\n\x03val\x18\x01 \x01(\x0b\x32\x39.buf.validate.conformance.cases.RequiredProto2Message.MsgB\x06\xbaH\x03\xc8\x01\x01R\x03val\x1a\x17\n\x03Msg\x12\x10\n\x03val\x18\x01 \x01(\tR\x03val\"\xa0\x01\n!RequiredProto2MessageIgnoreAlways\x12\x62\n\x03val\x18\x01 \x01(\x0b\x32\x45.buf.validate.conformance.cases.RequiredProto2MessageIgnoreAlways.MsgB\t\xbaH\x06\xc8\x01\x01\xd8\x01\x03R\x03val\x1a\x17\n\x03Msg\x12\x10\n\x03val\x18\x01 \x01(\tR\x03val\"D\n\x13RequiredProto2Oneof\x12\x16\n\x01\x61\x18\x01 \x01(\tB\x06\xbaH\x03\xc8\x01\x01H\x00R\x01\x61\x12\x0e\n\x01\x62\x18\x02 \x01(\tH\x00R\x01\x62\x42\x05\n\x03val\"S\n\x1fRequiredProto2OneofIgnoreAlways\x12\x19\n\x01\x61\x18\x01 \x01(\tB\t\xbaH\x06\xc8\x01\x01\xd8\x01\x03H\x00R\x01\x61\x12\x0e\n\x01\x62\x18\x02 \x01(\tH\x00R\x01\x62\x42\x05\n\x03val\"2\n\x16RequiredProto2Repeated\x12\x18\n\x03val\x18\x01 \x03(\tB\x06\xbaH\x03\xc8\x01\x01R\x03val\"A\n\"RequiredProto2RepeatedIgnoreAlways\x12\x1b\n\x03val\x18\x01 \x03(\tB\t\xbaH\x06\xc8\x01\x01\xd8\x01\x03R\x03val\"\xa1\x01\n\x11RequiredProto2Map\x12T\n\x03val\x18\x01 \x03(\x0b\x32:.buf.validate.conformance.cases.RequiredProto2Map.ValEntryB\x06\xbaH\x03\xc8\x01\x01R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\xbc\x01\n\x1dRequiredProto2MapIgnoreAlways\x12\x63\n\x03val\x18\x01 \x03(\x0b\x32\x46.buf.validate.conformance.cases.RequiredProto2MapIgnoreAlways.ValEntryB\t\xbaH\x06\xc8\x01\x01\xd8\x01\x03R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x42\xda\x01\n\"com.buf.validate.conformance.casesB\x18RequiredFieldProto2ProtoP\x01\xa2\x02\x04\x42VCC\xaa\x02\x1e\x42uf.Validate.Conformance.Cases\xca\x02\x1e\x42uf\\Validate\\Conformance\\Cases\xe2\x02*Buf\\Validate\\Conformance\\Cases\\GPBMetadata\xea\x02!Buf::Validate::Conformance::Cases')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'buf.validate.conformance.cases.required_field_proto2_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.buf.validate.conformance.casesB\030RequiredFieldProto2ProtoP\001\242\002\004BVCC\252\002\036Buf.Validate.Conformance.Cases\312\002\036Buf\\Validate\\Conformance\\Cases\342\002*Buf\\Validate\\Conformance\\Cases\\GPBMetadata\352\002!Buf::Validate::Conformance::Cases'
  _globals['_REQUIREDPROTO2SCALAROPTIONAL'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDPROTO2SCALAROPTIONAL'].fields_by_name['val']._serialized_options = b'\272H\003\310\001\001'
  _globals['_REQUIREDPROTO2SCALAROPTIONALIGNOREALWAYS'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDPROTO2SCALAROPTIONALIGNOREALWAYS'].fields_by_name['val']._serialized_options = b'\272H\006\310\001\001\330\001\003'
  _globals['_REQUIREDPROTO2SCALAROPTIONALDEFAULT'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDPROTO2SCALAROPTIONALDEFAULT'].fields_by_name['val']._serialized_options = b'\272H\003\310\001\001'
  _globals['_REQUIREDPROTO2SCALAROPTIONALDEFAULTIGNOREALWAYS'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDPROTO2SCALAROPTIONALDEFAULTIGNOREALWAYS'].fields_by_name['val']._serialized_options = b'\272H\006\310\001\001\330\001\003'
  _globals['_REQUIREDPROTO2SCALARREQUIRED'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDPROTO2SCALARREQUIRED'].fields_by_name['val']._serialized_options = b'\272H\003\310\001\001'
  _globals['_REQUIREDPROTO2MESSAGE'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDPROTO2MESSAGE'].fields_by_name['val']._serialized_options = b'\272H\003\310\001\001'
  _globals['_REQUIREDPROTO2MESSAGEIGNOREALWAYS'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDPROTO2MESSAGEIGNOREALWAYS'].fields_by_name['val']._serialized_options = b'\272H\006\310\001\001\330\001\003'
  _globals['_REQUIREDPROTO2ONEOF'].fields_by_name['a']._loaded_options = None
  _globals['_REQUIREDPROTO2ONEOF'].fields_by_name['a']._serialized_options = b'\272H\003\310\001\001'
  _globals['_REQUIREDPROTO2ONEOFIGNOREALWAYS'].fields_by_name['a']._loaded_options = None
  _globals['_REQUIREDPROTO2ONEOFIGNOREALWAYS'].fields_by_name['a']._serialized_options = b'\272H\006\310\001\001\330\001\003'
  _globals['_REQUIREDPROTO2REPEATED'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDPROTO2REPEATED'].fields_by_name['val']._serialized_options = b'\272H\003\310\001\001'
  _globals['_REQUIREDPROTO2REPEATEDIGNOREALWAYS'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDPROTO2REPEATEDIGNOREALWAYS'].fields_by_name['val']._serialized_options = b'\272H\006\310\001\001\330\001\003'
  _globals['_REQUIREDPROTO2MAP_VALENTRY']._loaded_options = None
  _globals['_REQUIREDPROTO2MAP_VALENTRY']._serialized_options = b'8\001'
  _globals['_REQUIREDPROTO2MAP'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDPROTO2MAP'].fields_by_name['val']._serialized_options = b'\272H\003\310\001\001'
  _globals['_REQUIREDPROTO2MAPIGNOREALWAYS_VALENTRY']._loaded_options = None
  _globals['_REQUIREDPROTO2MAPIGNOREALWAYS_VALENTRY']._serialized_options = b'8\001'
  _globals['_REQUIREDPROTO2MAPIGNOREALWAYS'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDPROTO2MAPIGNOREALWAYS'].fields_by_name['val']._serialized_options = b'\272H\006\310\001\001\330\001\003'
  _globals['_REQUIREDPROTO2SCALAROPTIONAL']._serialized_start=123
  _globals['_REQUIREDPROTO2SCALAROPTIONAL']._serialized_end=179
  _globals['_REQUIREDPROTO2SCALAROPTIONALIGNOREALWAYS']._serialized_start=181
  _globals['_REQUIREDPROTO2SCALAROPTIONALIGNOREALWAYS']._serialized_end=252
  _globals['_REQUIREDPROTO2SCALAROPTIONALDEFAULT']._serialized_start=254
  _globals['_REQUIREDPROTO2SCALAROPTIONALDEFAULT']._serialized_end=322
  _globals['_REQUIREDPROTO2SCALAROPTIONALDEFAULTIGNOREALWAYS']._serialized_start=324
  _globals['_REQUIREDPROTO2SCALAROPTIONALDEFAULTIGNOREALWAYS']._serialized_end=407
  _globals['_REQUIREDPROTO2SCALARREQUIRED']._serialized_start=409
  _globals['_REQUIREDPROTO2SCALARREQUIRED']._serialized_end=465
  _globals['_REQUIREDPROTO2MESSAGE']._serialized_start=468
  _globals['_REQUIREDPROTO2MESSAGE']._serialized_end=601
  _globals['_REQUIREDPROTO2MESSAGE_MSG']._serialized_start=578
  _globals['_REQUIREDPROTO2MESSAGE_MSG']._serialized_end=601
  _globals['_REQUIREDPROTO2MESSAGEIGNOREALWAYS']._serialized_start=604
  _globals['_REQUIREDPROTO2MESSAGEIGNOREALWAYS']._serialized_end=764
  _globals['_REQUIREDPROTO2MESSAGEIGNOREALWAYS_MSG']._serialized_start=578
  _globals['_REQUIREDPROTO2MESSAGEIGNOREALWAYS_MSG']._serialized_end=601
  _globals['_REQUIREDPROTO2ONEOF']._serialized_start=766
  _globals['_REQUIREDPROTO2ONEOF']._serialized_end=834
  _globals['_REQUIREDPROTO2ONEOFIGNOREALWAYS']._serialized_start=836
  _globals['_REQUIREDPROTO2ONEOFIGNOREALWAYS']._serialized_end=919
  _globals['_REQUIREDPROTO2REPEATED']._serialized_start=921
  _globals['_REQUIREDPROTO2REPEATED']._serialized_end=971
  _globals['_REQUIREDPROTO2REPEATEDIGNOREALWAYS']._serialized_start=973
  _globals['_REQUIREDPROTO2REPEATEDIGNOREALWAYS']._serialized_end=1038
  _globals['_REQUIREDPROTO2MAP']._serialized_start=1041
  _globals['_REQUIREDPROTO2MAP']._serialized_end=1202
  _globals['_REQUIREDPROTO2MAP_VALENTRY']._serialized_start=1148
  _globals['_REQUIREDPROTO2MAP_VALENTRY']._serialized_end=1202
  _globals['_REQUIREDPROTO2MAPIGNOREALWAYS']._serialized_start=1205
  _globals['_REQUIREDPROTO2MAPIGNOREALWAYS']._serialized_end=1393
  _globals['_REQUIREDPROTO2MAPIGNOREALWAYS_VALENTRY']._serialized_start=1148
  _globals['_REQUIREDPROTO2MAPIGNOREALWAYS_VALENTRY']._serialized_end=1202
# @@protoc_insertion_point(module_scope)
