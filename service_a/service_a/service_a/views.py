from ninja import Router, Query
from service_a.schemas import UserRequest, UserResponse

router = Router()

@router.get("/", response=UserResponse)
def get_user_info(request, user: UserRequest = Query(...)):
    return UserResponse(
        id=user.user_id,
        name=f"User_{user.user_id}",
        email=f"user_{user.user_id}@example.com"
    )
