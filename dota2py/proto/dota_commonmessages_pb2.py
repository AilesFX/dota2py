# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import google.protobuf.descriptor_pb2
import netmessages_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='dota_commonmessages.proto',
  package='',
  serialized_pb='\n\x19\x64ota_commonmessages.proto\x1a google/protobuf/descriptor.proto\x1a\x11netmessages.proto\"R\n\x15\x43\x44OTAMsg_LocationPing\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\x0e\n\x06target\x18\x03 \x01(\x05\x12\x13\n\x0b\x64irect_ping\x18\x04 \x01(\x08\"9\n\x10\x43\x44OTAMsg_MapLine\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\x0f\n\x07initial\x18\x03 \x01(\x08\x42\x05H\x01\x80\x01\x00')




_CDOTAMSG_LOCATIONPING = descriptor.Descriptor(
  name='CDOTAMsg_LocationPing',
  full_name='CDOTAMsg_LocationPing',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='x', full_name='CDOTAMsg_LocationPing.x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='y', full_name='CDOTAMsg_LocationPing.y', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='target', full_name='CDOTAMsg_LocationPing.target', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='direct_ping', full_name='CDOTAMsg_LocationPing.direct_ping', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=82,
  serialized_end=164,
)


_CDOTAMSG_MAPLINE = descriptor.Descriptor(
  name='CDOTAMsg_MapLine',
  full_name='CDOTAMsg_MapLine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='x', full_name='CDOTAMsg_MapLine.x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='y', full_name='CDOTAMsg_MapLine.y', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='initial', full_name='CDOTAMsg_MapLine.initial', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=166,
  serialized_end=223,
)

DESCRIPTOR.message_types_by_name['CDOTAMsg_LocationPing'] = _CDOTAMSG_LOCATIONPING
DESCRIPTOR.message_types_by_name['CDOTAMsg_MapLine'] = _CDOTAMSG_MAPLINE

class CDOTAMsg_LocationPing(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CDOTAMSG_LOCATIONPING
  
  # @@protoc_insertion_point(class_scope:CDOTAMsg_LocationPing)

class CDOTAMsg_MapLine(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CDOTAMSG_MAPLINE
  
  # @@protoc_insertion_point(class_scope:CDOTAMsg_MapLine)

# @@protoc_insertion_point(module_scope)
