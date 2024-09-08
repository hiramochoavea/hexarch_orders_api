from typing import List
from abc import ABC, abstractmethod
from ..entities.order import Order

class OrderRepositoryPort(ABC):
    """
    Abstract base class for the Order repository port.
    """

    @abstractmethod
    def get_by_id(self, order_id: int) -> Order:
        """
        Retrieve an order by its unique identifier.

        Args:
            order_id (int): The unique identifier of the order to retrieve.

        Returns:
            Order: The order with the specified identifier.
        """
        pass
    
    @abstractmethod
    def list_all(self) -> List[Order]:
        """
        List all orders.

        Returns:
            List[Order]: A list of all orders.
        """
        pass
    
    @abstractmethod
    def create(self, order: Order) -> Order:
        """
        Create a new order.

        Args:
            order (Order): The order to create.

        Returns:
            Order: The created order.
        """
        pass
    
    @abstractmethod
    def update(self, order: Order) -> Order:
        """
        Update an existing order.

        Args:
            order (Order): The order to update.

        Returns:
            Order: The updated order.
        """
        pass

    @abstractmethod
    def remove_items(self, order_id: int):
        """
        Remove all items from an order.

        Args:
            order_id (int): The unique identifier of the order from which to remove items.
        """
        pass

    @abstractmethod
    def add_item(self, order_id: int, item_reference: str, quantity: int):
        """
        Add an item to an existing order.

        Args:
            order_id (int): The unique identifier of the order to which to add the item.
            item_reference (str): The reference of the item to add.
            quantity (int): The quantity of the item to add.
        """
        pass
