from ...domain.entities.item import Item
from ...infrastructure.adapters.item_repository import ItemRepository

class CreateItemUseCase:
    def __init__(self, item_repository: ItemRepository):
        """
        Initialize the CreateItemUseCase with the given item repository.

        Args:
            item_repository (ItemRepository): The repository handling the item persistence.
        """        
        self.item_repository = item_repository

    def execute(self, data):
        """
        Create a new item using the provided data.

        Args:
            data (dict): Data required to create a new item (reference, name, description, price, tax, etc.).

        Returns:
            Item: The created item.
        """        
        item = Item(**data)
        return self.item_repository.create(item)