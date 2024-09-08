from ...infrastructure.adapters.item_repository import ItemRepository

class ListItemsUseCase:
    def __init__(self, item_repository: ItemRepository):
        """
        Initialize the ListItemsUseCase with the given item repository.

        Args:
            item_repository (ItemRepository): The repository for listing the items.
        """        
        self.item_repository = item_repository

    def execute(self):
        """
        List all available items.

        Returns:
            list[Item]: A list of all items in the system.
        """        
        return self.item_repository.list_all()
    