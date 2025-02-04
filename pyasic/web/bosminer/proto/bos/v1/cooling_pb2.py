# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bos/v1/cooling.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ...bos.v1 import common_pb2 as bos_dot_v1_dot_common__pb2
from ...bos.v1 import constraints_pb2 as bos_dot_v1_dot_constraints__pb2
from ...bos.v1 import units_pb2 as bos_dot_v1_dot_units__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x14\x62os/v1/cooling.proto\x12\x0e\x62raiins.bos.v1\x1a\x13\x62os/v1/common.proto\x1a\x18\x62os/v1/constraints.proto\x1a\x12\x62os/v1/units.proto"\xbc\x01\n\x0f\x43oolingAutoMode\x12\x37\n\x12target_temperature\x18\x01 \x01(\x0b\x32\x1b.braiins.bos.v1.Temperature\x12\x34\n\x0fhot_temperature\x18\x02 \x01(\x0b\x32\x1b.braiins.bos.v1.Temperature\x12:\n\x15\x64\x61ngerous_temperature\x18\x03 \x01(\x0b\x32\x1b.braiins.bos.v1.Temperature"\xb7\x01\n\x11\x43oolingManualMode\x12\x1c\n\x0f\x66\x61n_speed_ratio\x18\x01 \x01(\x01H\x00\x88\x01\x01\x12\x34\n\x0fhot_temperature\x18\x02 \x01(\x0b\x32\x1b.braiins.bos.v1.Temperature\x12:\n\x15\x64\x61ngerous_temperature\x18\x03 \x01(\x0b\x32\x1b.braiins.bos.v1.TemperatureB\x12\n\x10_fan_speed_ratio"G\n\x13\x43oolingDisabledMode\x12\x1c\n\x0f\x66\x61n_speed_ratio\x18\x01 \x01(\x01H\x00\x88\x01\x01\x42\x12\n\x10_fan_speed_ratio"\xfb\x01\n\x14\x43oolingConfiguration\x12"\n\x15minimum_required_fans\x18\x01 \x01(\rH\x01\x88\x01\x01\x12/\n\x04\x61uto\x18\x02 \x01(\x0b\x32\x1f.braiins.bos.v1.CoolingAutoModeH\x00\x12\x33\n\x06manual\x18\x03 \x01(\x0b\x32!.braiins.bos.v1.CoolingManualModeH\x00\x12\x37\n\x08\x64isabled\x18\x04 \x01(\x0b\x32#.braiins.bos.v1.CoolingDisabledModeH\x00\x42\x06\n\x04modeB\x18\n\x16_minimum_required_fans"\x99\x03\n\x12\x43oolingConstraints\x12\x39\n\x14\x64\x65\x66\x61ult_cooling_mode\x18\x01 \x01(\x0e\x32\x1b.braiins.bos.v1.CoolingMode\x12\x42\n\x12target_temperature\x18\x02 \x01(\x0b\x32&.braiins.bos.v1.TemperatureConstraints\x12?\n\x0fhot_temperature\x18\x03 \x01(\x0b\x32&.braiins.bos.v1.TemperatureConstraints\x12\x45\n\x15\x64\x61ngerous_temperature\x18\x04 \x01(\x0b\x32&.braiins.bos.v1.TemperatureConstraints\x12:\n\x0f\x66\x61n_speed_ratio\x18\x05 \x01(\x0b\x32!.braiins.bos.v1.DoubleConstraints\x12@\n\x15minimum_required_fans\x18\x06 \x01(\x0b\x32!.braiins.bos.v1.UInt32Constraints"s\n\x08\x46\x61nState\x12\x15\n\x08position\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x0b\n\x03rpm\x18\x02 \x01(\r\x12\x1f\n\x12target_speed_ratio\x18\x03 \x01(\x01H\x01\x88\x01\x01\x42\x0b\n\t_positionB\x15\n\x13_target_speed_ratio"\x8f\x01\n\x11TemperatureSensor\x12\x0f\n\x02id\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x30\n\x08location\x18\x02 \x01(\x0e\x32\x1e.braiins.bos.v1.SensorLocation\x12\x30\n\x0btemperature\x18\x03 \x01(\x0b\x32\x1b.braiins.bos.v1.TemperatureB\x05\n\x03_id"\x18\n\x16GetCoolingStateRequest"\x81\x01\n\x17GetCoolingStateResponse\x12&\n\x04\x66\x61ns\x18\x01 \x03(\x0b\x32\x18.braiins.bos.v1.FanState\x12>\n\x13highest_temperature\x18\x02 \x01(\x0b\x32!.braiins.bos.v1.TemperatureSensor"i\n\x17SetImmersionModeRequest\x12/\n\x0bsave_action\x18\x01 \x01(\x0e\x32\x1a.braiins.bos.v1.SaveAction\x12\x1d\n\x15\x65nable_immersion_mode\x18\x02 \x01(\x08"2\n\x18SetImmersionModeResponse\x12\x16\n\x0eimmersion_mode\x18\x01 \x01(\x08*v\n\x0b\x43oolingMode\x12\x1c\n\x18\x43OOLING_MODE_UNSPECIFIED\x10\x00\x12\x15\n\x11\x43OOLING_MODE_AUTO\x10\x01\x12\x17\n\x13\x43OOLING_MODE_MANUAL\x10\x02\x12\x19\n\x15\x43OOLING_MODE_DISABLED\x10\x03*d\n\x0eSensorLocation\x12\x1f\n\x1bSENSOR_LOCATION_UNSPECIFIED\x10\x00\x12\x18\n\x14SENSOR_LOCATION_CHIP\x10\x01\x12\x17\n\x13SENSOR_LOCATION_PCB\x10\x02\x32\xdb\x01\n\x0e\x43oolingService\x12\x62\n\x0fGetCoolingState\x12&.braiins.bos.v1.GetCoolingStateRequest\x1a\'.braiins.bos.v1.GetCoolingStateResponse\x12\x65\n\x10SetImmersionMode\x12\'.braiins.bos.v1.SetImmersionModeRequest\x1a(.braiins.bos.v1.SetImmersionModeResponseb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "bos.v1.cooling_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_COOLINGMODE"]._serialized_start = 1803
    _globals["_COOLINGMODE"]._serialized_end = 1921
    _globals["_SENSORLOCATION"]._serialized_start = 1923
    _globals["_SENSORLOCATION"]._serialized_end = 2023
    _globals["_COOLINGAUTOMODE"]._serialized_start = 108
    _globals["_COOLINGAUTOMODE"]._serialized_end = 296
    _globals["_COOLINGMANUALMODE"]._serialized_start = 299
    _globals["_COOLINGMANUALMODE"]._serialized_end = 482
    _globals["_COOLINGDISABLEDMODE"]._serialized_start = 484
    _globals["_COOLINGDISABLEDMODE"]._serialized_end = 555
    _globals["_COOLINGCONFIGURATION"]._serialized_start = 558
    _globals["_COOLINGCONFIGURATION"]._serialized_end = 809
    _globals["_COOLINGCONSTRAINTS"]._serialized_start = 812
    _globals["_COOLINGCONSTRAINTS"]._serialized_end = 1221
    _globals["_FANSTATE"]._serialized_start = 1223
    _globals["_FANSTATE"]._serialized_end = 1338
    _globals["_TEMPERATURESENSOR"]._serialized_start = 1341
    _globals["_TEMPERATURESENSOR"]._serialized_end = 1484
    _globals["_GETCOOLINGSTATEREQUEST"]._serialized_start = 1486
    _globals["_GETCOOLINGSTATEREQUEST"]._serialized_end = 1510
    _globals["_GETCOOLINGSTATERESPONSE"]._serialized_start = 1513
    _globals["_GETCOOLINGSTATERESPONSE"]._serialized_end = 1642
    _globals["_SETIMMERSIONMODEREQUEST"]._serialized_start = 1644
    _globals["_SETIMMERSIONMODEREQUEST"]._serialized_end = 1749
    _globals["_SETIMMERSIONMODERESPONSE"]._serialized_start = 1751
    _globals["_SETIMMERSIONMODERESPONSE"]._serialized_end = 1801
    _globals["_COOLINGSERVICE"]._serialized_start = 2026
    _globals["_COOLINGSERVICE"]._serialized_end = 2245
# @@protoc_insertion_point(module_scope)
