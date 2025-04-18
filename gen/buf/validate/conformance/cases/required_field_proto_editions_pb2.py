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
# source: buf/validate/conformance/cases/required_field_proto_editions.proto
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
    'buf/validate/conformance/cases/required_field_proto_editions.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBbuf/validate/conformance/cases/required_field_proto_editions.proto\x12\x1e\x62uf.validate.conformance.cases\x1a\x1b\x62uf/validate/validate.proto\"B\n&RequiredEditionsScalarExplicitPresence\x12\x18\n\x03val\x18\x01 \x01(\tB\x06\xbaH\x03\xc8\x01\x01R\x03val\"Q\n2RequiredEditionsScalarExplicitPresenceIgnoreAlways\x12\x1b\n\x03val\x18\x01 \x01(\tB\t\xbaH\x06\xc8\x01\x01\xd8\x01\x03R\x03val\"N\n-RequiredEditionsScalarExplicitPresenceDefault\x12\x1d\n\x03val\x18\x01 \x01(\t:\x03\x66ooB\x06\xbaH\x03\xc8\x01\x01R\x03val\"]\n9RequiredEditionsScalarExplicitPresenceDefaultIgnoreAlways\x12 \n\x03val\x18\x01 \x01(\t:\x03\x66ooB\t\xbaH\x06\xc8\x01\x01\xd8\x01\x03R\x03val\"G\n&RequiredEditionsScalarImplicitPresence\x12\x1d\n\x03val\x18\x01 \x01(\tB\x0b\xaa\x01\x02\x08\x02\xbaH\x03\xc8\x01\x01R\x03val\"V\n2RequiredEditionsScalarImplicitPresenceIgnoreAlways\x12 \n\x03val\x18\x01 \x01(\tB\x0e\xaa\x01\x02\x08\x02\xbaH\x06\xc8\x01\x01\xd8\x01\x03R\x03val\"E\n$RequiredEditionsScalarLegacyRequired\x12\x1d\n\x03val\x18\x01 \x01(\tB\x0b\xaa\x01\x02\x08\x03\xbaH\x03\xc8\x01\x01R\x03val\"\xa9\x01\n\'RequiredEditionsMessageExplicitPresence\x12\x65\n\x03val\x18\x01 \x01(\x0b\x32K.buf.validate.conformance.cases.RequiredEditionsMessageExplicitPresence.MsgB\x06\xbaH\x03\xc8\x01\x01R\x03val\x1a\x17\n\x03Msg\x12\x10\n\x03val\x18\x01 \x01(\tR\x03val\"\xc4\x01\n3RequiredEditionsMessageExplicitPresenceIgnoreAlways\x12t\n\x03val\x18\x01 \x01(\x0b\x32W.buf.validate.conformance.cases.RequiredEditionsMessageExplicitPresenceIgnoreAlways.MsgB\t\xbaH\x06\xc8\x01\x01\xd8\x01\x03R\x03val\x1a\x17\n\x03Msg\x12\x10\n\x03val\x18\x01 \x01(\tR\x03val\"\xc0\x01\n0RequiredEditionsMessageExplicitPresenceDelimited\x12s\n\x03val\x18\x01 \x01(\x0b\x32T.buf.validate.conformance.cases.RequiredEditionsMessageExplicitPresenceDelimited.MsgB\x0b\xaa\x01\x02(\x02\xbaH\x03\xc8\x01\x01R\x03val\x1a\x17\n\x03Msg\x12\x10\n\x03val\x18\x01 \x01(\tR\x03val\"\xdc\x01\n<RequiredEditionsMessageExplicitPresenceDelimitedIgnoreAlways\x12\x82\x01\n\x03val\x18\x01 \x01(\x0b\x32`.buf.validate.conformance.cases.RequiredEditionsMessageExplicitPresenceDelimitedIgnoreAlways.MsgB\x0e\xaa\x01\x02(\x02\xbaH\x06\xc8\x01\x01\xd8\x01\x03R\x03val\x1a\x17\n\x03Msg\x12\x10\n\x03val\x18\x01 \x01(\tR\x03val\"\xaa\x01\n%RequiredEditionsMessageLegacyRequired\x12h\n\x03val\x18\x01 \x01(\x0b\x32I.buf.validate.conformance.cases.RequiredEditionsMessageLegacyRequired.MsgB\x0b\xaa\x01\x02\x08\x03\xbaH\x03\xc8\x01\x01R\x03val\x1a\x17\n\x03Msg\x12\x10\n\x03val\x18\x01 \x01(\tR\x03val\"\xbe\x01\n.RequiredEditionsMessageLegacyRequiredDelimited\x12s\n\x03val\x18\x01 \x01(\x0b\x32R.buf.validate.conformance.cases.RequiredEditionsMessageLegacyRequiredDelimited.MsgB\r\xaa\x01\x04\x08\x03(\x02\xbaH\x03\xc8\x01\x01R\x03val\x1a\x17\n\x03Msg\x12\x10\n\x03val\x18\x01 \x01(\tR\x03val\"F\n\x15RequiredEditionsOneof\x12\x16\n\x01\x61\x18\x01 \x01(\tB\x06\xbaH\x03\xc8\x01\x01H\x00R\x01\x61\x12\x0e\n\x01\x62\x18\x02 \x01(\tH\x00R\x01\x62\x42\x05\n\x03val\"U\n!RequiredEditionsOneofIgnoreAlways\x12\x19\n\x01\x61\x18\x01 \x01(\tB\t\xbaH\x06\xc8\x01\x01\xd8\x01\x03H\x00R\x01\x61\x12\x0e\n\x01\x62\x18\x02 \x01(\tH\x00R\x01\x62\x42\x05\n\x03val\"4\n\x18RequiredEditionsRepeated\x12\x18\n\x03val\x18\x01 \x03(\tB\x06\xbaH\x03\xc8\x01\x01R\x03val\"C\n$RequiredEditionsRepeatedIgnoreAlways\x12\x1b\n\x03val\x18\x01 \x03(\tB\t\xbaH\x06\xc8\x01\x01\xd8\x01\x03R\x03val\"A\n RequiredEditionsRepeatedExpanded\x12\x1d\n\x03val\x18\x01 \x03(\tB\x0b\xaa\x01\x02\x18\x02\xbaH\x03\xc8\x01\x01R\x03val\"P\n,RequiredEditionsRepeatedExpandedIgnoreAlways\x12 \n\x03val\x18\x01 \x03(\tB\x0e\xaa\x01\x02\x18\x02\xbaH\x06\xc8\x01\x01\xd8\x01\x03R\x03val\"\xa5\x01\n\x13RequiredEditionsMap\x12V\n\x03val\x18\x01 \x03(\x0b\x32<.buf.validate.conformance.cases.RequiredEditionsMap.ValEntryB\x06\xbaH\x03\xc8\x01\x01R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\xc0\x01\n\x1fRequiredEditionsMapIgnoreAlways\x12\x65\n\x03val\x18\x01 \x03(\x0b\x32H.buf.validate.conformance.cases.RequiredEditionsMapIgnoreAlways.ValEntryB\t\xbaH\x06\xc8\x01\x01\xd8\x01\x03R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x42\xe1\x01\n\"com.buf.validate.conformance.casesB\x1fRequiredFieldProtoEditionsProtoP\x01\xa2\x02\x04\x42VCC\xaa\x02\x1e\x42uf.Validate.Conformance.Cases\xca\x02\x1e\x42uf\\Validate\\Conformance\\Cases\xe2\x02*Buf\\Validate\\Conformance\\Cases\\GPBMetadata\xea\x02!Buf::Validate::Conformance::Casesb\x08\x65\x64itionsp\xe8\x07')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'buf.validate.conformance.cases.required_field_proto_editions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.buf.validate.conformance.casesB\037RequiredFieldProtoEditionsProtoP\001\242\002\004BVCC\252\002\036Buf.Validate.Conformance.Cases\312\002\036Buf\\Validate\\Conformance\\Cases\342\002*Buf\\Validate\\Conformance\\Cases\\GPBMetadata\352\002!Buf::Validate::Conformance::Cases'
  _globals['_REQUIREDEDITIONSSCALAREXPLICITPRESENCE'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDEDITIONSSCALAREXPLICITPRESENCE'].fields_by_name['val']._serialized_options = b'\272H\003\310\001\001'
  _globals['_REQUIREDEDITIONSSCALAREXPLICITPRESENCEIGNOREALWAYS'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDEDITIONSSCALAREXPLICITPRESENCEIGNOREALWAYS'].fields_by_name['val']._serialized_options = b'\272H\006\310\001\001\330\001\003'
  _globals['_REQUIREDEDITIONSSCALAREXPLICITPRESENCEDEFAULT'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDEDITIONSSCALAREXPLICITPRESENCEDEFAULT'].fields_by_name['val']._serialized_options = b'\272H\003\310\001\001'
  _globals['_REQUIREDEDITIONSSCALAREXPLICITPRESENCEDEFAULTIGNOREALWAYS'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDEDITIONSSCALAREXPLICITPRESENCEDEFAULTIGNOREALWAYS'].fields_by_name['val']._serialized_options = b'\272H\006\310\001\001\330\001\003'
  _globals['_REQUIREDEDITIONSSCALARIMPLICITPRESENCE'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDEDITIONSSCALARIMPLICITPRESENCE'].fields_by_name['val']._serialized_options = b'\252\001\002\010\002\272H\003\310\001\001'
  _globals['_REQUIREDEDITIONSSCALARIMPLICITPRESENCEIGNOREALWAYS'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDEDITIONSSCALARIMPLICITPRESENCEIGNOREALWAYS'].fields_by_name['val']._serialized_options = b'\252\001\002\010\002\272H\006\310\001\001\330\001\003'
  _globals['_REQUIREDEDITIONSSCALARLEGACYREQUIRED'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDEDITIONSSCALARLEGACYREQUIRED'].fields_by_name['val']._serialized_options = b'\252\001\002\010\003\272H\003\310\001\001'
  _globals['_REQUIREDEDITIONSMESSAGEEXPLICITPRESENCE'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDEDITIONSMESSAGEEXPLICITPRESENCE'].fields_by_name['val']._serialized_options = b'\272H\003\310\001\001'
  _globals['_REQUIREDEDITIONSMESSAGEEXPLICITPRESENCEIGNOREALWAYS'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDEDITIONSMESSAGEEXPLICITPRESENCEIGNOREALWAYS'].fields_by_name['val']._serialized_options = b'\272H\006\310\001\001\330\001\003'
  _globals['_REQUIREDEDITIONSMESSAGEEXPLICITPRESENCEDELIMITED'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDEDITIONSMESSAGEEXPLICITPRESENCEDELIMITED'].fields_by_name['val']._serialized_options = b'\252\001\002(\002\272H\003\310\001\001'
  _globals['_REQUIREDEDITIONSMESSAGEEXPLICITPRESENCEDELIMITEDIGNOREALWAYS'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDEDITIONSMESSAGEEXPLICITPRESENCEDELIMITEDIGNOREALWAYS'].fields_by_name['val']._serialized_options = b'\252\001\002(\002\272H\006\310\001\001\330\001\003'
  _globals['_REQUIREDEDITIONSMESSAGELEGACYREQUIRED'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDEDITIONSMESSAGELEGACYREQUIRED'].fields_by_name['val']._serialized_options = b'\252\001\002\010\003\272H\003\310\001\001'
  _globals['_REQUIREDEDITIONSMESSAGELEGACYREQUIREDDELIMITED'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDEDITIONSMESSAGELEGACYREQUIREDDELIMITED'].fields_by_name['val']._serialized_options = b'\252\001\004\010\003(\002\272H\003\310\001\001'
  _globals['_REQUIREDEDITIONSONEOF'].fields_by_name['a']._loaded_options = None
  _globals['_REQUIREDEDITIONSONEOF'].fields_by_name['a']._serialized_options = b'\272H\003\310\001\001'
  _globals['_REQUIREDEDITIONSONEOFIGNOREALWAYS'].fields_by_name['a']._loaded_options = None
  _globals['_REQUIREDEDITIONSONEOFIGNOREALWAYS'].fields_by_name['a']._serialized_options = b'\272H\006\310\001\001\330\001\003'
  _globals['_REQUIREDEDITIONSREPEATED'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDEDITIONSREPEATED'].fields_by_name['val']._serialized_options = b'\272H\003\310\001\001'
  _globals['_REQUIREDEDITIONSREPEATEDIGNOREALWAYS'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDEDITIONSREPEATEDIGNOREALWAYS'].fields_by_name['val']._serialized_options = b'\272H\006\310\001\001\330\001\003'
  _globals['_REQUIREDEDITIONSREPEATEDEXPANDED'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDEDITIONSREPEATEDEXPANDED'].fields_by_name['val']._serialized_options = b'\252\001\002\030\002\272H\003\310\001\001'
  _globals['_REQUIREDEDITIONSREPEATEDEXPANDEDIGNOREALWAYS'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDEDITIONSREPEATEDEXPANDEDIGNOREALWAYS'].fields_by_name['val']._serialized_options = b'\252\001\002\030\002\272H\006\310\001\001\330\001\003'
  _globals['_REQUIREDEDITIONSMAP_VALENTRY']._loaded_options = None
  _globals['_REQUIREDEDITIONSMAP_VALENTRY']._serialized_options = b'8\001'
  _globals['_REQUIREDEDITIONSMAP'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDEDITIONSMAP'].fields_by_name['val']._serialized_options = b'\272H\003\310\001\001'
  _globals['_REQUIREDEDITIONSMAPIGNOREALWAYS_VALENTRY']._loaded_options = None
  _globals['_REQUIREDEDITIONSMAPIGNOREALWAYS_VALENTRY']._serialized_options = b'8\001'
  _globals['_REQUIREDEDITIONSMAPIGNOREALWAYS'].fields_by_name['val']._loaded_options = None
  _globals['_REQUIREDEDITIONSMAPIGNOREALWAYS'].fields_by_name['val']._serialized_options = b'\272H\006\310\001\001\330\001\003'
  _globals['_REQUIREDEDITIONSSCALAREXPLICITPRESENCE']._serialized_start=131
  _globals['_REQUIREDEDITIONSSCALAREXPLICITPRESENCE']._serialized_end=197
  _globals['_REQUIREDEDITIONSSCALAREXPLICITPRESENCEIGNOREALWAYS']._serialized_start=199
  _globals['_REQUIREDEDITIONSSCALAREXPLICITPRESENCEIGNOREALWAYS']._serialized_end=280
  _globals['_REQUIREDEDITIONSSCALAREXPLICITPRESENCEDEFAULT']._serialized_start=282
  _globals['_REQUIREDEDITIONSSCALAREXPLICITPRESENCEDEFAULT']._serialized_end=360
  _globals['_REQUIREDEDITIONSSCALAREXPLICITPRESENCEDEFAULTIGNOREALWAYS']._serialized_start=362
  _globals['_REQUIREDEDITIONSSCALAREXPLICITPRESENCEDEFAULTIGNOREALWAYS']._serialized_end=455
  _globals['_REQUIREDEDITIONSSCALARIMPLICITPRESENCE']._serialized_start=457
  _globals['_REQUIREDEDITIONSSCALARIMPLICITPRESENCE']._serialized_end=528
  _globals['_REQUIREDEDITIONSSCALARIMPLICITPRESENCEIGNOREALWAYS']._serialized_start=530
  _globals['_REQUIREDEDITIONSSCALARIMPLICITPRESENCEIGNOREALWAYS']._serialized_end=616
  _globals['_REQUIREDEDITIONSSCALARLEGACYREQUIRED']._serialized_start=618
  _globals['_REQUIREDEDITIONSSCALARLEGACYREQUIRED']._serialized_end=687
  _globals['_REQUIREDEDITIONSMESSAGEEXPLICITPRESENCE']._serialized_start=690
  _globals['_REQUIREDEDITIONSMESSAGEEXPLICITPRESENCE']._serialized_end=859
  _globals['_REQUIREDEDITIONSMESSAGEEXPLICITPRESENCE_MSG']._serialized_start=836
  _globals['_REQUIREDEDITIONSMESSAGEEXPLICITPRESENCE_MSG']._serialized_end=859
  _globals['_REQUIREDEDITIONSMESSAGEEXPLICITPRESENCEIGNOREALWAYS']._serialized_start=862
  _globals['_REQUIREDEDITIONSMESSAGEEXPLICITPRESENCEIGNOREALWAYS']._serialized_end=1058
  _globals['_REQUIREDEDITIONSMESSAGEEXPLICITPRESENCEIGNOREALWAYS_MSG']._serialized_start=836
  _globals['_REQUIREDEDITIONSMESSAGEEXPLICITPRESENCEIGNOREALWAYS_MSG']._serialized_end=859
  _globals['_REQUIREDEDITIONSMESSAGEEXPLICITPRESENCEDELIMITED']._serialized_start=1061
  _globals['_REQUIREDEDITIONSMESSAGEEXPLICITPRESENCEDELIMITED']._serialized_end=1253
  _globals['_REQUIREDEDITIONSMESSAGEEXPLICITPRESENCEDELIMITED_MSG']._serialized_start=836
  _globals['_REQUIREDEDITIONSMESSAGEEXPLICITPRESENCEDELIMITED_MSG']._serialized_end=859
  _globals['_REQUIREDEDITIONSMESSAGEEXPLICITPRESENCEDELIMITEDIGNOREALWAYS']._serialized_start=1256
  _globals['_REQUIREDEDITIONSMESSAGEEXPLICITPRESENCEDELIMITEDIGNOREALWAYS']._serialized_end=1476
  _globals['_REQUIREDEDITIONSMESSAGEEXPLICITPRESENCEDELIMITEDIGNOREALWAYS_MSG']._serialized_start=836
  _globals['_REQUIREDEDITIONSMESSAGEEXPLICITPRESENCEDELIMITEDIGNOREALWAYS_MSG']._serialized_end=859
  _globals['_REQUIREDEDITIONSMESSAGELEGACYREQUIRED']._serialized_start=1479
  _globals['_REQUIREDEDITIONSMESSAGELEGACYREQUIRED']._serialized_end=1649
  _globals['_REQUIREDEDITIONSMESSAGELEGACYREQUIRED_MSG']._serialized_start=836
  _globals['_REQUIREDEDITIONSMESSAGELEGACYREQUIRED_MSG']._serialized_end=859
  _globals['_REQUIREDEDITIONSMESSAGELEGACYREQUIREDDELIMITED']._serialized_start=1652
  _globals['_REQUIREDEDITIONSMESSAGELEGACYREQUIREDDELIMITED']._serialized_end=1842
  _globals['_REQUIREDEDITIONSMESSAGELEGACYREQUIREDDELIMITED_MSG']._serialized_start=836
  _globals['_REQUIREDEDITIONSMESSAGELEGACYREQUIREDDELIMITED_MSG']._serialized_end=859
  _globals['_REQUIREDEDITIONSONEOF']._serialized_start=1844
  _globals['_REQUIREDEDITIONSONEOF']._serialized_end=1914
  _globals['_REQUIREDEDITIONSONEOFIGNOREALWAYS']._serialized_start=1916
  _globals['_REQUIREDEDITIONSONEOFIGNOREALWAYS']._serialized_end=2001
  _globals['_REQUIREDEDITIONSREPEATED']._serialized_start=2003
  _globals['_REQUIREDEDITIONSREPEATED']._serialized_end=2055
  _globals['_REQUIREDEDITIONSREPEATEDIGNOREALWAYS']._serialized_start=2057
  _globals['_REQUIREDEDITIONSREPEATEDIGNOREALWAYS']._serialized_end=2124
  _globals['_REQUIREDEDITIONSREPEATEDEXPANDED']._serialized_start=2126
  _globals['_REQUIREDEDITIONSREPEATEDEXPANDED']._serialized_end=2191
  _globals['_REQUIREDEDITIONSREPEATEDEXPANDEDIGNOREALWAYS']._serialized_start=2193
  _globals['_REQUIREDEDITIONSREPEATEDEXPANDEDIGNOREALWAYS']._serialized_end=2273
  _globals['_REQUIREDEDITIONSMAP']._serialized_start=2276
  _globals['_REQUIREDEDITIONSMAP']._serialized_end=2441
  _globals['_REQUIREDEDITIONSMAP_VALENTRY']._serialized_start=2387
  _globals['_REQUIREDEDITIONSMAP_VALENTRY']._serialized_end=2441
  _globals['_REQUIREDEDITIONSMAPIGNOREALWAYS']._serialized_start=2444
  _globals['_REQUIREDEDITIONSMAPIGNOREALWAYS']._serialized_end=2636
  _globals['_REQUIREDEDITIONSMAPIGNOREALWAYS_VALENTRY']._serialized_start=2387
  _globals['_REQUIREDEDITIONSMAPIGNOREALWAYS_VALENTRY']._serialized_end=2441
# @@protoc_insertion_point(module_scope)
