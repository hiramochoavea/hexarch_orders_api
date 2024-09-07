from django.urls import path
from .views import OrderAPIView

urlpatterns = [
    path('orders/', OrderAPIView.as_view(), name='orders'),
    path('orders/<int:order_id>/', OrderAPIView.as_view(), name='order'),
]
