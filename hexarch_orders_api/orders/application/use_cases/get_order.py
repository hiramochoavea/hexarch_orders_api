from ...infrastructure.adapters.order_repository import OrderRepository

class GetOrderUseCase:
    """
    Use case for retrieving a single order by its unique identifier.
    """

    def __init__(self, order_repository: OrderRepository):
        """
        Initialize the GetOrderUseCase.

        Args:
            order_repository (OrderRepository): The repository used to access order data.
        """        
        self.order_repository = order_repository

    def execute(self, order_id):
        """
        Execute the use case to retrieve an order by its identifier.

        Args:
            order_id (int): The unique identifier of the order to retrieve.

        Returns:
            Order: The order with the specified identifier.
        """        
        return self.order_repository.get_by_id(order_id)
