# gRPCのサービス実装クラス
from service_a.grpc.stubs import service_a_pb2_grpc, service_a_pb2

from service_a.views import get_user_info_logic

class UserServiceImpl(service_a_pb2_grpc.UserServiceServicer):
    """
    gRPCのサービス実装クラス
    service_a_pb2_grpc.UserServiceServicerを継承して service_a.proto で定義したメソッドを実装する
    """
    def GetUser(self, request, context):
        """
        proto定義: rpc GetUser(GetUserRequest) returns (UserResponse);
        -> request: GetUserRequest, context: RPCのコンテキスト情報
        """
        user_id = request.user_id

        # ビジネスロジック（DB参照など）はここで行う想定
        # 既存のビジネスロジックはviews.pyに実装しているので、それを呼び出す
        user_data = get_user_info_logic(user_id)
        print(f"User data: {user_data}")

        # 成功時はレスポンスメッセージをreturnする
        return service_a_pb2.UserResponse(
            id=user_data.id,
            name=user_data.name,
            email=user_data.email
        )
