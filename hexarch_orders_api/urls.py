from django.urls import path, include

urlpatterns = [
    path('api/', include('hexarch_orders_api.items.infrastructure.urls')),
    path('api/', include('hexarch_orders_api.orders.infrastructure.urls')),
]