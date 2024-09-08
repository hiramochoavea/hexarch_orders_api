import pytest
from rest_framework import status
from rest_framework.test import APIClient
from typing import Callable
from ...orders.domain.utils import calculate_price_totals
from ...items.infrastructure.models import ItemModel


@pytest.mark.django_db
def test_create_order(api_client: APIClient, reverse_url: Callable[[str, ...], str], initial_item: ItemModel) -> None:
    """
    Tests the creation of an order through the API.

    Args:
        api_client: The APIClient instance for making requests.
        reverse_url: The function for reversing URL names.
        initial_item: The initial ItemModel instance to include in the order.

    Asserts:
        Response status code is 201 (Created).
        Response data contains the expected fields and values.
        Calculated total prices match the response.
    """

    payload = dict(
        items=[
            {
                "reference": initial_item.reference,
                "quantity": 2
            }
        ]
    )

    # Make the POST request to create an order
    response = api_client.post(reverse_url('orders'), payload, format='json')

    # Get the response data
    data = response.data

    # Assert the response status code is 201 (Created)
    assert response.status_code == status.HTTP_201_CREATED

    # Verify the response contains the expected fields and values
    assert "id" in data
    assert "items" in data
    assert "total_price_without_tax" in data
    assert "total_price_with_tax" in data
    assert "created_at" in data

    # Verify that the response contains the correct order data
    assert len(data['items']) > 0
    assert data['items'][0]['reference'] == payload['items'][0]['reference']
    assert data['items'][0]['quantity'] == payload['items'][0]['quantity']
    
    # Calculate expected prices based on the provided payload
    items = [
        {
            "price_without_tax": initial_item.price_without_tax,
            "tax": initial_item.tax,
            "quantity": payload['items'][0]['quantity']
        }
    ]
    expected_total_price_without_tax, expected_total_price_with_tax = calculate_price_totals(items)

    # Assert the calculated total prices match the response
    assert abs(data['total_price_without_tax'] - expected_total_price_without_tax) < 0.01
    assert abs(data['total_price_with_tax'] - expected_total_price_with_tax) < 0.01
