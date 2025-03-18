import grpc
from concurrent import futures

from service_a.grpc.stubs import service_a_pb2_grpc
from service_a.grpc.services.user_service import UserServiceImpl


def serve(port: int = 50051):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # 上で定義したUserServiceImplをサーバに登録
    service_a_pb2_grpc.add_UserServiceServicer_to_server(
        UserServiceImpl(), server
    )

    server.add_insecure_port(f"[::]:{port}")
    server.start()
    print("gRPC server started on port 50051.")
    server.wait_for_termination()
