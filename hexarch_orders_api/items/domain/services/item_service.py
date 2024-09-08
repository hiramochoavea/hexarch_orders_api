from ...infrastructure.adapters.item_repository import ItemRepository
from ...application.use_cases import create_item, update_item, list_item, get_item

class ItemService:
    def __init__(self, repository: ItemRepository):
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

    def get_item(self, item_id):
        """
        Get an item by its ID.

        Args:
            item_id (int): The unique identifier of the item.

        Returns:
            Item: The retrieved item.
        """        
        return self.get_item_use_case.execute(item_id)

    def list_items(self):
        """
        List all available items.

        Returns:
            list[Item]: A list of all items.
        """        
        return self.list_items_use_case.execute()

    def create_item(self, data):
        """
        Create a new item with the provided data.

        Args:
            data (dict): Data required to create a new item.

        Returns:
            Item: The created item.
        """        
        return self.create_item_use_case.execute(data)

    def update_item(self, item_id, item_data):
        """
        Update an existing item with new data.

        Args:
            item_id (int): The unique identifier of the item.
            item_data (dict): The new data to update the item.

        Returns:
            Item: The updated item.
        """        
        return self.update_item_use_case.execute(item_id, item_data)

