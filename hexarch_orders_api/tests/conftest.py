# conftest.py
import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from ..items.infrastructure.models import ItemModel
from ..orders.infrastructure.models import OrderModel, OrderItemModel
from ..orders.domain.utils import calculate_price_totals

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
    quantity = 70
    order = OrderModel.objects.create()
    OrderItemModel.objects.create(
        order=order,
        item=initial_item,
        quantity=quantity
    )
    
    items_info = [
        {
            'price_without_tax': initial_item.price_without_tax,
            'tax': initial_item.tax,
            'quantity': quantity
        }
    ]
    
    total_price_without_tax, total_price_with_tax = calculate_price_totals(items_info)
    
    order.total_price_without_tax = total_price_without_tax
    order.total_price_with_tax = total_price_with_tax
    order.save()

    return order
