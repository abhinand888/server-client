import grpc
import helloworld_pb2
import helloworld_pb2_grpc
import numpy as np
from sklearn.linear_model import LinearRegression

def generate_random_data():
    # Generate random features and weights
    features = [np.random.uniform(0, 1) for _ in range(10)]
    weights = [np.random.uniform(0, 1) for _ in range(10)]

    # Common label for both clients
    label = np.random.uniform(0, 1)
    
    return features, weights, label

def run_client():
    channel = grpc.insecure_channel('172.16.88.245:50051')
    stub = helloworld_pb2_grpc.LinearRegressionStub(channel)

    for _ in range(10):  # Sending 10 requests
        features, weights, label = generate_random_data()

        request = helloworld_pb2.TrainModelRequest(
            features=features,
            label=label,
            weights=weights
        )

        response_iterator = stub.TrainModel(iter([request]))
        for response in response_iterator:
            print(f"Loss: {response.loss}, Updated Weights: {response.updated_weights}")

if __name__ == '__main__':
    run_client()

