from ninja import Schema

class UserRequest(Schema):
    user_id: int

class UserResponse(Schema):
    id: int
    name: str
    email: str



