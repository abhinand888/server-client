# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: VFLcopy.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rVFLcopy.proto\x12\nhelloworld\"%\n\npartialsum\x12\x0b\n\x03num\x18\x01 \x01(\x02\x12\n\n\x02Id\x18\x02 \x01(\x05\"\x16\n\x04loss\x12\x0e\n\x06result\x18\x01 \x01(\x02\x32\x46\n\x07Greeter\x12;\n\tAggregate\x12\x16.helloworld.partialsum\x1a\x10.helloworld.loss\"\x00(\x01\x30\x01\x42\x36\n\x1bio.grpc.examples.helloworldB\x0fHelloWorldProtoP\x01\xa2\x02\x03HLWb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'VFLcopy_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033io.grpc.examples.helloworldB\017HelloWorldProtoP\001\242\002\003HLW'
  _globals['_PARTIALSUM']._serialized_start=29
  _globals['_PARTIALSUM']._serialized_end=66
  _globals['_LOSS']._serialized_start=68
  _globals['_LOSS']._serialized_end=90
  _globals['_GREETER']._serialized_start=92
  _globals['_GREETER']._serialized_end=162
# @@protoc_insertion_point(module_scope)
