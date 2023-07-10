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
# source: buf/validate/conformance/cases/messages.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate.conformance.cases.other_package import embed_pb2 as buf_dot_validate_dot_conformance_dot_cases_dot_other__package_dot_embed__pb2
from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-buf/validate/conformance/cases/messages.proto\x12\x1e\x62uf.validate.conformance.cases\x1a\x38\x62uf/validate/conformance/cases/other_package/embed.proto\x1a\x1b\x62uf/validate/validate.proto\"m\n\x07TestMsg\x12!\n\x05\x63onst\x18\x01 \x01(\tB\x0b\xfa\xf7\x18\x07r\x05\n\x03\x66ooR\x05\x63onst\x12?\n\x06nested\x18\x02 \x01(\x0b\x32\'.buf.validate.conformance.cases.TestMsgR\x06nested\"_\n\x0bMessageNone\x12\x45\n\x03val\x18\x01 \x01(\x0b\x32\x33.buf.validate.conformance.cases.MessageNone.NoneMsgR\x03val\x1a\t\n\x07NoneMsg\"5\n\x0fMessageDisabled\x12\x1a\n\x03val\x18\x01 \x01(\x04\x42\x08\xfa\xf7\x18\x04\x32\x02 {R\x03val:\x06\xfa\xf7\x18\x02\x08\x01\"D\n\x07Message\x12\x39\n\x03val\x18\x01 \x01(\x0b\x32\'.buf.validate.conformance.cases.TestMsgR\x03val\"\\\n\x13MessageCrossPackage\x12\x45\n\x03val\x18\x01 \x01(\x0b\x32\x33.buf.validate.conformance.cases.other_package.EmbedR\x03val\"Q\n\x0bMessageSkip\x12\x42\n\x03val\x18\x01 \x01(\x0b\x32\'.buf.validate.conformance.cases.TestMsgB\x07\xfa\xf7\x18\x03\xc0\x01\x01R\x03val\"U\n\x0fMessageRequired\x12\x42\n\x03val\x18\x01 \x01(\x0b\x32\'.buf.validate.conformance.cases.TestMsgB\x07\xfa\xf7\x18\x03\xc8\x01\x01R\x03val\"m\n\x1aMessageRequiredButOptional\x12G\n\x03val\x18\x01 \x01(\x0b\x32\'.buf.validate.conformance.cases.TestMsgB\x07\xfa\xf7\x18\x03\xc8\x01\x01H\x00R\x03val\x88\x01\x01\x42\x06\n\x04_val\"k\n\x14MessageRequiredOneof\x12\x44\n\x03val\x18\x01 \x01(\x0b\x32\'.buf.validate.conformance.cases.TestMsgB\x07\xfa\xf7\x18\x03\xc8\x01\x01H\x00R\x03valB\r\n\x03one\x12\x06\xfa\xf7\x18\x02\x08\x01\"\x15\n\x13MessageWith3dInsideb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'buf.validate.conformance.cases.messages_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TESTMSG.fields_by_name['const']._options = None
  _TESTMSG.fields_by_name['const']._serialized_options = b'\372\367\030\007r\005\n\003foo'
  _MESSAGEDISABLED.fields_by_name['val']._options = None
  _MESSAGEDISABLED.fields_by_name['val']._serialized_options = b'\372\367\030\0042\002 {'
  _MESSAGEDISABLED._options = None
  _MESSAGEDISABLED._serialized_options = b'\372\367\030\002\010\001'
  _MESSAGESKIP.fields_by_name['val']._options = None
  _MESSAGESKIP.fields_by_name['val']._serialized_options = b'\372\367\030\003\300\001\001'
  _MESSAGEREQUIRED.fields_by_name['val']._options = None
  _MESSAGEREQUIRED.fields_by_name['val']._serialized_options = b'\372\367\030\003\310\001\001'
  _MESSAGEREQUIREDBUTOPTIONAL.fields_by_name['val']._options = None
  _MESSAGEREQUIREDBUTOPTIONAL.fields_by_name['val']._serialized_options = b'\372\367\030\003\310\001\001'
  _MESSAGEREQUIREDONEOF.oneofs_by_name['one']._options = None
  _MESSAGEREQUIREDONEOF.oneofs_by_name['one']._serialized_options = b'\372\367\030\002\010\001'
  _MESSAGEREQUIREDONEOF.fields_by_name['val']._options = None
  _MESSAGEREQUIREDONEOF.fields_by_name['val']._serialized_options = b'\372\367\030\003\310\001\001'
  _globals['_TESTMSG']._serialized_start=168
  _globals['_TESTMSG']._serialized_end=277
  _globals['_MESSAGENONE']._serialized_start=279
  _globals['_MESSAGENONE']._serialized_end=374
  _globals['_MESSAGENONE_NONEMSG']._serialized_start=365
  _globals['_MESSAGENONE_NONEMSG']._serialized_end=374
  _globals['_MESSAGEDISABLED']._serialized_start=376
  _globals['_MESSAGEDISABLED']._serialized_end=429
  _globals['_MESSAGE']._serialized_start=431
  _globals['_MESSAGE']._serialized_end=499
  _globals['_MESSAGECROSSPACKAGE']._serialized_start=501
  _globals['_MESSAGECROSSPACKAGE']._serialized_end=593
  _globals['_MESSAGESKIP']._serialized_start=595
  _globals['_MESSAGESKIP']._serialized_end=676
  _globals['_MESSAGEREQUIRED']._serialized_start=678
  _globals['_MESSAGEREQUIRED']._serialized_end=763
  _globals['_MESSAGEREQUIREDBUTOPTIONAL']._serialized_start=765
  _globals['_MESSAGEREQUIREDBUTOPTIONAL']._serialized_end=874
  _globals['_MESSAGEREQUIREDONEOF']._serialized_start=876
  _globals['_MESSAGEREQUIREDONEOF']._serialized_end=983
  _globals['_MESSAGEWITH3DINSIDE']._serialized_start=985
  _globals['_MESSAGEWITH3DINSIDE']._serialized_end=1006
# @@protoc_insertion_point(module_scope)
