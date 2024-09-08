from typing import List
from ...domain.entities.item import Item
from ...infrastructure.adapters.item_repository import ItemRepository
from ...application.use_cases import create_item, update_item, list_item, get_item

class ItemService:
    """
    Service for handling item-related operations using various use cases.

    Attributes:
        repository (ItemRepository): The repository that handles item-related data.
        get_item_use_case (GetItemUseCase): Use case for retrieving an item.
        list_items_use_case (ListItemsUseCase): Use case for listing all items.
        create_item_use_case (CreateItemUseCase): Use case for creating a new item.
        update_item_use_case (UpdateItemUseCase): Use case for updating an existing item.
    """ 
        
    def __init__(self, repository: ItemRepository) -> None:
        """
        Initialize the ItemService with the repository and use cases.

        Args:
            repository (ItemRepository): The repository that handles item-related data.
        """        
        self.repository = repository

        self.get_item_use_case = get_item.GetItemUseCase(repository)        
        self.list_items_use_case = list_item.ListItemsUseCase(repository)        
        self.create_item_use_case = create_item.CreateItemUseCase(repository)
        self.update_item_use_case = update_item.UpdateItemUseCase(repository)

    def get_item(self, item_id: int) -> Item:
        """
        Get an item by its ID.

        Args:
            item_id (int): The unique identifier of the item.

        Returns:
            Item: The retrieved item.
        """        
        return self.get_item_use_case.execute(item_id)

    def list_items(self) -> List[Item]:
        """
        List all available items.

        Returns:
            List[Item]: A list of all items.
        """        
        return self.list_items_use_case.execute()

    def create_item(self, data: dict) -> Item:
        """
        Create a new item with the provided data.

        Args:
            data (dict): Data required to create a new item.

        Returns:
            Item: The created item.
        """        
        return self.create_item_use_case.execute(data)

    def update_item(self, item_id: int, item_data: dict) -> Item:
        """
        Update an existing item with new data.

        Args:
            item_id (int): The unique identifier of the item.
            item_data (dict): The new data to update the item.

        Returns:
            Item: The updated item.
        """        
        return self.update_item_use_case.execute(item_id, item_data)

