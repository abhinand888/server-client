import grpc
import helloworld_pb2
import helloworld_pb2_grpc

def run_client():
    # Establishing a channel to the gRPC server
    with grpc.insecure_channel('localhost:50051') as channel:
        # Creating a stub (client) for interacting with the server
        stub = helloworld_pb2_grpc.PartyAStub(channel)

        # Simulated gradients (from Party B's perspective)
        gradients = [5, 8, 10, 12]  # Placeholder gradients

        # Creating a gRPC request with gradients data
        request = helloworld_pb2.Gradients(gradients=gradients)

        # Sending gradients to Party A (Server) and getting a response
        try:
            response = stub.SendEncryptedGradients(request)
            print("Received encrypted gradients from Party A:", response.gradients)
        except grpc.RpcError as e:
            print(f"Error in RPC: {e.details()}")

if __name__ == '__main__':
    run_client()

