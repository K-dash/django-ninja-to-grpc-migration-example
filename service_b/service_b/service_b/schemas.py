from ninja import Schema

class OrderRequest(Schema):
    user_id: int

class UserInfo(Schema):
    id: int
    name: str
    email: str

class OrderResponse(Schema):
    order_id: str
    user_info: UserInfo
