import pytest
from typing import Callable
from rest_framework.test import APIClient
from django.urls import reverse
from ..items.infrastructure.models import ItemModel
from ..orders.domain.entities.order import Order
from ..orders.infrastructure.models import OrderModel, OrderItemModel
from ..orders.domain.utils import calculate_price_totals


@pytest.fixture
def api_client() -> APIClient:
    """
    Fixture that provides an instance of APIClient for making HTTP requests in tests.
    """
    return APIClient()


@pytest.fixture
def reverse_url() -> Callable[[str, tuple, dict], str]:
    """
    Fixture that provides a function to reverse URL names into actual URLs.

    Args:
        name: The name of the URL pattern.
        *args: Positional arguments for URL pattern.
        **kwargs: Keyword arguments for URL pattern.

    Returns:
        A function that reverses URL names into actual URLs.
    """
    def _reverse_url(name, *args, **kwargs):
        return reverse(name, *args, **kwargs)
    return _reverse_url


@pytest.fixture
def initial_item(db) -> ItemModel:
    """
    Fixture that creates and returns an initial ItemModel instance with realistic attributes.

    Args:
        db: The Django database fixture to ensure the database is available.

    Returns:
        An ItemModel instance.
    """

    item_obj = ItemModel.objects.create(
        reference="SM-S23",
        name="Samsung Galaxy S23",
        description="The latest Samsung Galaxy S23 with a 6.1-inch display, 128GB storage, and 5G support.",
        price_without_tax=849.99,
        tax=21
    )
    return item_obj


@pytest.fixture
def initial_order(db, initial_item: ItemModel) -> Order:
    """
    Fixture that creates and returns an initial OrderModel instance with one item.

    Args:
        db: The Django database fixture to ensure the database is available.
        initial_item: The initial ItemModel instance to include in the order.

    Returns:
        An OrderModel instance with the specified item.
    """

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

    total_price_without_tax, total_price_with_tax = calculate_price_totals(
        items_info)

    order.total_price_without_tax = total_price_without_tax
    order.total_price_with_tax = total_price_with_tax
    order.save()

    return order
