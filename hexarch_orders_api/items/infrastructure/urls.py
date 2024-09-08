from django.urls import path

from .views import ItemDetailView, ItemListView

urlpatterns = [
    path("", ItemListView.as_view(), name="items"),
    path("<int:item_id>/", ItemDetailView.as_view(), name="item"),
]
