from concurrent import futures
import grpc
import helloworld_pb2
import helloworld_pb2_grpc
from sklearn.linear_model import LinearRegression
import numpy as np

class LinearRegressionServicer(helloworld_pb2_grpc.LinearRegressionServicer):
    def TrainModel(self, request_iterator, context):
        for request in request_iterator:
            features = np.array(request.features).reshape(1, -1)
            label = np.array(request.label).reshape(1, -1)
            weights = np.array(request.weights).reshape(1, -1)

            model = LinearRegression()
            model.fit(features, label)

            predicted_values = model.predict(features)
            loss = np.mean((predicted_values - label) ** 2)

            updated_weights = np.array(weights)  # Some logic to update weights
            
            response = helloworld_pb2.TrainModelResponse(
                loss=loss,
                updated_weights=updated_weights.flatten().tolist()
            )
            yield response

def run_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_LinearRegressionServicer_to_server(LinearRegressionServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    run_server()

