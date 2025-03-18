from ninja import Router, Query
from service_a.schemas import UserRequest, UserResponse

router = Router()

def get_user_info_logic(user_id: int) -> UserResponse:
    """他の場所でも呼べる適当なビジネスロジックを想定"""
    return UserResponse(
        id=user_id,
        name=f"User_{user_id}",
        email=f"user_{user_id}@example.com"
    )


@router.get("/", response=UserResponse)
def get_user_info(request, user: UserRequest = Query(...)):
    get_user_info_logic(user.user_id)
