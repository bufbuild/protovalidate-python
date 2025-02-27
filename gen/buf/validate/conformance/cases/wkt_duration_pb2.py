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
# source: buf/validate/conformance/cases/wkt_duration.proto
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
    'buf/validate/conformance/cases/wkt_duration.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1buf/validate/conformance/cases/wkt_duration.proto\x12\x1e\x62uf.validate.conformance.cases\x1a\x1b\x62uf/validate/validate.proto\x1a\x1egoogle/protobuf/duration.proto\";\n\x0c\x44urationNone\x12+\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationR\x03val\"G\n\x10\x44urationRequired\x12\x33\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x06\xbaH\x03\xc8\x01\x01R\x03val\"H\n\rDurationConst\x12\x37\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\n\xbaH\x07\xaa\x01\x04\x12\x02\x08\x03R\x03val\"J\n\nDurationIn\x12<\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x0f\xbaH\x0c\xaa\x01\t:\x02\x08\x01:\x03\x10\xe8\x07R\x03val\"F\n\rDurationNotIn\x12\x35\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xbaH\x05\xaa\x01\x02\x42\x00R\x03val\"C\n\nDurationLT\x12\x35\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xbaH\x05\xaa\x01\x02\x1a\x00R\x03val\"F\n\x0b\x44urationLTE\x12\x37\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\n\xbaH\x07\xaa\x01\x04\"\x02\x08\x01R\x03val\"F\n\nDurationGT\x12\x38\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x0b\xbaH\x08\xaa\x01\x05*\x03\x10\xe8\x07R\x03val\"H\n\x0b\x44urationGTE\x12\x39\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x0c\xbaH\t\xaa\x01\x06\x32\x04\x10\xc0\x84=R\x03val\"I\n\x0c\x44urationGTLT\x12\x39\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x0c\xbaH\t\xaa\x01\x06\x1a\x02\x08\x01*\x00R\x03val\"K\n\x0e\x44urationExLTGT\x12\x39\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x0c\xbaH\t\xaa\x01\x06\x1a\x00*\x02\x08\x01R\x03val\"N\n\x0e\x44urationGTELTE\x12<\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x0f\xbaH\x0c\xaa\x01\t\"\x03\x08\x90\x1c\x32\x02\x08<R\x03val\"P\n\x10\x44urationExGTELTE\x12<\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x0f\xbaH\x0c\xaa\x01\t\"\x02\x08<2\x03\x08\x90\x1cR\x03val\"\x8a\x01\n\x1c\x44urationFieldWithOtherFields\x12H\n\x0c\x64uration_val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\n\xbaH\x07\xaa\x01\x04\"\x02\x08\x01R\x0b\x64urationVal\x12 \n\x07int_val\x18\x02 \x01(\x05\x42\x07\xbaH\x04\x1a\x02 \x10R\x06intVal\"J\n\x0f\x44urationExample\x12\x37\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\n\xbaH\x07\xaa\x01\x04J\x02\x08\x03R\x03valB\xd2\x01\n\"com.buf.validate.conformance.casesB\x10WktDurationProtoP\x01\xa2\x02\x04\x42VCC\xaa\x02\x1e\x42uf.Validate.Conformance.Cases\xca\x02\x1e\x42uf\\Validate\\Conformance\\Cases\xe2\x02*Buf\\Validate\\Conformance\\Cases\\GPBMetadata\xea\x02!Buf::Validate::Conformance::Casesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'buf.validate.conformance.cases.wkt_duration_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.buf.validate.conformance.casesB\020WktDurationProtoP\001\242\002\004BVCC\252\002\036Buf.Validate.Conformance.Cases\312\002\036Buf\\Validate\\Conformance\\Cases\342\002*Buf\\Validate\\Conformance\\Cases\\GPBMetadata\352\002!Buf::Validate::Conformance::Cases'
  _globals['_DURATIONREQUIRED'].fields_by_name['val']._loaded_options = None
  _globals['_DURATIONREQUIRED'].fields_by_name['val']._serialized_options = b'\272H\003\310\001\001'
  _globals['_DURATIONCONST'].fields_by_name['val']._loaded_options = None
  _globals['_DURATIONCONST'].fields_by_name['val']._serialized_options = b'\272H\007\252\001\004\022\002\010\003'
  _globals['_DURATIONIN'].fields_by_name['val']._loaded_options = None
  _globals['_DURATIONIN'].fields_by_name['val']._serialized_options = b'\272H\014\252\001\t:\002\010\001:\003\020\350\007'
  _globals['_DURATIONNOTIN'].fields_by_name['val']._loaded_options = None
  _globals['_DURATIONNOTIN'].fields_by_name['val']._serialized_options = b'\272H\005\252\001\002B\000'
  _globals['_DURATIONLT'].fields_by_name['val']._loaded_options = None
  _globals['_DURATIONLT'].fields_by_name['val']._serialized_options = b'\272H\005\252\001\002\032\000'
  _globals['_DURATIONLTE'].fields_by_name['val']._loaded_options = None
  _globals['_DURATIONLTE'].fields_by_name['val']._serialized_options = b'\272H\007\252\001\004\"\002\010\001'
  _globals['_DURATIONGT'].fields_by_name['val']._loaded_options = None
  _globals['_DURATIONGT'].fields_by_name['val']._serialized_options = b'\272H\010\252\001\005*\003\020\350\007'
  _globals['_DURATIONGTE'].fields_by_name['val']._loaded_options = None
  _globals['_DURATIONGTE'].fields_by_name['val']._serialized_options = b'\272H\t\252\001\0062\004\020\300\204='
  _globals['_DURATIONGTLT'].fields_by_name['val']._loaded_options = None
  _globals['_DURATIONGTLT'].fields_by_name['val']._serialized_options = b'\272H\t\252\001\006\032\002\010\001*\000'
  _globals['_DURATIONEXLTGT'].fields_by_name['val']._loaded_options = None
  _globals['_DURATIONEXLTGT'].fields_by_name['val']._serialized_options = b'\272H\t\252\001\006\032\000*\002\010\001'
  _globals['_DURATIONGTELTE'].fields_by_name['val']._loaded_options = None
  _globals['_DURATIONGTELTE'].fields_by_name['val']._serialized_options = b'\272H\014\252\001\t\"\003\010\220\0342\002\010<'
  _globals['_DURATIONEXGTELTE'].fields_by_name['val']._loaded_options = None
  _globals['_DURATIONEXGTELTE'].fields_by_name['val']._serialized_options = b'\272H\014\252\001\t\"\002\010<2\003\010\220\034'
  _globals['_DURATIONFIELDWITHOTHERFIELDS'].fields_by_name['duration_val']._loaded_options = None
  _globals['_DURATIONFIELDWITHOTHERFIELDS'].fields_by_name['duration_val']._serialized_options = b'\272H\007\252\001\004\"\002\010\001'
  _globals['_DURATIONFIELDWITHOTHERFIELDS'].fields_by_name['int_val']._loaded_options = None
  _globals['_DURATIONFIELDWITHOTHERFIELDS'].fields_by_name['int_val']._serialized_options = b'\272H\004\032\002 \020'
  _globals['_DURATIONEXAMPLE'].fields_by_name['val']._loaded_options = None
  _globals['_DURATIONEXAMPLE'].fields_by_name['val']._serialized_options = b'\272H\007\252\001\004J\002\010\003'
  _globals['_DURATIONNONE']._serialized_start=146
  _globals['_DURATIONNONE']._serialized_end=205
  _globals['_DURATIONREQUIRED']._serialized_start=207
  _globals['_DURATIONREQUIRED']._serialized_end=278
  _globals['_DURATIONCONST']._serialized_start=280
  _globals['_DURATIONCONST']._serialized_end=352
  _globals['_DURATIONIN']._serialized_start=354
  _globals['_DURATIONIN']._serialized_end=428
  _globals['_DURATIONNOTIN']._serialized_start=430
  _globals['_DURATIONNOTIN']._serialized_end=500
  _globals['_DURATIONLT']._serialized_start=502
  _globals['_DURATIONLT']._serialized_end=569
  _globals['_DURATIONLTE']._serialized_start=571
  _globals['_DURATIONLTE']._serialized_end=641
  _globals['_DURATIONGT']._serialized_start=643
  _globals['_DURATIONGT']._serialized_end=713
  _globals['_DURATIONGTE']._serialized_start=715
  _globals['_DURATIONGTE']._serialized_end=787
  _globals['_DURATIONGTLT']._serialized_start=789
  _globals['_DURATIONGTLT']._serialized_end=862
  _globals['_DURATIONEXLTGT']._serialized_start=864
  _globals['_DURATIONEXLTGT']._serialized_end=939
  _globals['_DURATIONGTELTE']._serialized_start=941
  _globals['_DURATIONGTELTE']._serialized_end=1019
  _globals['_DURATIONEXGTELTE']._serialized_start=1021
  _globals['_DURATIONEXGTELTE']._serialized_end=1101
  _globals['_DURATIONFIELDWITHOTHERFIELDS']._serialized_start=1104
  _globals['_DURATIONFIELDWITHOTHERFIELDS']._serialized_end=1242
  _globals['_DURATIONEXAMPLE']._serialized_start=1244
  _globals['_DURATIONEXAMPLE']._serialized_end=1318
# @@protoc_insertion_point(module_scope)
