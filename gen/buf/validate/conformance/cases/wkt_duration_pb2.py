# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: buf/validate/conformance/cases/wkt_duration.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.protovalidate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n1buf/validate/conformance/cases/wkt_duration.proto\x12\x1e\x62uf.validate.conformance.cases\x1a\x1b\x62uf/validate/validate.proto\x1a\x1egoogle/protobuf/duration.proto";\n\x0c\x44urationNone\x12+\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationR\x03val"H\n\x10\x44urationRequired\x12\x34\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x07\xfa\xf7\x18\x03\xc8\x01\x01R\x03val"I\n\rDurationConst\x12\x38\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x0b\xfa\xf7\x18\x07\xaa\x01\x04\x12\x02\x08\x03R\x03val"K\n\nDurationIn\x12=\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x10\xfa\xf7\x18\x0c\xaa\x01\t:\x02\x08\x01:\x03\x10\xe8\x07R\x03val"G\n\rDurationNotIn\x12\x36\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\t\xfa\xf7\x18\x05\xaa\x01\x02\x42\x00R\x03val"D\n\nDurationLT\x12\x36\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\t\xfa\xf7\x18\x05\xaa\x01\x02\x1a\x00R\x03val"G\n\x0b\x44urationLTE\x12\x38\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x0b\xfa\xf7\x18\x07\xaa\x01\x04"\x02\x08\x01R\x03val"G\n\nDurationGT\x12\x39\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x0c\xfa\xf7\x18\x08\xaa\x01\x05*\x03\x10\xe8\x07R\x03val"I\n\x0b\x44urationGTE\x12:\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\r\xfa\xf7\x18\t\xaa\x01\x06\x32\x04\x10\xc0\x84=R\x03val"J\n\x0c\x44urationGTLT\x12:\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\r\xfa\xf7\x18\t\xaa\x01\x06\x1a\x02\x08\x01*\x00R\x03val"L\n\x0e\x44urationExLTGT\x12:\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\r\xfa\xf7\x18\t\xaa\x01\x06\x1a\x00*\x02\x08\x01R\x03val"O\n\x0e\x44urationGTELTE\x12=\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x10\xfa\xf7\x18\x0c\xaa\x01\t"\x03\x08\x90\x1c\x32\x02\x08<R\x03val"Q\n\x10\x44urationExGTELTE\x12=\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x10\xfa\xf7\x18\x0c\xaa\x01\t"\x02\x08<2\x03\x08\x90\x1cR\x03val"\x8c\x01\n\x1c\x44urationFieldWithOtherFields\x12I\n\x0c\x64uration_val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x0b\xfa\xf7\x18\x07\xaa\x01\x04"\x02\x08\x01R\x0b\x64urationVal\x12!\n\x07int_val\x18\x02 \x01(\x05\x42\x08\xfa\xf7\x18\x04\x1a\x02 \x10R\x06intValb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "buf.validate.conformance.cases.wkt_duration_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _DURATIONREQUIRED.fields_by_name["val"]._options = None
    _DURATIONREQUIRED.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\003\310\001\001"
    _DURATIONCONST.fields_by_name["val"]._options = None
    _DURATIONCONST.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\007\252\001\004\022\002\010\003"
    _DURATIONIN.fields_by_name["val"]._options = None
    _DURATIONIN.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\014\252\001\t:\002\010\001:\003\020\350\007"
    _DURATIONNOTIN.fields_by_name["val"]._options = None
    _DURATIONNOTIN.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\005\252\001\002B\000"
    _DURATIONLT.fields_by_name["val"]._options = None
    _DURATIONLT.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\005\252\001\002\032\000"
    _DURATIONLTE.fields_by_name["val"]._options = None
    _DURATIONLTE.fields_by_name[
        "val"
    ]._serialized_options = b'\372\367\030\007\252\001\004"\002\010\001'
    _DURATIONGT.fields_by_name["val"]._options = None
    _DURATIONGT.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\010\252\001\005*\003\020\350\007"
    _DURATIONGTE.fields_by_name["val"]._options = None
    _DURATIONGTE.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\t\252\001\0062\004\020\300\204="
    _DURATIONGTLT.fields_by_name["val"]._options = None
    _DURATIONGTLT.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\t\252\001\006\032\002\010\001*\000"
    _DURATIONEXLTGT.fields_by_name["val"]._options = None
    _DURATIONEXLTGT.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\t\252\001\006\032\000*\002\010\001"
    _DURATIONGTELTE.fields_by_name["val"]._options = None
    _DURATIONGTELTE.fields_by_name[
        "val"
    ]._serialized_options = b'\372\367\030\014\252\001\t"\003\010\220\0342\002\010<'
    _DURATIONEXGTELTE.fields_by_name["val"]._options = None
    _DURATIONEXGTELTE.fields_by_name[
        "val"
    ]._serialized_options = b'\372\367\030\014\252\001\t"\002\010<2\003\010\220\034'
    _DURATIONFIELDWITHOTHERFIELDS.fields_by_name["duration_val"]._options = None
    _DURATIONFIELDWITHOTHERFIELDS.fields_by_name[
        "duration_val"
    ]._serialized_options = b'\372\367\030\007\252\001\004"\002\010\001'
    _DURATIONFIELDWITHOTHERFIELDS.fields_by_name["int_val"]._options = None
    _DURATIONFIELDWITHOTHERFIELDS.fields_by_name[
        "int_val"
    ]._serialized_options = b"\372\367\030\004\032\002 \020"
    _globals["_DURATIONNONE"]._serialized_start = 146
    _globals["_DURATIONNONE"]._serialized_end = 205
    _globals["_DURATIONREQUIRED"]._serialized_start = 207
    _globals["_DURATIONREQUIRED"]._serialized_end = 279
    _globals["_DURATIONCONST"]._serialized_start = 281
    _globals["_DURATIONCONST"]._serialized_end = 354
    _globals["_DURATIONIN"]._serialized_start = 356
    _globals["_DURATIONIN"]._serialized_end = 431
    _globals["_DURATIONNOTIN"]._serialized_start = 433
    _globals["_DURATIONNOTIN"]._serialized_end = 504
    _globals["_DURATIONLT"]._serialized_start = 506
    _globals["_DURATIONLT"]._serialized_end = 574
    _globals["_DURATIONLTE"]._serialized_start = 576
    _globals["_DURATIONLTE"]._serialized_end = 647
    _globals["_DURATIONGT"]._serialized_start = 649
    _globals["_DURATIONGT"]._serialized_end = 720
    _globals["_DURATIONGTE"]._serialized_start = 722
    _globals["_DURATIONGTE"]._serialized_end = 795
    _globals["_DURATIONGTLT"]._serialized_start = 797
    _globals["_DURATIONGTLT"]._serialized_end = 871
    _globals["_DURATIONEXLTGT"]._serialized_start = 873
    _globals["_DURATIONEXLTGT"]._serialized_end = 949
    _globals["_DURATIONGTELTE"]._serialized_start = 951
    _globals["_DURATIONGTELTE"]._serialized_end = 1030
    _globals["_DURATIONEXGTELTE"]._serialized_start = 1032
    _globals["_DURATIONEXGTELTE"]._serialized_end = 1113
    _globals["_DURATIONFIELDWITHOTHERFIELDS"]._serialized_start = 1116
    _globals["_DURATIONFIELDWITHOTHERFIELDS"]._serialized_end = 1256
# @@protoc_insertion_point(module_scope)
