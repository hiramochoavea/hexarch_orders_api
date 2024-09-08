from drf_spectacular.utils import OpenApiResponse, extend_schema
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
    Base view for handling order-related API requests.

    This view provides a base implementation for order-related operations
    by initializing the OrderService with an instance of OrderRepository,
    and an instance of ItemRepository.
    """

    def __init__(self, **kwargs) -> None:
        """
        Initialize the OrderAPIView with an instance of OrderService.

        Args:
            **kwargs: Additional keyword arguments for the APIView.

        This constructor sets up the OrderService with an OrderRepository and
        an ItemRepository instance, for handling item-related operations.
        """
        super().__init__(**kwargs)

        self.service = OrderService(OrderRepository(), ItemRepository())


class OrderListView(OrderAPIView):
    """
    View for handling GET and POST requests related to orders.

    This view handles retrieval of a list of orders or a specific order
    based on provided filters. It also supports creating new orders.
    """

    @extend_schema(
        responses={
            200: OrderSerializer,
            404: OpenApiResponse(description="Order not found"),
            204: OpenApiResponse(description="No orders found"),
        }
    )
    def get(self, request: Request) -> Response:
        """
        Handles GET requests to retrieve an order or list all orders.

        Args:
            request: The HTTP request object.

        Returns:
            A Response object with the list of orders.
        """
        orders = self.service.list_orders()
        serializer = OrderSerializer(orders, many=True)

        if not orders:
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=OrderSerializer,
        responses={
            201: OrderSerializer,
            400: OpenApiResponse(description="Invalid data"),
            409: OpenApiResponse(description="Item not found"),
            500: OpenApiResponse(description="Internal server error"),
        },
    )
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


class OrderDetailView(OrderAPIView):
    """
    View for handling GET and PUT requests related to a specific order.

    This view handles retrieval of a specific order by its ID, as well as
    updating an existing order.
    """

    @extend_schema(
        responses={
            200: OrderSerializer,
            404: OpenApiResponse(description="Order not found"),
            204: OpenApiResponse(description="No orders found"),
        }
    )
    def get(self, request: Request, order_id: int) -> Response:
        """
        Handles GET requests to retrieve an order.

        Args:
            request: The HTTP request object.
            order_id: The ID of the order to retrieve.

        Returns:
            A Response object with the order data.
        """
        order = self.service.get_order(order_id)

        if order is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=OrderSerializer,
        responses={
            200: OrderSerializer,
            400: OpenApiResponse(description="Invalid data"),
            404: OpenApiResponse(description="Order not found"),
        },
    )
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
