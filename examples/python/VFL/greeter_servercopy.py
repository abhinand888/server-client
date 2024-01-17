from concurrent import futures
import logging
import grpc
import VFL_pb2
import VFL_pb2_grpc
import threading

class Greeter(VFL_pb2_grpc.GreeterServicer):
    def __init__(self):
        self.lock = threading.Lock()
        self.clients = [0, 0]
        self.partial = [0.0, 0.0]

    def Aggregate(self, request_iterator, context):
        for request in request_iterator:
            with self.lock:
                if request.Id == 1:
                    self.clients[0] = 1
                    self.partial[0] = request.num
                else:
                    self.clients[1] = 1
                    self.partial[1] = request.num

                if all(client == 1 for client in self.clients):
                    self.clients = [0, 0]
                    yield VFL_pb2.loss(result=self.partial[0] + self.partial[1] - 10)

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

