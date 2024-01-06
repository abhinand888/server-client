import grpc
from concurrent import futures
import helloworld_pb2
import helloworld_pb2_grpc
from sklearn.linear_model import LinearRegression
import numpy as np

# Function for aggregating model updates (FedBCD logic)
def aggregate(global_weights, local_updates):
    # Implement FedBCD aggregation logic
    return np.mean(local_updates, axis=0)

class LinearRegressionServicer(helloworld_pb2_grpc.LinearRegressionServicer):
    def __init__(self):
        self.global_weights = np.zeros(10)  # Initialize global model weights

    def TrainModel(self, request_iterator, context):
        for request in request_iterator:
            features = np.array(request.features).reshape(1, -1)
            label = np.array(request.label).reshape(1, -1)
            weights = np.array(request.weights).reshape(1, -1)

            model = LinearRegression()
            model.fit(features, label)

            predicted_values = model.predict(features)
            loss = np.mean((predicted_values - label) ** 2)

            local_updates = np.array(weights)  # Extract local updates (e.g., weights)
            self.global_weights = aggregate(self.global_weights, local_updates)
            
            response = helloworld_pb2.TrainModelResponse(
                loss=loss,
                updated_weights=self.global_weights.flatten().tolist()
            )
            yield response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_LinearRegressionServicer_to_server(LinearRegressionServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

