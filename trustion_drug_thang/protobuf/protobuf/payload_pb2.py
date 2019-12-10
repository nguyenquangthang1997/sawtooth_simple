# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/payload.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protobuf/payload.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16protobuf/payload.proto\"\xe8\x02\n\x13SimpleSupplyPayload\x12+\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\x1b.SimpleSupplyPayload.Action\x12\x11\n\ttimestamp\x18\x02 \x01(\x04\x12!\n\x0b\x63reate_user\x18\x03 \x01(\x0b\x32\x0c.Create_User\x12 \n\x0b\x64rug_import\x18\x04 \x01(\x0b\x32\x0b.DrugImport\x12\x1a\n\x08get_drug\x18\x05 \x01(\x0b\x32\x08.GetDrug\x12$\n\rupdate_status\x18\x06 \x01(\x0b\x32\r.UpdateStatus\x12(\n\x0fupdate_location\x18\x07 \x01(\x0b\x32\x0f.UpdateLocation\"`\n\x06\x41\x63tion\x12\x0f\n\x0b\x43REATE_USER\x10\x00\x12\x0f\n\x0b\x44RUG_IMPORT\x10\x01\x12\x0c\n\x08GET_DRUG\x10\x02\x12\x11\n\rUPDATE_STATUS\x10\x03\x12\x13\n\x0fUPDATE_LOCATION\x10\x04\"[\n\nDrugImport\x12\x1e\n\x04role\x18\x01 \x01(\x0e\x32\x10.DrugImport.Role\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"\x13\n\x04Role\x12\x0b\n\x07PATIENT\x10\x00\"\x15\n\x07GetDrug\x12\n\n\x02id\x18\x01 \x01(\t\"r\n\x0cUpdateStatus\x12 \n\x04role\x18\x01 \x01(\x0e\x32\x12.UpdateStatus.Role\x12\n\n\x02id\x18\x02 \x01(\t\x12\x10\n\x08quantity\x18\x03 \x01(\t\x12\r\n\x05price\x18\x04 \x01(\t\"\x13\n\x04Role\x12\x0b\n\x07PATIENT\x10\x00\"z\n\x0eUpdateLocation\x12\"\n\x04role\x18\x01 \x01(\x0e\x32\x14.UpdateLocation.Role\x12\n\n\x02id\x18\x02 \x01(\t\x12\x11\n\tlongitude\x18\x03 \x01(\t\x12\x10\n\x08latitude\x18\x04 \x01(\t\"\x13\n\x04Role\x12\x0b\n\x07PATIENT\x10\x00\"r\n\x0b\x43reate_User\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x1f\n\x04role\x18\x02 \x01(\x0e\x32\x11.Create_User.Role\"0\n\x04Role\x12\x10\n\x0cSTOKE_KEEPER\x10\x00\x12\t\n\x05NURSE\x10\x01\x12\x0b\n\x07PATIENT\x10\x02\x62\x06proto3')
)



_SIMPLESUPPLYPAYLOAD_ACTION = _descriptor.EnumDescriptor(
  name='Action',
  full_name='SimpleSupplyPayload.Action',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CREATE_USER', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DRUG_IMPORT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_DRUG', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_STATUS', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_LOCATION', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=291,
  serialized_end=387,
)
_sym_db.RegisterEnumDescriptor(_SIMPLESUPPLYPAYLOAD_ACTION)

_DRUGIMPORT_ROLE = _descriptor.EnumDescriptor(
  name='Role',
  full_name='DrugImport.Role',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PATIENT', index=0, number=0,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=461,
  serialized_end=480,
)
_sym_db.RegisterEnumDescriptor(_DRUGIMPORT_ROLE)

_UPDATESTATUS_ROLE = _descriptor.EnumDescriptor(
  name='Role',
  full_name='UpdateStatus.Role',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PATIENT', index=0, number=0,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=461,
  serialized_end=480,
)
_sym_db.RegisterEnumDescriptor(_UPDATESTATUS_ROLE)

_UPDATELOCATION_ROLE = _descriptor.EnumDescriptor(
  name='Role',
  full_name='UpdateLocation.Role',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PATIENT', index=0, number=0,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=461,
  serialized_end=480,
)
_sym_db.RegisterEnumDescriptor(_UPDATELOCATION_ROLE)

_CREATE_USER_ROLE = _descriptor.EnumDescriptor(
  name='Role',
  full_name='Create_User.Role',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STOKE_KEEPER', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NURSE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PATIENT', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=811,
  serialized_end=859,
)
_sym_db.RegisterEnumDescriptor(_CREATE_USER_ROLE)


_SIMPLESUPPLYPAYLOAD = _descriptor.Descriptor(
  name='SimpleSupplyPayload',
  full_name='SimpleSupplyPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='SimpleSupplyPayload.action', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='SimpleSupplyPayload.timestamp', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_user', full_name='SimpleSupplyPayload.create_user', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='drug_import', full_name='SimpleSupplyPayload.drug_import', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_drug', full_name='SimpleSupplyPayload.get_drug', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_status', full_name='SimpleSupplyPayload.update_status', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_location', full_name='SimpleSupplyPayload.update_location', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SIMPLESUPPLYPAYLOAD_ACTION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=387,
)


_DRUGIMPORT = _descriptor.Descriptor(
  name='DrugImport',
  full_name='DrugImport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='role', full_name='DrugImport.role', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='DrugImport.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='DrugImport.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DRUGIMPORT_ROLE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=389,
  serialized_end=480,
)


_GETDRUG = _descriptor.Descriptor(
  name='GetDrug',
  full_name='GetDrug',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='GetDrug.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=482,
  serialized_end=503,
)


_UPDATESTATUS = _descriptor.Descriptor(
  name='UpdateStatus',
  full_name='UpdateStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='role', full_name='UpdateStatus.role', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='UpdateStatus.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='UpdateStatus.quantity', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='UpdateStatus.price', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _UPDATESTATUS_ROLE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=505,
  serialized_end=619,
)


_UPDATELOCATION = _descriptor.Descriptor(
  name='UpdateLocation',
  full_name='UpdateLocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='role', full_name='UpdateLocation.role', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='UpdateLocation.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='UpdateLocation.longitude', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='UpdateLocation.latitude', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _UPDATELOCATION_ROLE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=621,
  serialized_end=743,
)


_CREATE_USER = _descriptor.Descriptor(
  name='Create_User',
  full_name='Create_User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='Create_User.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role', full_name='Create_User.role', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CREATE_USER_ROLE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=745,
  serialized_end=859,
)

_SIMPLESUPPLYPAYLOAD.fields_by_name['action'].enum_type = _SIMPLESUPPLYPAYLOAD_ACTION
_SIMPLESUPPLYPAYLOAD.fields_by_name['create_user'].message_type = _CREATE_USER
_SIMPLESUPPLYPAYLOAD.fields_by_name['drug_import'].message_type = _DRUGIMPORT
_SIMPLESUPPLYPAYLOAD.fields_by_name['get_drug'].message_type = _GETDRUG
_SIMPLESUPPLYPAYLOAD.fields_by_name['update_status'].message_type = _UPDATESTATUS
_SIMPLESUPPLYPAYLOAD.fields_by_name['update_location'].message_type = _UPDATELOCATION
_SIMPLESUPPLYPAYLOAD_ACTION.containing_type = _SIMPLESUPPLYPAYLOAD
_DRUGIMPORT.fields_by_name['role'].enum_type = _DRUGIMPORT_ROLE
_DRUGIMPORT_ROLE.containing_type = _DRUGIMPORT
_UPDATESTATUS.fields_by_name['role'].enum_type = _UPDATESTATUS_ROLE
_UPDATESTATUS_ROLE.containing_type = _UPDATESTATUS
_UPDATELOCATION.fields_by_name['role'].enum_type = _UPDATELOCATION_ROLE
_UPDATELOCATION_ROLE.containing_type = _UPDATELOCATION
_CREATE_USER.fields_by_name['role'].enum_type = _CREATE_USER_ROLE
_CREATE_USER_ROLE.containing_type = _CREATE_USER
DESCRIPTOR.message_types_by_name['SimpleSupplyPayload'] = _SIMPLESUPPLYPAYLOAD
DESCRIPTOR.message_types_by_name['DrugImport'] = _DRUGIMPORT
DESCRIPTOR.message_types_by_name['GetDrug'] = _GETDRUG
DESCRIPTOR.message_types_by_name['UpdateStatus'] = _UPDATESTATUS
DESCRIPTOR.message_types_by_name['UpdateLocation'] = _UPDATELOCATION
DESCRIPTOR.message_types_by_name['Create_User'] = _CREATE_USER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SimpleSupplyPayload = _reflection.GeneratedProtocolMessageType('SimpleSupplyPayload', (_message.Message,), {
  'DESCRIPTOR' : _SIMPLESUPPLYPAYLOAD,
  '__module__' : 'protobuf.payload_pb2'
  # @@protoc_insertion_point(class_scope:SimpleSupplyPayload)
  })
_sym_db.RegisterMessage(SimpleSupplyPayload)

DrugImport = _reflection.GeneratedProtocolMessageType('DrugImport', (_message.Message,), {
  'DESCRIPTOR' : _DRUGIMPORT,
  '__module__' : 'protobuf.payload_pb2'
  # @@protoc_insertion_point(class_scope:DrugImport)
  })
_sym_db.RegisterMessage(DrugImport)

GetDrug = _reflection.GeneratedProtocolMessageType('GetDrug', (_message.Message,), {
  'DESCRIPTOR' : _GETDRUG,
  '__module__' : 'protobuf.payload_pb2'
  # @@protoc_insertion_point(class_scope:GetDrug)
  })
_sym_db.RegisterMessage(GetDrug)

UpdateStatus = _reflection.GeneratedProtocolMessageType('UpdateStatus', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESTATUS,
  '__module__' : 'protobuf.payload_pb2'
  # @@protoc_insertion_point(class_scope:UpdateStatus)
  })
_sym_db.RegisterMessage(UpdateStatus)

UpdateLocation = _reflection.GeneratedProtocolMessageType('UpdateLocation', (_message.Message,), {
  'DESCRIPTOR' : _UPDATELOCATION,
  '__module__' : 'protobuf.payload_pb2'
  # @@protoc_insertion_point(class_scope:UpdateLocation)
  })
_sym_db.RegisterMessage(UpdateLocation)

Create_User = _reflection.GeneratedProtocolMessageType('Create_User', (_message.Message,), {
  'DESCRIPTOR' : _CREATE_USER,
  '__module__' : 'protobuf.payload_pb2'
  # @@protoc_insertion_point(class_scope:Create_User)
  })
_sym_db.RegisterMessage(Create_User)


# @@protoc_insertion_point(module_scope)