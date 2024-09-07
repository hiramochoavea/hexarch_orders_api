import pytest


@pytest.mark.django_db
def test_create_order(api_client, reverse_url, initial_item):
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
    assert response.status_code == 201

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
    expected_total_price_without_tax = initial_item.price_without_tax * payload['items'][0]['quantity']
    expected_total_price_with_tax = (initial_item.price_without_tax * (1 + initial_item.tax / 100)) * payload['items'][0]['quantity']

    # Assert the calculated total prices match the response
    assert abs(data['total_price_without_tax'] - expected_total_price_without_tax) < 0.01
    assert abs(data['total_price_with_tax'] - expected_total_price_with_tax) < 0.01
