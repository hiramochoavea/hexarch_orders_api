from typing import List
from abc import ABC, abstractmethod
from ..entities.item import Item

class ItemRepositoryPort(ABC):
    """
    Abstract base class defining the interface for item repositories.

    Methods:
        list_all() -> List[Item]: Retrieves a list of all items.
        get_by_id(item_id: int) -> Item: Retrieves an item by its unique ID.
        get_by_reference(reference: str) -> Item: Retrieves an item by its reference.
        create(item: Item) -> Item: Creates a new item.
        update(item_id: int, item_data: dict) -> Item: Updates an existing item with new data.
    """       
    
    @abstractmethod
    def list_all(self) -> List[Item]:
        """
        Returns a list of all items.

        Returns:
            List[Item]: A list containing all item objects.
        """
        pass

    @abstractmethod
    def get_by_id(self, item_id: int) -> Item:
        """
        Fetches an item by its unique ID.

        Args:
            item_id (int): The unique identifier of the item.

        Returns:
            Item: The item object.
        """
        pass

    @abstractmethod
    def get_by_reference(self, reference: str) -> Item:
        """
        Fetches an item by its reference.

        Args:
            reference (str): The reference code of the item.

        Returns:
            Item: The item object.
        """
        pass

    @abstractmethod
    def create(self, item: Item) -> Item:
        """
        Creates a new item and returns the created item.

        Args:
            item (Item): The item object to be created.

        Returns:
            Item: The created item.
        """
        pass

    @abstractmethod
    def update(self, item_id: int, item_data: dict) -> Item:
        """
        Updates an existing item with new data.

        Args:
            item_id (int): The unique identifier of the item to be updated.
            item_data (dict): The new data to update the item with.

        Returns:
            Item: The updated item.
        """
        pass
