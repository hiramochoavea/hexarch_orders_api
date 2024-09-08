import pytest
from rest_framework import status
from rest_framework.test import APIClient
from typing import Callable
from ...items.infrastructure.models import ItemModel
from ...orders.infrastructure.models import OrderModel
from ...orders.domain.utils import calculate_price_totals


@pytest.mark.django_db
def test_edit_order(api_client: APIClient, reverse_url: Callable[[str, ...], str], initial_order: OrderModel, initial_item: ItemModel) -> None:
    """
    Tests the update of an order through the API.

    Args:
        api_client: The APIClient instance for making requests.
        reverse_url: The function for reversing URL names.
        initial_order: The initial OrderModel instance to update.
        initial_item: The initial ItemModel instance used in the update.

    Asserts:
        Response status code is 200 (OK).
        Response data contains the updated order details.
        Calculated total prices match the response.
    """

    # Define the updated payload
    payload = dict(
        items=[
            {
                "reference": initial_item.reference,
                "quantity": 3  # Update quantity to a different value
            }
        ]
    )

    # Make the PUT request to update the order
    url = reverse_url('order', kwargs={'order_id': initial_order.id})
    response = api_client.put(url, payload, format='json')

    # Get the response data
    data = response.data

    # Print the response data for debugging
    print(data)

    # Assert the response status code is 200 (OK)
    assert response.status_code == status.HTTP_200_OK

    # Verify the response contains the expected fields and values
    assert "id" in data
    assert "items" in data
    assert "total_price_without_tax" in data
    assert "total_price_with_tax" in data
    assert "created_at" in data

    # Verify that the response contains the updated order data
    assert len(data['items']) > 0
    assert data['items'][0]['reference'] == payload['items'][0]['reference']
    assert data['items'][0]['quantity'] == payload['items'][0]['quantity']

    # Calculate expected prices based on the updated payload
    items = [
        {
            "price_without_tax": initial_item.price_without_tax,
            "tax": initial_item.tax,
            "quantity": payload['items'][0]['quantity']
        }
    ]
    expected_total_price_without_tax, expected_total_price_with_tax = calculate_price_totals(
        items)

    # Assert the calculated total prices match the response
    assert abs(data['total_price_without_tax'] -
               expected_total_price_without_tax) < 0.01
    assert abs(data['total_price_with_tax'] -
               expected_total_price_with_tax) < 0.01
