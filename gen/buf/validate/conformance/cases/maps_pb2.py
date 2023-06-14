# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: buf/validate/conformance/cases/maps.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.protovalidate import validate_pb2 as buf_dot_validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n)buf/validate/conformance/cases/maps.proto\x12\x1e\x62uf.validate.conformance.cases\x1a\x1b\x62uf/validate/validate.proto"\x85\x01\n\x07MapNone\x12\x42\n\x03val\x18\x01 \x03(\x0b\x32\x30.buf.validate.conformance.cases.MapNone.ValEntryR\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\rR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x08R\x05value:\x02\x38\x01"\x8e\x01\n\x06MapMin\x12L\n\x03val\x18\x01 \x03(\x0b\x32/.buf.validate.conformance.cases.MapMin.ValEntryB\t\xfa\xf7\x18\x05\x9a\x01\x02\x08\x02R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\x05R\x03key\x12\x14\n\x05value\x18\x02 \x01(\x02R\x05value:\x02\x38\x01"\x8e\x01\n\x06MapMax\x12L\n\x03val\x18\x01 \x03(\x0b\x32/.buf.validate.conformance.cases.MapMax.ValEntryB\t\xfa\xf7\x18\x05\x9a\x01\x02\x10\x03R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\x03R\x03key\x12\x14\n\x05value\x18\x02 \x01(\x01R\x05value:\x02\x38\x01"\x96\x01\n\tMapMinMax\x12Q\n\x03val\x18\x01 \x03(\x0b\x32\x32.buf.validate.conformance.cases.MapMinMax.ValEntryB\x0b\xfa\xf7\x18\x07\x9a\x01\x04\x08\x02\x10\x04R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x08R\x05value:\x02\x38\x01"\x94\x01\n\x08MapExact\x12P\n\x03val\x18\x01 \x03(\x0b\x32\x31.buf.validate.conformance.cases.MapExact.ValEntryB\x0b\xfa\xf7\x18\x07\x9a\x01\x04\x08\x03\x10\x03R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\x04R\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01"\x94\x01\n\x07MapKeys\x12Q\n\x03val\x18\x01 \x03(\x0b\x32\x30.buf.validate.conformance.cases.MapKeys.ValEntryB\r\xfa\xf7\x18\t\x9a\x01\x06"\x04\x42\x02\x10\x00R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\x12R\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01"\x98\x01\n\tMapValues\x12S\n\x03val\x18\x01 \x03(\x0b\x32\x32.buf.validate.conformance.cases.MapValues.ValEntryB\r\xfa\xf7\x18\t\x9a\x01\x06*\x04r\x02\x10\x03R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01"\xb1\x01\n\x0eMapKeysPattern\x12g\n\x03val\x18\x01 \x03(\x0b\x32\x37.buf.validate.conformance.cases.MapKeysPattern.ValEntryB\x1c\xfa\xf7\x18\x18\x9a\x01\x15"\x13r\x11\x32\x0f(?i)^[a-z0-9]+$R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01"\xb5\x01\n\x10MapValuesPattern\x12i\n\x03val\x18\x01 \x03(\x0b\x32\x39.buf.validate.conformance.cases.MapValuesPattern.ValEntryB\x1c\xfa\xf7\x18\x18\x9a\x01\x15*\x13r\x11\x32\x0f(?i)^[a-z0-9]+$R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01"\xe4\x01\n\x0cMapRecursive\x12G\n\x03val\x18\x01 \x03(\x0b\x32\x35.buf.validate.conformance.cases.MapRecursive.ValEntryR\x03val\x1ah\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\rR\x03key\x12\x46\n\x05value\x18\x02 \x01(\x0b\x32\x30.buf.validate.conformance.cases.MapRecursive.MsgR\x05value:\x02\x38\x01\x1a!\n\x03Msg\x12\x1a\n\x03val\x18\x01 \x01(\tB\x08\xfa\xf7\x18\x04r\x02\x10\x03R\x03val"\xa3\x01\n\x0eMapExactIgnore\x12Y\n\x03val\x18\x01 \x03(\x0b\x32\x37.buf.validate.conformance.cases.MapExactIgnore.ValEntryB\x0e\xfa\xf7\x18\n\x9a\x01\x04\x08\x03\x10\x03\xd0\x01\x01R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\x04R\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01"\xda\x03\n\x0cMultipleMaps\x12\\\n\x05\x66irst\x18\x01 \x03(\x0b\x32\x37.buf.validate.conformance.cases.MultipleMaps.FirstEntryB\r\xfa\xf7\x18\t\x9a\x01\x06"\x04*\x02 \x00R\x05\x66irst\x12_\n\x06second\x18\x02 \x03(\x0b\x32\x38.buf.validate.conformance.cases.MultipleMaps.SecondEntryB\r\xfa\xf7\x18\t\x9a\x01\x06"\x04\x1a\x02\x10\x00R\x06second\x12\\\n\x05third\x18\x03 \x03(\x0b\x32\x37.buf.validate.conformance.cases.MultipleMaps.ThirdEntryB\r\xfa\xf7\x18\t\x9a\x01\x06"\x04\x1a\x02 \x00R\x05third\x1a\x38\n\nFirstEntry\x12\x10\n\x03key\x18\x01 \x01(\rR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x1a\x39\n\x0bSecondEntry\x12\x10\n\x03key\x18\x01 \x01(\x05R\x03key\x12\x14\n\x05value\x18\x02 \x01(\x08R\x05value:\x02\x38\x01\x1a\x38\n\nThirdEntry\x12\x10\n\x03key\x18\x01 \x01(\x05R\x03key\x12\x14\n\x05value\x18\x02 \x01(\x08R\x05value:\x02\x38\x01\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "buf.validate.conformance.cases.maps_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _MAPNONE_VALENTRY._options = None
    _MAPNONE_VALENTRY._serialized_options = b"8\001"
    _MAPMIN_VALENTRY._options = None
    _MAPMIN_VALENTRY._serialized_options = b"8\001"
    _MAPMIN.fields_by_name["val"]._options = None
    _MAPMIN.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\005\232\001\002\010\002"
    _MAPMAX_VALENTRY._options = None
    _MAPMAX_VALENTRY._serialized_options = b"8\001"
    _MAPMAX.fields_by_name["val"]._options = None
    _MAPMAX.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\005\232\001\002\020\003"
    _MAPMINMAX_VALENTRY._options = None
    _MAPMINMAX_VALENTRY._serialized_options = b"8\001"
    _MAPMINMAX.fields_by_name["val"]._options = None
    _MAPMINMAX.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\007\232\001\004\010\002\020\004"
    _MAPEXACT_VALENTRY._options = None
    _MAPEXACT_VALENTRY._serialized_options = b"8\001"
    _MAPEXACT.fields_by_name["val"]._options = None
    _MAPEXACT.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\007\232\001\004\010\003\020\003"
    _MAPKEYS_VALENTRY._options = None
    _MAPKEYS_VALENTRY._serialized_options = b"8\001"
    _MAPKEYS.fields_by_name["val"]._options = None
    _MAPKEYS.fields_by_name[
        "val"
    ]._serialized_options = b'\372\367\030\t\232\001\006"\004B\002\020\000'
    _MAPVALUES_VALENTRY._options = None
    _MAPVALUES_VALENTRY._serialized_options = b"8\001"
    _MAPVALUES.fields_by_name["val"]._options = None
    _MAPVALUES.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\t\232\001\006*\004r\002\020\003"
    _MAPKEYSPATTERN_VALENTRY._options = None
    _MAPKEYSPATTERN_VALENTRY._serialized_options = b"8\001"
    _MAPKEYSPATTERN.fields_by_name["val"]._options = None
    _MAPKEYSPATTERN.fields_by_name[
        "val"
    ]._serialized_options = (
        b'\372\367\030\030\232\001\025"\023r\0212\017(?i)^[a-z0-9]+$'
    )
    _MAPVALUESPATTERN_VALENTRY._options = None
    _MAPVALUESPATTERN_VALENTRY._serialized_options = b"8\001"
    _MAPVALUESPATTERN.fields_by_name["val"]._options = None
    _MAPVALUESPATTERN.fields_by_name[
        "val"
    ]._serialized_options = (
        b"\372\367\030\030\232\001\025*\023r\0212\017(?i)^[a-z0-9]+$"
    )
    _MAPRECURSIVE_VALENTRY._options = None
    _MAPRECURSIVE_VALENTRY._serialized_options = b"8\001"
    _MAPRECURSIVE_MSG.fields_by_name["val"]._options = None
    _MAPRECURSIVE_MSG.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\004r\002\020\003"
    _MAPEXACTIGNORE_VALENTRY._options = None
    _MAPEXACTIGNORE_VALENTRY._serialized_options = b"8\001"
    _MAPEXACTIGNORE.fields_by_name["val"]._options = None
    _MAPEXACTIGNORE.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\n\232\001\004\010\003\020\003\320\001\001"
    _MULTIPLEMAPS_FIRSTENTRY._options = None
    _MULTIPLEMAPS_FIRSTENTRY._serialized_options = b"8\001"
    _MULTIPLEMAPS_SECONDENTRY._options = None
    _MULTIPLEMAPS_SECONDENTRY._serialized_options = b"8\001"
    _MULTIPLEMAPS_THIRDENTRY._options = None
    _MULTIPLEMAPS_THIRDENTRY._serialized_options = b"8\001"
    _MULTIPLEMAPS.fields_by_name["first"]._options = None
    _MULTIPLEMAPS.fields_by_name[
        "first"
    ]._serialized_options = b'\372\367\030\t\232\001\006"\004*\002 \000'
    _MULTIPLEMAPS.fields_by_name["second"]._options = None
    _MULTIPLEMAPS.fields_by_name[
        "second"
    ]._serialized_options = b'\372\367\030\t\232\001\006"\004\032\002\020\000'
    _MULTIPLEMAPS.fields_by_name["third"]._options = None
    _MULTIPLEMAPS.fields_by_name[
        "third"
    ]._serialized_options = b'\372\367\030\t\232\001\006"\004\032\002 \000'
    _globals["_MAPNONE"]._serialized_start = 107
    _globals["_MAPNONE"]._serialized_end = 240
    _globals["_MAPNONE_VALENTRY"]._serialized_start = 186
    _globals["_MAPNONE_VALENTRY"]._serialized_end = 240
    _globals["_MAPMIN"]._serialized_start = 243
    _globals["_MAPMIN"]._serialized_end = 385
    _globals["_MAPMIN_VALENTRY"]._serialized_start = 331
    _globals["_MAPMIN_VALENTRY"]._serialized_end = 385
    _globals["_MAPMAX"]._serialized_start = 388
    _globals["_MAPMAX"]._serialized_end = 530
    _globals["_MAPMAX_VALENTRY"]._serialized_start = 476
    _globals["_MAPMAX_VALENTRY"]._serialized_end = 530
    _globals["_MAPMINMAX"]._serialized_start = 533
    _globals["_MAPMINMAX"]._serialized_end = 683
    _globals["_MAPMINMAX_VALENTRY"]._serialized_start = 629
    _globals["_MAPMINMAX_VALENTRY"]._serialized_end = 683
    _globals["_MAPEXACT"]._serialized_start = 686
    _globals["_MAPEXACT"]._serialized_end = 834
    _globals["_MAPEXACT_VALENTRY"]._serialized_start = 780
    _globals["_MAPEXACT_VALENTRY"]._serialized_end = 834
    _globals["_MAPKEYS"]._serialized_start = 837
    _globals["_MAPKEYS"]._serialized_end = 985
    _globals["_MAPKEYS_VALENTRY"]._serialized_start = 931
    _globals["_MAPKEYS_VALENTRY"]._serialized_end = 985
    _globals["_MAPVALUES"]._serialized_start = 988
    _globals["_MAPVALUES"]._serialized_end = 1140
    _globals["_MAPVALUES_VALENTRY"]._serialized_start = 1086
    _globals["_MAPVALUES_VALENTRY"]._serialized_end = 1140
    _globals["_MAPKEYSPATTERN"]._serialized_start = 1143
    _globals["_MAPKEYSPATTERN"]._serialized_end = 1320
    _globals["_MAPKEYSPATTERN_VALENTRY"]._serialized_start = 1086
    _globals["_MAPKEYSPATTERN_VALENTRY"]._serialized_end = 1140
    _globals["_MAPVALUESPATTERN"]._serialized_start = 1323
    _globals["_MAPVALUESPATTERN"]._serialized_end = 1504
    _globals["_MAPVALUESPATTERN_VALENTRY"]._serialized_start = 1086
    _globals["_MAPVALUESPATTERN_VALENTRY"]._serialized_end = 1140
    _globals["_MAPRECURSIVE"]._serialized_start = 1507
    _globals["_MAPRECURSIVE"]._serialized_end = 1735
    _globals["_MAPRECURSIVE_VALENTRY"]._serialized_start = 1596
    _globals["_MAPRECURSIVE_VALENTRY"]._serialized_end = 1700
    _globals["_MAPRECURSIVE_MSG"]._serialized_start = 1702
    _globals["_MAPRECURSIVE_MSG"]._serialized_end = 1735
    _globals["_MAPEXACTIGNORE"]._serialized_start = 1738
    _globals["_MAPEXACTIGNORE"]._serialized_end = 1901
    _globals["_MAPEXACTIGNORE_VALENTRY"]._serialized_start = 780
    _globals["_MAPEXACTIGNORE_VALENTRY"]._serialized_end = 834
    _globals["_MULTIPLEMAPS"]._serialized_start = 1904
    _globals["_MULTIPLEMAPS"]._serialized_end = 2378
    _globals["_MULTIPLEMAPS_FIRSTENTRY"]._serialized_start = 2205
    _globals["_MULTIPLEMAPS_FIRSTENTRY"]._serialized_end = 2261
    _globals["_MULTIPLEMAPS_SECONDENTRY"]._serialized_start = 2263
    _globals["_MULTIPLEMAPS_SECONDENTRY"]._serialized_end = 2320
    _globals["_MULTIPLEMAPS_THIRDENTRY"]._serialized_start = 2322
    _globals["_MULTIPLEMAPS_THIRDENTRY"]._serialized_end = 2378
# @@protoc_insertion_point(module_scope)
