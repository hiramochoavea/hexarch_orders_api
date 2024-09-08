from typing import List
from ...domain.entities.item import Item
from ...infrastructure.adapters.item_repository import ItemRepository

class ListItemsUseCase:
    def __init__(self, item_repository: ItemRepository) -> None:
        """
        Initialize the ListItemsUseCase with the given item repository.

        Args:
            item_repository (ItemRepository): The repository for listing the items.
        """        
        self.item_repository = item_repository

    def execute(self) -> List[Item]:
        """
        List all available items.

        Returns:
            List[Item]: A list of all items in the system.
        """        
        return self.item_repository.list_all()
    