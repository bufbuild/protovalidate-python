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
# source: buf/validate/conformance/cases/custom_constraints/custom_constraints.proto
# Protobuf Python Version: 5.29.2
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
    2,
    '',
    'buf/validate/conformance/cases/custom_constraints/custom_constraints.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nJbuf/validate/conformance/cases/custom_constraints/custom_constraints.proto\x12\x31\x62uf.validate.conformance.cases.custom_constraints\x1a\x1b\x62uf/validate/validate.proto\"\xc5\x01\n\rNoExpressions\x12\x0c\n\x01\x61\x18\x01 \x01(\x05R\x01\x61\x12\x45\n\x01\x62\x18\x02 \x01(\x0e\x32\x37.buf.validate.conformance.cases.custom_constraints.EnumR\x01\x62\x12U\n\x01\x63\x18\x03 \x01(\x0b\x32G.buf.validate.conformance.cases.custom_constraints.NoExpressions.NestedR\x01\x63\x1a\x08\n\x06Nested\"\xc3\x05\n\x12MessageExpressions\x12\x0c\n\x01\x61\x18\x01 \x01(\x05R\x01\x61\x12\x0c\n\x01\x62\x18\x02 \x01(\x05R\x01\x62\x12\x45\n\x01\x63\x18\x03 \x01(\x0e\x32\x37.buf.validate.conformance.cases.custom_constraints.EnumR\x01\x63\x12\x45\n\x01\x64\x18\x04 \x01(\x0e\x32\x37.buf.validate.conformance.cases.custom_constraints.EnumR\x01\x64\x12Z\n\x01\x65\x18\x05 \x01(\x0b\x32L.buf.validate.conformance.cases.custom_constraints.MessageExpressions.NestedR\x01\x65\x12Z\n\x01\x66\x18\x06 \x01(\x0b\x32L.buf.validate.conformance.cases.custom_constraints.MessageExpressions.NestedR\x01\x66\x1ax\n\x06Nested\x12\x0c\n\x01\x61\x18\x01 \x01(\x05R\x01\x61\x12\x0c\n\x01\x62\x18\x02 \x01(\x05R\x01\x62:R\xbaHO\x1aM\n\x19message_expression_nested\x1a\x30this.a > this.b ? \'\': \'a must be greater than b\':\xd0\x01\xbaH\xcc\x01\x1a\x43\n\x19message_expression_scalar\x12\x15\x61 must be less than b\x1a\x0fthis.a < this.b\x1a?\n\x17message_expression_enum\x12\x12\x63 must not equal d\x1a\x10this.c != this.d\x1a\x44\n\x18message_expression_embed\x12\x12\x65.a must equal f.a\x1a\x14this.e.a == this.f.a\"\xaa\x05\n\x10\x46ieldExpressions\x12Z\n\x01\x61\x18\x01 \x01(\x05\x42L\xbaHI\xba\x01\x46\n\x17\x66ield_expression_scalar\x1a+this > 42 ? \'\': \'a must be greater than 42\'R\x01\x61\x12\x7f\n\x01\x62\x18\x02 \x01(\x0e\x32\x37.buf.validate.conformance.cases.custom_constraints.EnumB8\xbaH5\xba\x01\x32\n\x15\x66ield_expression_enum\x12\x0e\x62 must be ~ONE\x1a\tthis == 1R\x01\x62\x12\xa6\x01\n\x01\x63\x18\x03 \x01(\x0b\x32J.buf.validate.conformance.cases.custom_constraints.FieldExpressions.NestedBL\xbaHI\xba\x01\x46\n\x16\x66ield_expression_embed\x12\x1b\x63.a must be a multiple of 4\x1a\x0fthis.a % 4 == 0R\x01\x63\x12\xb1\x01\n\x01\x64\x18\x04 \x01(\x05\x42\xa2\x01\xbaH\x9e\x01\xba\x01L\n\"field_expression_scalar_multiple_1\x1a&this < 1 ? \'\': \'d must be less than 1\'\xba\x01L\n\"field_expression_scalar_multiple_2\x1a&this < 2 ? \'\': \'d must be less than 2\'R\x01\x64\x1a\\\n\x06Nested\x12R\n\x01\x61\x18\x01 \x01(\x05\x42\x44\xbaHA\xba\x01>\n\x17\x66ield_expression_nested\x1a#this > 0 ? \'\': \'a must be positive\'R\x01\x61\"R\n\x0cMissingField\x12\x0c\n\x01\x61\x18\x01 \x01(\x05R\x01\x61:4\xbaH1\x1a/\n\rmissing_field\x12\x12\x62 must be positive\x1a\nthis.b > 0\"g\n\rIncorrectType\x12\x0c\n\x01\x61\x18\x01 \x01(\x05R\x01\x61:H\xbaHE\x1a\x43\n\x0eincorrect_type\x12\x17\x61 must start with \'foo\'\x1a\x18this.a.startsWith(\'foo\')\"}\n\x0f\x44ynRuntimeError\x12\x0c\n\x01\x61\x18\x01 \x01(\x05R\x01\x61:\\\xbaHY\x1aW\n\x0f\x64yn_runtime_err\x12.dynamic type tries to use a non-existent field\x1a\x14\x64yn(this).b == \'foo\'\"\\\n\x0cNowEqualsNow:L\xbaHI\x1aG\n\x0enow_equals_now\x12)now should equal now within an expression\x1a\nnow == now**\n\x04\x45num\x12\x14\n\x10\x45NUM_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x45NUM_ONE\x10\x01\x42\xb5\x02\n5com.buf.validate.conformance.cases.custom_constraintsB\x16\x43ustomConstraintsProtoP\x01\xa2\x02\x05\x42VCCC\xaa\x02\x30\x42uf.Validate.Conformance.Cases.CustomConstraints\xca\x02\x30\x42uf\\Validate\\Conformance\\Cases\\CustomConstraints\xe2\x02<Buf\\Validate\\Conformance\\Cases\\CustomConstraints\\GPBMetadata\xea\x02\x34\x42uf::Validate::Conformance::Cases::CustomConstraintsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'buf.validate.conformance.cases.custom_constraints.custom_constraints_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n5com.buf.validate.conformance.cases.custom_constraintsB\026CustomConstraintsProtoP\001\242\002\005BVCCC\252\0020Buf.Validate.Conformance.Cases.CustomConstraints\312\0020Buf\\Validate\\Conformance\\Cases\\CustomConstraints\342\002<Buf\\Validate\\Conformance\\Cases\\CustomConstraints\\GPBMetadata\352\0024Buf::Validate::Conformance::Cases::CustomConstraints'
  _globals['_MESSAGEEXPRESSIONS_NESTED']._loaded_options = None
  _globals['_MESSAGEEXPRESSIONS_NESTED']._serialized_options = b'\272HO\032M\n\031message_expression_nested\0320this.a > this.b ? \'\': \'a must be greater than b\''
  _globals['_MESSAGEEXPRESSIONS']._loaded_options = None
  _globals['_MESSAGEEXPRESSIONS']._serialized_options = b'\272H\314\001\032C\n\031message_expression_scalar\022\025a must be less than b\032\017this.a < this.b\032?\n\027message_expression_enum\022\022c must not equal d\032\020this.c != this.d\032D\n\030message_expression_embed\022\022e.a must equal f.a\032\024this.e.a == this.f.a'
  _globals['_FIELDEXPRESSIONS_NESTED'].fields_by_name['a']._loaded_options = None
  _globals['_FIELDEXPRESSIONS_NESTED'].fields_by_name['a']._serialized_options = b'\272HA\272\001>\n\027field_expression_nested\032#this > 0 ? \'\': \'a must be positive\''
  _globals['_FIELDEXPRESSIONS'].fields_by_name['a']._loaded_options = None
  _globals['_FIELDEXPRESSIONS'].fields_by_name['a']._serialized_options = b'\272HI\272\001F\n\027field_expression_scalar\032+this > 42 ? \'\': \'a must be greater than 42\''
  _globals['_FIELDEXPRESSIONS'].fields_by_name['b']._loaded_options = None
  _globals['_FIELDEXPRESSIONS'].fields_by_name['b']._serialized_options = b'\272H5\272\0012\n\025field_expression_enum\022\016b must be ~ONE\032\tthis == 1'
  _globals['_FIELDEXPRESSIONS'].fields_by_name['c']._loaded_options = None
  _globals['_FIELDEXPRESSIONS'].fields_by_name['c']._serialized_options = b'\272HI\272\001F\n\026field_expression_embed\022\033c.a must be a multiple of 4\032\017this.a % 4 == 0'
  _globals['_FIELDEXPRESSIONS'].fields_by_name['d']._loaded_options = None
  _globals['_FIELDEXPRESSIONS'].fields_by_name['d']._serialized_options = b'\272H\236\001\272\001L\n\"field_expression_scalar_multiple_1\032&this < 1 ? \'\': \'d must be less than 1\'\272\001L\n\"field_expression_scalar_multiple_2\032&this < 2 ? \'\': \'d must be less than 2\''
  _globals['_MISSINGFIELD']._loaded_options = None
  _globals['_MISSINGFIELD']._serialized_options = b'\272H1\032/\n\rmissing_field\022\022b must be positive\032\nthis.b > 0'
  _globals['_INCORRECTTYPE']._loaded_options = None
  _globals['_INCORRECTTYPE']._serialized_options = b'\272HE\032C\n\016incorrect_type\022\027a must start with \'foo\'\032\030this.a.startsWith(\'foo\')'
  _globals['_DYNRUNTIMEERROR']._loaded_options = None
  _globals['_DYNRUNTIMEERROR']._serialized_options = b'\272HY\032W\n\017dyn_runtime_err\022.dynamic type tries to use a non-existent field\032\024dyn(this).b == \'foo\''
  _globals['_NOWEQUALSNOW']._loaded_options = None
  _globals['_NOWEQUALSNOW']._serialized_options = b'\272HI\032G\n\016now_equals_now\022)now should equal now within an expression\032\nnow == now'
  _globals['_ENUM']._serialized_start=2163
  _globals['_ENUM']._serialized_end=2205
  _globals['_NOEXPRESSIONS']._serialized_start=159
  _globals['_NOEXPRESSIONS']._serialized_end=356
  _globals['_NOEXPRESSIONS_NESTED']._serialized_start=348
  _globals['_NOEXPRESSIONS_NESTED']._serialized_end=356
  _globals['_MESSAGEEXPRESSIONS']._serialized_start=359
  _globals['_MESSAGEEXPRESSIONS']._serialized_end=1066
  _globals['_MESSAGEEXPRESSIONS_NESTED']._serialized_start=735
  _globals['_MESSAGEEXPRESSIONS_NESTED']._serialized_end=855
  _globals['_FIELDEXPRESSIONS']._serialized_start=1069
  _globals['_FIELDEXPRESSIONS']._serialized_end=1751
  _globals['_FIELDEXPRESSIONS_NESTED']._serialized_start=1659
  _globals['_FIELDEXPRESSIONS_NESTED']._serialized_end=1751
  _globals['_MISSINGFIELD']._serialized_start=1753
  _globals['_MISSINGFIELD']._serialized_end=1835
  _globals['_INCORRECTTYPE']._serialized_start=1837
  _globals['_INCORRECTTYPE']._serialized_end=1940
  _globals['_DYNRUNTIMEERROR']._serialized_start=1942
  _globals['_DYNRUNTIMEERROR']._serialized_end=2067
  _globals['_NOWEQUALSNOW']._serialized_start=2069
  _globals['_NOWEQUALSNOW']._serialized_end=2161
# @@protoc_insertion_point(module_scope)
