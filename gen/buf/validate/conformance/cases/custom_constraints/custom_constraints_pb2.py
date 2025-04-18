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
# source: buf/validate/conformance/cases/custom_constraints/custom_constraints.proto
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
    'buf/validate/conformance/cases/custom_constraints/custom_constraints.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nJbuf/validate/conformance/cases/custom_constraints/custom_constraints.proto\x12\x31\x62uf.validate.conformance.cases.custom_constraints\x1a\x1b\x62uf/validate/validate.proto\"\xc5\x01\n\rNoExpressions\x12\x0c\n\x01\x61\x18\x01 \x01(\x05R\x01\x61\x12\x45\n\x01\x62\x18\x02 \x01(\x0e\x32\x37.buf.validate.conformance.cases.custom_constraints.EnumR\x01\x62\x12U\n\x01\x63\x18\x03 \x01(\x0b\x32G.buf.validate.conformance.cases.custom_constraints.NoExpressions.NestedR\x01\x63\x1a\x08\n\x06Nested\"\xc3\x05\n\x12MessageExpressions\x12\x0c\n\x01\x61\x18\x01 \x01(\x05R\x01\x61\x12\x0c\n\x01\x62\x18\x02 \x01(\x05R\x01\x62\x12\x45\n\x01\x63\x18\x03 \x01(\x0e\x32\x37.buf.validate.conformance.cases.custom_constraints.EnumR\x01\x63\x12\x45\n\x01\x64\x18\x04 \x01(\x0e\x32\x37.buf.validate.conformance.cases.custom_constraints.EnumR\x01\x64\x12Z\n\x01\x65\x18\x05 \x01(\x0b\x32L.buf.validate.conformance.cases.custom_constraints.MessageExpressions.NestedR\x01\x65\x12Z\n\x01\x66\x18\x06 \x01(\x0b\x32L.buf.validate.conformance.cases.custom_constraints.MessageExpressions.NestedR\x01\x66\x1ax\n\x06Nested\x12\x0c\n\x01\x61\x18\x01 \x01(\x05R\x01\x61\x12\x0c\n\x01\x62\x18\x02 \x01(\x05R\x01\x62:R\xbaHO\x1aM\n\x19message_expression_nested\x1a\x30this.a > this.b ? \'\': \'a must be greater than b\':\xd0\x01\xbaH\xcc\x01\x1a\x43\n\x19message_expression_scalar\x12\x15\x61 must be less than b\x1a\x0fthis.a < this.b\x1a?\n\x17message_expression_enum\x12\x12\x63 must not equal d\x1a\x10this.c != this.d\x1a\x44\n\x18message_expression_embed\x12\x12\x65.a must equal f.a\x1a\x14this.e.a == this.f.a\"R\n\x0cMissingField\x12\x0c\n\x01\x61\x18\x01 \x01(\x05R\x01\x61:4\xbaH1\x1a/\n\rmissing_field\x12\x12\x62 must be positive\x1a\nthis.b > 0\"g\n\rIncorrectType\x12\x0c\n\x01\x61\x18\x01 \x01(\x05R\x01\x61:H\xbaHE\x1a\x43\n\x0eincorrect_type\x12\x17\x61 must start with \'foo\'\x1a\x18this.a.startsWith(\'foo\')\"}\n\x0f\x44ynRuntimeError\x12\x0c\n\x01\x61\x18\x01 \x01(\x05R\x01\x61:\\\xbaHY\x1aW\n\x0f\x64yn_runtime_err\x12.dynamic type tries to use a non-existent field\x1a\x14\x64yn(this).b == \'foo\'\"\\\n\x0cNowEqualsNow:L\xbaHI\x1aG\n\x0enow_equals_now\x12)now should equal now within an expression\x1a\nnow == now\"\xdf\x02\n\x1d\x46ieldExpressionMultipleScalar\x12\xbd\x02\n\x03val\x18\x01 \x01(\x05\x42\xaa\x02\xbaH\xa6\x02\xba\x01_\n\"field_expression.multiple.scalar.1\x12/test message field_expression.multiple.scalar.1\x1a\x08this > 0\xba\x01_\n\"field_expression.multiple.scalar.2\x12/test message field_expression.multiple.scalar.2\x1a\x08this > 1\xba\x01_\n\"field_expression.multiple.scalar.3\x12/test message field_expression.multiple.scalar.3\x1a\x08this > 2R\x03val\"\x7f\n\x1b\x46ieldExpressionNestedScalar\x12`\n\x06nested\x18\x01 \x01(\x0b\x32H.buf.validate.conformance.cases.custom_constraints.FieldExpressionScalarR\x06nested\"\xa2\x01\n\x1d\x46ieldExpressionOptionalScalar\x12y\n\x03val\x18\x01 \x01(\x05\x42\x62\xbaH_\xba\x01\\\n field_expression.optional.scalar\x12-test message field_expression.optional.scalar\x1a\tthis == 1H\x00R\x03val\x88\x01\x01\x42\x06\n\x04_val\"{\n\x15\x46ieldExpressionScalar\x12\x62\n\x03val\x18\x01 \x01(\x05\x42P\xbaHM\xba\x01J\n\x17\x66ield_expression.scalar\x12$test message field_expression.scalar\x1a\tthis == 1R\x03val\"\xaf\x01\n\x13\x46ieldExpressionEnum\x12\x97\x01\n\x03val\x18\x01 \x01(\x0e\x32\x37.buf.validate.conformance.cases.custom_constraints.EnumBL\xbaHI\xba\x01\x46\n\x15\x66ield_expression.enum\x12\"test message field_expression.enum\x1a\tthis == 1R\x03val\"\xe5\x01\n\x16\x46ieldExpressionMessage\x12\xb5\x01\n\x03val\x18\x01 \x01(\x0b\x32M.buf.validate.conformance.cases.custom_constraints.FieldExpressionMessage.MsgBT\xbaHQ\xba\x01N\n\x18\x66ield_expression.message\x12%test message field_expression.message\x1a\x0bthis.a == 1R\x03val\x1a\x13\n\x03Msg\x12\x0c\n\x01\x61\x18\x01 \x01(\x05R\x01\x61\"\xa5\x02\n\x18\x46ieldExpressionMapScalar\x12\xd0\x01\n\x03val\x18\x01 \x03(\x0b\x32T.buf.validate.conformance.cases.custom_constraints.FieldExpressionMapScalar.ValEntryBh\xbaHe\xba\x01\x62\n\x1b\x66ield_expression.map.scalar\x12(test message field_expression.map.scalar\x1a\x19this.all(k, this[k] == 1)R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\x05R\x03key\x12\x14\n\x05value\x18\x02 \x01(\x05R\x05value:\x02\x38\x01\"\xd6\x02\n\x16\x46ieldExpressionMapEnum\x12\xca\x01\n\x03val\x18\x01 \x03(\x0b\x32R.buf.validate.conformance.cases.custom_constraints.FieldExpressionMapEnum.ValEntryBd\xbaHa\xba\x01^\n\x19\x66ield_expression.map.enum\x12&test message field_expression.map.enum\x1a\x19this.all(k, this[k] == 1)R\x03val\x1ao\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\x05R\x03key\x12M\n\x05value\x18\x02 \x01(\x0e\x32\x37.buf.validate.conformance.cases.custom_constraints.EnumR\x05value:\x02\x38\x01\"\x93\x03\n\x19\x46ieldExpressionMapMessage\x12\xd5\x01\n\x03val\x18\x01 \x03(\x0b\x32U.buf.validate.conformance.cases.custom_constraints.FieldExpressionMapMessage.ValEntryBl\xbaHi\xba\x01\x66\n\x1c\x66ield_expression.map.message\x12)test message field_expression.map.message\x1a\x1bthis.all(k, this[k].a == 1)R\x03val\x1a\x88\x01\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\x05R\x03key\x12\x66\n\x05value\x18\x02 \x01(\x0b\x32P.buf.validate.conformance.cases.custom_constraints.FieldExpressionMapMessage.MsgR\x05value:\x02\x38\x01\x1a\x13\n\x03Msg\x12\x0c\n\x01\x61\x18\x01 \x01(\x05R\x01\x61\"\x9f\x02\n\x16\x46ieldExpressionMapKeys\x12\xcc\x01\n\x03val\x18\x01 \x03(\x0b\x32R.buf.validate.conformance.cases.custom_constraints.FieldExpressionMapKeys.ValEntryBf\xbaHc\x9a\x01`\"^\xba\x01[\n\x19\x66ield_expression.map.keys\x12&test message field_expression.map.keys\x1a\x16this == 4 || this == 8R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\x05R\x03key\x12\x14\n\x05value\x18\x02 \x01(\x05R\x05value:\x02\x38\x01\"\xb4\x02\n\x1e\x46ieldExpressionMapScalarValues\x12\xd9\x01\n\x03val\x18\x01 \x03(\x0b\x32Z.buf.validate.conformance.cases.custom_constraints.FieldExpressionMapScalarValues.ValEntryBk\xbaHh\x9a\x01\x65*c\xba\x01`\n\"field_expression.map.scalar.values\x12/test message field_expression.map.scalar.values\x1a\tthis == 1R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\x05R\x03key\x12\x14\n\x05value\x18\x02 \x01(\x05R\x05value:\x02\x38\x01\"\xe5\x02\n\x1c\x46ieldExpressionMapEnumValues\x12\xd3\x01\n\x03val\x18\x01 \x03(\x0b\x32X.buf.validate.conformance.cases.custom_constraints.FieldExpressionMapEnumValues.ValEntryBg\xbaHd\x9a\x01\x61*_\xba\x01\\\n field_expression.map.enum.values\x12-test message field_expression.map.enum.values\x1a\tthis == 1R\x03val\x1ao\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\x05R\x03key\x12M\n\x05value\x18\x02 \x01(\x0e\x32\x37.buf.validate.conformance.cases.custom_constraints.EnumR\x05value:\x02\x38\x01\"\xa8\x03\n\x1f\x46ieldExpressionMapMessageValues\x12\xde\x01\n\x03val\x18\x01 \x03(\x0b\x32[.buf.validate.conformance.cases.custom_constraints.FieldExpressionMapMessageValues.ValEntryBo\xbaHl\x9a\x01i*g\xba\x01\x64\n#field_expression.map.message.values\x12\x30test message field_expression.map.message.values\x1a\x0bthis.a == 1R\x03val\x1a\x8e\x01\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\x05R\x03key\x12l\n\x05value\x18\x02 \x01(\x0b\x32V.buf.validate.conformance.cases.custom_constraints.FieldExpressionMapMessageValues.MsgR\x05value:\x02\x38\x01\x1a\x13\n\x03Msg\x12\x0c\n\x01\x61\x18\x01 \x01(\x05R\x01\x61\"\x9f\x01\n\x1d\x46ieldExpressionRepeatedScalar\x12~\n\x03val\x18\x01 \x03(\x05\x42l\xbaHi\xba\x01\x66\n field_expression.repeated.scalar\x12-test message field_expression.repeated.scalar\x1a\x13this.all(e, e == 1)R\x03val\"\xd3\x01\n\x1b\x46ieldExpressionRepeatedEnum\x12\xb3\x01\n\x03val\x18\x01 \x03(\x0e\x32\x37.buf.validate.conformance.cases.custom_constraints.EnumBh\xbaHe\xba\x01\x62\n\x1e\x66ield_expression.repeated.enum\x12+test message field_expression.repeated.enum\x1a\x13this.all(e, e == 1)R\x03val\"\x91\x02\n\x1e\x46ieldExpressionRepeatedMessage\x12\xd9\x01\n\x03val\x18\x01 \x03(\x0b\x32U.buf.validate.conformance.cases.custom_constraints.FieldExpressionRepeatedMessage.MsgBp\xbaHm\xba\x01j\n!field_expression.repeated.message\x12.test message field_expression.repeated.message\x1a\x15this.all(e, e.a == 1)R\x03val\x1a\x13\n\x03Msg\x12\x0c\n\x01\x61\x18\x01 \x01(\x05R\x01\x61\"\xac\x01\n\"FieldExpressionRepeatedScalarItems\x12\x85\x01\n\x03val\x18\x01 \x03(\x05\x42s\xbaHp\x92\x01m\"k\xba\x01h\n&field_expression.repeated.scalar.items\x12\x33test message field_expression.repeated.scalar.items\x1a\tthis == 1R\x03val\"\xdf\x01\n FieldExpressionRepeatedEnumItems\x12\xba\x01\n\x03val\x18\x01 \x03(\x0e\x32\x37.buf.validate.conformance.cases.custom_constraints.EnumBo\xbaHl\x92\x01i\"g\xba\x01\x64\n$field_expression.repeated.enum.items\x12\x31test message field_expression.repeated.enum.items\x1a\tthis == 1R\x03val\"\xa2\x02\n#FieldExpressionRepeatedMessageItems\x12\xe5\x01\n\x03val\x18\x01 \x03(\x0b\x32Z.buf.validate.conformance.cases.custom_constraints.FieldExpressionRepeatedMessageItems.MsgBw\xbaHt\x92\x01q\"o\xba\x01l\n\'field_expression.repeated.message.items\x12\x34test message field_expression.repeated.message.items\x1a\x0bthis.a == 1R\x03val\x1a\x13\n\x03Msg\x12\x0c\n\x01\x61\x18\x01 \x01(\x05R\x01\x61**\n\x04\x45num\x12\x14\n\x10\x45NUM_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x45NUM_ONE\x10\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'buf.validate.conformance.cases.custom_constraints.custom_constraints_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MESSAGEEXPRESSIONS_NESTED']._loaded_options = None
  _globals['_MESSAGEEXPRESSIONS_NESTED']._serialized_options = b'\272HO\032M\n\031message_expression_nested\0320this.a > this.b ? \'\': \'a must be greater than b\''
  _globals['_MESSAGEEXPRESSIONS']._loaded_options = None
  _globals['_MESSAGEEXPRESSIONS']._serialized_options = b'\272H\314\001\032C\n\031message_expression_scalar\022\025a must be less than b\032\017this.a < this.b\032?\n\027message_expression_enum\022\022c must not equal d\032\020this.c != this.d\032D\n\030message_expression_embed\022\022e.a must equal f.a\032\024this.e.a == this.f.a'
  _globals['_MISSINGFIELD']._loaded_options = None
  _globals['_MISSINGFIELD']._serialized_options = b'\272H1\032/\n\rmissing_field\022\022b must be positive\032\nthis.b > 0'
  _globals['_INCORRECTTYPE']._loaded_options = None
  _globals['_INCORRECTTYPE']._serialized_options = b'\272HE\032C\n\016incorrect_type\022\027a must start with \'foo\'\032\030this.a.startsWith(\'foo\')'
  _globals['_DYNRUNTIMEERROR']._loaded_options = None
  _globals['_DYNRUNTIMEERROR']._serialized_options = b'\272HY\032W\n\017dyn_runtime_err\022.dynamic type tries to use a non-existent field\032\024dyn(this).b == \'foo\''
  _globals['_NOWEQUALSNOW']._loaded_options = None
  _globals['_NOWEQUALSNOW']._serialized_options = b'\272HI\032G\n\016now_equals_now\022)now should equal now within an expression\032\nnow == now'
  _globals['_FIELDEXPRESSIONMULTIPLESCALAR'].fields_by_name['val']._loaded_options = None
  _globals['_FIELDEXPRESSIONMULTIPLESCALAR'].fields_by_name['val']._serialized_options = b'\272H\246\002\272\001_\n\"field_expression.multiple.scalar.1\022/test message field_expression.multiple.scalar.1\032\010this > 0\272\001_\n\"field_expression.multiple.scalar.2\022/test message field_expression.multiple.scalar.2\032\010this > 1\272\001_\n\"field_expression.multiple.scalar.3\022/test message field_expression.multiple.scalar.3\032\010this > 2'
  _globals['_FIELDEXPRESSIONOPTIONALSCALAR'].fields_by_name['val']._loaded_options = None
  _globals['_FIELDEXPRESSIONOPTIONALSCALAR'].fields_by_name['val']._serialized_options = b'\272H_\272\001\\\n field_expression.optional.scalar\022-test message field_expression.optional.scalar\032\tthis == 1'
  _globals['_FIELDEXPRESSIONSCALAR'].fields_by_name['val']._loaded_options = None
  _globals['_FIELDEXPRESSIONSCALAR'].fields_by_name['val']._serialized_options = b'\272HM\272\001J\n\027field_expression.scalar\022$test message field_expression.scalar\032\tthis == 1'
  _globals['_FIELDEXPRESSIONENUM'].fields_by_name['val']._loaded_options = None
  _globals['_FIELDEXPRESSIONENUM'].fields_by_name['val']._serialized_options = b'\272HI\272\001F\n\025field_expression.enum\022\"test message field_expression.enum\032\tthis == 1'
  _globals['_FIELDEXPRESSIONMESSAGE'].fields_by_name['val']._loaded_options = None
  _globals['_FIELDEXPRESSIONMESSAGE'].fields_by_name['val']._serialized_options = b'\272HQ\272\001N\n\030field_expression.message\022%test message field_expression.message\032\013this.a == 1'
  _globals['_FIELDEXPRESSIONMAPSCALAR_VALENTRY']._loaded_options = None
  _globals['_FIELDEXPRESSIONMAPSCALAR_VALENTRY']._serialized_options = b'8\001'
  _globals['_FIELDEXPRESSIONMAPSCALAR'].fields_by_name['val']._loaded_options = None
  _globals['_FIELDEXPRESSIONMAPSCALAR'].fields_by_name['val']._serialized_options = b'\272He\272\001b\n\033field_expression.map.scalar\022(test message field_expression.map.scalar\032\031this.all(k, this[k] == 1)'
  _globals['_FIELDEXPRESSIONMAPENUM_VALENTRY']._loaded_options = None
  _globals['_FIELDEXPRESSIONMAPENUM_VALENTRY']._serialized_options = b'8\001'
  _globals['_FIELDEXPRESSIONMAPENUM'].fields_by_name['val']._loaded_options = None
  _globals['_FIELDEXPRESSIONMAPENUM'].fields_by_name['val']._serialized_options = b'\272Ha\272\001^\n\031field_expression.map.enum\022&test message field_expression.map.enum\032\031this.all(k, this[k] == 1)'
  _globals['_FIELDEXPRESSIONMAPMESSAGE_VALENTRY']._loaded_options = None
  _globals['_FIELDEXPRESSIONMAPMESSAGE_VALENTRY']._serialized_options = b'8\001'
  _globals['_FIELDEXPRESSIONMAPMESSAGE'].fields_by_name['val']._loaded_options = None
  _globals['_FIELDEXPRESSIONMAPMESSAGE'].fields_by_name['val']._serialized_options = b'\272Hi\272\001f\n\034field_expression.map.message\022)test message field_expression.map.message\032\033this.all(k, this[k].a == 1)'
  _globals['_FIELDEXPRESSIONMAPKEYS_VALENTRY']._loaded_options = None
  _globals['_FIELDEXPRESSIONMAPKEYS_VALENTRY']._serialized_options = b'8\001'
  _globals['_FIELDEXPRESSIONMAPKEYS'].fields_by_name['val']._loaded_options = None
  _globals['_FIELDEXPRESSIONMAPKEYS'].fields_by_name['val']._serialized_options = b'\272Hc\232\001`\"^\272\001[\n\031field_expression.map.keys\022&test message field_expression.map.keys\032\026this == 4 || this == 8'
  _globals['_FIELDEXPRESSIONMAPSCALARVALUES_VALENTRY']._loaded_options = None
  _globals['_FIELDEXPRESSIONMAPSCALARVALUES_VALENTRY']._serialized_options = b'8\001'
  _globals['_FIELDEXPRESSIONMAPSCALARVALUES'].fields_by_name['val']._loaded_options = None
  _globals['_FIELDEXPRESSIONMAPSCALARVALUES'].fields_by_name['val']._serialized_options = b'\272Hh\232\001e*c\272\001`\n\"field_expression.map.scalar.values\022/test message field_expression.map.scalar.values\032\tthis == 1'
  _globals['_FIELDEXPRESSIONMAPENUMVALUES_VALENTRY']._loaded_options = None
  _globals['_FIELDEXPRESSIONMAPENUMVALUES_VALENTRY']._serialized_options = b'8\001'
  _globals['_FIELDEXPRESSIONMAPENUMVALUES'].fields_by_name['val']._loaded_options = None
  _globals['_FIELDEXPRESSIONMAPENUMVALUES'].fields_by_name['val']._serialized_options = b'\272Hd\232\001a*_\272\001\\\n field_expression.map.enum.values\022-test message field_expression.map.enum.values\032\tthis == 1'
  _globals['_FIELDEXPRESSIONMAPMESSAGEVALUES_VALENTRY']._loaded_options = None
  _globals['_FIELDEXPRESSIONMAPMESSAGEVALUES_VALENTRY']._serialized_options = b'8\001'
  _globals['_FIELDEXPRESSIONMAPMESSAGEVALUES'].fields_by_name['val']._loaded_options = None
  _globals['_FIELDEXPRESSIONMAPMESSAGEVALUES'].fields_by_name['val']._serialized_options = b'\272Hl\232\001i*g\272\001d\n#field_expression.map.message.values\0220test message field_expression.map.message.values\032\013this.a == 1'
  _globals['_FIELDEXPRESSIONREPEATEDSCALAR'].fields_by_name['val']._loaded_options = None
  _globals['_FIELDEXPRESSIONREPEATEDSCALAR'].fields_by_name['val']._serialized_options = b'\272Hi\272\001f\n field_expression.repeated.scalar\022-test message field_expression.repeated.scalar\032\023this.all(e, e == 1)'
  _globals['_FIELDEXPRESSIONREPEATEDENUM'].fields_by_name['val']._loaded_options = None
  _globals['_FIELDEXPRESSIONREPEATEDENUM'].fields_by_name['val']._serialized_options = b'\272He\272\001b\n\036field_expression.repeated.enum\022+test message field_expression.repeated.enum\032\023this.all(e, e == 1)'
  _globals['_FIELDEXPRESSIONREPEATEDMESSAGE'].fields_by_name['val']._loaded_options = None
  _globals['_FIELDEXPRESSIONREPEATEDMESSAGE'].fields_by_name['val']._serialized_options = b'\272Hm\272\001j\n!field_expression.repeated.message\022.test message field_expression.repeated.message\032\025this.all(e, e.a == 1)'
  _globals['_FIELDEXPRESSIONREPEATEDSCALARITEMS'].fields_by_name['val']._loaded_options = None
  _globals['_FIELDEXPRESSIONREPEATEDSCALARITEMS'].fields_by_name['val']._serialized_options = b'\272Hp\222\001m\"k\272\001h\n&field_expression.repeated.scalar.items\0223test message field_expression.repeated.scalar.items\032\tthis == 1'
  _globals['_FIELDEXPRESSIONREPEATEDENUMITEMS'].fields_by_name['val']._loaded_options = None
  _globals['_FIELDEXPRESSIONREPEATEDENUMITEMS'].fields_by_name['val']._serialized_options = b'\272Hl\222\001i\"g\272\001d\n$field_expression.repeated.enum.items\0221test message field_expression.repeated.enum.items\032\tthis == 1'
  _globals['_FIELDEXPRESSIONREPEATEDMESSAGEITEMS'].fields_by_name['val']._loaded_options = None
  _globals['_FIELDEXPRESSIONREPEATEDMESSAGEITEMS'].fields_by_name['val']._serialized_options = b'\272Ht\222\001q\"o\272\001l\n\'field_expression.repeated.message.items\0224test message field_expression.repeated.message.items\032\013this.a == 1'
  _globals['_ENUM']._serialized_start=6442
  _globals['_ENUM']._serialized_end=6484
  _globals['_NOEXPRESSIONS']._serialized_start=159
  _globals['_NOEXPRESSIONS']._serialized_end=356
  _globals['_NOEXPRESSIONS_NESTED']._serialized_start=348
  _globals['_NOEXPRESSIONS_NESTED']._serialized_end=356
  _globals['_MESSAGEEXPRESSIONS']._serialized_start=359
  _globals['_MESSAGEEXPRESSIONS']._serialized_end=1066
  _globals['_MESSAGEEXPRESSIONS_NESTED']._serialized_start=735
  _globals['_MESSAGEEXPRESSIONS_NESTED']._serialized_end=855
  _globals['_MISSINGFIELD']._serialized_start=1068
  _globals['_MISSINGFIELD']._serialized_end=1150
  _globals['_INCORRECTTYPE']._serialized_start=1152
  _globals['_INCORRECTTYPE']._serialized_end=1255
  _globals['_DYNRUNTIMEERROR']._serialized_start=1257
  _globals['_DYNRUNTIMEERROR']._serialized_end=1382
  _globals['_NOWEQUALSNOW']._serialized_start=1384
  _globals['_NOWEQUALSNOW']._serialized_end=1476
  _globals['_FIELDEXPRESSIONMULTIPLESCALAR']._serialized_start=1479
  _globals['_FIELDEXPRESSIONMULTIPLESCALAR']._serialized_end=1830
  _globals['_FIELDEXPRESSIONNESTEDSCALAR']._serialized_start=1832
  _globals['_FIELDEXPRESSIONNESTEDSCALAR']._serialized_end=1959
  _globals['_FIELDEXPRESSIONOPTIONALSCALAR']._serialized_start=1962
  _globals['_FIELDEXPRESSIONOPTIONALSCALAR']._serialized_end=2124
  _globals['_FIELDEXPRESSIONSCALAR']._serialized_start=2126
  _globals['_FIELDEXPRESSIONSCALAR']._serialized_end=2249
  _globals['_FIELDEXPRESSIONENUM']._serialized_start=2252
  _globals['_FIELDEXPRESSIONENUM']._serialized_end=2427
  _globals['_FIELDEXPRESSIONMESSAGE']._serialized_start=2430
  _globals['_FIELDEXPRESSIONMESSAGE']._serialized_end=2659
  _globals['_FIELDEXPRESSIONMESSAGE_MSG']._serialized_start=2640
  _globals['_FIELDEXPRESSIONMESSAGE_MSG']._serialized_end=2659
  _globals['_FIELDEXPRESSIONMAPSCALAR']._serialized_start=2662
  _globals['_FIELDEXPRESSIONMAPSCALAR']._serialized_end=2955
  _globals['_FIELDEXPRESSIONMAPSCALAR_VALENTRY']._serialized_start=2901
  _globals['_FIELDEXPRESSIONMAPSCALAR_VALENTRY']._serialized_end=2955
  _globals['_FIELDEXPRESSIONMAPENUM']._serialized_start=2958
  _globals['_FIELDEXPRESSIONMAPENUM']._serialized_end=3300
  _globals['_FIELDEXPRESSIONMAPENUM_VALENTRY']._serialized_start=3189
  _globals['_FIELDEXPRESSIONMAPENUM_VALENTRY']._serialized_end=3300
  _globals['_FIELDEXPRESSIONMAPMESSAGE']._serialized_start=3303
  _globals['_FIELDEXPRESSIONMAPMESSAGE']._serialized_end=3706
  _globals['_FIELDEXPRESSIONMAPMESSAGE_VALENTRY']._serialized_start=3549
  _globals['_FIELDEXPRESSIONMAPMESSAGE_VALENTRY']._serialized_end=3685
  _globals['_FIELDEXPRESSIONMAPMESSAGE_MSG']._serialized_start=2640
  _globals['_FIELDEXPRESSIONMAPMESSAGE_MSG']._serialized_end=2659
  _globals['_FIELDEXPRESSIONMAPKEYS']._serialized_start=3709
  _globals['_FIELDEXPRESSIONMAPKEYS']._serialized_end=3996
  _globals['_FIELDEXPRESSIONMAPKEYS_VALENTRY']._serialized_start=2901
  _globals['_FIELDEXPRESSIONMAPKEYS_VALENTRY']._serialized_end=2955
  _globals['_FIELDEXPRESSIONMAPSCALARVALUES']._serialized_start=3999
  _globals['_FIELDEXPRESSIONMAPSCALARVALUES']._serialized_end=4307
  _globals['_FIELDEXPRESSIONMAPSCALARVALUES_VALENTRY']._serialized_start=2901
  _globals['_FIELDEXPRESSIONMAPSCALARVALUES_VALENTRY']._serialized_end=2955
  _globals['_FIELDEXPRESSIONMAPENUMVALUES']._serialized_start=4310
  _globals['_FIELDEXPRESSIONMAPENUMVALUES']._serialized_end=4667
  _globals['_FIELDEXPRESSIONMAPENUMVALUES_VALENTRY']._serialized_start=3189
  _globals['_FIELDEXPRESSIONMAPENUMVALUES_VALENTRY']._serialized_end=3300
  _globals['_FIELDEXPRESSIONMAPMESSAGEVALUES']._serialized_start=4670
  _globals['_FIELDEXPRESSIONMAPMESSAGEVALUES']._serialized_end=5094
  _globals['_FIELDEXPRESSIONMAPMESSAGEVALUES_VALENTRY']._serialized_start=4931
  _globals['_FIELDEXPRESSIONMAPMESSAGEVALUES_VALENTRY']._serialized_end=5073
  _globals['_FIELDEXPRESSIONMAPMESSAGEVALUES_MSG']._serialized_start=2640
  _globals['_FIELDEXPRESSIONMAPMESSAGEVALUES_MSG']._serialized_end=2659
  _globals['_FIELDEXPRESSIONREPEATEDSCALAR']._serialized_start=5097
  _globals['_FIELDEXPRESSIONREPEATEDSCALAR']._serialized_end=5256
  _globals['_FIELDEXPRESSIONREPEATEDENUM']._serialized_start=5259
  _globals['_FIELDEXPRESSIONREPEATEDENUM']._serialized_end=5470
  _globals['_FIELDEXPRESSIONREPEATEDMESSAGE']._serialized_start=5473
  _globals['_FIELDEXPRESSIONREPEATEDMESSAGE']._serialized_end=5746
  _globals['_FIELDEXPRESSIONREPEATEDMESSAGE_MSG']._serialized_start=2640
  _globals['_FIELDEXPRESSIONREPEATEDMESSAGE_MSG']._serialized_end=2659
  _globals['_FIELDEXPRESSIONREPEATEDSCALARITEMS']._serialized_start=5749
  _globals['_FIELDEXPRESSIONREPEATEDSCALARITEMS']._serialized_end=5921
  _globals['_FIELDEXPRESSIONREPEATEDENUMITEMS']._serialized_start=5924
  _globals['_FIELDEXPRESSIONREPEATEDENUMITEMS']._serialized_end=6147
  _globals['_FIELDEXPRESSIONREPEATEDMESSAGEITEMS']._serialized_start=6150
  _globals['_FIELDEXPRESSIONREPEATEDMESSAGEITEMS']._serialized_end=6440
  _globals['_FIELDEXPRESSIONREPEATEDMESSAGEITEMS_MSG']._serialized_start=2640
  _globals['_FIELDEXPRESSIONREPEATEDMESSAGEITEMS_MSG']._serialized_end=2659
# @@protoc_insertion_point(module_scope)
