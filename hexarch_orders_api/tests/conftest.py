# conftest.py
import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from ..items.infrastructure.models import ItemModel
from ..orders.infrastructure.models import OrderModel, OrderItemModel

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def reverse_url():
    def _reverse_url(name, *args, **kwargs):
        return reverse(name, *args, **kwargs)
    return _reverse_url

@pytest.fixture
def initial_item(db):
    # Create an item (phone) with realistic attributes
    item_obj = ItemModel.objects.create(
        reference="SM-S23",
        name="Samsung Galaxy S23",
        description="The latest Samsung Galaxy S23 with a 6.1-inch display, 128GB storage, and 5G support.",
        price_without_tax=849.99,
        tax=21
    )
    return item_obj

@pytest.fixture
def initial_order(db, initial_item):
    # Create an order with one item
    order = OrderModel.objects.create()
    OrderItemModel.objects.create(
        order=order,
        item=initial_item,
        quantity=70
    )
    
    order.total_price_without_tax = initial_item.price_without_tax * 70
    order.total_price_with_tax = (initial_item.price_without_tax * (1 + initial_item.tax / 100)) * 70
    order.save()

    return order
