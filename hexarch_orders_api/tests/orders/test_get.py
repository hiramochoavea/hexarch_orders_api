import pytest
from rest_framework import status


@pytest.mark.django_db
def test_get_order_by_id(api_client, reverse_url, initial_order):
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
    assert any(
        item['reference'] == initial_order.items.first().reference and 
        item['quantity'] == initial_order.items.first().orderitemmodel_set.first().quantity
        for item in order['items']
    )
    assert abs(order['total_price_without_tax'] - initial_order.total_price_without_tax) < 0.01
    assert abs(order['total_price_with_tax'] - initial_order.total_price_with_tax) < 0.01
