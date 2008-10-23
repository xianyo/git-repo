#!/usr/bin/python2.4
# Generated by the protocol buffer compiler.  DO NOT EDIT!

from froofle.protobuf import descriptor
from froofle.protobuf import message
from froofle.protobuf import reflection
from froofle.protobuf import service
from froofle.protobuf import service_reflection


_FIELDDESCRIPTORPROTO_TYPE = descriptor.EnumDescriptor(
  name='Type',
  full_name='froofle.protobuf.FieldDescriptorProto.Type',
  filename='Type',
  values=[
    descriptor.EnumValueDescriptor(
      name='TYPE_DOUBLE', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TYPE_FLOAT', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TYPE_INT64', index=2, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TYPE_UINT64', index=3, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TYPE_INT32', index=4, number=5,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TYPE_FIXED64', index=5, number=6,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TYPE_FIXED32', index=6, number=7,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TYPE_BOOL', index=7, number=8,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TYPE_STRING', index=8, number=9,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TYPE_GROUP', index=9, number=10,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TYPE_MESSAGE', index=10, number=11,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TYPE_BYTES', index=11, number=12,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TYPE_UINT32', index=12, number=13,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TYPE_ENUM', index=13, number=14,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TYPE_SFIXED32', index=14, number=15,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TYPE_SFIXED64', index=15, number=16,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TYPE_SINT32', index=16, number=17,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TYPE_SINT64', index=17, number=18,
      options=None,
      type=None),
  ],
  options=None,
)

_FIELDDESCRIPTORPROTO_LABEL = descriptor.EnumDescriptor(
  name='Label',
  full_name='froofle.protobuf.FieldDescriptorProto.Label',
  filename='Label',
  values=[
    descriptor.EnumValueDescriptor(
      name='LABEL_OPTIONAL', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='LABEL_REQUIRED', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='LABEL_REPEATED', index=2, number=3,
      options=None,
      type=None),
  ],
  options=None,
)

_FILEOPTIONS_OPTIMIZEMODE = descriptor.EnumDescriptor(
  name='OptimizeMode',
  full_name='froofle.protobuf.FileOptions.OptimizeMode',
  filename='OptimizeMode',
  values=[
    descriptor.EnumValueDescriptor(
      name='SPEED', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='CODE_SIZE', index=1, number=2,
      options=None,
      type=None),
  ],
  options=None,
)

_FIELDOPTIONS_CTYPE = descriptor.EnumDescriptor(
  name='CType',
  full_name='froofle.protobuf.FieldOptions.CType',
  filename='CType',
  values=[
    descriptor.EnumValueDescriptor(
      name='CORD', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='STRING_PIECE', index=1, number=2,
      options=None,
      type=None),
  ],
  options=None,
)


_FILEDESCRIPTORSET = descriptor.Descriptor(
  name='FileDescriptorSet',
  full_name='froofle.protobuf.FileDescriptorSet',
  filename='froofle/protobuf/descriptor.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='file', full_name='froofle.protobuf.FileDescriptorSet.file', index=0,
      number=1, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_FILEDESCRIPTORPROTO = descriptor.Descriptor(
  name='FileDescriptorProto',
  full_name='froofle.protobuf.FileDescriptorProto',
  filename='froofle/protobuf/descriptor.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='froofle.protobuf.FileDescriptorProto.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='package', full_name='froofle.protobuf.FileDescriptorProto.package', index=1,
      number=2, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='dependency', full_name='froofle.protobuf.FileDescriptorProto.dependency', index=2,
      number=3, type=9, cpp_type=9, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message_type', full_name='froofle.protobuf.FileDescriptorProto.message_type', index=3,
      number=4, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='enum_type', full_name='froofle.protobuf.FileDescriptorProto.enum_type', index=4,
      number=5, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='service', full_name='froofle.protobuf.FileDescriptorProto.service', index=5,
      number=6, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='extension', full_name='froofle.protobuf.FileDescriptorProto.extension', index=6,
      number=7, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='options', full_name='froofle.protobuf.FileDescriptorProto.options', index=7,
      number=8, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_DESCRIPTORPROTO_EXTENSIONRANGE = descriptor.Descriptor(
  name='ExtensionRange',
  full_name='froofle.protobuf.DescriptorProto.ExtensionRange',
  filename='froofle/protobuf/descriptor.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='start', full_name='froofle.protobuf.DescriptorProto.ExtensionRange.start', index=0,
      number=1, type=5, cpp_type=1, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='end', full_name='froofle.protobuf.DescriptorProto.ExtensionRange.end', index=1,
      number=2, type=5, cpp_type=1, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)

_DESCRIPTORPROTO = descriptor.Descriptor(
  name='DescriptorProto',
  full_name='froofle.protobuf.DescriptorProto',
  filename='froofle/protobuf/descriptor.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='froofle.protobuf.DescriptorProto.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='field', full_name='froofle.protobuf.DescriptorProto.field', index=1,
      number=2, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='extension', full_name='froofle.protobuf.DescriptorProto.extension', index=2,
      number=6, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='nested_type', full_name='froofle.protobuf.DescriptorProto.nested_type', index=3,
      number=3, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='enum_type', full_name='froofle.protobuf.DescriptorProto.enum_type', index=4,
      number=4, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='extension_range', full_name='froofle.protobuf.DescriptorProto.extension_range', index=5,
      number=5, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='options', full_name='froofle.protobuf.DescriptorProto.options', index=6,
      number=7, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_FIELDDESCRIPTORPROTO = descriptor.Descriptor(
  name='FieldDescriptorProto',
  full_name='froofle.protobuf.FieldDescriptorProto',
  filename='froofle/protobuf/descriptor.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='froofle.protobuf.FieldDescriptorProto.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='number', full_name='froofle.protobuf.FieldDescriptorProto.number', index=1,
      number=3, type=5, cpp_type=1, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='label', full_name='froofle.protobuf.FieldDescriptorProto.label', index=2,
      number=4, type=14, cpp_type=8, label=1,
      default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='froofle.protobuf.FieldDescriptorProto.type', index=3,
      number=5, type=14, cpp_type=8, label=1,
      default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type_name', full_name='froofle.protobuf.FieldDescriptorProto.type_name', index=4,
      number=6, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='extendee', full_name='froofle.protobuf.FieldDescriptorProto.extendee', index=5,
      number=2, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='default_value', full_name='froofle.protobuf.FieldDescriptorProto.default_value', index=6,
      number=7, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='options', full_name='froofle.protobuf.FieldDescriptorProto.options', index=7,
      number=8, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
    _FIELDDESCRIPTORPROTO_TYPE,
    _FIELDDESCRIPTORPROTO_LABEL,
  ],
  options=None)


_ENUMDESCRIPTORPROTO = descriptor.Descriptor(
  name='EnumDescriptorProto',
  full_name='froofle.protobuf.EnumDescriptorProto',
  filename='froofle/protobuf/descriptor.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='froofle.protobuf.EnumDescriptorProto.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value', full_name='froofle.protobuf.EnumDescriptorProto.value', index=1,
      number=2, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='options', full_name='froofle.protobuf.EnumDescriptorProto.options', index=2,
      number=3, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_ENUMVALUEDESCRIPTORPROTO = descriptor.Descriptor(
  name='EnumValueDescriptorProto',
  full_name='froofle.protobuf.EnumValueDescriptorProto',
  filename='froofle/protobuf/descriptor.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='froofle.protobuf.EnumValueDescriptorProto.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='number', full_name='froofle.protobuf.EnumValueDescriptorProto.number', index=1,
      number=2, type=5, cpp_type=1, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='options', full_name='froofle.protobuf.EnumValueDescriptorProto.options', index=2,
      number=3, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_SERVICEDESCRIPTORPROTO = descriptor.Descriptor(
  name='ServiceDescriptorProto',
  full_name='froofle.protobuf.ServiceDescriptorProto',
  filename='froofle/protobuf/descriptor.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='froofle.protobuf.ServiceDescriptorProto.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='method', full_name='froofle.protobuf.ServiceDescriptorProto.method', index=1,
      number=2, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='options', full_name='froofle.protobuf.ServiceDescriptorProto.options', index=2,
      number=3, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_METHODDESCRIPTORPROTO = descriptor.Descriptor(
  name='MethodDescriptorProto',
  full_name='froofle.protobuf.MethodDescriptorProto',
  filename='froofle/protobuf/descriptor.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='froofle.protobuf.MethodDescriptorProto.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='input_type', full_name='froofle.protobuf.MethodDescriptorProto.input_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='output_type', full_name='froofle.protobuf.MethodDescriptorProto.output_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='options', full_name='froofle.protobuf.MethodDescriptorProto.options', index=3,
      number=4, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_FILEOPTIONS = descriptor.Descriptor(
  name='FileOptions',
  full_name='froofle.protobuf.FileOptions',
  filename='froofle/protobuf/descriptor.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='java_package', full_name='froofle.protobuf.FileOptions.java_package', index=0,
      number=1, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='java_outer_classname', full_name='froofle.protobuf.FileOptions.java_outer_classname', index=1,
      number=8, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='java_multiple_files', full_name='froofle.protobuf.FileOptions.java_multiple_files', index=2,
      number=10, type=8, cpp_type=7, label=1,
      default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='optimize_for', full_name='froofle.protobuf.FileOptions.optimize_for', index=3,
      number=9, type=14, cpp_type=8, label=1,
      default_value=2,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='uninterpreted_option', full_name='froofle.protobuf.FileOptions.uninterpreted_option', index=4,
      number=999, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
    _FILEOPTIONS_OPTIMIZEMODE,
  ],
  options=None)


_MESSAGEOPTIONS = descriptor.Descriptor(
  name='MessageOptions',
  full_name='froofle.protobuf.MessageOptions',
  filename='froofle/protobuf/descriptor.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='message_set_wire_format', full_name='froofle.protobuf.MessageOptions.message_set_wire_format', index=0,
      number=1, type=8, cpp_type=7, label=1,
      default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='uninterpreted_option', full_name='froofle.protobuf.MessageOptions.uninterpreted_option', index=1,
      number=999, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_FIELDOPTIONS = descriptor.Descriptor(
  name='FieldOptions',
  full_name='froofle.protobuf.FieldOptions',
  filename='froofle/protobuf/descriptor.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ctype', full_name='froofle.protobuf.FieldOptions.ctype', index=0,
      number=1, type=14, cpp_type=8, label=1,
      default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='experimental_map_key', full_name='froofle.protobuf.FieldOptions.experimental_map_key', index=1,
      number=9, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='uninterpreted_option', full_name='froofle.protobuf.FieldOptions.uninterpreted_option', index=2,
      number=999, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
    _FIELDOPTIONS_CTYPE,
  ],
  options=None)


_ENUMOPTIONS = descriptor.Descriptor(
  name='EnumOptions',
  full_name='froofle.protobuf.EnumOptions',
  filename='froofle/protobuf/descriptor.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='uninterpreted_option', full_name='froofle.protobuf.EnumOptions.uninterpreted_option', index=0,
      number=999, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_ENUMVALUEOPTIONS = descriptor.Descriptor(
  name='EnumValueOptions',
  full_name='froofle.protobuf.EnumValueOptions',
  filename='froofle/protobuf/descriptor.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='uninterpreted_option', full_name='froofle.protobuf.EnumValueOptions.uninterpreted_option', index=0,
      number=999, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_SERVICEOPTIONS = descriptor.Descriptor(
  name='ServiceOptions',
  full_name='froofle.protobuf.ServiceOptions',
  filename='froofle/protobuf/descriptor.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='uninterpreted_option', full_name='froofle.protobuf.ServiceOptions.uninterpreted_option', index=0,
      number=999, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_METHODOPTIONS = descriptor.Descriptor(
  name='MethodOptions',
  full_name='froofle.protobuf.MethodOptions',
  filename='froofle/protobuf/descriptor.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='uninterpreted_option', full_name='froofle.protobuf.MethodOptions.uninterpreted_option', index=0,
      number=999, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_UNINTERPRETEDOPTION_NAMEPART = descriptor.Descriptor(
  name='NamePart',
  full_name='froofle.protobuf.UninterpretedOption.NamePart',
  filename='froofle/protobuf/descriptor.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name_part', full_name='froofle.protobuf.UninterpretedOption.NamePart.name_part', index=0,
      number=1, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_extension', full_name='froofle.protobuf.UninterpretedOption.NamePart.is_extension', index=1,
      number=2, type=8, cpp_type=7, label=2,
      default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)

_UNINTERPRETEDOPTION = descriptor.Descriptor(
  name='UninterpretedOption',
  full_name='froofle.protobuf.UninterpretedOption',
  filename='froofle/protobuf/descriptor.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='froofle.protobuf.UninterpretedOption.name', index=0,
      number=2, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='identifier_value', full_name='froofle.protobuf.UninterpretedOption.identifier_value', index=1,
      number=3, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='positive_int_value', full_name='froofle.protobuf.UninterpretedOption.positive_int_value', index=2,
      number=4, type=4, cpp_type=4, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='negative_int_value', full_name='froofle.protobuf.UninterpretedOption.negative_int_value', index=3,
      number=5, type=3, cpp_type=2, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='double_value', full_name='froofle.protobuf.UninterpretedOption.double_value', index=4,
      number=6, type=1, cpp_type=5, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='string_value', full_name='froofle.protobuf.UninterpretedOption.string_value', index=5,
      number=7, type=12, cpp_type=9, label=1,
      default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_FILEDESCRIPTORSET.fields_by_name['file'].message_type = _FILEDESCRIPTORPROTO
_FILEDESCRIPTORPROTO.fields_by_name['message_type'].message_type = _DESCRIPTORPROTO
_FILEDESCRIPTORPROTO.fields_by_name['enum_type'].message_type = _ENUMDESCRIPTORPROTO
_FILEDESCRIPTORPROTO.fields_by_name['service'].message_type = _SERVICEDESCRIPTORPROTO
_FILEDESCRIPTORPROTO.fields_by_name['extension'].message_type = _FIELDDESCRIPTORPROTO
_FILEDESCRIPTORPROTO.fields_by_name['options'].message_type = _FILEOPTIONS
_DESCRIPTORPROTO.fields_by_name['field'].message_type = _FIELDDESCRIPTORPROTO
_DESCRIPTORPROTO.fields_by_name['extension'].message_type = _FIELDDESCRIPTORPROTO
_DESCRIPTORPROTO.fields_by_name['nested_type'].message_type = _DESCRIPTORPROTO
_DESCRIPTORPROTO.fields_by_name['enum_type'].message_type = _ENUMDESCRIPTORPROTO
_DESCRIPTORPROTO.fields_by_name['extension_range'].message_type = _DESCRIPTORPROTO_EXTENSIONRANGE
_DESCRIPTORPROTO.fields_by_name['options'].message_type = _MESSAGEOPTIONS
_FIELDDESCRIPTORPROTO.fields_by_name['label'].enum_type = _FIELDDESCRIPTORPROTO_LABEL
_FIELDDESCRIPTORPROTO.fields_by_name['type'].enum_type = _FIELDDESCRIPTORPROTO_TYPE
_FIELDDESCRIPTORPROTO.fields_by_name['options'].message_type = _FIELDOPTIONS
_ENUMDESCRIPTORPROTO.fields_by_name['value'].message_type = _ENUMVALUEDESCRIPTORPROTO
_ENUMDESCRIPTORPROTO.fields_by_name['options'].message_type = _ENUMOPTIONS
_ENUMVALUEDESCRIPTORPROTO.fields_by_name['options'].message_type = _ENUMVALUEOPTIONS
_SERVICEDESCRIPTORPROTO.fields_by_name['method'].message_type = _METHODDESCRIPTORPROTO
_SERVICEDESCRIPTORPROTO.fields_by_name['options'].message_type = _SERVICEOPTIONS
_METHODDESCRIPTORPROTO.fields_by_name['options'].message_type = _METHODOPTIONS
_FILEOPTIONS.fields_by_name['optimize_for'].enum_type = _FILEOPTIONS_OPTIMIZEMODE
_FILEOPTIONS.fields_by_name['uninterpreted_option'].message_type = _UNINTERPRETEDOPTION
_MESSAGEOPTIONS.fields_by_name['uninterpreted_option'].message_type = _UNINTERPRETEDOPTION
_FIELDOPTIONS.fields_by_name['ctype'].enum_type = _FIELDOPTIONS_CTYPE
_FIELDOPTIONS.fields_by_name['uninterpreted_option'].message_type = _UNINTERPRETEDOPTION
_ENUMOPTIONS.fields_by_name['uninterpreted_option'].message_type = _UNINTERPRETEDOPTION
_ENUMVALUEOPTIONS.fields_by_name['uninterpreted_option'].message_type = _UNINTERPRETEDOPTION
_SERVICEOPTIONS.fields_by_name['uninterpreted_option'].message_type = _UNINTERPRETEDOPTION
_METHODOPTIONS.fields_by_name['uninterpreted_option'].message_type = _UNINTERPRETEDOPTION
_UNINTERPRETEDOPTION.fields_by_name['name'].message_type = _UNINTERPRETEDOPTION_NAMEPART

class FileDescriptorSet(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FILEDESCRIPTORSET

class FileDescriptorProto(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FILEDESCRIPTORPROTO

class DescriptorProto(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class ExtensionRange(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _DESCRIPTORPROTO_EXTENSIONRANGE
  DESCRIPTOR = _DESCRIPTORPROTO

class FieldDescriptorProto(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FIELDDESCRIPTORPROTO

class EnumDescriptorProto(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ENUMDESCRIPTORPROTO

class EnumValueDescriptorProto(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ENUMVALUEDESCRIPTORPROTO

class ServiceDescriptorProto(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SERVICEDESCRIPTORPROTO

class MethodDescriptorProto(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _METHODDESCRIPTORPROTO

class FileOptions(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FILEOPTIONS

class MessageOptions(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MESSAGEOPTIONS

class FieldOptions(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FIELDOPTIONS

class EnumOptions(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ENUMOPTIONS

class EnumValueOptions(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ENUMVALUEOPTIONS

class ServiceOptions(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SERVICEOPTIONS

class MethodOptions(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _METHODOPTIONS

class UninterpretedOption(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class NamePart(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _UNINTERPRETEDOPTION_NAMEPART
  DESCRIPTOR = _UNINTERPRETEDOPTION
