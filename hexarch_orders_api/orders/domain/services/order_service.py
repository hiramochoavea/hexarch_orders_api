#from ..entities.order import Order
from ...infrastructure.repositories.order_repository import OrderRepository
from ...application.use_cases import list_order, get_order, create_order, update_order
from hexarch_orders_api.items.infrastructure.adapters.item_repository import ItemRepository

class OrderService:
    def __init__(self, order_repository: OrderRepository, item_repository: ItemRepository):
        self.order_repository = order_repository
        self.item_repository = item_repository

        self.create_order_use_case = create_order.CreateOrderUseCase(order_repository, item_repository)
        self.update_order_use_case = update_order.UpdateOrderUseCase(order_repository, item_repository)
        self.list_orders_use_case = list_order.ListOrdersUseCase(order_repository)
        self.get_order_use_case = get_order.GetOrderUseCase(order_repository)

    def create_order(self, data):
        return self.create_order_use_case.execute(data)

    def update_order(self, order_id, order_data):
        return self.update_order_use_case.execute(order_id, order_data)

    def get_order(self, order_id):
        return self.get_order_use_case.execute(order_id)

    def list_orders(self):
        return self.list_orders_use_case.execute()