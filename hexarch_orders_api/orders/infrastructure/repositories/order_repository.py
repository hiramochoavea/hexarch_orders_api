from django.shortcuts import get_object_or_404
from ...domain.entities.order import Order
from ...infrastructure.models import OrderModel

class OrderRepository:
    def __init__(self):
        self.model_class = OrderModel

    def get(self, order_id: int) -> Order:
        order_model = get_object_or_404(OrderModel, id=order_id)

        return Order(

        )

    def list_all(self) -> list:
        orders = OrderModel.objects.all()
        
        return [
            Order(

            )
            for order in orders
        ]