from ninja import NinjaAPI
from service_b.views import router as order_router

api = NinjaAPI(
    title="Service B: Order Service API",
    version="1.0.0"
)

api.add_router("/orders/", order_router)
