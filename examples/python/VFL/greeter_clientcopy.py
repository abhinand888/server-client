import logging
import grpc
import VFL_pb2
import VFL_pb2_grpc

def get_partial_sum():
    for i in [1.0, 11.0, 21.0, 31.0]:
        yield VFL_pb2.partialsum(num=i, Id=1)

def run():
    with grpc.insecure_channel('127.0.0.1:50051') as channel:
        stub = VFL_pb2_grpc.GreeterStub(channel)
        partial_iterator = get_partial_sum()
        response = stub.Aggregate(partial_iterator)
        for i in response:
            print("Loss = " + str(i.result))

if __name__ == "__main__":
    logging.basicConfig()
    run()
