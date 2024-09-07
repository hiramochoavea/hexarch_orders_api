from typing import List
from abc import ABC, abstractmethod
from ..entities.item import Item

class ItemRepositoryPort(ABC):
    
    @abstractmethod
    def list_all(self) -> List[Item]:
        """ Returns a list of all items. """
        pass

    @abstractmethod
    def get_by_id(self, item_id: int) -> Item:
        """ Fetches an item by its unique ID. """
        pass

    @abstractmethod
    def get_by_reference(self, reference: str) -> Item:
        """ Fetches an item by its reference. """
        pass

    @abstractmethod
    def create(self, item: Item) -> Item:
        """ Creates a new item and returns the created item. """
        pass

    @abstractmethod
    def update(self, item_id: int, item_data: dict) -> Item:
        """ Updates an existing item with new data. """
        pass
