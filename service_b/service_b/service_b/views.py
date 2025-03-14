import requests
from ninja import Router, Query
from service_b.schemas import OrderRequest, OrderResponse, UserInfo

router = Router()

@router.get("/", response=OrderResponse)
def get_order_info(request, order_req: OrderRequest = Query(...)):

    service_a_endpoint = "http://localhost:8000/api/users"

    resp = requests.get(
        service_a_endpoint,
        params={"user_id": order_req.user_id}
    )
    resp.raise_for_status()

    user_data = resp.json()

    # UserInfoオブジェクトを作成
    user_info = UserInfo(
        id=user_data["id"],
        name=user_data["name"],
        email=user_data["email"]
    )

    # OrderResponseオブジェクトを作成して返す
    return OrderResponse(
        order_id=f"ORDER_{order_req.user_id}",
        user_info=user_info
    )
