# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: buf/validate/conformance/cases/repeated.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.protovalidate.conformance.cases.other_package import (
    embed_pb2 as buf_dot_validate_dot_conformance_dot_cases_dot_other__package_dot_embed__pb2,
)
from buf.protovalidate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n-buf/validate/conformance/cases/repeated.proto\x12\x1e\x62uf.validate.conformance.cases\x1a\x38\x62uf/validate/conformance/cases/other_package/embed.proto\x1a\x1b\x62uf/validate/validate.proto\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/duration.proto"#\n\x05\x45mbed\x12\x1a\n\x03val\x18\x01 \x01(\x03\x42\x08\xfa\xf7\x18\x04"\x02 \x00R\x03val" \n\x0cRepeatedNone\x12\x10\n\x03val\x18\x01 \x03(\x03R\x03val"L\n\x11RepeatedEmbedNone\x12\x37\n\x03val\x18\x01 \x03(\x0b\x32%.buf.validate.conformance.cases.EmbedR\x03val"f\n\x1dRepeatedEmbedCrossPackageNone\x12\x45\n\x03val\x18\x01 \x03(\x0b\x32\x33.buf.validate.conformance.cases.other_package.EmbedR\x03val"Q\n\x0bRepeatedMin\x12\x42\n\x03val\x18\x01 \x03(\x0b\x32%.buf.validate.conformance.cases.EmbedB\t\xfa\xf7\x18\x05\x92\x01\x02\x08\x02R\x03val"*\n\x0bRepeatedMax\x12\x1b\n\x03val\x18\x01 \x03(\x01\x42\t\xfa\xf7\x18\x05\x92\x01\x02\x10\x03R\x03val"/\n\x0eRepeatedMinMax\x12\x1d\n\x03val\x18\x01 \x03(\x0f\x42\x0b\xfa\xf7\x18\x07\x92\x01\x04\x08\x02\x10\x04R\x03val".\n\rRepeatedExact\x12\x1d\n\x03val\x18\x01 \x03(\rB\x0b\xfa\xf7\x18\x07\x92\x01\x04\x08\x03\x10\x03R\x03val"-\n\x0eRepeatedUnique\x12\x1b\n\x03val\x18\x01 \x03(\tB\t\xfa\xf7\x18\x05\x92\x01\x02\x18\x01R\x03val"6\n\x10RepeatedItemRule\x12"\n\x03val\x18\x01 \x03(\x02\x42\x10\xfa\xf7\x18\x0c\x92\x01\t"\x07\n\x05%\x00\x00\x00\x00R\x03val"E\n\x13RepeatedItemPattern\x12.\n\x03val\x18\x01 \x03(\tB\x1c\xfa\xf7\x18\x18\x92\x01\x15"\x13r\x11\x32\x0f(?i)^[a-z0-9]+$R\x03val"Z\n\x11RepeatedEmbedSkip\x12\x45\n\x03val\x18\x01 \x03(\x0b\x32%.buf.validate.conformance.cases.EmbedB\x0c\xfa\xf7\x18\x08\x92\x01\x05"\x03\xc0\x01\x01R\x03val"9\n\x0eRepeatedItemIn\x12\'\n\x03val\x18\x01 \x03(\tB\x15\xfa\xf7\x18\x11\x92\x01\x0e"\x0cr\nR\x03\x66ooR\x03\x62\x61rR\x03val"<\n\x11RepeatedItemNotIn\x12\'\n\x03val\x18\x01 \x03(\tB\x15\xfa\xf7\x18\x11\x92\x01\x0e"\x0cr\nZ\x03\x66ooZ\x03\x62\x61rR\x03val"[\n\x0eRepeatedEnumIn\x12I\n\x03val\x18\x01 \x03(\x0e\x32&.buf.validate.conformance.cases.AnEnumB\x0f\xfa\xf7\x18\x0b\x92\x01\x08"\x06\x82\x01\x03\x1a\x01\x00R\x03val"^\n\x11RepeatedEnumNotIn\x12I\n\x03val\x18\x01 \x03(\x0e\x32&.buf.validate.conformance.cases.AnEnumB\x0f\xfa\xf7\x18\x0b\x92\x01\x08"\x06\x82\x01\x03"\x01\x00R\x03val"\xe1\x01\n\x16RepeatedEmbeddedEnumIn\x12g\n\x03val\x18\x01 \x03(\x0e\x32\x44.buf.validate.conformance.cases.RepeatedEmbeddedEnumIn.AnotherInEnumB\x0f\xfa\xf7\x18\x0b\x92\x01\x08"\x06\x82\x01\x03\x1a\x01\x00R\x03val"^\n\rAnotherInEnum\x12\x1f\n\x1b\x41NOTHER_IN_ENUM_UNSPECIFIED\x10\x00\x12\x15\n\x11\x41NOTHER_IN_ENUM_A\x10\x01\x12\x15\n\x11\x41NOTHER_IN_ENUM_B\x10\x02"\xf9\x01\n\x19RepeatedEmbeddedEnumNotIn\x12m\n\x03val\x18\x01 \x03(\x0e\x32J.buf.validate.conformance.cases.RepeatedEmbeddedEnumNotIn.AnotherNotInEnumB\x0f\xfa\xf7\x18\x0b\x92\x01\x08"\x06\x82\x01\x03"\x01\x00R\x03val"m\n\x10\x41notherNotInEnum\x12#\n\x1f\x41NOTHER_NOT_IN_ENUM_UNSPECIFIED\x10\x00\x12\x19\n\x15\x41NOTHER_NOT_IN_ENUM_A\x10\x01\x12\x19\n\x15\x41NOTHER_NOT_IN_ENUM_B\x10\x02"s\n\rRepeatedAnyIn\x12\x62\n\x03val\x18\x01 \x03(\x0b\x32\x14.google.protobuf.AnyB:\xfa\xf7\x18\x36\x92\x01\x33"1\xa2\x01.\x12,type.googleapis.com/google.protobuf.DurationR\x03val"w\n\x10RepeatedAnyNotIn\x12\x63\n\x03val\x18\x01 \x03(\x0b\x32\x14.google.protobuf.AnyB;\xfa\xf7\x18\x37\x92\x01\x34"2\xa2\x01/\x1a-type.googleapis.com/google.protobuf.TimestampR\x03val";\n\x15RepeatedMinAndItemLen\x12"\n\x03val\x18\x01 \x03(\tB\x10\xfa\xf7\x18\x0c\x92\x01\t\x08\x01"\x05r\x03\x98\x01\x03R\x03val"9\n\x18RepeatedMinAndMaxItemLen\x12\x1d\n\x03val\x18\x01 \x03(\tB\x0b\xfa\xf7\x18\x07\x92\x01\x04\x08\x01\x10\x03R\x03val"S\n\x10RepeatedDuration\x12?\n\x03val\x18\x01 \x03(\x0b\x32\x19.google.protobuf.DurationB\x12\xfa\xf7\x18\x0e\x92\x01\x0b"\t\xaa\x01\x06\x32\x04\x10\xc0\x84=R\x03val"7\n\x13RepeatedExactIgnore\x12 \n\x03val\x18\x01 \x03(\rB\x0e\xfa\xf7\x18\n\x92\x01\x04\x08\x03\x10\x03\xd0\x01\x01R\x03val*?\n\x06\x41nEnum\x12\x17\n\x13\x41N_ENUM_UNSPECIFIED\x10\x00\x12\r\n\tAN_ENUM_X\x10\x01\x12\r\n\tAN_ENUM_Y\x10\x02\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "buf.validate.conformance.cases.repeated_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _EMBED.fields_by_name["val"]._options = None
    _EMBED.fields_by_name["val"]._serialized_options = b'\372\367\030\004"\002 \000'
    _REPEATEDMIN.fields_by_name["val"]._options = None
    _REPEATEDMIN.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\005\222\001\002\010\002"
    _REPEATEDMAX.fields_by_name["val"]._options = None
    _REPEATEDMAX.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\005\222\001\002\020\003"
    _REPEATEDMINMAX.fields_by_name["val"]._options = None
    _REPEATEDMINMAX.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\007\222\001\004\010\002\020\004"
    _REPEATEDEXACT.fields_by_name["val"]._options = None
    _REPEATEDEXACT.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\007\222\001\004\010\003\020\003"
    _REPEATEDUNIQUE.fields_by_name["val"]._options = None
    _REPEATEDUNIQUE.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\005\222\001\002\030\001"
    _REPEATEDITEMRULE.fields_by_name["val"]._options = None
    _REPEATEDITEMRULE.fields_by_name[
        "val"
    ]._serialized_options = b'\372\367\030\014\222\001\t"\007\n\005%\000\000\000\000'
    _REPEATEDITEMPATTERN.fields_by_name["val"]._options = None
    _REPEATEDITEMPATTERN.fields_by_name[
        "val"
    ]._serialized_options = (
        b'\372\367\030\030\222\001\025"\023r\0212\017(?i)^[a-z0-9]+$'
    )
    _REPEATEDEMBEDSKIP.fields_by_name["val"]._options = None
    _REPEATEDEMBEDSKIP.fields_by_name[
        "val"
    ]._serialized_options = b'\372\367\030\010\222\001\005"\003\300\001\001'
    _REPEATEDITEMIN.fields_by_name["val"]._options = None
    _REPEATEDITEMIN.fields_by_name[
        "val"
    ]._serialized_options = b'\372\367\030\021\222\001\016"\014r\nR\003fooR\003bar'
    _REPEATEDITEMNOTIN.fields_by_name["val"]._options = None
    _REPEATEDITEMNOTIN.fields_by_name[
        "val"
    ]._serialized_options = b'\372\367\030\021\222\001\016"\014r\nZ\003fooZ\003bar'
    _REPEATEDENUMIN.fields_by_name["val"]._options = None
    _REPEATEDENUMIN.fields_by_name[
        "val"
    ]._serialized_options = b'\372\367\030\013\222\001\010"\006\202\001\003\032\001\000'
    _REPEATEDENUMNOTIN.fields_by_name["val"]._options = None
    _REPEATEDENUMNOTIN.fields_by_name[
        "val"
    ]._serialized_options = b'\372\367\030\013\222\001\010"\006\202\001\003"\001\000'
    _REPEATEDEMBEDDEDENUMIN.fields_by_name["val"]._options = None
    _REPEATEDEMBEDDEDENUMIN.fields_by_name[
        "val"
    ]._serialized_options = b'\372\367\030\013\222\001\010"\006\202\001\003\032\001\000'
    _REPEATEDEMBEDDEDENUMNOTIN.fields_by_name["val"]._options = None
    _REPEATEDEMBEDDEDENUMNOTIN.fields_by_name[
        "val"
    ]._serialized_options = b'\372\367\030\013\222\001\010"\006\202\001\003"\001\000'
    _REPEATEDANYIN.fields_by_name["val"]._options = None
    _REPEATEDANYIN.fields_by_name[
        "val"
    ]._serialized_options = b'\372\367\0306\222\0013"1\242\001.\022,type.googleapis.com/google.protobuf.Duration'
    _REPEATEDANYNOTIN.fields_by_name["val"]._options = None
    _REPEATEDANYNOTIN.fields_by_name[
        "val"
    ]._serialized_options = b'\372\367\0307\222\0014"2\242\001/\032-type.googleapis.com/google.protobuf.Timestamp'
    _REPEATEDMINANDITEMLEN.fields_by_name["val"]._options = None
    _REPEATEDMINANDITEMLEN.fields_by_name[
        "val"
    ]._serialized_options = b'\372\367\030\014\222\001\t\010\001"\005r\003\230\001\003'
    _REPEATEDMINANDMAXITEMLEN.fields_by_name["val"]._options = None
    _REPEATEDMINANDMAXITEMLEN.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\007\222\001\004\010\001\020\003"
    _REPEATEDDURATION.fields_by_name["val"]._options = None
    _REPEATEDDURATION.fields_by_name[
        "val"
    ]._serialized_options = (
        b'\372\367\030\016\222\001\013"\t\252\001\0062\004\020\300\204='
    )
    _REPEATEDEXACTIGNORE.fields_by_name["val"]._options = None
    _REPEATEDEXACTIGNORE.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\n\222\001\004\010\003\020\003\320\001\001"
    _globals["_ANENUM"]._serialized_start = 2260
    _globals["_ANENUM"]._serialized_end = 2323
    _globals["_EMBED"]._serialized_start = 227
    _globals["_EMBED"]._serialized_end = 262
    _globals["_REPEATEDNONE"]._serialized_start = 264
    _globals["_REPEATEDNONE"]._serialized_end = 296
    _globals["_REPEATEDEMBEDNONE"]._serialized_start = 298
    _globals["_REPEATEDEMBEDNONE"]._serialized_end = 374
    _globals["_REPEATEDEMBEDCROSSPACKAGENONE"]._serialized_start = 376
    _globals["_REPEATEDEMBEDCROSSPACKAGENONE"]._serialized_end = 478
    _globals["_REPEATEDMIN"]._serialized_start = 480
    _globals["_REPEATEDMIN"]._serialized_end = 561
    _globals["_REPEATEDMAX"]._serialized_start = 563
    _globals["_REPEATEDMAX"]._serialized_end = 605
    _globals["_REPEATEDMINMAX"]._serialized_start = 607
    _globals["_REPEATEDMINMAX"]._serialized_end = 654
    _globals["_REPEATEDEXACT"]._serialized_start = 656
    _globals["_REPEATEDEXACT"]._serialized_end = 702
    _globals["_REPEATEDUNIQUE"]._serialized_start = 704
    _globals["_REPEATEDUNIQUE"]._serialized_end = 749
    _globals["_REPEATEDITEMRULE"]._serialized_start = 751
    _globals["_REPEATEDITEMRULE"]._serialized_end = 805
    _globals["_REPEATEDITEMPATTERN"]._serialized_start = 807
    _globals["_REPEATEDITEMPATTERN"]._serialized_end = 876
    _globals["_REPEATEDEMBEDSKIP"]._serialized_start = 878
    _globals["_REPEATEDEMBEDSKIP"]._serialized_end = 968
    _globals["_REPEATEDITEMIN"]._serialized_start = 970
    _globals["_REPEATEDITEMIN"]._serialized_end = 1027
    _globals["_REPEATEDITEMNOTIN"]._serialized_start = 1029
    _globals["_REPEATEDITEMNOTIN"]._serialized_end = 1089
    _globals["_REPEATEDENUMIN"]._serialized_start = 1091
    _globals["_REPEATEDENUMIN"]._serialized_end = 1182
    _globals["_REPEATEDENUMNOTIN"]._serialized_start = 1184
    _globals["_REPEATEDENUMNOTIN"]._serialized_end = 1278
    _globals["_REPEATEDEMBEDDEDENUMIN"]._serialized_start = 1281
    _globals["_REPEATEDEMBEDDEDENUMIN"]._serialized_end = 1506
    _globals["_REPEATEDEMBEDDEDENUMIN_ANOTHERINENUM"]._serialized_start = 1412
    _globals["_REPEATEDEMBEDDEDENUMIN_ANOTHERINENUM"]._serialized_end = 1506
    _globals["_REPEATEDEMBEDDEDENUMNOTIN"]._serialized_start = 1509
    _globals["_REPEATEDEMBEDDEDENUMNOTIN"]._serialized_end = 1758
    _globals["_REPEATEDEMBEDDEDENUMNOTIN_ANOTHERNOTINENUM"]._serialized_start = 1649
    _globals["_REPEATEDEMBEDDEDENUMNOTIN_ANOTHERNOTINENUM"]._serialized_end = 1758
    _globals["_REPEATEDANYIN"]._serialized_start = 1760
    _globals["_REPEATEDANYIN"]._serialized_end = 1875
    _globals["_REPEATEDANYNOTIN"]._serialized_start = 1877
    _globals["_REPEATEDANYNOTIN"]._serialized_end = 1996
    _globals["_REPEATEDMINANDITEMLEN"]._serialized_start = 1998
    _globals["_REPEATEDMINANDITEMLEN"]._serialized_end = 2057
    _globals["_REPEATEDMINANDMAXITEMLEN"]._serialized_start = 2059
    _globals["_REPEATEDMINANDMAXITEMLEN"]._serialized_end = 2116
    _globals["_REPEATEDDURATION"]._serialized_start = 2118
    _globals["_REPEATEDDURATION"]._serialized_end = 2201
    _globals["_REPEATEDEXACTIGNORE"]._serialized_start = 2203
    _globals["_REPEATEDEXACTIGNORE"]._serialized_end = 2258
# @@protoc_insertion_point(module_scope)
