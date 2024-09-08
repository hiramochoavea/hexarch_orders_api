import pytest
from rest_framework import status
from rest_framework.test import APIClient
from typing import Callable
from ...items.infrastructure.models import ItemModel


@pytest.mark.django_db
def test_get_item_by_id(api_client: APIClient, reverse_url: Callable[[str, ...], str], initial_item: ItemModel) -> None:
    """
    Tests retrieving an item by its ID through the API.

    Args:
        api_client: The APIClient instance for making requests.
        reverse_url: The function for reversing URL names.
        initial_item: The initial ItemModel instance to retrieve.

    Asserts:
        Response status code is 200 (OK).
        Response data matches the initial item.
    """

    # Make the GET request to retrieve the item by its ID
    url = reverse_url('item', kwargs={'item_id': initial_item.id})
    response = api_client.get(url)

    # Get the response data
    item = response.data

    # Assert the response status code is 200 (OK)
    assert response.status_code == status.HTTP_200_OK

    # Verify that the response contains the item created in the fixture
    assert item['id'] == initial_item.id
    assert item['reference'] == initial_item.reference
    assert item['name'] == initial_item.name
    assert item['description'] == initial_item.description
    assert item['price_without_tax'] == initial_item.price_without_tax
    assert item['tax'] == initial_item.tax
