import pytest
from rest_framework import status
from rest_framework.test import APIClient
from typing import Callable
from ...items.infrastructure.models import ItemModel

@pytest.mark.django_db
def test_list_all_items(api_client: APIClient, reverse_url: Callable[[str, ...], str], initial_item: ItemModel) -> None:
    """
    Tests listing all items through the API.

    Args:
        api_client: The APIClient instance for making requests.
        reverse_url: The function for reversing URL names.
        initial_item: The initial ItemModel instance to ensure it is included in the list.

    Asserts:
        Response status code is 200 (OK).
        Response data contains the initial item.
    """

    # Make the GET request to list all items
    response = api_client.get(reverse_url('items'))

    # Get the response data
    items = response.data

    # Assert the response status code is 200 (OK)
    assert response.status_code == status.HTTP_200_OK

    # Verify that the response contains the item created in the fixture
    assert len(items) > 0
    assert any(item['reference'] == initial_item.reference for item in items)
    assert any(item['name'] == initial_item.name for item in items)
    assert any(item['description'] == initial_item.description for item in items)
    assert any(item['price_without_tax'] == initial_item.price_without_tax for item in items)
    assert any(item['tax'] == initial_item.tax for item in items)    