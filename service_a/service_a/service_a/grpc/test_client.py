import grpc
from service_a.grpc.stubs import service_a_pb2_grpc, service_a_pb2

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = service_a_pb2_grpc.UserServiceStub(channel)
        request = service_a_pb2.GetUserRequest(user_id=123)
        response = stub.GetUser(request)
        print("Received:", response)

if __name__ == "__main__":
    run()
