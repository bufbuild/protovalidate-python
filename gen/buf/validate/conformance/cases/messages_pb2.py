# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: buf/validate/conformance/cases/messages.proto
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
    'buf/validate/conformance/cases/messages.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate.conformance.cases.other_package import embed_pb2 as buf_dot_validate_dot_conformance_dot_cases_dot_other__package_dot_embed__pb2
from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-buf/validate/conformance/cases/messages.proto\x12\x1e\x62uf.validate.conformance.cases\x1a\x38\x62uf/validate/conformance/cases/other_package/embed.proto\x1a\x1b\x62uf/validate/validate.proto\"l\n\x07TestMsg\x12 \n\x05\x63onst\x18\x01 \x01(\tB\n\xbaH\x07r\x05\n\x03\x66ooR\x05\x63onst\x12?\n\x06nested\x18\x02 \x01(\x0b\x32\'.buf.validate.conformance.cases.TestMsgR\x06nested\"_\n\x0bMessageNone\x12\x45\n\x03val\x18\x01 \x01(\x0b\x32\x33.buf.validate.conformance.cases.MessageNone.NoneMsgR\x03val\x1a\t\n\x07NoneMsg\"3\n\x0fMessageDisabled\x12\x19\n\x03val\x18\x01 \x01(\x04\x42\x07\xbaH\x04\x32\x02 {R\x03val:\x05\xbaH\x02\x08\x01\"D\n\x07Message\x12\x39\n\x03val\x18\x01 \x01(\x0b\x32\'.buf.validate.conformance.cases.TestMsgR\x03val\"\\\n\x13MessageCrossPackage\x12\x45\n\x03val\x18\x01 \x01(\x0b\x32\x33.buf.validate.conformance.cases.other_package.EmbedR\x03val\"P\n\x0bMessageSkip\x12\x41\n\x03val\x18\x01 \x01(\x0b\x32\'.buf.validate.conformance.cases.TestMsgB\x06\xbaH\x03\xd8\x01\x03R\x03val\"T\n\x0fMessageRequired\x12\x41\n\x03val\x18\x01 \x01(\x0b\x32\'.buf.validate.conformance.cases.TestMsgB\x06\xbaH\x03\xc8\x01\x01R\x03val\"l\n\x1aMessageRequiredButOptional\x12\x46\n\x03val\x18\x01 \x01(\x0b\x32\'.buf.validate.conformance.cases.TestMsgB\x06\xbaH\x03\xc8\x01\x01H\x00R\x03val\x88\x01\x01\x42\x06\n\x04_val\"i\n\x14MessageRequiredOneof\x12\x43\n\x03val\x18\x01 \x01(\x0b\x32\'.buf.validate.conformance.cases.TestMsgB\x06\xbaH\x03\xc8\x01\x01H\x00R\x03valB\x0c\n\x03one\x12\x05\xbaH\x02\x08\x01\"\x15\n\x13MessageWith3dInsideb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'buf.validate.conformance.cases.messages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TESTMSG'].fields_by_name['const']._loaded_options = None
  _globals['_TESTMSG'].fields_by_name['const']._serialized_options = b'\272H\007r\005\n\003foo'
  _globals['_MESSAGEDISABLED'].fields_by_name['val']._loaded_options = None
  _globals['_MESSAGEDISABLED'].fields_by_name['val']._serialized_options = b'\272H\0042\002 {'
  _globals['_MESSAGEDISABLED']._loaded_options = None
  _globals['_MESSAGEDISABLED']._serialized_options = b'\272H\002\010\001'
  _globals['_MESSAGESKIP'].fields_by_name['val']._loaded_options = None
  _globals['_MESSAGESKIP'].fields_by_name['val']._serialized_options = b'\272H\003\330\001\003'
  _globals['_MESSAGEREQUIRED'].fields_by_name['val']._loaded_options = None
  _globals['_MESSAGEREQUIRED'].fields_by_name['val']._serialized_options = b'\272H\003\310\001\001'
  _globals['_MESSAGEREQUIREDBUTOPTIONAL'].fields_by_name['val']._loaded_options = None
  _globals['_MESSAGEREQUIREDBUTOPTIONAL'].fields_by_name['val']._serialized_options = b'\272H\003\310\001\001'
  _globals['_MESSAGEREQUIREDONEOF'].oneofs_by_name['one']._loaded_options = None
  _globals['_MESSAGEREQUIREDONEOF'].oneofs_by_name['one']._serialized_options = b'\272H\002\010\001'
  _globals['_MESSAGEREQUIREDONEOF'].fields_by_name['val']._loaded_options = None
  _globals['_MESSAGEREQUIREDONEOF'].fields_by_name['val']._serialized_options = b'\272H\003\310\001\001'
  _globals['_TESTMSG']._serialized_start=168
  _globals['_TESTMSG']._serialized_end=276
  _globals['_MESSAGENONE']._serialized_start=278
  _globals['_MESSAGENONE']._serialized_end=373
  _globals['_MESSAGENONE_NONEMSG']._serialized_start=364
  _globals['_MESSAGENONE_NONEMSG']._serialized_end=373
  _globals['_MESSAGEDISABLED']._serialized_start=375
  _globals['_MESSAGEDISABLED']._serialized_end=426
  _globals['_MESSAGE']._serialized_start=428
  _globals['_MESSAGE']._serialized_end=496
  _globals['_MESSAGECROSSPACKAGE']._serialized_start=498
  _globals['_MESSAGECROSSPACKAGE']._serialized_end=590
  _globals['_MESSAGESKIP']._serialized_start=592
  _globals['_MESSAGESKIP']._serialized_end=672
  _globals['_MESSAGEREQUIRED']._serialized_start=674
  _globals['_MESSAGEREQUIRED']._serialized_end=758
  _globals['_MESSAGEREQUIREDBUTOPTIONAL']._serialized_start=760
  _globals['_MESSAGEREQUIREDBUTOPTIONAL']._serialized_end=868
  _globals['_MESSAGEREQUIREDONEOF']._serialized_start=870
  _globals['_MESSAGEREQUIREDONEOF']._serialized_end=975
  _globals['_MESSAGEWITH3DINSIDE']._serialized_start=977
  _globals['_MESSAGEWITH3DINSIDE']._serialized_end=998
# @@protoc_insertion_point(module_scope)
