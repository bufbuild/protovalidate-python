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
# source: buf/validate/conformance/cases/wkt_any.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,buf/validate/conformance/cases/wkt_any.proto\x12\x1e\x62uf.validate.conformance.cases\x1a\x1b\x62uf/validate/validate.proto\x1a\x19google/protobuf/any.proto\"1\n\x07\x41nyNone\x12&\n\x03val\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyR\x03val\">\n\x0b\x41nyRequired\x12/\n\x03val\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyB\x07\xfa\xf7\x18\x03\xc8\x01\x01R\x03val\"f\n\x05\x41nyIn\x12]\n\x03val\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyB5\xfa\xf7\x18\x31\xa2\x01.\x12,type.googleapis.com/google.protobuf.DurationR\x03val\"j\n\x08\x41nyNotIn\x12^\n\x03val\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyB6\xfa\xf7\x18\x32\xa2\x01/\x1a-type.googleapis.com/google.protobuf.TimestampR\x03valb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'buf.validate.conformance.cases.wkt_any_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ANYREQUIRED.fields_by_name['val']._options = None
  _ANYREQUIRED.fields_by_name['val']._serialized_options = b'\372\367\030\003\310\001\001'
  _ANYIN.fields_by_name['val']._options = None
  _ANYIN.fields_by_name['val']._serialized_options = b'\372\367\0301\242\001.\022,type.googleapis.com/google.protobuf.Duration'
  _ANYNOTIN.fields_by_name['val']._options = None
  _ANYNOTIN.fields_by_name['val']._serialized_options = b'\372\367\0302\242\001/\032-type.googleapis.com/google.protobuf.Timestamp'
  _globals['_ANYNONE']._serialized_start=136
  _globals['_ANYNONE']._serialized_end=185
  _globals['_ANYREQUIRED']._serialized_start=187
  _globals['_ANYREQUIRED']._serialized_end=249
  _globals['_ANYIN']._serialized_start=251
  _globals['_ANYIN']._serialized_end=353
  _globals['_ANYNOTIN']._serialized_start=355
  _globals['_ANYNOTIN']._serialized_end=461
# @@protoc_insertion_point(module_scope)
