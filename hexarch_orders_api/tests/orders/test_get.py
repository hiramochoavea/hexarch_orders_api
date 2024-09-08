import pytest
from rest_framework import status
from rest_framework.test import APIClient
from typing import Callable
from ...orders.infrastructure.models import OrderModel


@pytest.mark.django_db
def test_get_order_by_id(api_client: APIClient, reverse_url: Callable[[str, ...], str], initial_order: OrderModel) -> None:
    """
    Tests retrieving an order by its ID through the API.

    Args:
        api_client: The APIClient instance for making requests.
        reverse_url: The function for reversing URL names.
        initial_order: The initial OrderModel instance to retrieve.

    Asserts:
        Response status code is 200 (OK).
        Response data matches the initial order details.
    """

    # Define the URL for the specific order by its ID
    url = reverse_url('order', kwargs={'order_id': initial_order.id})

    # Make the GET request to fetch the order by its ID
    response = api_client.get(url)

    # Get the response data
    order = response.data

    # Assert the response status code is 200 (OK)
    assert response.status_code == status.HTTP_200_OK

    # Verify that the response contains the correct order data
    assert order['id'] == initial_order.id

    first_item_on_order = initial_order.items.first()

    assert any(
        item['reference'] == first_item_on_order.reference and
        item['quantity'] == first_item_on_order.item_orders.first().quantity
        for item in order['items']
    )
    assert abs(order['total_price_without_tax'] -
               initial_order.total_price_without_tax) < 0.01
    assert abs(order['total_price_with_tax'] -
               initial_order.total_price_with_tax) < 0.01
