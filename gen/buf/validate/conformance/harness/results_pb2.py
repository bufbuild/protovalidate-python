# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: buf/validate/conformance/harness/results.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate.conformance.harness import harness_pb2 as buf_dot_validate_dot_conformance_dot_harness_dot_harness__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.buf/validate/conformance/harness/results.proto\x12 buf.validate.conformance.harness\x1a.buf/validate/conformance/harness/harness.proto\x1a\x19google/protobuf/any.proto\x1a google/protobuf/descriptor.proto\"\xcf\x01\n\rResultOptions\x12!\n\x0csuite_filter\x18\x01 \x01(\tR\x0bsuiteFilter\x12\x1f\n\x0b\x63\x61se_filter\x18\x02 \x01(\tR\ncaseFilter\x12\x18\n\x07verbose\x18\x03 \x01(\x08R\x07verbose\x12\x16\n\x06strict\x18\x04 \x01(\x08R\x06strict\x12%\n\x0estrict_message\x18\x05 \x01(\x08R\rstrictMessage\x12!\n\x0cstrict_error\x18\x06 \x01(\x08R\x0bstrictError\"\x85\x02\n\tResultSet\x12\x1c\n\tsuccesses\x18\x01 \x01(\x05R\tsuccesses\x12\x1a\n\x08\x66\x61ilures\x18\x02 \x01(\x05R\x08\x66\x61ilures\x12\x46\n\x06suites\x18\x03 \x03(\x0b\x32..buf.validate.conformance.harness.SuiteResultsR\x06suites\x12I\n\x07options\x18\x04 \x01(\x0b\x32/.buf.validate.conformance.harness.ResultOptionsR\x07options\x12+\n\x11\x65xpected_failures\x18\x05 \x01(\x05R\x10\x65xpectedFailures\"\x87\x02\n\x0cSuiteResults\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1c\n\tsuccesses\x18\x02 \x01(\x05R\tsuccesses\x12\x1a\n\x08\x66\x61ilures\x18\x03 \x01(\x05R\x08\x66\x61ilures\x12\x42\n\x05\x63\x61ses\x18\x04 \x03(\x0b\x32,.buf.validate.conformance.harness.CaseResultR\x05\x63\x61ses\x12\x38\n\x05\x66\x64set\x18\x05 \x01(\x0b\x32\".google.protobuf.FileDescriptorSetR\x05\x66\x64set\x12+\n\x11\x65xpected_failures\x18\x06 \x01(\x05R\x10\x65xpectedFailures\"\x97\x02\n\nCaseResult\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x18\n\x07success\x18\x02 \x01(\x08R\x07success\x12\x44\n\x06wanted\x18\x03 \x01(\x0b\x32,.buf.validate.conformance.harness.TestResultR\x06wanted\x12>\n\x03got\x18\x04 \x01(\x0b\x32,.buf.validate.conformance.harness.TestResultR\x03got\x12*\n\x05input\x18\x05 \x01(\x0b\x32\x14.google.protobuf.AnyR\x05input\x12)\n\x10\x65xpected_failure\x18\x06 \x01(\x08R\x0f\x65xpectedFailureb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'buf.validate.conformance.harness.results_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_RESULTOPTIONS']._serialized_start=194
  _globals['_RESULTOPTIONS']._serialized_end=401
  _globals['_RESULTSET']._serialized_start=404
  _globals['_RESULTSET']._serialized_end=665
  _globals['_SUITERESULTS']._serialized_start=668
  _globals['_SUITERESULTS']._serialized_end=931
  _globals['_CASERESULT']._serialized_start=934
  _globals['_CASERESULT']._serialized_end=1213
# @@protoc_insertion_point(module_scope)
