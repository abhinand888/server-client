# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging

import grpc
import helloworld_pb2
import helloworld_pb2_grpc



def run():
    # Establish an insecure gRPC channel with the server
#    with grpc.insecure_channel('172.16.88.251:50051') as channel:
    with grpc.insecure_channel('172.16.88.245:50051') as channel:
        
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        
       
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
        print("Greeter client received: " + response.message)
        
        response = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name='you'))
        print("Greeter client received: " + response.message)
        
        N1 = 14
        N2 = 16
        
       
        response = stub.SendSum(helloworld_pb2.ArithRequest(Num1=N1, Num2=N2, Id=1))
        print("Greeter sum received: " + str(response.Result))
        
        response = stub.SendDiff(helloworld_pb2.ArithRequest(Num1=N1, Num2=N2, Id=1))
        print("Greeter Difference received: " + str(response.Result))

if __name__ == "__main__":
    logging.basicConfig()
    run()
