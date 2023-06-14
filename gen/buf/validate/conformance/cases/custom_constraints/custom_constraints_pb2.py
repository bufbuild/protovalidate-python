# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: buf/validate/conformance/cases/custom_constraints/custom_constraints.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nJbuf/validate/conformance/cases/custom_constraints/custom_constraints.proto\x12\x31\x62uf.validate.conformance.cases.custom_constraints\x1a\x1b\x62uf/validate/validate.proto\"\xc5\x01\n\rNoExpressions\x12\x0c\n\x01\x61\x18\x01 \x01(\x05R\x01\x61\x12\x45\n\x01\x62\x18\x02 \x01(\x0e\x32\x37.buf.validate.conformance.cases.custom_constraints.EnumR\x01\x62\x12U\n\x01\x63\x18\x03 \x01(\x0b\x32G.buf.validate.conformance.cases.custom_constraints.NoExpressions.NestedR\x01\x63\x1a\x08\n\x06Nested\"\xc5\x05\n\x12MessageExpressions\x12\x0c\n\x01\x61\x18\x01 \x01(\x05R\x01\x61\x12\x0c\n\x01\x62\x18\x02 \x01(\x05R\x01\x62\x12\x45\n\x01\x63\x18\x03 \x01(\x0e\x32\x37.buf.validate.conformance.cases.custom_constraints.EnumR\x01\x63\x12\x45\n\x01\x64\x18\x04 \x01(\x0e\x32\x37.buf.validate.conformance.cases.custom_constraints.EnumR\x01\x64\x12Z\n\x01\x65\x18\x05 \x01(\x0b\x32L.buf.validate.conformance.cases.custom_constraints.MessageExpressions.NestedR\x01\x65\x12Z\n\x01\x66\x18\x06 \x01(\x0b\x32L.buf.validate.conformance.cases.custom_constraints.MessageExpressions.NestedR\x01\x66\x1ay\n\x06Nested\x12\x0c\n\x01\x61\x18\x01 \x01(\x05R\x01\x61\x12\x0c\n\x01\x62\x18\x02 \x01(\x05R\x01\x62:S\xfa\xf7\x18O\x1aM\n\x19message_expression_nested\x1a\x30this.a > this.b ? \'\': \'a must be greater than b\':\xd1\x01\xfa\xf7\x18\xcc\x01\x1a\x43\n\x19message_expression_scalar\x12\x15\x61 must be less than b\x1a\x0fthis.a < this.b\x1a?\n\x17message_expression_enum\x12\x12\x63 must not equal d\x1a\x10this.c != this.d\x1a\x44\n\x18message_expression_embed\x12\x12\x65.a must equal f.a\x1a\x14this.e.a == this.f.a\"\xfb\x03\n\x10\x46ieldExpressions\x12[\n\x01\x61\x18\x01 \x01(\x05\x42M\xfa\xf7\x18I\xba\x01\x46\n\x17\x66ield_expression_scalar\x1a+this > 42 ? \'\': \'a must be greater than 42\'R\x01\x61\x12\x80\x01\n\x01\x62\x18\x02 \x01(\x0e\x32\x37.buf.validate.conformance.cases.custom_constraints.EnumB9\xfa\xf7\x18\x35\xba\x01\x32\n\x15\x66ield_expression_enum\x12\x0e\x62 must be ~ONE\x1a\tthis == 1R\x01\x62\x12\xa7\x01\n\x01\x63\x18\x03 \x01(\x0b\x32J.buf.validate.conformance.cases.custom_constraints.FieldExpressions.NestedBM\xfa\xf7\x18I\xba\x01\x46\n\x16\x66ield_expression_embed\x12\x1b\x63.a must be a multiple of 4\x1a\x0fthis.a % 4 == 0R\x01\x63\x1a]\n\x06Nested\x12S\n\x01\x61\x18\x01 \x01(\x05\x42\x45\xfa\xf7\x18\x41\xba\x01>\n\x17\x66ield_expression_nested\x1a#this > 0 ? \'\': \'a must be positive\'R\x01\x61\"S\n\x0cMissingField\x12\x0c\n\x01\x61\x18\x01 \x01(\x05R\x01\x61:5\xfa\xf7\x18\x31\x1a/\n\rmissing_field\x12\x12\x62 must be positive\x1a\nthis.b > 0\"h\n\rIncorrectType\x12\x0c\n\x01\x61\x18\x01 \x01(\x05R\x01\x61:I\xfa\xf7\x18\x45\x1a\x43\n\x0eincorrect_type\x12\x17\x61 must start with \'foo\'\x1a\x18this.a.startsWith(\'foo\')\"~\n\x0f\x44ynRuntimeError\x12\x0c\n\x01\x61\x18\x01 \x01(\x05R\x01\x61:]\xfa\xf7\x18Y\x1aW\n\x0f\x64yn_runtime_err\x12.dynamic type tries to use a non-existent field\x1a\x14\x64yn(this).b == \'foo\'\"]\n\x0cNowEqualsNow:M\xfa\xf7\x18I\x1aG\n\x0enow_equals_now\x12)now should equal now within an expression\x1a\nnow == now**\n\x04\x45num\x12\x14\n\x10\x45NUM_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x45NUM_ONE\x10\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'buf.validate.conformance.cases.custom_constraints.custom_constraints_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MESSAGEEXPRESSIONS_NESTED._options = None
  _MESSAGEEXPRESSIONS_NESTED._serialized_options = b'\372\367\030O\032M\n\031message_expression_nested\0320this.a > this.b ? \'\': \'a must be greater than b\''
  _MESSAGEEXPRESSIONS._options = None
  _MESSAGEEXPRESSIONS._serialized_options = b'\372\367\030\314\001\032C\n\031message_expression_scalar\022\025a must be less than b\032\017this.a < this.b\032?\n\027message_expression_enum\022\022c must not equal d\032\020this.c != this.d\032D\n\030message_expression_embed\022\022e.a must equal f.a\032\024this.e.a == this.f.a'
  _FIELDEXPRESSIONS_NESTED.fields_by_name['a']._options = None
  _FIELDEXPRESSIONS_NESTED.fields_by_name['a']._serialized_options = b'\372\367\030A\272\001>\n\027field_expression_nested\032#this > 0 ? \'\': \'a must be positive\''
  _FIELDEXPRESSIONS.fields_by_name['a']._options = None
  _FIELDEXPRESSIONS.fields_by_name['a']._serialized_options = b'\372\367\030I\272\001F\n\027field_expression_scalar\032+this > 42 ? \'\': \'a must be greater than 42\''
  _FIELDEXPRESSIONS.fields_by_name['b']._options = None
  _FIELDEXPRESSIONS.fields_by_name['b']._serialized_options = b'\372\367\0305\272\0012\n\025field_expression_enum\022\016b must be ~ONE\032\tthis == 1'
  _FIELDEXPRESSIONS.fields_by_name['c']._options = None
  _FIELDEXPRESSIONS.fields_by_name['c']._serialized_options = b'\372\367\030I\272\001F\n\026field_expression_embed\022\033c.a must be a multiple of 4\032\017this.a % 4 == 0'
  _MISSINGFIELD._options = None
  _MISSINGFIELD._serialized_options = b'\372\367\0301\032/\n\rmissing_field\022\022b must be positive\032\nthis.b > 0'
  _INCORRECTTYPE._options = None
  _INCORRECTTYPE._serialized_options = b'\372\367\030E\032C\n\016incorrect_type\022\027a must start with \'foo\'\032\030this.a.startsWith(\'foo\')'
  _DYNRUNTIMEERROR._options = None
  _DYNRUNTIMEERROR._serialized_options = b'\372\367\030Y\032W\n\017dyn_runtime_err\022.dynamic type tries to use a non-existent field\032\024dyn(this).b == \'foo\''
  _NOWEQUALSNOW._options = None
  _NOWEQUALSNOW._serialized_options = b'\372\367\030I\032G\n\016now_equals_now\022)now should equal now within an expression\032\nnow == now'
  _globals['_ENUM']._serialized_start=1994
  _globals['_ENUM']._serialized_end=2036
  _globals['_NOEXPRESSIONS']._serialized_start=159
  _globals['_NOEXPRESSIONS']._serialized_end=356
  _globals['_NOEXPRESSIONS_NESTED']._serialized_start=348
  _globals['_NOEXPRESSIONS_NESTED']._serialized_end=356
  _globals['_MESSAGEEXPRESSIONS']._serialized_start=359
  _globals['_MESSAGEEXPRESSIONS']._serialized_end=1068
  _globals['_MESSAGEEXPRESSIONS_NESTED']._serialized_start=735
  _globals['_MESSAGEEXPRESSIONS_NESTED']._serialized_end=856
  _globals['_FIELDEXPRESSIONS']._serialized_start=1071
  _globals['_FIELDEXPRESSIONS']._serialized_end=1578
  _globals['_FIELDEXPRESSIONS_NESTED']._serialized_start=1485
  _globals['_FIELDEXPRESSIONS_NESTED']._serialized_end=1578
  _globals['_MISSINGFIELD']._serialized_start=1580
  _globals['_MISSINGFIELD']._serialized_end=1663
  _globals['_INCORRECTTYPE']._serialized_start=1665
  _globals['_INCORRECTTYPE']._serialized_end=1769
  _globals['_DYNRUNTIMEERROR']._serialized_start=1771
  _globals['_DYNRUNTIMEERROR']._serialized_end=1897
  _globals['_NOWEQUALSNOW']._serialized_start=1899
  _globals['_NOWEQUALSNOW']._serialized_end=1992
# @@protoc_insertion_point(module_scope)
