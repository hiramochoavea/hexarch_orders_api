from ...infrastructure.adapters.order_repository import OrderRepository

class GetOrderUseCase:
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def execute(self, order_id):
        return self.order_repository.get_by_id(order_id)
