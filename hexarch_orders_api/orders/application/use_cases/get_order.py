from ...infrastructure.repositories.order_repository import OrderRepository
from django.shortcuts import get_object_or_404

class GetOrderUseCase:
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def execute(self, order_id):
        return self.order_repository.get(order_id)
