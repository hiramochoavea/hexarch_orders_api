from typing import Callable

import pytest
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_create_item(
    api_client: APIClient, reverse_url: Callable[[str, ...], str]
) -> None:
    """
    Tests the creation of an item through the API.

    Args:
        api_client: The APIClient instance for making requests.
        reverse_url: The function for reversing URL names.

    Asserts:
        Response status code is 201 (Created).
        Response data matches the payload and contains expected fields.
    """

    payload = {
        "reference": "PIX2022",
        "name": "Google Pixel 6",
        "description": (
            "A high-performance smartphone with a 6.4-inch AMOLED display, "
            "128GB storage, and Google's Tensor chip."
        ),
        "price_without_tax": 649.00,
        "tax": 21,
    }

    # Make the POST request to create an item
    response = api_client.post(reverse_url("items"), payload, format="json")

    # Get the response data
    data = response.data

    # Assert the response status code is 201 (Created)
    assert response.status_code == status.HTTP_201_CREATED

    # Verify the response contains the expected fields and values
    assert data.get("reference") == payload["reference"]
    assert data.get("name") == payload["name"]
    assert data.get("description") == payload["description"]
    assert data.get("price_without_tax") == payload["price_without_tax"]
    assert data.get("tax") == payload["tax"]

    # Assert that an ID and creation date are present in the response
    assert "id" in data
    assert "created_at" in data
