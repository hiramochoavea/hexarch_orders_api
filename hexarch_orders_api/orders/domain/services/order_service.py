#from ..entities.order import Order
from ...infrastructure.repositories.order_repository import OrderRepository
from ...application.use_cases import list_order, get_order #create_order, update_order

class OrderService:
    def __init__(self, repository: OrderRepository):
        self.repository = repository
        # self.create_order_use_case = create_order.CreateOrderUseCase(repository)
        # self.update_order_use_case = update_order.UpdateOrderUseCase(repository)
        self.list_orders_use_case = list_order.ListOrdersUseCase(repository)
        self.get_order_use_case = get_order.GetOrderUseCase(repository)

    # def create_order(self, data):
    #     return self.create_order_use_case.execute(data)

    # def update_order(self, order_id, order_data):
    #     return self.update_order_use_case.execute(order_id, order_data)

    def get_order(self, order_id):
        return self.get_order_use_case.execute(order_id)

    def list_orders(self):
        return self.list_orders_use_case.execute()
    
    # @staticmethod
    # def calculate_total_price_excluding_taxes(order):
    #     return sum(order.price for order in order.orders)

    # @staticmethod
    # def calculate_total_price_including_taxes(order):
    #     return sum(order.price + (order.price * order.tax) for order in order.orders)    