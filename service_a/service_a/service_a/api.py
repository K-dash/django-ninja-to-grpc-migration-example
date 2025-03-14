from ninja import NinjaAPI
from service_a.views import router as user_router

api = NinjaAPI(
    title="Service A: User Management API",
    version="1.0.0"
)

# ユーザ管理用のルーターを "/users" というパスにまとめる
api.add_router("/users/", user_router)
