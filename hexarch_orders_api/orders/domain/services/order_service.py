#from ..entities.order import Order
from ...infrastructure.adapters.order_repository import OrderRepository
from ...application.use_cases import list_order, get_order, create_order, update_order
from hexarch_orders_api.items.infrastructure.adapters.item_repository import ItemRepository

class OrderService:
    """
    Service class for managing orders.
    """

    def __init__(self, order_repository: OrderRepository, item_repository: ItemRepository):
        """
        Initialize the OrderService.

        Args:
            order_repository (OrderRepository): The repository used to access order data.
            item_repository (ItemRepository): The repository used to access item data.
        """
        self.order_repository = order_repository
        self.item_repository = item_repository

        self.get_order_use_case = get_order.GetOrderUseCase(order_repository)
        self.list_orders_use_case = list_order.ListOrdersUseCase(order_repository)        
        self.create_order_use_case = create_order.CreateOrderUseCase(order_repository, item_repository)
        self.update_order_use_case = update_order.UpdateOrderUseCase(order_repository, item_repository)

    def get_order(self, order_id):
        """
        Retrieve an order by its unique identifier.

        Args:
            order_id (int): The unique identifier of the order to retrieve.

        Returns:
            Order: The order with the specified identifier.
        """        
        return self.get_order_use_case.execute(order_id)

    def list_orders(self):
        """
        List all orders.

        Returns:
            List[Order]: A list of all orders.
        """        
        return self.list_orders_use_case.execute()

    def create_order(self, data):
        """
        Create a new order.

        Args:
            data (dict): The data to create the new order with.

        Returns:
            Order: The created order.
        """        
        return self.create_order_use_case.execute(data)

    def update_order(self, order_id, order_data):
        """
        Update an existing order.

        Args:
            order_id (int): The unique identifier of the order to update.
            order_data (dict): The data to update the order with.

        Returns:
            Order: The updated order.
        """        
        return self.update_order_use_case.execute(order_id, order_data)
