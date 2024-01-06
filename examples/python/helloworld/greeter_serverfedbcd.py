import grpc
import helloworld_pb2
import helloworld_pb2_grpc
import numpy as np
import grpc
from concurrent import futures  


class LinearRegressionServicer(helloworld_pb2_grpc.LinearRegressionServicer):
    def __init__(self):
        # Initialize global weights for FedBCD
        self.global_weights = np.zeros(10)  # Assuming 10 weights for demonstration
        
    def TrainModel(self, request_iterator, context):
        for request in request_iterator:
            features = np.array(request.features).reshape(1, -1)
            label = np.array(request.label).reshape(1, -1)
            weights = np.array(request.weights).reshape(1, -1)

            # Use features from both clients for training
            combined_features = np.concatenate((features, self.global_weights.reshape(1, -1)), axis=1)

            # Some logic to update weights using FedBCD algorithm
            updated_weights = self.fedbcd_update(combined_features, label, weights)

            # Update global weights for next iteration
            self.global_weights = updated_weights.flatten()

            response = helloworld_pb2.TrainModelResponse(
                loss=0,  # Placeholder for loss calculation in FedBCD
                updated_weights=updated_weights.flatten().tolist()
            )
            yield response

    def fedbcd_update(self, features, label, weights):
       # write actual algorithm
        return weights + 0.1

def run_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_LinearRegressionServicer_to_server(LinearRegressionServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    run_server()

