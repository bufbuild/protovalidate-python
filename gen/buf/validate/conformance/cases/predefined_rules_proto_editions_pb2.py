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
# source: buf/validate/conformance/cases/predefined_rules_proto_editions.proto
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
    'buf/validate/conformance/cases/predefined_rules_proto_editions.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nDbuf/validate/conformance/cases/predefined_rules_proto_editions.proto\x12\x1e\x62uf.validate.conformance.cases\x1a\x1b\x62uf/validate/validate.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"?\n\x1ePredefinedFloatRuleEdition2023\x12\x1d\n\x03val\x18\x01 \x01(\x02\x42\x0b\xbaH\x08\n\x06\xd5H\x00\x00\x80?R\x03val\"D\n\x1fPredefinedDoubleRuleEdition2023\x12!\n\x03val\x18\x01 \x01(\x01\x42\x0f\xbaH\x0c\x12\n\xd1H\x00\x00\x00\x00\x00\x00\xf0?R\x03val\"<\n\x1ePredefinedInt32RuleEdition2023\x12\x1a\n\x03val\x18\x01 \x01(\x05\x42\x08\xbaH\x05\x1a\x03\xd0H\x01R\x03val\"<\n\x1ePredefinedInt64RuleEdition2023\x12\x1a\n\x03val\x18\x01 \x01(\x03\x42\x08\xbaH\x05\"\x03\xd0H\x01R\x03val\"=\n\x1fPredefinedUInt32RuleEdition2023\x12\x1a\n\x03val\x18\x01 \x01(\rB\x08\xbaH\x05*\x03\xd0H\x01R\x03val\"=\n\x1fPredefinedUInt64RuleEdition2023\x12\x1a\n\x03val\x18\x01 \x01(\x04\x42\x08\xbaH\x05\x32\x03\xd0H\x01R\x03val\"=\n\x1fPredefinedSInt32RuleEdition2023\x12\x1a\n\x03val\x18\x01 \x01(\x11\x42\x08\xbaH\x05:\x03\xd0H\x01R\x03val\"=\n\x1fPredefinedSInt64RuleEdition2023\x12\x1a\n\x03val\x18\x01 \x01(\x12\x42\x08\xbaH\x05\x42\x03\xd0H\x01R\x03val\">\n PredefinedFixed32RuleEdition2023\x12\x1a\n\x03val\x18\x01 \x01(\x07\x42\x08\xbaH\x05J\x03\xd0H\x01R\x03val\">\n PredefinedFixed64RuleEdition2023\x12\x1a\n\x03val\x18\x01 \x01(\x06\x42\x08\xbaH\x05R\x03\xd0H\x01R\x03val\"?\n!PredefinedSFixed32RuleEdition2023\x12\x1a\n\x03val\x18\x01 \x01(\x0f\x42\x08\xbaH\x05Z\x03\xd0H\x01R\x03val\"?\n!PredefinedSFixed64RuleEdition2023\x12\x1a\n\x03val\x18\x01 \x01(\x10\x42\x08\xbaH\x05\x62\x03\xd0H\x01R\x03val\";\n\x1dPredefinedBoolRuleEdition2023\x12\x1a\n\x03val\x18\x01 \x01(\x08\x42\x08\xbaH\x05j\x03\xd0H\x01R\x03val\"=\n\x1fPredefinedStringRuleEdition2023\x12\x1a\n\x03val\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xd0H\x01R\x03val\"<\n\x1ePredefinedBytesRuleEdition2023\x12\x1a\n\x03val\x18\x01 \x01(\x0c\x42\x08\xbaH\x05z\x03\xd0H\x01R\x03val\"\xdf\x01\n\x1dPredefinedEnumRuleEdition2023\x12j\n\x03val\x18\x01 \x01(\x0e\x32M.buf.validate.conformance.cases.PredefinedEnumRuleEdition2023.EnumEdition2023B\t\xbaH\x06\x82\x01\x03\xd0H\x01R\x03val\"R\n\x0f\x45numEdition2023\x12%\n!ENUM_EDITION2023_ZERO_UNSPECIFIED\x10\x00\x12\x18\n\x14\x45NUM_EDITION2023_ONE\x10\x01\"@\n!PredefinedRepeatedRuleEdition2023\x12\x1b\n\x03val\x18\x01 \x03(\x04\x42\t\xbaH\x06\x92\x01\x03\xd0H\x01R\x03val\"\xba\x01\n\x1cPredefinedMapRuleEdition2023\x12\x62\n\x03val\x18\x01 \x03(\x0b\x32\x45.buf.validate.conformance.cases.PredefinedMapRuleEdition2023.ValEntryB\t\xbaH\x06\x9a\x01\x03\xd0H\x01R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\x04R\x03key\x12\x14\n\x05value\x18\x02 \x01(\x04R\x05value:\x02\x38\x01\"[\n!PredefinedDurationRuleEdition2023\x12\x36\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\t\xbaH\x06\xaa\x01\x03\xd0H\x01R\x03val\"]\n\"PredefinedTimestampRuleEdition2023\x12\x37\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\t\xbaH\x06\xb2\x01\x03\xd0H\x01R\x03val\"\xda\x03\n\"PredefinedAndCustomRuleEdition2023\x12w\n\x01\x61\x18\x01 \x01(\x05\x42i\xbaHf\x1a\x03\xd0H\x01\xba\x01^\n.predefined_and_custom_rule_scalar_edition_2023\x1a,this > 24 ? \'\' : \'a must be greater than 24\'R\x01\x61\x12\xbf\x01\n\x01\x62\x18\x02 \x01(\x0b\x32I.buf.validate.conformance.cases.PredefinedAndCustomRuleEdition2023.NestedBf\xbaHc\xba\x01`\n0predefined_and_custom_rule_embedded_edition_2023\x12\x1b\x62.c must be a multiple of 3\x1a\x0fthis.c % 3 == 0R\x01\x62\x1ay\n\x06Nested\x12o\n\x01\x63\x18\x01 \x01(\x05\x42\x61\xbaH^\x1a\x03\xd0H\x01\xba\x01V\n.predefined_and_custom_rule_nested_edition_2023\x1a$this > 0 ? \'\' : \'c must be positive\'R\x01\x63\"\xb1\x01\n*StandardPredefinedAndCustomRuleEdition2023\x12\x82\x01\n\x01\x61\x18\x01 \x01(\x05\x42t\xbaHq\x1a\x05\x10\x1c\xd0H\x01\xba\x01g\n7standard_predefined_and_custom_rule_scalar_edition_2023\x1a,this > 24 ? \'\' : \'a must be greater than 24\'R\x01\x61:\xba\x01\n\x1c\x66loat_abs_range_edition_2023\x12\x18.buf.validate.FloatRules\x18\x8a\t \x01(\x02\x42_\xc2H\\\nZ\n\x1c\x66loat.abs_range.edition_2023\x12\x1b\x66loat value is out of range\x1a\x1dthis >= -rule && this <= ruleR\x18\x66loatAbsRangeEdition2023:\xbf\x01\n\x1d\x64ouble_abs_range_edition_2023\x12\x19.buf.validate.DoubleRules\x18\x8a\t \x01(\x01\x42\x61\xc2H^\n\\\n\x1d\x64ouble.abs_range.edition_2023\x12\x1c\x64ouble value is out of range\x1a\x1dthis >= -rule && this <= ruleR\x19\x64oubleAbsRangeEdition2023:\x98\x01\n\x17int32_even_edition_2023\x12\x18.buf.validate.Int32Rules\x18\x8a\t \x01(\x08\x42\x46\xc2HC\nA\n\x17int32.even.edition_2023\x12\x17int32 value is not even\x1a\rthis % 2 == 0R\x14int32EvenEdition2023:\x98\x01\n\x17int64_even_edition_2023\x12\x18.buf.validate.Int64Rules\x18\x8a\t \x01(\x08\x42\x46\xc2HC\nA\n\x17int64.even.edition_2023\x12\x17int64 value is not even\x1a\rthis % 2 == 0R\x14int64EvenEdition2023:\x9f\x01\n\x18uint32_even_edition_2023\x12\x19.buf.validate.UInt32Rules\x18\x8a\t \x01(\x08\x42J\xc2HG\nE\n\x18uint32.even.edition_2023\x12\x18uint32 value is not even\x1a\x0fthis % 2u == 0uR\x15uint32EvenEdition2023:\x9f\x01\n\x18uint64_even_edition_2023\x12\x19.buf.validate.UInt64Rules\x18\x8a\t \x01(\x08\x42J\xc2HG\nE\n\x18uint64.even.edition_2023\x12\x18uint64 value is not even\x1a\x0fthis % 2u == 0uR\x15uint64EvenEdition2023:\x9d\x01\n\x18sint32_even_edition_2023\x12\x19.buf.validate.SInt32Rules\x18\x8a\t \x01(\x08\x42H\xc2HE\nC\n\x18sint32.even.edition_2023\x12\x18sint32 value is not even\x1a\rthis % 2 == 0R\x15sint32EvenEdition2023:\x9d\x01\n\x18sint64_even_edition_2023\x12\x19.buf.validate.SInt64Rules\x18\x8a\t \x01(\x08\x42H\xc2HE\nC\n\x18sint64.even.edition_2023\x12\x18sint64 value is not even\x1a\rthis % 2 == 0R\x15sint64EvenEdition2023:\xa4\x01\n\x19\x66ixed32_even_edition_2023\x12\x1a.buf.validate.Fixed32Rules\x18\x8a\t \x01(\x08\x42L\xc2HI\nG\n\x19\x66ixed32.even.edition_2023\x12\x19\x66ixed32 value is not even\x1a\x0fthis % 2u == 0uR\x16\x66ixed32EvenEdition2023:\xa4\x01\n\x19\x66ixed64_even_edition_2023\x12\x1a.buf.validate.Fixed64Rules\x18\x8a\t \x01(\x08\x42L\xc2HI\nG\n\x19\x66ixed64.even.edition_2023\x12\x19\x66ixed64 value is not even\x1a\x0fthis % 2u == 0uR\x16\x66ixed64EvenEdition2023:\xa7\x01\n\x1asfixed32_even_edition_2023\x12\x1b.buf.validate.SFixed32Rules\x18\x8a\t \x01(\x08\x42L\xc2HI\nG\n\x1asfixed32.even.edition_2023\x12\x1asfixed32 value is not even\x1a\rthis % 2 == 0R\x17sfixed32EvenEdition2023:\xa7\x01\n\x1asfixed64_even_edition_2023\x12\x1b.buf.validate.SFixed64Rules\x18\x8a\t \x01(\x08\x42L\xc2HI\nG\n\x1asfixed64.even.edition_2023\x12\x1asfixed64 value is not even\x1a\rthis % 2 == 0R\x17sfixed64EvenEdition2023:\x97\x01\n\x17\x62ool_false_edition_2023\x12\x17.buf.validate.BoolRules\x18\x8a\t \x01(\x08\x42\x46\xc2HC\nA\n\x17\x62ool.false.edition_2023\x12\x17\x62ool value is not false\x1a\rthis == falseR\x14\x62oolFalseEdition2023:\x8f\x02\n\x1estring_valid_path_edition_2023\x12\x19.buf.validate.StringRules\x18\x8a\t \x01(\x08\x42\xae\x01\xc2H\xaa\x01\n\xa7\x01\n\x1estring.valid_path.edition_2023\x1a\x84\x01!this.matches(\'^([^/.][^/]?|[^/][^/.]|[^/]{3,})(/([^/.][^/]?|[^/][^/.]|[^/]{3,}))*$\') ? \'not a valid path: `%s`\'.format([this]) : \'\'R\x1astringValidPathEdition2023:\x93\x02\n\x1d\x62ytes_valid_path_edition_2023\x12\x18.buf.validate.BytesRules\x18\x8a\t \x01(\x08\x42\xb5\x01\xc2H\xb1\x01\n\xae\x01\n\x1d\x62ytes.valid_path.edition_2023\x1a\x8c\x01!string(this).matches(\'^([^/.][^/]?|[^/][^/.]|[^/]{3,})(/([^/.][^/]?|[^/][^/.]|[^/]{3,}))*$\') ? \'not a valid path: `%s`\'.format([this]) : \'\'R\x19\x62ytesValidPathEdition2023:\xa3\x01\n\x1a\x65num_non_zero_edition_2023\x12\x17.buf.validate.EnumRules\x18\x8a\t \x01(\x08\x42M\xc2HJ\nH\n\x1a\x65num.non_zero.edition_2023\x12\x1a\x65num value is not non-zero\x1a\x0eint(this) != 0R\x16\x65numNonZeroEdition2023:\xdd\x01\n#repeated_at_least_five_edition_2023\x12\x1b.buf.validate.RepeatedRules\x18\x8a\t \x01(\x08\x42r\xc2Ho\nm\n#repeated.at_least_five.edition_2023\x12-repeated field must have at least five values\x1a\x17uint(this.size()) >= 5uR\x1erepeatedAtLeastFiveEdition2023:\xbd\x01\n\x1emap_at_least_five_edition_2023\x12\x16.buf.validate.MapRules\x18\x8a\t \x01(\x08\x42\x61\xc2H^\n\\\n\x1emap.at_least_five.edition_2023\x12!map must have at least five pairs\x1a\x17uint(this.size()) >= 5uR\x19mapAtLeastFiveEdition2023:\xca\x01\n\x1e\x64uration_too_long_edition_2023\x12\x1b.buf.validate.DurationRules\x18\x8a\t \x01(\x08\x42h\xc2He\nc\n\x1e\x64uration.too_long.edition_2023\x12(duration can\'t be longer than 10 seconds\x1a\x17this <= duration(\'10s\')R\x1a\x64urationTooLongEdition2023:\xd9\x01\n\x1ftimestamp_in_range_edition_2023\x12\x1c.buf.validate.TimestampRules\x18\x8a\t \x01(\x08\x42t\xc2Hq\no\n!timestamp.time_range.edition_2023\x12\x16timestamp out of range\x1a\x32int(this) >= 1049587200 && int(this) <= 1080432000R\x1btimestampInRangeEdition2023b\x08\x65\x64itionsp\xe8\x07')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'buf.validate.conformance.cases.predefined_rules_proto_editions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['float_abs_range_edition_2023']._loaded_options = None
  _globals['float_abs_range_edition_2023']._serialized_options = b'\302H\\\nZ\n\034float.abs_range.edition_2023\022\033float value is out of range\032\035this >= -rule && this <= rule'
  _globals['double_abs_range_edition_2023']._loaded_options = None
  _globals['double_abs_range_edition_2023']._serialized_options = b'\302H^\n\\\n\035double.abs_range.edition_2023\022\034double value is out of range\032\035this >= -rule && this <= rule'
  _globals['int32_even_edition_2023']._loaded_options = None
  _globals['int32_even_edition_2023']._serialized_options = b'\302HC\nA\n\027int32.even.edition_2023\022\027int32 value is not even\032\rthis % 2 == 0'
  _globals['int64_even_edition_2023']._loaded_options = None
  _globals['int64_even_edition_2023']._serialized_options = b'\302HC\nA\n\027int64.even.edition_2023\022\027int64 value is not even\032\rthis % 2 == 0'
  _globals['uint32_even_edition_2023']._loaded_options = None
  _globals['uint32_even_edition_2023']._serialized_options = b'\302HG\nE\n\030uint32.even.edition_2023\022\030uint32 value is not even\032\017this % 2u == 0u'
  _globals['uint64_even_edition_2023']._loaded_options = None
  _globals['uint64_even_edition_2023']._serialized_options = b'\302HG\nE\n\030uint64.even.edition_2023\022\030uint64 value is not even\032\017this % 2u == 0u'
  _globals['sint32_even_edition_2023']._loaded_options = None
  _globals['sint32_even_edition_2023']._serialized_options = b'\302HE\nC\n\030sint32.even.edition_2023\022\030sint32 value is not even\032\rthis % 2 == 0'
  _globals['sint64_even_edition_2023']._loaded_options = None
  _globals['sint64_even_edition_2023']._serialized_options = b'\302HE\nC\n\030sint64.even.edition_2023\022\030sint64 value is not even\032\rthis % 2 == 0'
  _globals['fixed32_even_edition_2023']._loaded_options = None
  _globals['fixed32_even_edition_2023']._serialized_options = b'\302HI\nG\n\031fixed32.even.edition_2023\022\031fixed32 value is not even\032\017this % 2u == 0u'
  _globals['fixed64_even_edition_2023']._loaded_options = None
  _globals['fixed64_even_edition_2023']._serialized_options = b'\302HI\nG\n\031fixed64.even.edition_2023\022\031fixed64 value is not even\032\017this % 2u == 0u'
  _globals['sfixed32_even_edition_2023']._loaded_options = None
  _globals['sfixed32_even_edition_2023']._serialized_options = b'\302HI\nG\n\032sfixed32.even.edition_2023\022\032sfixed32 value is not even\032\rthis % 2 == 0'
  _globals['sfixed64_even_edition_2023']._loaded_options = None
  _globals['sfixed64_even_edition_2023']._serialized_options = b'\302HI\nG\n\032sfixed64.even.edition_2023\022\032sfixed64 value is not even\032\rthis % 2 == 0'
  _globals['bool_false_edition_2023']._loaded_options = None
  _globals['bool_false_edition_2023']._serialized_options = b'\302HC\nA\n\027bool.false.edition_2023\022\027bool value is not false\032\rthis == false'
  _globals['string_valid_path_edition_2023']._loaded_options = None
  _globals['string_valid_path_edition_2023']._serialized_options = b'\302H\252\001\n\247\001\n\036string.valid_path.edition_2023\032\204\001!this.matches(\'^([^/.][^/]?|[^/][^/.]|[^/]{3,})(/([^/.][^/]?|[^/][^/.]|[^/]{3,}))*$\') ? \'not a valid path: `%s`\'.format([this]) : \'\''
  _globals['bytes_valid_path_edition_2023']._loaded_options = None
  _globals['bytes_valid_path_edition_2023']._serialized_options = b'\302H\261\001\n\256\001\n\035bytes.valid_path.edition_2023\032\214\001!string(this).matches(\'^([^/.][^/]?|[^/][^/.]|[^/]{3,})(/([^/.][^/]?|[^/][^/.]|[^/]{3,}))*$\') ? \'not a valid path: `%s`\'.format([this]) : \'\''
  _globals['enum_non_zero_edition_2023']._loaded_options = None
  _globals['enum_non_zero_edition_2023']._serialized_options = b'\302HJ\nH\n\032enum.non_zero.edition_2023\022\032enum value is not non-zero\032\016int(this) != 0'
  _globals['repeated_at_least_five_edition_2023']._loaded_options = None
  _globals['repeated_at_least_five_edition_2023']._serialized_options = b'\302Ho\nm\n#repeated.at_least_five.edition_2023\022-repeated field must have at least five values\032\027uint(this.size()) >= 5u'
  _globals['map_at_least_five_edition_2023']._loaded_options = None
  _globals['map_at_least_five_edition_2023']._serialized_options = b'\302H^\n\\\n\036map.at_least_five.edition_2023\022!map must have at least five pairs\032\027uint(this.size()) >= 5u'
  _globals['duration_too_long_edition_2023']._loaded_options = None
  _globals['duration_too_long_edition_2023']._serialized_options = b'\302He\nc\n\036duration.too_long.edition_2023\022(duration can\'t be longer than 10 seconds\032\027this <= duration(\'10s\')'
  _globals['timestamp_in_range_edition_2023']._loaded_options = None
  _globals['timestamp_in_range_edition_2023']._serialized_options = b'\302Hq\no\n!timestamp.time_range.edition_2023\022\026timestamp out of range\0322int(this) >= 1049587200 && int(this) <= 1080432000'
  _globals['_PREDEFINEDFLOATRULEEDITION2023'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDFLOATRULEEDITION2023'].fields_by_name['val']._serialized_options = b'\272H\010\n\006\325H\000\000\200?'
  _globals['_PREDEFINEDDOUBLERULEEDITION2023'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDDOUBLERULEEDITION2023'].fields_by_name['val']._serialized_options = b'\272H\014\022\n\321H\000\000\000\000\000\000\360?'
  _globals['_PREDEFINEDINT32RULEEDITION2023'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDINT32RULEEDITION2023'].fields_by_name['val']._serialized_options = b'\272H\005\032\003\320H\001'
  _globals['_PREDEFINEDINT64RULEEDITION2023'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDINT64RULEEDITION2023'].fields_by_name['val']._serialized_options = b'\272H\005\"\003\320H\001'
  _globals['_PREDEFINEDUINT32RULEEDITION2023'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDUINT32RULEEDITION2023'].fields_by_name['val']._serialized_options = b'\272H\005*\003\320H\001'
  _globals['_PREDEFINEDUINT64RULEEDITION2023'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDUINT64RULEEDITION2023'].fields_by_name['val']._serialized_options = b'\272H\0052\003\320H\001'
  _globals['_PREDEFINEDSINT32RULEEDITION2023'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDSINT32RULEEDITION2023'].fields_by_name['val']._serialized_options = b'\272H\005:\003\320H\001'
  _globals['_PREDEFINEDSINT64RULEEDITION2023'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDSINT64RULEEDITION2023'].fields_by_name['val']._serialized_options = b'\272H\005B\003\320H\001'
  _globals['_PREDEFINEDFIXED32RULEEDITION2023'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDFIXED32RULEEDITION2023'].fields_by_name['val']._serialized_options = b'\272H\005J\003\320H\001'
  _globals['_PREDEFINEDFIXED64RULEEDITION2023'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDFIXED64RULEEDITION2023'].fields_by_name['val']._serialized_options = b'\272H\005R\003\320H\001'
  _globals['_PREDEFINEDSFIXED32RULEEDITION2023'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDSFIXED32RULEEDITION2023'].fields_by_name['val']._serialized_options = b'\272H\005Z\003\320H\001'
  _globals['_PREDEFINEDSFIXED64RULEEDITION2023'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDSFIXED64RULEEDITION2023'].fields_by_name['val']._serialized_options = b'\272H\005b\003\320H\001'
  _globals['_PREDEFINEDBOOLRULEEDITION2023'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDBOOLRULEEDITION2023'].fields_by_name['val']._serialized_options = b'\272H\005j\003\320H\001'
  _globals['_PREDEFINEDSTRINGRULEEDITION2023'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDSTRINGRULEEDITION2023'].fields_by_name['val']._serialized_options = b'\272H\005r\003\320H\001'
  _globals['_PREDEFINEDBYTESRULEEDITION2023'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDBYTESRULEEDITION2023'].fields_by_name['val']._serialized_options = b'\272H\005z\003\320H\001'
  _globals['_PREDEFINEDENUMRULEEDITION2023'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDENUMRULEEDITION2023'].fields_by_name['val']._serialized_options = b'\272H\006\202\001\003\320H\001'
  _globals['_PREDEFINEDREPEATEDRULEEDITION2023'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDREPEATEDRULEEDITION2023'].fields_by_name['val']._serialized_options = b'\272H\006\222\001\003\320H\001'
  _globals['_PREDEFINEDMAPRULEEDITION2023_VALENTRY']._loaded_options = None
  _globals['_PREDEFINEDMAPRULEEDITION2023_VALENTRY']._serialized_options = b'8\001'
  _globals['_PREDEFINEDMAPRULEEDITION2023'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDMAPRULEEDITION2023'].fields_by_name['val']._serialized_options = b'\272H\006\232\001\003\320H\001'
  _globals['_PREDEFINEDDURATIONRULEEDITION2023'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDDURATIONRULEEDITION2023'].fields_by_name['val']._serialized_options = b'\272H\006\252\001\003\320H\001'
  _globals['_PREDEFINEDTIMESTAMPRULEEDITION2023'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDTIMESTAMPRULEEDITION2023'].fields_by_name['val']._serialized_options = b'\272H\006\262\001\003\320H\001'
  _globals['_PREDEFINEDANDCUSTOMRULEEDITION2023_NESTED'].fields_by_name['c']._loaded_options = None
  _globals['_PREDEFINEDANDCUSTOMRULEEDITION2023_NESTED'].fields_by_name['c']._serialized_options = b'\272H^\032\003\320H\001\272\001V\n.predefined_and_custom_rule_nested_edition_2023\032$this > 0 ? \'\' : \'c must be positive\''
  _globals['_PREDEFINEDANDCUSTOMRULEEDITION2023'].fields_by_name['a']._loaded_options = None
  _globals['_PREDEFINEDANDCUSTOMRULEEDITION2023'].fields_by_name['a']._serialized_options = b'\272Hf\032\003\320H\001\272\001^\n.predefined_and_custom_rule_scalar_edition_2023\032,this > 24 ? \'\' : \'a must be greater than 24\''
  _globals['_PREDEFINEDANDCUSTOMRULEEDITION2023'].fields_by_name['b']._loaded_options = None
  _globals['_PREDEFINEDANDCUSTOMRULEEDITION2023'].fields_by_name['b']._serialized_options = b'\272Hc\272\001`\n0predefined_and_custom_rule_embedded_edition_2023\022\033b.c must be a multiple of 3\032\017this.c % 3 == 0'
  _globals['_STANDARDPREDEFINEDANDCUSTOMRULEEDITION2023'].fields_by_name['a']._loaded_options = None
  _globals['_STANDARDPREDEFINEDANDCUSTOMRULEEDITION2023'].fields_by_name['a']._serialized_options = b'\272Hq\032\005\020\034\320H\001\272\001g\n7standard_predefined_and_custom_rule_scalar_edition_2023\032,this > 24 ? \'\' : \'a must be greater than 24\''
  _globals['_PREDEFINEDFLOATRULEEDITION2023']._serialized_start=198
  _globals['_PREDEFINEDFLOATRULEEDITION2023']._serialized_end=261
  _globals['_PREDEFINEDDOUBLERULEEDITION2023']._serialized_start=263
  _globals['_PREDEFINEDDOUBLERULEEDITION2023']._serialized_end=331
  _globals['_PREDEFINEDINT32RULEEDITION2023']._serialized_start=333
  _globals['_PREDEFINEDINT32RULEEDITION2023']._serialized_end=393
  _globals['_PREDEFINEDINT64RULEEDITION2023']._serialized_start=395
  _globals['_PREDEFINEDINT64RULEEDITION2023']._serialized_end=455
  _globals['_PREDEFINEDUINT32RULEEDITION2023']._serialized_start=457
  _globals['_PREDEFINEDUINT32RULEEDITION2023']._serialized_end=518
  _globals['_PREDEFINEDUINT64RULEEDITION2023']._serialized_start=520
  _globals['_PREDEFINEDUINT64RULEEDITION2023']._serialized_end=581
  _globals['_PREDEFINEDSINT32RULEEDITION2023']._serialized_start=583
  _globals['_PREDEFINEDSINT32RULEEDITION2023']._serialized_end=644
  _globals['_PREDEFINEDSINT64RULEEDITION2023']._serialized_start=646
  _globals['_PREDEFINEDSINT64RULEEDITION2023']._serialized_end=707
  _globals['_PREDEFINEDFIXED32RULEEDITION2023']._serialized_start=709
  _globals['_PREDEFINEDFIXED32RULEEDITION2023']._serialized_end=771
  _globals['_PREDEFINEDFIXED64RULEEDITION2023']._serialized_start=773
  _globals['_PREDEFINEDFIXED64RULEEDITION2023']._serialized_end=835
  _globals['_PREDEFINEDSFIXED32RULEEDITION2023']._serialized_start=837
  _globals['_PREDEFINEDSFIXED32RULEEDITION2023']._serialized_end=900
  _globals['_PREDEFINEDSFIXED64RULEEDITION2023']._serialized_start=902
  _globals['_PREDEFINEDSFIXED64RULEEDITION2023']._serialized_end=965
  _globals['_PREDEFINEDBOOLRULEEDITION2023']._serialized_start=967
  _globals['_PREDEFINEDBOOLRULEEDITION2023']._serialized_end=1026
  _globals['_PREDEFINEDSTRINGRULEEDITION2023']._serialized_start=1028
  _globals['_PREDEFINEDSTRINGRULEEDITION2023']._serialized_end=1089
  _globals['_PREDEFINEDBYTESRULEEDITION2023']._serialized_start=1091
  _globals['_PREDEFINEDBYTESRULEEDITION2023']._serialized_end=1151
  _globals['_PREDEFINEDENUMRULEEDITION2023']._serialized_start=1154
  _globals['_PREDEFINEDENUMRULEEDITION2023']._serialized_end=1377
  _globals['_PREDEFINEDENUMRULEEDITION2023_ENUMEDITION2023']._serialized_start=1295
  _globals['_PREDEFINEDENUMRULEEDITION2023_ENUMEDITION2023']._serialized_end=1377
  _globals['_PREDEFINEDREPEATEDRULEEDITION2023']._serialized_start=1379
  _globals['_PREDEFINEDREPEATEDRULEEDITION2023']._serialized_end=1443
  _globals['_PREDEFINEDMAPRULEEDITION2023']._serialized_start=1446
  _globals['_PREDEFINEDMAPRULEEDITION2023']._serialized_end=1632
  _globals['_PREDEFINEDMAPRULEEDITION2023_VALENTRY']._serialized_start=1578
  _globals['_PREDEFINEDMAPRULEEDITION2023_VALENTRY']._serialized_end=1632
  _globals['_PREDEFINEDDURATIONRULEEDITION2023']._serialized_start=1634
  _globals['_PREDEFINEDDURATIONRULEEDITION2023']._serialized_end=1725
  _globals['_PREDEFINEDTIMESTAMPRULEEDITION2023']._serialized_start=1727
  _globals['_PREDEFINEDTIMESTAMPRULEEDITION2023']._serialized_end=1820
  _globals['_PREDEFINEDANDCUSTOMRULEEDITION2023']._serialized_start=1823
  _globals['_PREDEFINEDANDCUSTOMRULEEDITION2023']._serialized_end=2297
  _globals['_PREDEFINEDANDCUSTOMRULEEDITION2023_NESTED']._serialized_start=2176
  _globals['_PREDEFINEDANDCUSTOMRULEEDITION2023_NESTED']._serialized_end=2297
  _globals['_STANDARDPREDEFINEDANDCUSTOMRULEEDITION2023']._serialized_start=2300
  _globals['_STANDARDPREDEFINEDANDCUSTOMRULEEDITION2023']._serialized_end=2477
# @@protoc_insertion_point(module_scope)
