from django.urls import path
from .views import ItemAPIView

urlpatterns = [
    path('items/', ItemAPIView.as_view(), name='items'),
    path('items/<int:item_id>/', ItemAPIView.as_view(), name='item'),
]
