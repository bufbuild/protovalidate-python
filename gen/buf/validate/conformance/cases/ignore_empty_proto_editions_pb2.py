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
# source: buf/validate/conformance/cases/ignore_empty_proto_editions.proto
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
    'buf/validate/conformance/cases/ignore_empty_proto_editions.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@buf/validate/conformance/cases/ignore_empty_proto_editions.proto\x12\x1e\x62uf.validate.conformance.cases\x1a\x1b\x62uf/validate/validate.proto\"I\n)IgnoreEmptyEditionsScalarExplicitPresence\x12\x1c\n\x03val\x18\x01 \x01(\x05\x42\n\xbaH\x07\x1a\x02 \x00\xd0\x01\x01R\x03val\"X\n4IgnoreEmptyEditionsScalarExplicitPresenceWithDefault\x12 \n\x03val\x18\x01 \x01(\x05:\x02\x34\x32\x42\n\xbaH\x07\x1a\x02 \x00\xd0\x01\x01R\x03val\"N\n)IgnoreEmptyEditionsScalarImplicitPresence\x12!\n\x03val\x18\x01 \x01(\x05\x42\x0f\xaa\x01\x02\x08\x02\xbaH\x07\x1a\x02 \x00\xd0\x01\x01R\x03val\"L\n\'IgnoreEmptyEditionsScalarLegacyRequired\x12!\n\x03val\x18\x01 \x01(\x05\x42\x0f\xaa\x01\x02\x08\x03\xbaH\x07\x1a\x02 \x00\xd0\x01\x01R\x03val\"[\n2IgnoreEmptyEditionsScalarLegacyRequiredWithDefault\x12%\n\x03val\x18\x01 \x01(\x05:\x02\x34\x32\x42\x0f\xaa\x01\x02\x08\x03\xbaH\x07\x1a\x02 \x00\xd0\x01\x01R\x03val\"\xed\x01\n*IgnoreEmptyEditionsMessageExplicitPresence\x12\xa5\x01\n\x03val\x18\x01 \x01(\x0b\x32N.buf.validate.conformance.cases.IgnoreEmptyEditionsMessageExplicitPresence.MsgBC\xbaH@\xba\x01:\n\x1dignore_empty.editions.message\x12\x06\x66oobar\x1a\x11this.val == \'foo\'\xd0\x01\x01R\x03val\x1a\x17\n\x03Msg\x12\x10\n\x03val\x18\x01 \x01(\tR\x03val\"\x84\x02\n3IgnoreEmptyEditionsMessageExplicitPresenceDelimited\x12\xb3\x01\n\x03val\x18\x01 \x01(\x0b\x32W.buf.validate.conformance.cases.IgnoreEmptyEditionsMessageExplicitPresenceDelimited.MsgBH\xaa\x01\x02(\x02\xbaH@\xba\x01:\n\x1dignore_empty.editions.message\x12\x06\x66oobar\x1a\x11this.val == \'foo\'\xd0\x01\x01R\x03val\x1a\x17\n\x03Msg\x12\x10\n\x03val\x18\x01 \x01(\tR\x03val\"\xee\x01\n(IgnoreEmptyEditionsMessageLegacyRequired\x12\xa8\x01\n\x03val\x18\x01 \x01(\x0b\x32L.buf.validate.conformance.cases.IgnoreEmptyEditionsMessageLegacyRequired.MsgBH\xaa\x01\x02\x08\x03\xbaH@\xba\x01:\n\x1dignore_empty.editions.message\x12\x06\x66oobar\x1a\x11this.val == \'foo\'\xd0\x01\x01R\x03val\x1a\x17\n\x03Msg\x12\x10\n\x03val\x18\x01 \x01(\tR\x03val\"\x82\x02\n1IgnoreEmptyEditionsMessageLegacyRequiredDelimited\x12\xb3\x01\n\x03val\x18\x01 \x01(\x0b\x32U.buf.validate.conformance.cases.IgnoreEmptyEditionsMessageLegacyRequiredDelimited.MsgBJ\xaa\x01\x04\x08\x03(\x02\xbaH@\xba\x01:\n\x1dignore_empty.editions.message\x12\x06\x66oobar\x1a\x11this.val == \'foo\'\xd0\x01\x01R\x03val\x1a\x17\n\x03Msg\x12\x10\n\x03val\x18\x01 \x01(\tR\x03val\"?\n\x18IgnoreEmptyEditionsOneof\x12\x1e\n\x03val\x18\x01 \x01(\x05\x42\n\xbaH\x07\x1a\x02 \x00\xd0\x01\x01H\x00R\x03valB\x03\n\x01o\"<\n\x1bIgnoreEmptyEditionsRepeated\x12\x1d\n\x03val\x18\x01 \x03(\x05\x42\x0b\xbaH\x08\x92\x01\x02\x08\x03\xd0\x01\x01R\x03val\"I\n#IgnoreEmptyEditionsRepeatedExpanded\x12\"\n\x03val\x18\x01 \x03(\x05\x42\x10\xaa\x01\x02\x18\x02\xbaH\x08\x92\x01\x02\x08\x03\xd0\x01\x01R\x03val\"\xb0\x01\n\x16IgnoreEmptyEditionsMap\x12^\n\x03val\x18\x01 \x03(\x0b\x32?.buf.validate.conformance.cases.IgnoreEmptyEditionsMap.ValEntryB\x0b\xbaH\x08\x9a\x01\x02\x08\x03\xd0\x01\x01R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\x05R\x03key\x12\x14\n\x05value\x18\x02 \x01(\x05R\x05value:\x02\x38\x01\x62\x08\x65\x64itionsp\xe8\x07')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'buf.validate.conformance.cases.ignore_empty_proto_editions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_IGNOREEMPTYEDITIONSSCALAREXPLICITPRESENCE'].fields_by_name['val']._loaded_options = None
  _globals['_IGNOREEMPTYEDITIONSSCALAREXPLICITPRESENCE'].fields_by_name['val']._serialized_options = b'\272H\007\032\002 \000\320\001\001'
  _globals['_IGNOREEMPTYEDITIONSSCALAREXPLICITPRESENCEWITHDEFAULT'].fields_by_name['val']._loaded_options = None
  _globals['_IGNOREEMPTYEDITIONSSCALAREXPLICITPRESENCEWITHDEFAULT'].fields_by_name['val']._serialized_options = b'\272H\007\032\002 \000\320\001\001'
  _globals['_IGNOREEMPTYEDITIONSSCALARIMPLICITPRESENCE'].fields_by_name['val']._loaded_options = None
  _globals['_IGNOREEMPTYEDITIONSSCALARIMPLICITPRESENCE'].fields_by_name['val']._serialized_options = b'\252\001\002\010\002\272H\007\032\002 \000\320\001\001'
  _globals['_IGNOREEMPTYEDITIONSSCALARLEGACYREQUIRED'].fields_by_name['val']._loaded_options = None
  _globals['_IGNOREEMPTYEDITIONSSCALARLEGACYREQUIRED'].fields_by_name['val']._serialized_options = b'\252\001\002\010\003\272H\007\032\002 \000\320\001\001'
  _globals['_IGNOREEMPTYEDITIONSSCALARLEGACYREQUIREDWITHDEFAULT'].fields_by_name['val']._loaded_options = None
  _globals['_IGNOREEMPTYEDITIONSSCALARLEGACYREQUIREDWITHDEFAULT'].fields_by_name['val']._serialized_options = b'\252\001\002\010\003\272H\007\032\002 \000\320\001\001'
  _globals['_IGNOREEMPTYEDITIONSMESSAGEEXPLICITPRESENCE'].fields_by_name['val']._loaded_options = None
  _globals['_IGNOREEMPTYEDITIONSMESSAGEEXPLICITPRESENCE'].fields_by_name['val']._serialized_options = b'\272H@\272\001:\n\035ignore_empty.editions.message\022\006foobar\032\021this.val == \'foo\'\320\001\001'
  _globals['_IGNOREEMPTYEDITIONSMESSAGEEXPLICITPRESENCEDELIMITED'].fields_by_name['val']._loaded_options = None
  _globals['_IGNOREEMPTYEDITIONSMESSAGEEXPLICITPRESENCEDELIMITED'].fields_by_name['val']._serialized_options = b'\252\001\002(\002\272H@\272\001:\n\035ignore_empty.editions.message\022\006foobar\032\021this.val == \'foo\'\320\001\001'
  _globals['_IGNOREEMPTYEDITIONSMESSAGELEGACYREQUIRED'].fields_by_name['val']._loaded_options = None
  _globals['_IGNOREEMPTYEDITIONSMESSAGELEGACYREQUIRED'].fields_by_name['val']._serialized_options = b'\252\001\002\010\003\272H@\272\001:\n\035ignore_empty.editions.message\022\006foobar\032\021this.val == \'foo\'\320\001\001'
  _globals['_IGNOREEMPTYEDITIONSMESSAGELEGACYREQUIREDDELIMITED'].fields_by_name['val']._loaded_options = None
  _globals['_IGNOREEMPTYEDITIONSMESSAGELEGACYREQUIREDDELIMITED'].fields_by_name['val']._serialized_options = b'\252\001\004\010\003(\002\272H@\272\001:\n\035ignore_empty.editions.message\022\006foobar\032\021this.val == \'foo\'\320\001\001'
  _globals['_IGNOREEMPTYEDITIONSONEOF'].fields_by_name['val']._loaded_options = None
  _globals['_IGNOREEMPTYEDITIONSONEOF'].fields_by_name['val']._serialized_options = b'\272H\007\032\002 \000\320\001\001'
  _globals['_IGNOREEMPTYEDITIONSREPEATED'].fields_by_name['val']._loaded_options = None
  _globals['_IGNOREEMPTYEDITIONSREPEATED'].fields_by_name['val']._serialized_options = b'\272H\010\222\001\002\010\003\320\001\001'
  _globals['_IGNOREEMPTYEDITIONSREPEATEDEXPANDED'].fields_by_name['val']._loaded_options = None
  _globals['_IGNOREEMPTYEDITIONSREPEATEDEXPANDED'].fields_by_name['val']._serialized_options = b'\252\001\002\030\002\272H\010\222\001\002\010\003\320\001\001'
  _globals['_IGNOREEMPTYEDITIONSMAP_VALENTRY']._loaded_options = None
  _globals['_IGNOREEMPTYEDITIONSMAP_VALENTRY']._serialized_options = b'8\001'
  _globals['_IGNOREEMPTYEDITIONSMAP'].fields_by_name['val']._loaded_options = None
  _globals['_IGNOREEMPTYEDITIONSMAP'].fields_by_name['val']._serialized_options = b'\272H\010\232\001\002\010\003\320\001\001'
  _globals['_IGNOREEMPTYEDITIONSSCALAREXPLICITPRESENCE']._serialized_start=129
  _globals['_IGNOREEMPTYEDITIONSSCALAREXPLICITPRESENCE']._serialized_end=202
  _globals['_IGNOREEMPTYEDITIONSSCALAREXPLICITPRESENCEWITHDEFAULT']._serialized_start=204
  _globals['_IGNOREEMPTYEDITIONSSCALAREXPLICITPRESENCEWITHDEFAULT']._serialized_end=292
  _globals['_IGNOREEMPTYEDITIONSSCALARIMPLICITPRESENCE']._serialized_start=294
  _globals['_IGNOREEMPTYEDITIONSSCALARIMPLICITPRESENCE']._serialized_end=372
  _globals['_IGNOREEMPTYEDITIONSSCALARLEGACYREQUIRED']._serialized_start=374
  _globals['_IGNOREEMPTYEDITIONSSCALARLEGACYREQUIRED']._serialized_end=450
  _globals['_IGNOREEMPTYEDITIONSSCALARLEGACYREQUIREDWITHDEFAULT']._serialized_start=452
  _globals['_IGNOREEMPTYEDITIONSSCALARLEGACYREQUIREDWITHDEFAULT']._serialized_end=543
  _globals['_IGNOREEMPTYEDITIONSMESSAGEEXPLICITPRESENCE']._serialized_start=546
  _globals['_IGNOREEMPTYEDITIONSMESSAGEEXPLICITPRESENCE']._serialized_end=783
  _globals['_IGNOREEMPTYEDITIONSMESSAGEEXPLICITPRESENCE_MSG']._serialized_start=760
  _globals['_IGNOREEMPTYEDITIONSMESSAGEEXPLICITPRESENCE_MSG']._serialized_end=783
  _globals['_IGNOREEMPTYEDITIONSMESSAGEEXPLICITPRESENCEDELIMITED']._serialized_start=786
  _globals['_IGNOREEMPTYEDITIONSMESSAGEEXPLICITPRESENCEDELIMITED']._serialized_end=1046
  _globals['_IGNOREEMPTYEDITIONSMESSAGEEXPLICITPRESENCEDELIMITED_MSG']._serialized_start=760
  _globals['_IGNOREEMPTYEDITIONSMESSAGEEXPLICITPRESENCEDELIMITED_MSG']._serialized_end=783
  _globals['_IGNOREEMPTYEDITIONSMESSAGELEGACYREQUIRED']._serialized_start=1049
  _globals['_IGNOREEMPTYEDITIONSMESSAGELEGACYREQUIRED']._serialized_end=1287
  _globals['_IGNOREEMPTYEDITIONSMESSAGELEGACYREQUIRED_MSG']._serialized_start=760
  _globals['_IGNOREEMPTYEDITIONSMESSAGELEGACYREQUIRED_MSG']._serialized_end=783
  _globals['_IGNOREEMPTYEDITIONSMESSAGELEGACYREQUIREDDELIMITED']._serialized_start=1290
  _globals['_IGNOREEMPTYEDITIONSMESSAGELEGACYREQUIREDDELIMITED']._serialized_end=1548
  _globals['_IGNOREEMPTYEDITIONSMESSAGELEGACYREQUIREDDELIMITED_MSG']._serialized_start=760
  _globals['_IGNOREEMPTYEDITIONSMESSAGELEGACYREQUIREDDELIMITED_MSG']._serialized_end=783
  _globals['_IGNOREEMPTYEDITIONSONEOF']._serialized_start=1550
  _globals['_IGNOREEMPTYEDITIONSONEOF']._serialized_end=1613
  _globals['_IGNOREEMPTYEDITIONSREPEATED']._serialized_start=1615
  _globals['_IGNOREEMPTYEDITIONSREPEATED']._serialized_end=1675
  _globals['_IGNOREEMPTYEDITIONSREPEATEDEXPANDED']._serialized_start=1677
  _globals['_IGNOREEMPTYEDITIONSREPEATEDEXPANDED']._serialized_end=1750
  _globals['_IGNOREEMPTYEDITIONSMAP']._serialized_start=1753
  _globals['_IGNOREEMPTYEDITIONSMAP']._serialized_end=1929
  _globals['_IGNOREEMPTYEDITIONSMAP_VALENTRY']._serialized_start=1875
  _globals['_IGNOREEMPTYEDITIONSMAP_VALENTRY']._serialized_end=1929
# @@protoc_insertion_point(module_scope)