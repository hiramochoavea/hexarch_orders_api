from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderSerializer
from ..domain.services.order_service import OrderService
from ..infrastructure.adapters.order_repository import OrderRepository
from hexarch_orders_api.items.infrastructure.adapters.item_repository import ItemRepository
from ..domain.exceptions import ItemNotFoundException

class OrderAPIView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.service = OrderService(OrderRepository(), ItemRepository())


    def get(self, request, order_id=None):
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
    
    
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        
        if serializer.is_valid():
            order_data = serializer.validated_data
            
            try:
                order = self.service.create_order(order_data)
                response_serializer = OrderSerializer(order)
                return Response(response_serializer.data, status=status.HTTP_201_CREATED)
            except ItemNotFoundException as e:
                return Response({'error': str(e)}, status=status.HTTP_409_CONFLICT)
            except Exception as e:
                return Response({'error': 'An unexpected error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, order_id):
        serializer = OrderSerializer(data=request.data)
        
        if serializer.is_valid():
            try:
                updated_order = self.service.update_order(order_id, serializer.validated_data)
                response_serializer = OrderSerializer(updated_order)
                return Response(response_serializer.data, status=status.HTTP_200_OK)
            except ValueError as e:
                return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)