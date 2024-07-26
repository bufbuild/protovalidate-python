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
# NO CHECKED-IN PROTOBUF GENCODE
# source: buf/validate/conformance/cases/ignore_proto2.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'buf/validate/conformance/cases/ignore_proto2.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2buf/validate/conformance/cases/ignore_proto2.proto\x12\x1e\x62uf.validate.conformance.cases\x1a\x1b\x62uf/validate/validate.proto\"B\n%Proto2ScalarOptionalIgnoreUnspecified\x12\x19\n\x03val\x18\x01 \x01(\x05\x42\x07\xbaH\x04\x1a\x02 \x00R\x03val\"R\n0Proto2ScalarOptionalIgnoreUnspecifiedWithDefault\x12\x1e\n\x03val\x18\x01 \x01(\x05:\x03-42B\x07\xbaH\x04\x1a\x02 \x00R\x03val\"?\n\x1fProto2ScalarOptionalIgnoreEmpty\x12\x1c\n\x03val\x18\x01 \x01(\x05\x42\n\xbaH\x07\x1a\x02 \x00\xd8\x01\x01R\x03val\"O\n*Proto2ScalarOptionalIgnoreEmptyWithDefault\x12!\n\x03val\x18\x01 \x01(\x05:\x03-42B\n\xbaH\x07\x1a\x02 \x00\xd8\x01\x01R\x03val\"A\n!Proto2ScalarOptionalIgnoreDefault\x12\x1c\n\x03val\x18\x01 \x01(\x05\x42\n\xbaH\x07\x1a\x02 \x00\xd8\x01\x02R\x03val\"Q\n,Proto2ScalarOptionalIgnoreDefaultWithDefault\x12!\n\x03val\x18\x01 \x01(\x05:\x03-42B\n\xbaH\x07\x1a\x02 \x00\xd8\x01\x02R\x03val\"B\n%Proto2ScalarRequiredIgnoreUnspecified\x12\x19\n\x03val\x18\x01 \x02(\x05\x42\x07\xbaH\x04\x1a\x02 \x00R\x03val\"R\n0Proto2ScalarRequiredIgnoreUnspecifiedWithDefault\x12\x1e\n\x03val\x18\x01 \x02(\x05:\x03-42B\x07\xbaH\x04\x1a\x02 \x00R\x03val\"?\n\x1fProto2ScalarRequiredIgnoreEmpty\x12\x1c\n\x03val\x18\x01 \x02(\x05\x42\n\xbaH\x07\x1a\x02 \x00\xd8\x01\x01R\x03val\"O\n*Proto2ScalarRequiredIgnoreEmptyWithDefault\x12!\n\x03val\x18\x01 \x02(\x05:\x03-42B\n\xbaH\x07\x1a\x02 \x00\xd8\x01\x01R\x03val\"A\n!Proto2ScalarRequiredIgnoreDefault\x12\x1c\n\x03val\x18\x01 \x02(\x05\x42\n\xbaH\x07\x1a\x02 \x00\xd8\x01\x02R\x03val\"Q\n,Proto2ScalarRequiredIgnoreDefaultWithDefault\x12!\n\x03val\x18\x01 \x02(\x05:\x03-42B\n\xbaH\x07\x1a\x02 \x00\xd8\x01\x02R\x03val\"\xe0\x01\n&Proto2MessageOptionalIgnoreUnspecified\x12\x9c\x01\n\x03val\x18\x01 \x01(\x0b\x32J.buf.validate.conformance.cases.Proto2MessageOptionalIgnoreUnspecified.MsgB>\xbaH;\xba\x01\x38\n\x1bproto2.message.ignore.empty\x12\x06\x66oobar\x1a\x11this.val == \'foo\'R\x03val\x1a\x17\n\x03Msg\x12\x10\n\x03val\x18\x01 \x01(\tR\x03val\"\xd7\x01\n Proto2MessageOptionalIgnoreEmpty\x12\x99\x01\n\x03val\x18\x01 \x01(\x0b\x32\x44.buf.validate.conformance.cases.Proto2MessageOptionalIgnoreEmpty.MsgBA\xbaH>\xba\x01\x38\n\x1bproto2.message.ignore.empty\x12\x06\x66oobar\x1a\x11this.val == \'foo\'\xd8\x01\x01R\x03val\x1a\x17\n\x03Msg\x12\x10\n\x03val\x18\x01 \x01(\tR\x03val\"\xdb\x01\n\"Proto2MessageOptionalIgnoreDefault\x12\x9b\x01\n\x03val\x18\x01 \x01(\x0b\x32\x46.buf.validate.conformance.cases.Proto2MessageOptionalIgnoreDefault.MsgBA\xbaH>\xba\x01\x38\n\x1bproto2.message.ignore.empty\x12\x06\x66oobar\x1a\x11this.val == \'foo\'\xd8\x01\x02R\x03val\x1a\x17\n\x03Msg\x12\x10\n\x03val\x18\x01 \x01(\tR\x03val\"\xe0\x01\n&Proto2MessageRequiredIgnoreUnspecified\x12\x9c\x01\n\x03val\x18\x01 \x02(\x0b\x32J.buf.validate.conformance.cases.Proto2MessageRequiredIgnoreUnspecified.MsgB>\xbaH;\xba\x01\x38\n\x1bproto2.message.ignore.empty\x12\x06\x66oobar\x1a\x11this.val == \'foo\'R\x03val\x1a\x17\n\x03Msg\x12\x10\n\x03val\x18\x01 \x01(\tR\x03val\"\xd7\x01\n Proto2MessageRequiredIgnoreEmpty\x12\x99\x01\n\x03val\x18\x01 \x02(\x0b\x32\x44.buf.validate.conformance.cases.Proto2MessageRequiredIgnoreEmpty.MsgBA\xbaH>\xba\x01\x38\n\x1bproto2.message.ignore.empty\x12\x06\x66oobar\x1a\x11this.val == \'foo\'\xd8\x01\x01R\x03val\x1a\x17\n\x03Msg\x12\x10\n\x03val\x18\x01 \x01(\tR\x03val\"\xdb\x01\n\"Proto2MessageRequiredIgnoreDefault\x12\x9b\x01\n\x03val\x18\x01 \x02(\x0b\x32\x46.buf.validate.conformance.cases.Proto2MessageRequiredIgnoreDefault.MsgBA\xbaH>\xba\x01\x38\n\x1bproto2.message.ignore.empty\x12\x06\x66oobar\x1a\x11this.val == \'foo\'\xd8\x01\x02R\x03val\x1a\x17\n\x03Msg\x12\x10\n\x03val\x18\x01 \x01(\tR\x03val\"@\n\x1cProto2OneofIgnoreUnspecified\x12\x1b\n\x03val\x18\x01 \x01(\x05\x42\x07\xbaH\x04\x1a\x02 \x00H\x00R\x03valB\x03\n\x01o\"P\n\'Proto2OneofIgnoreUnspecifiedWithDefault\x12 \n\x03val\x18\x01 \x01(\x05:\x03-42B\x07\xbaH\x04\x1a\x02 \x00H\x00R\x03valB\x03\n\x01o\"=\n\x16Proto2OneofIgnoreEmpty\x12\x1e\n\x03val\x18\x01 \x01(\x05\x42\n\xbaH\x07\x1a\x02 \x00\xd8\x01\x01H\x00R\x03valB\x03\n\x01o\"M\n!Proto2OneofIgnoreEmptyWithDefault\x12#\n\x03val\x18\x01 \x01(\x05:\x03-42B\n\xbaH\x07\x1a\x02 \x00\xd8\x01\x01H\x00R\x03valB\x03\n\x01o\"?\n\x18Proto2OneofIgnoreDefault\x12\x1e\n\x03val\x18\x01 \x01(\x05\x42\n\xbaH\x07\x1a\x02 \x00\xd8\x01\x02H\x00R\x03valB\x03\n\x01o\"O\n#Proto2OneofIgnoreDefaultWithDefault\x12#\n\x03val\x18\x01 \x01(\x05:\x03-42B\n\xbaH\x07\x1a\x02 \x00\xd8\x01\x02H\x00R\x03valB\x03\n\x01o\"=\n\x1fProto2RepeatedIgnoreUnspecified\x12\x1a\n\x03val\x18\x01 \x03(\x05\x42\x08\xbaH\x05\x92\x01\x02\x08\x03R\x03val\":\n\x19Proto2RepeatedIgnoreEmpty\x12\x1d\n\x03val\x18\x01 \x03(\x05\x42\x0b\xbaH\x08\x92\x01\x02\x08\x03\xd8\x01\x01R\x03val\"<\n\x1bProto2RepeatedIgnoreDefault\x12\x1d\n\x03val\x18\x01 \x03(\x05\x42\x0b\xbaH\x08\x92\x01\x02\x08\x03\xd8\x01\x02R\x03val\"\xb5\x01\n\x1aProto2MapIgnoreUnspecified\x12_\n\x03val\x18\x01 \x03(\x0b\x32\x43.buf.validate.conformance.cases.Proto2MapIgnoreUnspecified.ValEntryB\x08\xbaH\x05\x9a\x01\x02\x08\x03R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\x05R\x03key\x12\x14\n\x05value\x18\x02 \x01(\x05R\x05value:\x02\x38\x01\"\xac\x01\n\x14Proto2MapIgnoreEmpty\x12\\\n\x03val\x18\x01 \x03(\x0b\x32=.buf.validate.conformance.cases.Proto2MapIgnoreEmpty.ValEntryB\x0b\xbaH\x08\x9a\x01\x02\x08\x03\xd8\x01\x01R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\x05R\x03key\x12\x14\n\x05value\x18\x02 \x01(\x05R\x05value:\x02\x38\x01\"\xb0\x01\n\x16Proto2MapIgnoreDefault\x12^\n\x03val\x18\x01 \x03(\x0b\x32?.buf.validate.conformance.cases.Proto2MapIgnoreDefault.ValEntryB\x0b\xbaH\x08\x9a\x01\x02\x08\x03\xd8\x01\x02R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\x05R\x03key\x12\x14\n\x05value\x18\x02 \x01(\x05R\x05value:\x02\x38\x01\"E\n#Proto2RepeatedItemIgnoreUnspecified\x12\x1e\n\x03val\x18\x01 \x03(\x05\x42\x0c\xbaH\t\x92\x01\x06\"\x04\x1a\x02 \x00R\x03val\"B\n\x1dProto2RepeatedItemIgnoreEmpty\x12!\n\x03val\x18\x01 \x03(\x05\x42\x0f\xbaH\x0c\x92\x01\t\"\x07\x1a\x02 \x00\xd8\x01\x01R\x03val\"D\n\x1fProto2RepeatedItemIgnoreDefault\x12!\n\x03val\x18\x01 \x03(\x05\x42\x0f\xbaH\x0c\x92\x01\t\"\x07\x1a\x02 \x00\xd8\x01\x02R\x03val\"\xbf\x01\n\x1dProto2MapKeyIgnoreUnspecified\x12\x66\n\x03val\x18\x01 \x03(\x0b\x32\x46.buf.validate.conformance.cases.Proto2MapKeyIgnoreUnspecified.ValEntryB\x0c\xbaH\t\x9a\x01\x06\"\x04\x1a\x02 \x00R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\x05R\x03key\x12\x14\n\x05value\x18\x02 \x01(\x05R\x05value:\x02\x38\x01\"\xb6\x01\n\x17Proto2MapKeyIgnoreEmpty\x12\x63\n\x03val\x18\x01 \x03(\x0b\x32@.buf.validate.conformance.cases.Proto2MapKeyIgnoreEmpty.ValEntryB\x0f\xbaH\x0c\x9a\x01\t\"\x07\x1a\x02 \x00\xd8\x01\x01R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\x05R\x03key\x12\x14\n\x05value\x18\x02 \x01(\x05R\x05value:\x02\x38\x01\"\xba\x01\n\x19Proto2MapKeyIgnoreDefault\x12\x65\n\x03val\x18\x01 \x03(\x0b\x32\x42.buf.validate.conformance.cases.Proto2MapKeyIgnoreDefault.ValEntryB\x0f\xbaH\x0c\x9a\x01\t\"\x07\x1a\x02 \x00\xd8\x01\x02R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\x05R\x03key\x12\x14\n\x05value\x18\x02 \x01(\x05R\x05value:\x02\x38\x01\"\xc3\x01\n\x1fProto2MapValueIgnoreUnspecified\x12h\n\x03val\x18\x01 \x03(\x0b\x32H.buf.validate.conformance.cases.Proto2MapValueIgnoreUnspecified.ValEntryB\x0c\xbaH\t\x9a\x01\x06*\x04\x1a\x02 \x00R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\x05R\x03key\x12\x14\n\x05value\x18\x02 \x01(\x05R\x05value:\x02\x38\x01\"\xba\x01\n\x19Proto2MapValueIgnoreEmpty\x12\x65\n\x03val\x18\x01 \x03(\x0b\x32\x42.buf.validate.conformance.cases.Proto2MapValueIgnoreEmpty.ValEntryB\x0f\xbaH\x0c\x9a\x01\t*\x07\x1a\x02 \x00\xd8\x01\x01R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\x05R\x03key\x12\x14\n\x05value\x18\x02 \x01(\x05R\x05value:\x02\x38\x01\"\xbe\x01\n\x1bProto2MapValueIgnoreDefault\x12g\n\x03val\x18\x01 \x03(\x0b\x32\x44.buf.validate.conformance.cases.Proto2MapValueIgnoreDefault.ValEntryB\x0f\xbaH\x0c\x9a\x01\t*\x07\x1a\x02 \x00\xd8\x01\x02R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\x05R\x03key\x12\x14\n\x05value\x18\x02 \x01(\x05R\x05value:\x02\x38\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'buf.validate.conformance.cases.ignore_proto2_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PROTO2SCALAROPTIONALIGNOREUNSPECIFIED'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2SCALAROPTIONALIGNOREUNSPECIFIED'].fields_by_name['val']._serialized_options = b'\272H\004\032\002 \000'
  _globals['_PROTO2SCALAROPTIONALIGNOREUNSPECIFIEDWITHDEFAULT'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2SCALAROPTIONALIGNOREUNSPECIFIEDWITHDEFAULT'].fields_by_name['val']._serialized_options = b'\272H\004\032\002 \000'
  _globals['_PROTO2SCALAROPTIONALIGNOREEMPTY'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2SCALAROPTIONALIGNOREEMPTY'].fields_by_name['val']._serialized_options = b'\272H\007\032\002 \000\330\001\001'
  _globals['_PROTO2SCALAROPTIONALIGNOREEMPTYWITHDEFAULT'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2SCALAROPTIONALIGNOREEMPTYWITHDEFAULT'].fields_by_name['val']._serialized_options = b'\272H\007\032\002 \000\330\001\001'
  _globals['_PROTO2SCALAROPTIONALIGNOREDEFAULT'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2SCALAROPTIONALIGNOREDEFAULT'].fields_by_name['val']._serialized_options = b'\272H\007\032\002 \000\330\001\002'
  _globals['_PROTO2SCALAROPTIONALIGNOREDEFAULTWITHDEFAULT'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2SCALAROPTIONALIGNOREDEFAULTWITHDEFAULT'].fields_by_name['val']._serialized_options = b'\272H\007\032\002 \000\330\001\002'
  _globals['_PROTO2SCALARREQUIREDIGNOREUNSPECIFIED'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2SCALARREQUIREDIGNOREUNSPECIFIED'].fields_by_name['val']._serialized_options = b'\272H\004\032\002 \000'
  _globals['_PROTO2SCALARREQUIREDIGNOREUNSPECIFIEDWITHDEFAULT'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2SCALARREQUIREDIGNOREUNSPECIFIEDWITHDEFAULT'].fields_by_name['val']._serialized_options = b'\272H\004\032\002 \000'
  _globals['_PROTO2SCALARREQUIREDIGNOREEMPTY'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2SCALARREQUIREDIGNOREEMPTY'].fields_by_name['val']._serialized_options = b'\272H\007\032\002 \000\330\001\001'
  _globals['_PROTO2SCALARREQUIREDIGNOREEMPTYWITHDEFAULT'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2SCALARREQUIREDIGNOREEMPTYWITHDEFAULT'].fields_by_name['val']._serialized_options = b'\272H\007\032\002 \000\330\001\001'
  _globals['_PROTO2SCALARREQUIREDIGNOREDEFAULT'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2SCALARREQUIREDIGNOREDEFAULT'].fields_by_name['val']._serialized_options = b'\272H\007\032\002 \000\330\001\002'
  _globals['_PROTO2SCALARREQUIREDIGNOREDEFAULTWITHDEFAULT'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2SCALARREQUIREDIGNOREDEFAULTWITHDEFAULT'].fields_by_name['val']._serialized_options = b'\272H\007\032\002 \000\330\001\002'
  _globals['_PROTO2MESSAGEOPTIONALIGNOREUNSPECIFIED'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2MESSAGEOPTIONALIGNOREUNSPECIFIED'].fields_by_name['val']._serialized_options = b'\272H;\272\0018\n\033proto2.message.ignore.empty\022\006foobar\032\021this.val == \'foo\''
  _globals['_PROTO2MESSAGEOPTIONALIGNOREEMPTY'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2MESSAGEOPTIONALIGNOREEMPTY'].fields_by_name['val']._serialized_options = b'\272H>\272\0018\n\033proto2.message.ignore.empty\022\006foobar\032\021this.val == \'foo\'\330\001\001'
  _globals['_PROTO2MESSAGEOPTIONALIGNOREDEFAULT'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2MESSAGEOPTIONALIGNOREDEFAULT'].fields_by_name['val']._serialized_options = b'\272H>\272\0018\n\033proto2.message.ignore.empty\022\006foobar\032\021this.val == \'foo\'\330\001\002'
  _globals['_PROTO2MESSAGEREQUIREDIGNOREUNSPECIFIED'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2MESSAGEREQUIREDIGNOREUNSPECIFIED'].fields_by_name['val']._serialized_options = b'\272H;\272\0018\n\033proto2.message.ignore.empty\022\006foobar\032\021this.val == \'foo\''
  _globals['_PROTO2MESSAGEREQUIREDIGNOREEMPTY'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2MESSAGEREQUIREDIGNOREEMPTY'].fields_by_name['val']._serialized_options = b'\272H>\272\0018\n\033proto2.message.ignore.empty\022\006foobar\032\021this.val == \'foo\'\330\001\001'
  _globals['_PROTO2MESSAGEREQUIREDIGNOREDEFAULT'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2MESSAGEREQUIREDIGNOREDEFAULT'].fields_by_name['val']._serialized_options = b'\272H>\272\0018\n\033proto2.message.ignore.empty\022\006foobar\032\021this.val == \'foo\'\330\001\002'
  _globals['_PROTO2ONEOFIGNOREUNSPECIFIED'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2ONEOFIGNOREUNSPECIFIED'].fields_by_name['val']._serialized_options = b'\272H\004\032\002 \000'
  _globals['_PROTO2ONEOFIGNOREUNSPECIFIEDWITHDEFAULT'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2ONEOFIGNOREUNSPECIFIEDWITHDEFAULT'].fields_by_name['val']._serialized_options = b'\272H\004\032\002 \000'
  _globals['_PROTO2ONEOFIGNOREEMPTY'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2ONEOFIGNOREEMPTY'].fields_by_name['val']._serialized_options = b'\272H\007\032\002 \000\330\001\001'
  _globals['_PROTO2ONEOFIGNOREEMPTYWITHDEFAULT'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2ONEOFIGNOREEMPTYWITHDEFAULT'].fields_by_name['val']._serialized_options = b'\272H\007\032\002 \000\330\001\001'
  _globals['_PROTO2ONEOFIGNOREDEFAULT'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2ONEOFIGNOREDEFAULT'].fields_by_name['val']._serialized_options = b'\272H\007\032\002 \000\330\001\002'
  _globals['_PROTO2ONEOFIGNOREDEFAULTWITHDEFAULT'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2ONEOFIGNOREDEFAULTWITHDEFAULT'].fields_by_name['val']._serialized_options = b'\272H\007\032\002 \000\330\001\002'
  _globals['_PROTO2REPEATEDIGNOREUNSPECIFIED'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2REPEATEDIGNOREUNSPECIFIED'].fields_by_name['val']._serialized_options = b'\272H\005\222\001\002\010\003'
  _globals['_PROTO2REPEATEDIGNOREEMPTY'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2REPEATEDIGNOREEMPTY'].fields_by_name['val']._serialized_options = b'\272H\010\222\001\002\010\003\330\001\001'
  _globals['_PROTO2REPEATEDIGNOREDEFAULT'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2REPEATEDIGNOREDEFAULT'].fields_by_name['val']._serialized_options = b'\272H\010\222\001\002\010\003\330\001\002'
  _globals['_PROTO2MAPIGNOREUNSPECIFIED_VALENTRY']._loaded_options = None
  _globals['_PROTO2MAPIGNOREUNSPECIFIED_VALENTRY']._serialized_options = b'8\001'
  _globals['_PROTO2MAPIGNOREUNSPECIFIED'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2MAPIGNOREUNSPECIFIED'].fields_by_name['val']._serialized_options = b'\272H\005\232\001\002\010\003'
  _globals['_PROTO2MAPIGNOREEMPTY_VALENTRY']._loaded_options = None
  _globals['_PROTO2MAPIGNOREEMPTY_VALENTRY']._serialized_options = b'8\001'
  _globals['_PROTO2MAPIGNOREEMPTY'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2MAPIGNOREEMPTY'].fields_by_name['val']._serialized_options = b'\272H\010\232\001\002\010\003\330\001\001'
  _globals['_PROTO2MAPIGNOREDEFAULT_VALENTRY']._loaded_options = None
  _globals['_PROTO2MAPIGNOREDEFAULT_VALENTRY']._serialized_options = b'8\001'
  _globals['_PROTO2MAPIGNOREDEFAULT'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2MAPIGNOREDEFAULT'].fields_by_name['val']._serialized_options = b'\272H\010\232\001\002\010\003\330\001\002'
  _globals['_PROTO2REPEATEDITEMIGNOREUNSPECIFIED'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2REPEATEDITEMIGNOREUNSPECIFIED'].fields_by_name['val']._serialized_options = b'\272H\t\222\001\006\"\004\032\002 \000'
  _globals['_PROTO2REPEATEDITEMIGNOREEMPTY'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2REPEATEDITEMIGNOREEMPTY'].fields_by_name['val']._serialized_options = b'\272H\014\222\001\t\"\007\032\002 \000\330\001\001'
  _globals['_PROTO2REPEATEDITEMIGNOREDEFAULT'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2REPEATEDITEMIGNOREDEFAULT'].fields_by_name['val']._serialized_options = b'\272H\014\222\001\t\"\007\032\002 \000\330\001\002'
  _globals['_PROTO2MAPKEYIGNOREUNSPECIFIED_VALENTRY']._loaded_options = None
  _globals['_PROTO2MAPKEYIGNOREUNSPECIFIED_VALENTRY']._serialized_options = b'8\001'
  _globals['_PROTO2MAPKEYIGNOREUNSPECIFIED'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2MAPKEYIGNOREUNSPECIFIED'].fields_by_name['val']._serialized_options = b'\272H\t\232\001\006\"\004\032\002 \000'
  _globals['_PROTO2MAPKEYIGNOREEMPTY_VALENTRY']._loaded_options = None
  _globals['_PROTO2MAPKEYIGNOREEMPTY_VALENTRY']._serialized_options = b'8\001'
  _globals['_PROTO2MAPKEYIGNOREEMPTY'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2MAPKEYIGNOREEMPTY'].fields_by_name['val']._serialized_options = b'\272H\014\232\001\t\"\007\032\002 \000\330\001\001'
  _globals['_PROTO2MAPKEYIGNOREDEFAULT_VALENTRY']._loaded_options = None
  _globals['_PROTO2MAPKEYIGNOREDEFAULT_VALENTRY']._serialized_options = b'8\001'
  _globals['_PROTO2MAPKEYIGNOREDEFAULT'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2MAPKEYIGNOREDEFAULT'].fields_by_name['val']._serialized_options = b'\272H\014\232\001\t\"\007\032\002 \000\330\001\002'
  _globals['_PROTO2MAPVALUEIGNOREUNSPECIFIED_VALENTRY']._loaded_options = None
  _globals['_PROTO2MAPVALUEIGNOREUNSPECIFIED_VALENTRY']._serialized_options = b'8\001'
  _globals['_PROTO2MAPVALUEIGNOREUNSPECIFIED'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2MAPVALUEIGNOREUNSPECIFIED'].fields_by_name['val']._serialized_options = b'\272H\t\232\001\006*\004\032\002 \000'
  _globals['_PROTO2MAPVALUEIGNOREEMPTY_VALENTRY']._loaded_options = None
  _globals['_PROTO2MAPVALUEIGNOREEMPTY_VALENTRY']._serialized_options = b'8\001'
  _globals['_PROTO2MAPVALUEIGNOREEMPTY'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2MAPVALUEIGNOREEMPTY'].fields_by_name['val']._serialized_options = b'\272H\014\232\001\t*\007\032\002 \000\330\001\001'
  _globals['_PROTO2MAPVALUEIGNOREDEFAULT_VALENTRY']._loaded_options = None
  _globals['_PROTO2MAPVALUEIGNOREDEFAULT_VALENTRY']._serialized_options = b'8\001'
  _globals['_PROTO2MAPVALUEIGNOREDEFAULT'].fields_by_name['val']._loaded_options = None
  _globals['_PROTO2MAPVALUEIGNOREDEFAULT'].fields_by_name['val']._serialized_options = b'\272H\014\232\001\t*\007\032\002 \000\330\001\002'
  _globals['_PROTO2SCALAROPTIONALIGNOREUNSPECIFIED']._serialized_start=115
  _globals['_PROTO2SCALAROPTIONALIGNOREUNSPECIFIED']._serialized_end=181
  _globals['_PROTO2SCALAROPTIONALIGNOREUNSPECIFIEDWITHDEFAULT']._serialized_start=183
  _globals['_PROTO2SCALAROPTIONALIGNOREUNSPECIFIEDWITHDEFAULT']._serialized_end=265
  _globals['_PROTO2SCALAROPTIONALIGNOREEMPTY']._serialized_start=267
  _globals['_PROTO2SCALAROPTIONALIGNOREEMPTY']._serialized_end=330
  _globals['_PROTO2SCALAROPTIONALIGNOREEMPTYWITHDEFAULT']._serialized_start=332
  _globals['_PROTO2SCALAROPTIONALIGNOREEMPTYWITHDEFAULT']._serialized_end=411
  _globals['_PROTO2SCALAROPTIONALIGNOREDEFAULT']._serialized_start=413
  _globals['_PROTO2SCALAROPTIONALIGNOREDEFAULT']._serialized_end=478
  _globals['_PROTO2SCALAROPTIONALIGNOREDEFAULTWITHDEFAULT']._serialized_start=480
  _globals['_PROTO2SCALAROPTIONALIGNOREDEFAULTWITHDEFAULT']._serialized_end=561
  _globals['_PROTO2SCALARREQUIREDIGNOREUNSPECIFIED']._serialized_start=563
  _globals['_PROTO2SCALARREQUIREDIGNOREUNSPECIFIED']._serialized_end=629
  _globals['_PROTO2SCALARREQUIREDIGNOREUNSPECIFIEDWITHDEFAULT']._serialized_start=631
  _globals['_PROTO2SCALARREQUIREDIGNOREUNSPECIFIEDWITHDEFAULT']._serialized_end=713
  _globals['_PROTO2SCALARREQUIREDIGNOREEMPTY']._serialized_start=715
  _globals['_PROTO2SCALARREQUIREDIGNOREEMPTY']._serialized_end=778
  _globals['_PROTO2SCALARREQUIREDIGNOREEMPTYWITHDEFAULT']._serialized_start=780
  _globals['_PROTO2SCALARREQUIREDIGNOREEMPTYWITHDEFAULT']._serialized_end=859
  _globals['_PROTO2SCALARREQUIREDIGNOREDEFAULT']._serialized_start=861
  _globals['_PROTO2SCALARREQUIREDIGNOREDEFAULT']._serialized_end=926
  _globals['_PROTO2SCALARREQUIREDIGNOREDEFAULTWITHDEFAULT']._serialized_start=928
  _globals['_PROTO2SCALARREQUIREDIGNOREDEFAULTWITHDEFAULT']._serialized_end=1009
  _globals['_PROTO2MESSAGEOPTIONALIGNOREUNSPECIFIED']._serialized_start=1012
  _globals['_PROTO2MESSAGEOPTIONALIGNOREUNSPECIFIED']._serialized_end=1236
  _globals['_PROTO2MESSAGEOPTIONALIGNOREUNSPECIFIED_MSG']._serialized_start=1213
  _globals['_PROTO2MESSAGEOPTIONALIGNOREUNSPECIFIED_MSG']._serialized_end=1236
  _globals['_PROTO2MESSAGEOPTIONALIGNOREEMPTY']._serialized_start=1239
  _globals['_PROTO2MESSAGEOPTIONALIGNOREEMPTY']._serialized_end=1454
  _globals['_PROTO2MESSAGEOPTIONALIGNOREEMPTY_MSG']._serialized_start=1213
  _globals['_PROTO2MESSAGEOPTIONALIGNOREEMPTY_MSG']._serialized_end=1236
  _globals['_PROTO2MESSAGEOPTIONALIGNOREDEFAULT']._serialized_start=1457
  _globals['_PROTO2MESSAGEOPTIONALIGNOREDEFAULT']._serialized_end=1676
  _globals['_PROTO2MESSAGEOPTIONALIGNOREDEFAULT_MSG']._serialized_start=1213
  _globals['_PROTO2MESSAGEOPTIONALIGNOREDEFAULT_MSG']._serialized_end=1236
  _globals['_PROTO2MESSAGEREQUIREDIGNOREUNSPECIFIED']._serialized_start=1679
  _globals['_PROTO2MESSAGEREQUIREDIGNOREUNSPECIFIED']._serialized_end=1903
  _globals['_PROTO2MESSAGEREQUIREDIGNOREUNSPECIFIED_MSG']._serialized_start=1213
  _globals['_PROTO2MESSAGEREQUIREDIGNOREUNSPECIFIED_MSG']._serialized_end=1236
  _globals['_PROTO2MESSAGEREQUIREDIGNOREEMPTY']._serialized_start=1906
  _globals['_PROTO2MESSAGEREQUIREDIGNOREEMPTY']._serialized_end=2121
  _globals['_PROTO2MESSAGEREQUIREDIGNOREEMPTY_MSG']._serialized_start=1213
  _globals['_PROTO2MESSAGEREQUIREDIGNOREEMPTY_MSG']._serialized_end=1236
  _globals['_PROTO2MESSAGEREQUIREDIGNOREDEFAULT']._serialized_start=2124
  _globals['_PROTO2MESSAGEREQUIREDIGNOREDEFAULT']._serialized_end=2343
  _globals['_PROTO2MESSAGEREQUIREDIGNOREDEFAULT_MSG']._serialized_start=1213
  _globals['_PROTO2MESSAGEREQUIREDIGNOREDEFAULT_MSG']._serialized_end=1236
  _globals['_PROTO2ONEOFIGNOREUNSPECIFIED']._serialized_start=2345
  _globals['_PROTO2ONEOFIGNOREUNSPECIFIED']._serialized_end=2409
  _globals['_PROTO2ONEOFIGNOREUNSPECIFIEDWITHDEFAULT']._serialized_start=2411
  _globals['_PROTO2ONEOFIGNOREUNSPECIFIEDWITHDEFAULT']._serialized_end=2491
  _globals['_PROTO2ONEOFIGNOREEMPTY']._serialized_start=2493
  _globals['_PROTO2ONEOFIGNOREEMPTY']._serialized_end=2554
  _globals['_PROTO2ONEOFIGNOREEMPTYWITHDEFAULT']._serialized_start=2556
  _globals['_PROTO2ONEOFIGNOREEMPTYWITHDEFAULT']._serialized_end=2633
  _globals['_PROTO2ONEOFIGNOREDEFAULT']._serialized_start=2635
  _globals['_PROTO2ONEOFIGNOREDEFAULT']._serialized_end=2698
  _globals['_PROTO2ONEOFIGNOREDEFAULTWITHDEFAULT']._serialized_start=2700
  _globals['_PROTO2ONEOFIGNOREDEFAULTWITHDEFAULT']._serialized_end=2779
  _globals['_PROTO2REPEATEDIGNOREUNSPECIFIED']._serialized_start=2781
  _globals['_PROTO2REPEATEDIGNOREUNSPECIFIED']._serialized_end=2842
  _globals['_PROTO2REPEATEDIGNOREEMPTY']._serialized_start=2844
  _globals['_PROTO2REPEATEDIGNOREEMPTY']._serialized_end=2902
  _globals['_PROTO2REPEATEDIGNOREDEFAULT']._serialized_start=2904
  _globals['_PROTO2REPEATEDIGNOREDEFAULT']._serialized_end=2964
  _globals['_PROTO2MAPIGNOREUNSPECIFIED']._serialized_start=2967
  _globals['_PROTO2MAPIGNOREUNSPECIFIED']._serialized_end=3148
  _globals['_PROTO2MAPIGNOREUNSPECIFIED_VALENTRY']._serialized_start=3094
  _globals['_PROTO2MAPIGNOREUNSPECIFIED_VALENTRY']._serialized_end=3148
  _globals['_PROTO2MAPIGNOREEMPTY']._serialized_start=3151
  _globals['_PROTO2MAPIGNOREEMPTY']._serialized_end=3323
  _globals['_PROTO2MAPIGNOREEMPTY_VALENTRY']._serialized_start=3094
  _globals['_PROTO2MAPIGNOREEMPTY_VALENTRY']._serialized_end=3148
  _globals['_PROTO2MAPIGNOREDEFAULT']._serialized_start=3326
  _globals['_PROTO2MAPIGNOREDEFAULT']._serialized_end=3502
  _globals['_PROTO2MAPIGNOREDEFAULT_VALENTRY']._serialized_start=3094
  _globals['_PROTO2MAPIGNOREDEFAULT_VALENTRY']._serialized_end=3148
  _globals['_PROTO2REPEATEDITEMIGNOREUNSPECIFIED']._serialized_start=3504
  _globals['_PROTO2REPEATEDITEMIGNOREUNSPECIFIED']._serialized_end=3573
  _globals['_PROTO2REPEATEDITEMIGNOREEMPTY']._serialized_start=3575
  _globals['_PROTO2REPEATEDITEMIGNOREEMPTY']._serialized_end=3641
  _globals['_PROTO2REPEATEDITEMIGNOREDEFAULT']._serialized_start=3643
  _globals['_PROTO2REPEATEDITEMIGNOREDEFAULT']._serialized_end=3711
  _globals['_PROTO2MAPKEYIGNOREUNSPECIFIED']._serialized_start=3714
  _globals['_PROTO2MAPKEYIGNOREUNSPECIFIED']._serialized_end=3905
  _globals['_PROTO2MAPKEYIGNOREUNSPECIFIED_VALENTRY']._serialized_start=3094
  _globals['_PROTO2MAPKEYIGNOREUNSPECIFIED_VALENTRY']._serialized_end=3148
  _globals['_PROTO2MAPKEYIGNOREEMPTY']._serialized_start=3908
  _globals['_PROTO2MAPKEYIGNOREEMPTY']._serialized_end=4090
  _globals['_PROTO2MAPKEYIGNOREEMPTY_VALENTRY']._serialized_start=3094
  _globals['_PROTO2MAPKEYIGNOREEMPTY_VALENTRY']._serialized_end=3148
  _globals['_PROTO2MAPKEYIGNOREDEFAULT']._serialized_start=4093
  _globals['_PROTO2MAPKEYIGNOREDEFAULT']._serialized_end=4279
  _globals['_PROTO2MAPKEYIGNOREDEFAULT_VALENTRY']._serialized_start=3094
  _globals['_PROTO2MAPKEYIGNOREDEFAULT_VALENTRY']._serialized_end=3148
  _globals['_PROTO2MAPVALUEIGNOREUNSPECIFIED']._serialized_start=4282
  _globals['_PROTO2MAPVALUEIGNOREUNSPECIFIED']._serialized_end=4477
  _globals['_PROTO2MAPVALUEIGNOREUNSPECIFIED_VALENTRY']._serialized_start=3094
  _globals['_PROTO2MAPVALUEIGNOREUNSPECIFIED_VALENTRY']._serialized_end=3148
  _globals['_PROTO2MAPVALUEIGNOREEMPTY']._serialized_start=4480
  _globals['_PROTO2MAPVALUEIGNOREEMPTY']._serialized_end=4666
  _globals['_PROTO2MAPVALUEIGNOREEMPTY_VALENTRY']._serialized_start=3094
  _globals['_PROTO2MAPVALUEIGNOREEMPTY_VALENTRY']._serialized_end=3148
  _globals['_PROTO2MAPVALUEIGNOREDEFAULT']._serialized_start=4669
  _globals['_PROTO2MAPVALUEIGNOREDEFAULT']._serialized_end=4859
  _globals['_PROTO2MAPVALUEIGNOREDEFAULT_VALENTRY']._serialized_start=3094
  _globals['_PROTO2MAPVALUEIGNOREDEFAULT_VALENTRY']._serialized_end=3148
# @@protoc_insertion_point(module_scope)
