from ...domain.entities.item import Item
from ...infrastructure.adapters.item_repository import ItemRepository

class UpdateItemUseCase:
    def __init__(self, item_repository: ItemRepository):
        """
        Initialize the UpdateItemUseCase with the given item repository.

        Args:
            item_repository (ItemRepository): The repository for updating the item data.
        """        
        self.item_repository = item_repository

    def execute(self, item_id, item_data):
        """
        Update an existing item using the provided data.

        Args:
            item_id (int): The unique identifier of the item to be updated.
            item_data (dict): The new data to update the item with.

        Returns:
            Item: The updated item.
        """        
        return self.item_repository.update(item_id, item_data)