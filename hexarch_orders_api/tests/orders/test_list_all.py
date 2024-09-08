import pytest
from rest_framework import status
from rest_framework.test import APIClient
from typing import Callable
from ...orders.infrastructure.models import OrderModel


@pytest.mark.django_db
def test_list_all_orders(api_client: APIClient, reverse_url: Callable[[str, ...], str], initial_order: OrderModel) -> None:
    """
    Tests listing all orders through the API.

    Args:
        api_client: The APIClient instance for making requests.
        reverse_url: The function for reversing URL names.
        initial_order: The initial OrderModel instance to ensure it is included in the list.

    Asserts:
        Response status code is 200 (OK).
        Response data contains the initial order details.
    """

    # Make the GET request to list all orders
    response = api_client.get(reverse_url('orders'))

    # Get the response data
    orders = response.data

    # Assert the response status code is 200 (OK)
    assert response.status_code == status.HTTP_200_OK

    # Verify that the response contains the order created in the fixture
    assert len(orders) > 0
    assert any(order['id'] == initial_order.id for order in orders)
    assert any(
        any(item['reference'] == initial_order.items.first(
        ).reference for item in order['items'])
        for order in orders
    )

    # Check total prices with an absolute tolerance for floating-point comparison
    assert any(
        abs(order['total_price_without_tax'] -
            initial_order.total_price_without_tax) < 0.01
        for order in orders
    )
    assert any(
        abs(order['total_price_with_tax'] -
            initial_order.total_price_with_tax) < 0.01
        for order in orders
    )
