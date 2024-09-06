from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderSerializer
from ..domain.services.order_service import OrderService
from ..infrastructure.repositories.order_repository import OrderRepository

class OrderAPIView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.service = OrderService(OrderRepository())


    def get(self, request, order_id=None):

        # Retrieve an existent id
        if order_id is not None:
            order = self.service.get_order(order_id)

            if order is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_200_OK)        

        # List all orders
        orders = self.service.list_orders()
        serializer = OrderSerializer(orders, many=True)

        if not orders:
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        return Response(serializer.data, status=status.HTTP_200_OK)