# frozen_string_literal: true
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: src/proto/grpc/testing/report_qps_scenario_service.proto

require 'google/protobuf'

require 'src/proto/grpc/testing/control_pb'


descriptor_data = "\n8src/proto/grpc/testing/report_qps_scenario_service.proto\x12\x0cgrpc.testing\x1a$src/proto/grpc/testing/control.proto2^\n\x18ReportQpsScenarioService\x12\x42\n\x0eReportScenario\x12\x1c.grpc.testing.ScenarioResult\x1a\x12.grpc.testing.Voidb\x06proto3"

pool = Google::Protobuf::DescriptorPool.generated_pool

begin
  pool.add_serialized_file(descriptor_data)
rescue TypeError
  # Compatibility code: will be removed in the next major version.
  require 'google/protobuf/descriptor_pb'
  parsed = Google::Protobuf::FileDescriptorProto.decode(descriptor_data)
  parsed.clear_dependency
  serialized = parsed.class.encode(parsed)
  file = pool.add_serialized_file(serialized)
  warn "Warning: Protobuf detected an import path issue while loading generated file #{__FILE__}"
  imports = [
  ]
  imports.each do |type_name, expected_filename|
    import_file = pool.lookup(type_name).file_descriptor
    if import_file.name != expected_filename
      warn "- #{file.name} imports #{expected_filename}, but that import was loaded as #{import_file.name}"
    end
  end
  warn "Each proto file must use a consistent fully-qualified name."
  warn "This will become an error in the next major version."
end

module Grpc
  module Testing
  end
end
