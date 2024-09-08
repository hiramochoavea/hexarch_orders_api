from typing import List
from ...domain.entities.order import Order
from ...infrastructure.adapters.order_repository import OrderRepository

class ListOrdersUseCase:
    """
    Use case for listing all orders.
    """

    def __init__(self, order_repository: OrderRepository) -> None:
        """
        Initialize the ListOrdersUseCase.

        Args:
            order_repository (OrderRepository): The repository used to access order data.
        """        
        self.order_repository = order_repository

    def execute(self) -> List[Order]:
        """
        Execute the use case to list all orders.

        Returns:
            List[Order]: A list of all orders.
        """        
        return self.order_repository.list_all()
