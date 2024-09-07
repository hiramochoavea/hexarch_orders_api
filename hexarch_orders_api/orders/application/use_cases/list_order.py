from ...infrastructure.adapters.order_repository import OrderRepository

class ListOrdersUseCase:
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def execute(self):
        return self.order_repository.list_all()
