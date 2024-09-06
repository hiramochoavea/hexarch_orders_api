from ...infrastructure.repositories.order_repository import OrderRepository
from django.shortcuts import get_object_or_404

class GetOrderUseCase:
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def execute(self, order_id):
        return get_object_or_404(self.order_repository.model_class, pk=order_id)
