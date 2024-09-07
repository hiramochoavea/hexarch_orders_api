from typing import List
from abc import ABC, abstractmethod
from ..entities.order import Order

class OrderRepositoryPort(ABC):
    @abstractmethod
    def get_by_id(self, order_id: int) -> Order:
        """ Retrieve an order by its unique identifier. """
        pass
    
    @abstractmethod
    def list_all(self) -> List[Order]:
        """ List all orders. """
        pass
    
    @abstractmethod
    def create(self, order: Order) -> Order:
        """ Create a new order. """
        pass
    
    @abstractmethod
    def update(self, order: Order) -> Order:
        """ Update an existing order. """
        pass

    @abstractmethod
    def remove_items(self, order_id: int):
        """ Remove all items from an order. """
        pass

    @abstractmethod
    def add_item(self, order_id: int, item_reference: str, quantity: int):
        """ Add an item to an existing order. """
        pass
