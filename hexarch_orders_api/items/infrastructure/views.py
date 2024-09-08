from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ..domain.services.item_service import ItemService
from ..infrastructure.adapters.item_repository import ItemRepository
from .serializers import ItemSerializer


class ItemAPIView(APIView):
    """
    Base view for handling item-related API requests.

    This view provides a base implementation for item-related operations
    by initializing the ItemService with an instance of ItemRepository.
    """

    def __init__(self, **kwargs) -> None:
        """
        Initialize the ItemAPIView with an instance of ItemService.

        Args:
            **kwargs: Additional keyword arguments for the APIView.

        This constructor sets up the ItemService with an ItemRepository instance
        for handling item-related operations.
        """
        super().__init__(**kwargs)

        self.service = ItemService(ItemRepository())


class ItemListView(ItemAPIView):
    """
    View for handling list and creation of items.

    This view handles HTTP GET requests to retrieve a list of items and
    HTTP POST requests to create new items.
    """

    @extend_schema(
        responses={
            200: ItemSerializer,
            404: OpenApiResponse(description="Item not found"),
            204: OpenApiResponse(description="No items found"),
        }
    )
    def get(self, request: Request) -> Response:
        """
        Handle GET requests to retrieve items list.

        Args:
            request: The HTTP request object.

        Returns:
            Response: The HTTP response object containing the items list or a status code.
        """

        items = self.service.list_items()
        serializer = ItemSerializer(items, many=True)

        if not items:
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=ItemSerializer,
        responses={
            201: ItemSerializer,
            400: OpenApiResponse(description="Invalid data"),
        },
    )
    def post(self, request: Request) -> Response:
        """
        Handle POST requests to create a new item.

        Args:
            request: The HTTP request object containing the item data.

        Returns:
            Response: The HTTP response object containing the created item data or errors.
        """

        # Create a new item
        serializer = ItemSerializer(data=request.data)

        if serializer.is_valid():
            item_data = serializer.validated_data
            item = self.service.create_item(item_data)
            response_serializer = ItemSerializer(item)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemDetailView(ItemAPIView):
    """
    View for handling retrieval, update, and deletion of a single item.

    This view handles HTTP GET requests to retrieve a single item by its ID,
    HTTP PUT requests to update an existing item.
    """

    @extend_schema(
        responses={
            200: ItemSerializer,
            404: OpenApiResponse(description="Item not found"),
            204: OpenApiResponse(description="No items found"),
        }
    )
    def get(self, request: Request, item_id: int) -> Response:
        """
        Handle GET requests to retrieve items.

        Args:
            request: The HTTP request object.
            item_id (int): The unique identifier of the item to retrieve.

        Returns:
            Response: The HTTP response object containing the item data or a status code.
        """
        item = self.service.get_item(item_id)

        if item is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=ItemSerializer,
        responses={
            200: ItemSerializer,
            400: OpenApiResponse(description="Invalid data"),
            404: OpenApiResponse(description="Item not found"),
            500: OpenApiResponse(description="Internal server error"),
        },
    )
    def put(self, request: Request, item_id: int) -> Response:
        """
        Handle PUT requests to update an existing item.

        Args:
            request: The HTTP request object containing the updated item data.
            item_id (int): The unique identifier of the item to update.

        Returns:
            Response: The HTTP response object containing the updated item data or an error message.
        """

        # Retrieve the item to update
        item = self.service.get_item(item_id)
        if item is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        request_data = request.data.copy()

        try:
            # Pass the data to the service
            updated_item = self.service.update_item(item_id, request_data)

            # Serialize the updated item back to the response
            serializer = ItemSerializer(updated_item)
            return Response(serializer.data)

        except Exception as e:
            return Response(
                {"detail": "An error occurred during update."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
