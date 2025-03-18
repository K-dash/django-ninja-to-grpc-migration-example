# import requests
import grpc
from ninja import Router, Query
from service_b.schemas import OrderRequest, OrderResponse, UserInfo
from service_b.grpc.stubs import service_a_pb2_grpc, service_a_pb2

router = Router()

@router.get("/", response=OrderResponse)
def get_order_info(request, order_req: OrderRequest = Query(...)):

    # # Service A へのREST APIリクエストを廃止
    # service_a_endpoint = "http://localhost:8000/api/users"

    # resp = requests.get(
    #     service_a_endpoint,
    #     params={"user_id": order_req.user_id}
    # )
    # resp.raise_for_status()

    # user_data = resp.json()

    # # UserInfoオブジェクトを作成
    # user_info = UserInfo(
    #     id=user_data["id"],
    #     name=user_data["name"],
    #     email=user_data["email"]
    # )

    # gRPC 接続先（service_a）へのチャンネルを作成
    with grpc.insecure_channel("host.docker.internal:50051") as channel:
        # クライアントを作成
        stub = service_a_pb2_grpc.UserServiceStub(channel)

        # gRPC リクエスト作成
        grpc_request = service_a_pb2.GetUserRequest(
            user_id=order_req.user_id
        )

        # RPC呼び出し -> ユーザ情報を取得
        grpc_response = stub.GetUser(grpc_request)

    user_info = UserInfo(
        id=grpc_response.id,
        name=grpc_response.name,
        email=grpc_response.email
    )

    # OrderResponseオブジェクトを作成して返す
    return OrderResponse(
        order_id=f"ORDER_{order_req.user_id}",
        user_info=user_info
    )
