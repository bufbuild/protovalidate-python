# Copyright 2023 Buf Technologies, Inc.
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
# source: buf/validate/conformance/cases/required_field_proto2.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:buf/validate/conformance/cases/required_field_proto2.proto\x12\x1e\x62uf.validate.conformance.cases\x1a\x1b\x62uf/validate/validate.proto\"8\n\x1cRequiredProto2ScalarOptional\x12\x18\n\x03val\x18\x01 \x01(\tB\x06\xbaH\x03\xc8\x01\x01R\x03val\"D\n#RequiredProto2ScalarOptionalDefault\x12\x1d\n\x03val\x18\x01 \x01(\t:\x03\x66ooB\x06\xbaH\x03\xc8\x01\x01R\x03val\"8\n\x1cRequiredProto2ScalarRequired\x12\x18\n\x03val\x18\x01 \x02(\tB\x06\xbaH\x03\xc8\x01\x01R\x03val\"\x85\x01\n\x15RequiredProto2Message\x12S\n\x03val\x18\x01 \x01(\x0b\x32\x39.buf.validate.conformance.cases.RequiredProto2Message.MsgB\x06\xbaH\x03\xc8\x01\x01R\x03val\x1a\x17\n\x03Msg\x12\x10\n\x03val\x18\x01 \x01(\tR\x03val\"D\n\x13RequiredProto2Oneof\x12\x16\n\x01\x61\x18\x01 \x01(\tB\x06\xbaH\x03\xc8\x01\x01H\x00R\x01\x61\x12\x0e\n\x01\x62\x18\x02 \x01(\tH\x00R\x01\x62\x42\x05\n\x03val\"2\n\x16RequiredProto2Repeated\x12\x18\n\x03val\x18\x01 \x03(\tB\x06\xbaH\x03\xc8\x01\x01R\x03val\"\xa1\x01\n\x11RequiredProto2Map\x12T\n\x03val\x18\x01 \x03(\x0b\x32:.buf.validate.conformance.cases.RequiredProto2Map.ValEntryB\x06\xbaH\x03\xc8\x01\x01R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'buf.validate.conformance.cases.required_field_proto2_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUIREDPROTO2SCALAROPTIONAL.fields_by_name['val']._options = None
  _REQUIREDPROTO2SCALAROPTIONAL.fields_by_name['val']._serialized_options = b'\272H\003\310\001\001'
  _REQUIREDPROTO2SCALAROPTIONALDEFAULT.fields_by_name['val']._options = None
  _REQUIREDPROTO2SCALAROPTIONALDEFAULT.fields_by_name['val']._serialized_options = b'\272H\003\310\001\001'
  _REQUIREDPROTO2SCALARREQUIRED.fields_by_name['val']._options = None
  _REQUIREDPROTO2SCALARREQUIRED.fields_by_name['val']._serialized_options = b'\272H\003\310\001\001'
  _REQUIREDPROTO2MESSAGE.fields_by_name['val']._options = None
  _REQUIREDPROTO2MESSAGE.fields_by_name['val']._serialized_options = b'\272H\003\310\001\001'
  _REQUIREDPROTO2ONEOF.fields_by_name['a']._options = None
  _REQUIREDPROTO2ONEOF.fields_by_name['a']._serialized_options = b'\272H\003\310\001\001'
  _REQUIREDPROTO2REPEATED.fields_by_name['val']._options = None
  _REQUIREDPROTO2REPEATED.fields_by_name['val']._serialized_options = b'\272H\003\310\001\001'
  _REQUIREDPROTO2MAP_VALENTRY._options = None
  _REQUIREDPROTO2MAP_VALENTRY._serialized_options = b'8\001'
  _REQUIREDPROTO2MAP.fields_by_name['val']._options = None
  _REQUIREDPROTO2MAP.fields_by_name['val']._serialized_options = b'\272H\003\310\001\001'
  _globals['_REQUIREDPROTO2SCALAROPTIONAL']._serialized_start=123
  _globals['_REQUIREDPROTO2SCALAROPTIONAL']._serialized_end=179
  _globals['_REQUIREDPROTO2SCALAROPTIONALDEFAULT']._serialized_start=181
  _globals['_REQUIREDPROTO2SCALAROPTIONALDEFAULT']._serialized_end=249
  _globals['_REQUIREDPROTO2SCALARREQUIRED']._serialized_start=251
  _globals['_REQUIREDPROTO2SCALARREQUIRED']._serialized_end=307
  _globals['_REQUIREDPROTO2MESSAGE']._serialized_start=310
  _globals['_REQUIREDPROTO2MESSAGE']._serialized_end=443
  _globals['_REQUIREDPROTO2MESSAGE_MSG']._serialized_start=420
  _globals['_REQUIREDPROTO2MESSAGE_MSG']._serialized_end=443
  _globals['_REQUIREDPROTO2ONEOF']._serialized_start=445
  _globals['_REQUIREDPROTO2ONEOF']._serialized_end=513
  _globals['_REQUIREDPROTO2REPEATED']._serialized_start=515
  _globals['_REQUIREDPROTO2REPEATED']._serialized_end=565
  _globals['_REQUIREDPROTO2MAP']._serialized_start=568
  _globals['_REQUIREDPROTO2MAP']._serialized_end=729
  _globals['_REQUIREDPROTO2MAP_VALENTRY']._serialized_start=675
  _globals['_REQUIREDPROTO2MAP_VALENTRY']._serialized_end=729
# @@protoc_insertion_point(module_scope)
