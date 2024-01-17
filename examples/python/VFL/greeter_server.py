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
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc
import VFL_pb2
import VFL_pb2_grpc

from threading import Lock
from threading import Condition

class Greeter(VFL_pb2_grpc.GreeterServicer):
#    Clients = [0,0]
    Partial = [0.0,0.0]
    lock1 = Lock()
    lock2 = Lock()
    condition = Condition()

    remaining=0
#    lock2 = Lock()
    
    def Aggregate(self,request_iterator, context):
#        barrier = threading.Barrier(2)
        for request in request_iterator:
          if self.remaining == 0:
              with self.lock2:
                 self.remaining=2 
          if request.Id == 1:
#             self.Clients[0] = 1
             self.Partial[0] = request.num
             with self.lock1:
                self.remaining-=1
          else:
#             self.Clients[1] = 2
             self.Partial[1] = request.num                
#          with lock1:
#            while self.Clients[0] == 0 or self.Clients[1] == 0:
#               pass            
             with self.lock1:
                self.remaining-=1

          if self.remaining>0:
               with self.condition:
                    self.condition.wait() 
          else:
               with self.condition:
                    self.condition.notify()          
#          if self.remaining == 0:
#              with self.lock1:
#                 self.remaining=2 

#          breakpoint()
#          barrier.wait() 
        # Create and return the response using the appropriate response message type
#        return helloworld_pb2.ArithReply(Result=request.Num1 + request.Num2, Id=request.Id)
#        return VFL_pb2.ArithReply(Result=sum(self.Nums)/4)
#          self.Clients = [0,0]
          yield  VFL_pb2.loss(result=self.Partial[0]+self.Partial[1]-10)
    



    
def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    VFL_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
