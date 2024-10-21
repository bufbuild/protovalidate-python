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
# source: buf/validate/conformance/cases/strings.proto
# Protobuf Python Version: 5.28.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    2,
    '',
    'buf/validate/conformance/cases/strings.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,buf/validate/conformance/cases/strings.proto\x12\x1e\x62uf.validate.conformance.cases\x1a\x1b\x62uf/validate/validate.proto\"\x1e\n\nStringNone\x12\x10\n\x03val\x18\x01 \x01(\tR\x03val\"+\n\x0bStringConst\x12\x1c\n\x03val\x18\x01 \x01(\tB\n\xbaH\x07r\x05\n\x03\x66ooR\x03val\"-\n\x08StringIn\x12!\n\x03val\x18\x01 \x01(\tB\x0f\xbaH\x0cr\nR\x03\x62\x61rR\x03\x62\x61zR\x03val\"2\n\x0bStringNotIn\x12#\n\x03val\x18\x01 \x01(\tB\x11\xbaH\x0er\x0cZ\x04\x66izzZ\x04\x62uzzR\x03val\"\'\n\tStringLen\x12\x1a\n\x03val\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\x98\x01\x03R\x03val\")\n\x0cStringMinLen\x12\x19\n\x03val\x18\x01 \x01(\tB\x07\xbaH\x04r\x02\x10\x03R\x03val\")\n\x0cStringMaxLen\x12\x19\n\x03val\x18\x01 \x01(\tB\x07\xbaH\x04r\x02\x18\x05R\x03val\".\n\x0fStringMinMaxLen\x12\x1b\n\x03val\x18\x01 \x01(\tB\t\xbaH\x06r\x04\x10\x03\x18\x05R\x03val\"3\n\x14StringEqualMinMaxLen\x12\x1b\n\x03val\x18\x01 \x01(\tB\t\xbaH\x06r\x04\x10\x05\x18\x05R\x03val\",\n\x0eStringLenBytes\x12\x1a\n\x03val\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xa0\x01\x04R\x03val\"+\n\x0eStringMinBytes\x12\x19\n\x03val\x18\x01 \x01(\tB\x07\xbaH\x04r\x02 \x04R\x03val\"+\n\x0eStringMaxBytes\x12\x19\n\x03val\x18\x01 \x01(\tB\x07\xbaH\x04r\x02(\x08R\x03val\"0\n\x11StringMinMaxBytes\x12\x1b\n\x03val\x18\x01 \x01(\tB\t\xbaH\x06r\x04 \x04(\x08R\x03val\"5\n\x16StringEqualMinMaxBytes\x12\x1b\n\x03val\x18\x01 \x01(\tB\t\xbaH\x06r\x04 \x04(\x04R\x03val\"9\n\rStringPattern\x12(\n\x03val\x18\x01 \x01(\tB\x16\xbaH\x13r\x11\x32\x0f(?i)^[a-z0-9]+$R\x03val\"9\n\x14StringPatternEscapes\x12!\n\x03val\x18\x01 \x01(\tB\x0f\xbaH\x0cr\n2\x08\\* \\\\ \\wR\x03val\",\n\x0cStringPrefix\x12\x1c\n\x03val\x18\x01 \x01(\tB\n\xbaH\x07r\x05:\x03\x66ooR\x03val\".\n\x0eStringContains\x12\x1c\n\x03val\x18\x01 \x01(\tB\n\xbaH\x07r\x05J\x03\x62\x61rR\x03val\"2\n\x11StringNotContains\x12\x1d\n\x03val\x18\x01 \x01(\tB\x0b\xbaH\x08r\x06\xba\x01\x03\x62\x61rR\x03val\",\n\x0cStringSuffix\x12\x1c\n\x03val\x18\x01 \x01(\tB\n\xbaH\x07r\x05\x42\x03\x62\x61zR\x03val\"(\n\x0bStringEmail\x12\x19\n\x03val\x18\x01 \x01(\tB\x07\xbaH\x04r\x02`\x01R\x03val\"+\n\x0eStringNotEmail\x12\x19\n\x03val\x18\x01 \x01(\tB\x07\xbaH\x04r\x02`\x00R\x03val\"+\n\rStringAddress\x12\x1a\n\x03val\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xa8\x01\x01R\x03val\".\n\x10StringNotAddress\x12\x1a\n\x03val\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xa8\x01\x00R\x03val\"+\n\x0eStringHostname\x12\x19\n\x03val\x18\x01 \x01(\tB\x07\xbaH\x04r\x02h\x01R\x03val\".\n\x11StringNotHostname\x12\x19\n\x03val\x18\x01 \x01(\tB\x07\xbaH\x04r\x02h\x00R\x03val\"%\n\x08StringIP\x12\x19\n\x03val\x18\x01 \x01(\tB\x07\xbaH\x04r\x02p\x01R\x03val\"(\n\x0bStringNotIP\x12\x19\n\x03val\x18\x01 \x01(\tB\x07\xbaH\x04r\x02p\x00R\x03val\"\'\n\nStringIPv4\x12\x19\n\x03val\x18\x01 \x01(\tB\x07\xbaH\x04r\x02x\x01R\x03val\"*\n\rStringNotIPv4\x12\x19\n\x03val\x18\x01 \x01(\tB\x07\xbaH\x04r\x02x\x00R\x03val\"(\n\nStringIPv6\x12\x1a\n\x03val\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\x80\x01\x01R\x03val\"+\n\rStringNotIPv6\x12\x1a\n\x03val\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\x80\x01\x00R\x03val\"3\n\x15StringIPWithPrefixLen\x12\x1a\n\x03val\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xd0\x01\x01R\x03val\"6\n\x18StringNotIPWithPrefixLen\x12\x1a\n\x03val\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xd0\x01\x00R\x03val\"5\n\x17StringIPv4WithPrefixLen\x12\x1a\n\x03val\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xd8\x01\x01R\x03val\"8\n\x1aStringNotIPv4WithPrefixLen\x12\x1a\n\x03val\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xd8\x01\x00R\x03val\"5\n\x17StringIPv6WithPrefixLen\x12\x1a\n\x03val\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xe0\x01\x01R\x03val\"8\n\x1aStringNotIPv6WithPrefixLen\x12\x1a\n\x03val\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xe0\x01\x00R\x03val\",\n\x0eStringIPPrefix\x12\x1a\n\x03val\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xe8\x01\x01R\x03val\"/\n\x11StringNotIPPrefix\x12\x1a\n\x03val\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xe8\x01\x00R\x03val\".\n\x10StringIPv4Prefix\x12\x1a\n\x03val\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xf0\x01\x01R\x03val\"1\n\x13StringNotIPv4Prefix\x12\x1a\n\x03val\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xf0\x01\x00R\x03val\".\n\x10StringIPv6Prefix\x12\x1a\n\x03val\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xf8\x01\x01R\x03val\"1\n\x13StringNotIPv6Prefix\x12\x1a\n\x03val\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xf8\x01\x00R\x03val\"\'\n\tStringURI\x12\x1a\n\x03val\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\x88\x01\x01R\x03val\"*\n\x0cStringNotURI\x12\x1a\n\x03val\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\x88\x01\x00R\x03val\"*\n\x0cStringURIRef\x12\x1a\n\x03val\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\x90\x01\x01R\x03val\"-\n\x0fStringNotURIRef\x12\x1a\n\x03val\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\x90\x01\x00R\x03val\"(\n\nStringUUID\x12\x1a\n\x03val\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\x03val\"+\n\rStringNotUUID\x12\x1a\n\x03val\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x00R\x03val\")\n\x0bStringTUUID\x12\x1a\n\x03val\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\x88\x02\x01R\x03val\",\n\x0eStringNotTUUID\x12\x1a\n\x03val\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\x88\x02\x00R\x03val\"2\n\x14StringHttpHeaderName\x12\x1a\n\x03val\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xc0\x01\x01R\x03val\"3\n\x15StringHttpHeaderValue\x12\x1a\n\x03val\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xc0\x01\x02R\x03val\":\n\x19StringHttpHeaderNameLoose\x12\x1d\n\x03val\x18\x01 \x01(\tB\x0b\xbaH\x08r\x06\xc0\x01\x01\xc8\x01\x00R\x03val\";\n\x1aStringHttpHeaderValueLoose\x12\x1d\n\x03val\x18\x01 \x01(\tB\x0b\xbaH\x08r\x06\xc0\x01\x02\xc8\x01\x00R\x03val\"1\n\x10StringUUIDIgnore\x12\x1d\n\x03val\x18\x01 \x01(\tB\x0b\xbaH\x08r\x03\xb0\x01\x01\xd0\x01\x01R\x03val\"7\n\rStringInOneof\x12\x1f\n\x03\x62\x61r\x18\x01 \x01(\tB\x0b\xbaH\x08r\x06R\x01\x61R\x01\x62H\x00R\x03\x62\x61rB\x05\n\x03\x66oo\"/\n\x11StringHostAndPort\x12\x1a\n\x03val\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\x80\x02\x01R\x03val\"\xa4\x01\n\x19StringHostAndOptionalPort\x12\x86\x01\n\x03val\x18\x01 \x01(\tBt\xbaHq\xba\x01n\n\"string.host_and_port.optional_port\x12-value must be a host and (optional) port pair\x1a\x19this.isHostAndPort(false)R\x03val\".\n\rStringExample\x12\x1d\n\x03val\x18\x01 \x01(\tB\x0b\xbaH\x08r\x06\x92\x02\x03\x66ooR\x03valB\xce\x01\n\"com.buf.validate.conformance.casesB\x0cStringsProtoP\x01\xa2\x02\x04\x42VCC\xaa\x02\x1e\x42uf.Validate.Conformance.Cases\xca\x02\x1e\x42uf\\Validate\\Conformance\\Cases\xe2\x02*Buf\\Validate\\Conformance\\Cases\\GPBMetadata\xea\x02!Buf::Validate::Conformance::Casesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'buf.validate.conformance.cases.strings_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.buf.validate.conformance.casesB\014StringsProtoP\001\242\002\004BVCC\252\002\036Buf.Validate.Conformance.Cases\312\002\036Buf\\Validate\\Conformance\\Cases\342\002*Buf\\Validate\\Conformance\\Cases\\GPBMetadata\352\002!Buf::Validate::Conformance::Cases'
  _globals['_STRINGCONST'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGCONST'].fields_by_name['val']._serialized_options = b'\272H\007r\005\n\003foo'
  _globals['_STRINGIN'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGIN'].fields_by_name['val']._serialized_options = b'\272H\014r\nR\003barR\003baz'
  _globals['_STRINGNOTIN'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGNOTIN'].fields_by_name['val']._serialized_options = b'\272H\016r\014Z\004fizzZ\004buzz'
  _globals['_STRINGLEN'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGLEN'].fields_by_name['val']._serialized_options = b'\272H\005r\003\230\001\003'
  _globals['_STRINGMINLEN'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGMINLEN'].fields_by_name['val']._serialized_options = b'\272H\004r\002\020\003'
  _globals['_STRINGMAXLEN'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGMAXLEN'].fields_by_name['val']._serialized_options = b'\272H\004r\002\030\005'
  _globals['_STRINGMINMAXLEN'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGMINMAXLEN'].fields_by_name['val']._serialized_options = b'\272H\006r\004\020\003\030\005'
  _globals['_STRINGEQUALMINMAXLEN'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGEQUALMINMAXLEN'].fields_by_name['val']._serialized_options = b'\272H\006r\004\020\005\030\005'
  _globals['_STRINGLENBYTES'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGLENBYTES'].fields_by_name['val']._serialized_options = b'\272H\005r\003\240\001\004'
  _globals['_STRINGMINBYTES'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGMINBYTES'].fields_by_name['val']._serialized_options = b'\272H\004r\002 \004'
  _globals['_STRINGMAXBYTES'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGMAXBYTES'].fields_by_name['val']._serialized_options = b'\272H\004r\002(\010'
  _globals['_STRINGMINMAXBYTES'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGMINMAXBYTES'].fields_by_name['val']._serialized_options = b'\272H\006r\004 \004(\010'
  _globals['_STRINGEQUALMINMAXBYTES'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGEQUALMINMAXBYTES'].fields_by_name['val']._serialized_options = b'\272H\006r\004 \004(\004'
  _globals['_STRINGPATTERN'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGPATTERN'].fields_by_name['val']._serialized_options = b'\272H\023r\0212\017(?i)^[a-z0-9]+$'
  _globals['_STRINGPATTERNESCAPES'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGPATTERNESCAPES'].fields_by_name['val']._serialized_options = b'\272H\014r\n2\010\\* \\\\ \\w'
  _globals['_STRINGPREFIX'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGPREFIX'].fields_by_name['val']._serialized_options = b'\272H\007r\005:\003foo'
  _globals['_STRINGCONTAINS'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGCONTAINS'].fields_by_name['val']._serialized_options = b'\272H\007r\005J\003bar'
  _globals['_STRINGNOTCONTAINS'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGNOTCONTAINS'].fields_by_name['val']._serialized_options = b'\272H\010r\006\272\001\003bar'
  _globals['_STRINGSUFFIX'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGSUFFIX'].fields_by_name['val']._serialized_options = b'\272H\007r\005B\003baz'
  _globals['_STRINGEMAIL'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGEMAIL'].fields_by_name['val']._serialized_options = b'\272H\004r\002`\001'
  _globals['_STRINGNOTEMAIL'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGNOTEMAIL'].fields_by_name['val']._serialized_options = b'\272H\004r\002`\000'
  _globals['_STRINGADDRESS'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGADDRESS'].fields_by_name['val']._serialized_options = b'\272H\005r\003\250\001\001'
  _globals['_STRINGNOTADDRESS'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGNOTADDRESS'].fields_by_name['val']._serialized_options = b'\272H\005r\003\250\001\000'
  _globals['_STRINGHOSTNAME'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGHOSTNAME'].fields_by_name['val']._serialized_options = b'\272H\004r\002h\001'
  _globals['_STRINGNOTHOSTNAME'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGNOTHOSTNAME'].fields_by_name['val']._serialized_options = b'\272H\004r\002h\000'
  _globals['_STRINGIP'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGIP'].fields_by_name['val']._serialized_options = b'\272H\004r\002p\001'
  _globals['_STRINGNOTIP'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGNOTIP'].fields_by_name['val']._serialized_options = b'\272H\004r\002p\000'
  _globals['_STRINGIPV4'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGIPV4'].fields_by_name['val']._serialized_options = b'\272H\004r\002x\001'
  _globals['_STRINGNOTIPV4'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGNOTIPV4'].fields_by_name['val']._serialized_options = b'\272H\004r\002x\000'
  _globals['_STRINGIPV6'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGIPV6'].fields_by_name['val']._serialized_options = b'\272H\005r\003\200\001\001'
  _globals['_STRINGNOTIPV6'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGNOTIPV6'].fields_by_name['val']._serialized_options = b'\272H\005r\003\200\001\000'
  _globals['_STRINGIPWITHPREFIXLEN'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGIPWITHPREFIXLEN'].fields_by_name['val']._serialized_options = b'\272H\005r\003\320\001\001'
  _globals['_STRINGNOTIPWITHPREFIXLEN'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGNOTIPWITHPREFIXLEN'].fields_by_name['val']._serialized_options = b'\272H\005r\003\320\001\000'
  _globals['_STRINGIPV4WITHPREFIXLEN'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGIPV4WITHPREFIXLEN'].fields_by_name['val']._serialized_options = b'\272H\005r\003\330\001\001'
  _globals['_STRINGNOTIPV4WITHPREFIXLEN'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGNOTIPV4WITHPREFIXLEN'].fields_by_name['val']._serialized_options = b'\272H\005r\003\330\001\000'
  _globals['_STRINGIPV6WITHPREFIXLEN'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGIPV6WITHPREFIXLEN'].fields_by_name['val']._serialized_options = b'\272H\005r\003\340\001\001'
  _globals['_STRINGNOTIPV6WITHPREFIXLEN'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGNOTIPV6WITHPREFIXLEN'].fields_by_name['val']._serialized_options = b'\272H\005r\003\340\001\000'
  _globals['_STRINGIPPREFIX'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGIPPREFIX'].fields_by_name['val']._serialized_options = b'\272H\005r\003\350\001\001'
  _globals['_STRINGNOTIPPREFIX'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGNOTIPPREFIX'].fields_by_name['val']._serialized_options = b'\272H\005r\003\350\001\000'
  _globals['_STRINGIPV4PREFIX'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGIPV4PREFIX'].fields_by_name['val']._serialized_options = b'\272H\005r\003\360\001\001'
  _globals['_STRINGNOTIPV4PREFIX'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGNOTIPV4PREFIX'].fields_by_name['val']._serialized_options = b'\272H\005r\003\360\001\000'
  _globals['_STRINGIPV6PREFIX'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGIPV6PREFIX'].fields_by_name['val']._serialized_options = b'\272H\005r\003\370\001\001'
  _globals['_STRINGNOTIPV6PREFIX'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGNOTIPV6PREFIX'].fields_by_name['val']._serialized_options = b'\272H\005r\003\370\001\000'
  _globals['_STRINGURI'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGURI'].fields_by_name['val']._serialized_options = b'\272H\005r\003\210\001\001'
  _globals['_STRINGNOTURI'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGNOTURI'].fields_by_name['val']._serialized_options = b'\272H\005r\003\210\001\000'
  _globals['_STRINGURIREF'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGURIREF'].fields_by_name['val']._serialized_options = b'\272H\005r\003\220\001\001'
  _globals['_STRINGNOTURIREF'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGNOTURIREF'].fields_by_name['val']._serialized_options = b'\272H\005r\003\220\001\000'
  _globals['_STRINGUUID'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGUUID'].fields_by_name['val']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_STRINGNOTUUID'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGNOTUUID'].fields_by_name['val']._serialized_options = b'\272H\005r\003\260\001\000'
  _globals['_STRINGTUUID'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGTUUID'].fields_by_name['val']._serialized_options = b'\272H\005r\003\210\002\001'
  _globals['_STRINGNOTTUUID'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGNOTTUUID'].fields_by_name['val']._serialized_options = b'\272H\005r\003\210\002\000'
  _globals['_STRINGHTTPHEADERNAME'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGHTTPHEADERNAME'].fields_by_name['val']._serialized_options = b'\272H\005r\003\300\001\001'
  _globals['_STRINGHTTPHEADERVALUE'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGHTTPHEADERVALUE'].fields_by_name['val']._serialized_options = b'\272H\005r\003\300\001\002'
  _globals['_STRINGHTTPHEADERNAMELOOSE'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGHTTPHEADERNAMELOOSE'].fields_by_name['val']._serialized_options = b'\272H\010r\006\300\001\001\310\001\000'
  _globals['_STRINGHTTPHEADERVALUELOOSE'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGHTTPHEADERVALUELOOSE'].fields_by_name['val']._serialized_options = b'\272H\010r\006\300\001\002\310\001\000'
  _globals['_STRINGUUIDIGNORE'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGUUIDIGNORE'].fields_by_name['val']._serialized_options = b'\272H\010r\003\260\001\001\320\001\001'
  _globals['_STRINGINONEOF'].fields_by_name['bar']._loaded_options = None
  _globals['_STRINGINONEOF'].fields_by_name['bar']._serialized_options = b'\272H\010r\006R\001aR\001b'
  _globals['_STRINGHOSTANDPORT'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGHOSTANDPORT'].fields_by_name['val']._serialized_options = b'\272H\005r\003\200\002\001'
  _globals['_STRINGHOSTANDOPTIONALPORT'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGHOSTANDOPTIONALPORT'].fields_by_name['val']._serialized_options = b'\272Hq\272\001n\n\"string.host_and_port.optional_port\022-value must be a host and (optional) port pair\032\031this.isHostAndPort(false)'
  _globals['_STRINGEXAMPLE'].fields_by_name['val']._loaded_options = None
  _globals['_STRINGEXAMPLE'].fields_by_name['val']._serialized_options = b'\272H\010r\006\222\002\003foo'
  _globals['_STRINGNONE']._serialized_start=109
  _globals['_STRINGNONE']._serialized_end=139
  _globals['_STRINGCONST']._serialized_start=141
  _globals['_STRINGCONST']._serialized_end=184
  _globals['_STRINGIN']._serialized_start=186
  _globals['_STRINGIN']._serialized_end=231
  _globals['_STRINGNOTIN']._serialized_start=233
  _globals['_STRINGNOTIN']._serialized_end=283
  _globals['_STRINGLEN']._serialized_start=285
  _globals['_STRINGLEN']._serialized_end=324
  _globals['_STRINGMINLEN']._serialized_start=326
  _globals['_STRINGMINLEN']._serialized_end=367
  _globals['_STRINGMAXLEN']._serialized_start=369
  _globals['_STRINGMAXLEN']._serialized_end=410
  _globals['_STRINGMINMAXLEN']._serialized_start=412
  _globals['_STRINGMINMAXLEN']._serialized_end=458
  _globals['_STRINGEQUALMINMAXLEN']._serialized_start=460
  _globals['_STRINGEQUALMINMAXLEN']._serialized_end=511
  _globals['_STRINGLENBYTES']._serialized_start=513
  _globals['_STRINGLENBYTES']._serialized_end=557
  _globals['_STRINGMINBYTES']._serialized_start=559
  _globals['_STRINGMINBYTES']._serialized_end=602
  _globals['_STRINGMAXBYTES']._serialized_start=604
  _globals['_STRINGMAXBYTES']._serialized_end=647
  _globals['_STRINGMINMAXBYTES']._serialized_start=649
  _globals['_STRINGMINMAXBYTES']._serialized_end=697
  _globals['_STRINGEQUALMINMAXBYTES']._serialized_start=699
  _globals['_STRINGEQUALMINMAXBYTES']._serialized_end=752
  _globals['_STRINGPATTERN']._serialized_start=754
  _globals['_STRINGPATTERN']._serialized_end=811
  _globals['_STRINGPATTERNESCAPES']._serialized_start=813
  _globals['_STRINGPATTERNESCAPES']._serialized_end=870
  _globals['_STRINGPREFIX']._serialized_start=872
  _globals['_STRINGPREFIX']._serialized_end=916
  _globals['_STRINGCONTAINS']._serialized_start=918
  _globals['_STRINGCONTAINS']._serialized_end=964
  _globals['_STRINGNOTCONTAINS']._serialized_start=966
  _globals['_STRINGNOTCONTAINS']._serialized_end=1016
  _globals['_STRINGSUFFIX']._serialized_start=1018
  _globals['_STRINGSUFFIX']._serialized_end=1062
  _globals['_STRINGEMAIL']._serialized_start=1064
  _globals['_STRINGEMAIL']._serialized_end=1104
  _globals['_STRINGNOTEMAIL']._serialized_start=1106
  _globals['_STRINGNOTEMAIL']._serialized_end=1149
  _globals['_STRINGADDRESS']._serialized_start=1151
  _globals['_STRINGADDRESS']._serialized_end=1194
  _globals['_STRINGNOTADDRESS']._serialized_start=1196
  _globals['_STRINGNOTADDRESS']._serialized_end=1242
  _globals['_STRINGHOSTNAME']._serialized_start=1244
  _globals['_STRINGHOSTNAME']._serialized_end=1287
  _globals['_STRINGNOTHOSTNAME']._serialized_start=1289
  _globals['_STRINGNOTHOSTNAME']._serialized_end=1335
  _globals['_STRINGIP']._serialized_start=1337
  _globals['_STRINGIP']._serialized_end=1374
  _globals['_STRINGNOTIP']._serialized_start=1376
  _globals['_STRINGNOTIP']._serialized_end=1416
  _globals['_STRINGIPV4']._serialized_start=1418
  _globals['_STRINGIPV4']._serialized_end=1457
  _globals['_STRINGNOTIPV4']._serialized_start=1459
  _globals['_STRINGNOTIPV4']._serialized_end=1501
  _globals['_STRINGIPV6']._serialized_start=1503
  _globals['_STRINGIPV6']._serialized_end=1543
  _globals['_STRINGNOTIPV6']._serialized_start=1545
  _globals['_STRINGNOTIPV6']._serialized_end=1588
  _globals['_STRINGIPWITHPREFIXLEN']._serialized_start=1590
  _globals['_STRINGIPWITHPREFIXLEN']._serialized_end=1641
  _globals['_STRINGNOTIPWITHPREFIXLEN']._serialized_start=1643
  _globals['_STRINGNOTIPWITHPREFIXLEN']._serialized_end=1697
  _globals['_STRINGIPV4WITHPREFIXLEN']._serialized_start=1699
  _globals['_STRINGIPV4WITHPREFIXLEN']._serialized_end=1752
  _globals['_STRINGNOTIPV4WITHPREFIXLEN']._serialized_start=1754
  _globals['_STRINGNOTIPV4WITHPREFIXLEN']._serialized_end=1810
  _globals['_STRINGIPV6WITHPREFIXLEN']._serialized_start=1812
  _globals['_STRINGIPV6WITHPREFIXLEN']._serialized_end=1865
  _globals['_STRINGNOTIPV6WITHPREFIXLEN']._serialized_start=1867
  _globals['_STRINGNOTIPV6WITHPREFIXLEN']._serialized_end=1923
  _globals['_STRINGIPPREFIX']._serialized_start=1925
  _globals['_STRINGIPPREFIX']._serialized_end=1969
  _globals['_STRINGNOTIPPREFIX']._serialized_start=1971
  _globals['_STRINGNOTIPPREFIX']._serialized_end=2018
  _globals['_STRINGIPV4PREFIX']._serialized_start=2020
  _globals['_STRINGIPV4PREFIX']._serialized_end=2066
  _globals['_STRINGNOTIPV4PREFIX']._serialized_start=2068
  _globals['_STRINGNOTIPV4PREFIX']._serialized_end=2117
  _globals['_STRINGIPV6PREFIX']._serialized_start=2119
  _globals['_STRINGIPV6PREFIX']._serialized_end=2165
  _globals['_STRINGNOTIPV6PREFIX']._serialized_start=2167
  _globals['_STRINGNOTIPV6PREFIX']._serialized_end=2216
  _globals['_STRINGURI']._serialized_start=2218
  _globals['_STRINGURI']._serialized_end=2257
  _globals['_STRINGNOTURI']._serialized_start=2259
  _globals['_STRINGNOTURI']._serialized_end=2301
  _globals['_STRINGURIREF']._serialized_start=2303
  _globals['_STRINGURIREF']._serialized_end=2345
  _globals['_STRINGNOTURIREF']._serialized_start=2347
  _globals['_STRINGNOTURIREF']._serialized_end=2392
  _globals['_STRINGUUID']._serialized_start=2394
  _globals['_STRINGUUID']._serialized_end=2434
  _globals['_STRINGNOTUUID']._serialized_start=2436
  _globals['_STRINGNOTUUID']._serialized_end=2479
  _globals['_STRINGTUUID']._serialized_start=2481
  _globals['_STRINGTUUID']._serialized_end=2522
  _globals['_STRINGNOTTUUID']._serialized_start=2524
  _globals['_STRINGNOTTUUID']._serialized_end=2568
  _globals['_STRINGHTTPHEADERNAME']._serialized_start=2570
  _globals['_STRINGHTTPHEADERNAME']._serialized_end=2620
  _globals['_STRINGHTTPHEADERVALUE']._serialized_start=2622
  _globals['_STRINGHTTPHEADERVALUE']._serialized_end=2673
  _globals['_STRINGHTTPHEADERNAMELOOSE']._serialized_start=2675
  _globals['_STRINGHTTPHEADERNAMELOOSE']._serialized_end=2733
  _globals['_STRINGHTTPHEADERVALUELOOSE']._serialized_start=2735
  _globals['_STRINGHTTPHEADERVALUELOOSE']._serialized_end=2794
  _globals['_STRINGUUIDIGNORE']._serialized_start=2796
  _globals['_STRINGUUIDIGNORE']._serialized_end=2845
  _globals['_STRINGINONEOF']._serialized_start=2847
  _globals['_STRINGINONEOF']._serialized_end=2902
  _globals['_STRINGHOSTANDPORT']._serialized_start=2904
  _globals['_STRINGHOSTANDPORT']._serialized_end=2951
  _globals['_STRINGHOSTANDOPTIONALPORT']._serialized_start=2954
  _globals['_STRINGHOSTANDOPTIONALPORT']._serialized_end=3118
  _globals['_STRINGEXAMPLE']._serialized_start=3120
  _globals['_STRINGEXAMPLE']._serialized_end=3166
# @@protoc_insertion_point(module_scope)
