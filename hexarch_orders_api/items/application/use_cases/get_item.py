from ...infrastructure.adapters.item_repository import ItemRepository

class GetItemUseCase:
    def __init__(self, item_repository: ItemRepository):
        """
        Initialize the GetItemUseCase with the given item repository.

        Args:
            item_repository (ItemRepository): The repository for fetching the item data.
        """        
        self.item_repository = item_repository

    def execute(self, item_id):
        """
        Retrieve an item by its unique identifier.

        Args:
            item_id (int): The unique identifier of the item.

        Returns:
            Item: The retrieved item object.
        """        
        return self.item_repository.get_by_id(item_id)
