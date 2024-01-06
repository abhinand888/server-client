import grpc
from concurrent import futures
import helloworld_pb2  # Assuming this contains necessary message definitions
import helloworld_pb2_grpc  # Assuming this contains necessary gRPC service definitions

class PartyAServicer(helloworld_pb2_grpc.PartyAServicer):
    def SendEncryptedGradients(self, request, context):
        # Simulating processing received gradients and sending encrypted gradients
        encrypted_gradients = [gradient + 10 for gradient in request.gradients]
        return helloworld_pb2.EncryptedGradients(gradients=encrypted_gradients)

def run_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_PartyAServicer_to_server(PartyAServicer(), server)
    server.add_insecure_port('[::]:50051')  # Specify the server port
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    run_server()

