from typing import Optional
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ItemSerializer
from ..domain.services.item_service import ItemService
from ..infrastructure.adapters.item_repository import ItemRepository


class ItemAPIView(APIView):

    def __init__(self, **kwargs) -> None:
        """
        Initialize the ItemAPIView with an instance of ItemService.

        Args:
            **kwargs: Additional keyword arguments for the APIView.
        """
        super().__init__(**kwargs)

        self.service = ItemService(ItemRepository())

    def get(self, request: Request, item_id: Optional[int] = None) -> Response:
        """
        Handle GET requests to retrieve items.

        Args:
            request: The HTTP request object.
            item_id (int, optional): The unique identifier of the item to retrieve.

        Returns:
            Response: The HTTP response object containing the item data or a status code.
        """

        # Retrieve an existent id
        if item_id is not None:
            item = self.service.get_item(item_id)

            if item is None:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = ItemSerializer(item)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # List all items
        items = self.service.list_items()
        serializer = ItemSerializer(items, many=True)

        if not items:
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.data, status=status.HTTP_200_OK)

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

    def put(self, request: Request, item_id: Optional[int] = None) -> Response:
        """
        Handle PUT requests to update an existing item.

        Args:
            request: The HTTP request object containing the updated item data.
            item_id (int, optional): The unique identifier of the item to update.

        Returns:
            Response: The HTTP response object containing the updated item data or an error message.
        """
        if item_id is None:
            return Response({"detail": "Item ID is required."}, status=status.HTTP_400_BAD_REQUEST)

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
            return Response({"detail": "An error occurred during update."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
