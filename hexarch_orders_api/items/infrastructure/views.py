from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ItemSerializer
from ..domain.services.item_service import ItemService
from ..infrastructure.repositories.item_repository import ItemRepository

class ItemAPIView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.service = ItemService(ItemRepository())


    def get(self, request, item_id=None):

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
    

    def post(self, request):

        # Create a new item
        serializer = ItemSerializer(data=request.data)
        
        if serializer.is_valid():
            item_data = serializer.validated_data
            item = self.service.create_item(item_data)
            response_serializer = ItemSerializer(item)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, item_id=None):
        if item_id is None:
            return Response({"detail": "Item ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Retrieve the item to update
        item = self.service.get_item(item_id)
        if item is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # Update item data
        serializer = ItemSerializer(data=request.data, partial=True, instance=item)

        if serializer.is_valid():
            updated_item = self.service.update_item(item_id, serializer.validated_data)
            response_serializer = ItemSerializer(updated_item)
            return Response(response_serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)