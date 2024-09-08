from django.urls import include, path

urlpatterns = [
    path("api/", include("hexarch_orders_api.items.infrastructure.urls")),
    path("api/", include("hexarch_orders_api.orders.infrastructure.urls")),
]
