from typing import Optional

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from hexarch_orders_api.items.infrastructure.adapters.item_repository import (
    ItemRepository,
)

from ..domain.exceptions import ItemNotFoundException
from ..domain.services.order_service import OrderService
from ..infrastructure.adapters.order_repository import OrderRepository
from .serializers import OrderSerializer


class OrderAPIView(APIView):
    """
    API view for managing orders.

    Methods:
        get: Retrieves a specific order by ID or lists all orders.
        post: Creates a new order.
        put: Updates an existing order by ID.
    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes the OrderAPIView with the OrderService.
        """
        super().__init__(**kwargs)

        self.service = OrderService(OrderRepository(), ItemRepository())

    def get(self, request: Request, order_id: Optional[int] = None) -> Response:
        """
        Handles GET requests to retrieve an order or list all orders.

        Args:
            request: The HTTP request object.
            order_id: The ID of the order to retrieve. If None, lists all orders.

        Returns:
            A Response object with the order data or a list of orders.
        """
        if order_id is not None:
            order = self.service.get_order(order_id)

            if order is None:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_200_OK)

        orders = self.service.list_orders()
        serializer = OrderSerializer(orders, many=True)

        if not orders:
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        """
        Handles POST requests to create a new order.

        Args:
            request: The HTTP request object containing order data.

        Returns:
            A Response object with the created order data or an error message.
        """
        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            order_data = serializer.validated_data

            try:
                order = self.service.create_order(order_data)
                response_serializer = OrderSerializer(order)
                return Response(
                    response_serializer.data, status=status.HTTP_201_CREATED
                )
            except ItemNotFoundException as e:
                return Response({"error": str(e)}, status=status.HTTP_409_CONFLICT)
            except Exception as e:
                return Response(
                    {"error": "An unexpected error occurred."},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request: Request, order_id: int) -> Response:
        """
        Handles PUT requests to update an existing order.

        Args:
            request: The HTTP request object containing updated order data.
            order_id: The ID of the order to update.

        Returns:
            A Response object with the updated order data or an error message.
        """
        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            try:
                updated_order = self.service.update_order(
                    order_id, serializer.validated_data
                )
                response_serializer = OrderSerializer(updated_order)
                return Response(response_serializer.data, status=status.HTTP_200_OK)
            except ValueError as e:
                return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
