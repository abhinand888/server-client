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
"""The Python implementation of the GRPC VFL.Greeter client."""

from __future__ import print_function

import logging

import grpc
import VFL_pb2
import VFL_pb2_grpc

#def getpartialsum():
#    for i in range(101,200):
#      yield (VFL_pb2.partialsum(num=i,Id=1))

#def getpartialsum(i):
#      yield (VFL_pb2.partialsum(num=i,Id=2))

def getpartialsum():
    for i in range(100001,200001):
      yield (VFL_pb2.partialsum(num=i,Id=2))

def run():
    # Establish an insecure gRPC channel with the server
    with grpc.insecure_channel('127.0.0.1:50051') as channel:
#    with grpc.insecure_channel('127.0.0.1:50051') as channel:
#        n1 = 1,n2 = 11,n3 = 21,n4 = 31
         stub = VFL_pb2_grpc.GreeterStub(channel)
#         breakpoint()
#        response = stub.Aggregate(VFL_pb2.ArithRequest(Num1=N1, Num2=N2, Id=1))
#        print("Greeter sum received: " + str(response.Result))
#         response = stub.Aggregate(VFL_pb2.partialsum(num=20,Id=2))         


#         partialiterator=getpartialsum(100)
#         response = stub.Aggregate(partialiterator)         
#         for i in response:
#                 print("Loss i= "+ str(i.result))
#                 response2 = stub.Aggregate(getpartialsum(i.result))         
#                 for j in response2:
#                    print("Loss j= "+ str(j.result))
 

         partialiterator=getpartialsum()
         response = stub.Aggregate(partialiterator)         
         counter=0
         for i in response:
              counter+=1
              if counter > 99990:
                  print("Loss = "+ str(i.result))

                 
if __name__ == "__main__":
    logging.basicConfig()
    run()
