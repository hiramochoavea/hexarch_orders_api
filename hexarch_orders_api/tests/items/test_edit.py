import pytest
from rest_framework import status
from rest_framework.test import APIClient
from typing import Callable
from ...items.infrastructure.models import ItemModel


@pytest.mark.django_db
def test_edit_item(api_client: APIClient, reverse_url: Callable[[str, ...], str], initial_item: ItemModel) -> None:
    """
    Tests the update of an item through the API.

    Args:
        api_client: The APIClient instance for making requests.
        reverse_url: The function for reversing URL names.
        initial_item: The initial ItemModel instance to update.

    Asserts:
        Response status code is 200 (OK).
        Response data matches the updated payload.
    """

    # Define the payload with updated data
    updated_payload = dict(
        reference="PHN2024",
        name="Updated Smartphone",
        description="An updated description for the high-end smartphone.",
        price_without_tax=899.99,
        tax=23
    )

    # Make the PUT request to update the item by its ID
    url = reverse_url('item', kwargs={'item_id': initial_item.id})
    response = api_client.put(url, updated_payload, format='json')

    # Get the response data
    item = response.data

    # Assert the response status code is 200 (OK)
    assert response.status_code == status.HTTP_200_OK

    # Verify that the response contains the updated item data
    assert item['id'] == initial_item.id
    assert item['reference'] == updated_payload['reference']
    assert item['name'] == updated_payload['name']
    assert item['description'] == updated_payload['description']
    assert item['price_without_tax'] == updated_payload['price_without_tax']
    assert item['tax'] == updated_payload['tax']
