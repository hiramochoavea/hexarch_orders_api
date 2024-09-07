import pytest
from rest_framework import status


@pytest.mark.django_db
def test_list_all_orders(api_client, reverse_url, initial_order):
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
        any(item['reference'] == initial_order.items.first().reference for item in order['items'])
        for order in orders
    )
    #assert any(order['total_price_without_tax'] == initial_order.total_price_without_tax for order in orders)
    #assert any(order['total_price_with_tax'] == initial_order.total_price_with_tax for order in orders)