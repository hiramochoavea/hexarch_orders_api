from ...domain.entities.item import Item
from ...infrastructure.adapters.item_repository import ItemRepository


class CreateItemUseCase:
    """
    Use case for creating a new item.

    Attributes:
        item_repository (ItemRepository): The repository responsible for item persistence.
    """

    def __init__(self, item_repository: ItemRepository) -> None:
        """
        Initialize the CreateItemUseCase with the given item repository.

        Args:
            item_repository (ItemRepository): The repository handling the item persistence.
        """
        self.item_repository = item_repository

    def execute(self, data: dict) -> Item:
        """
        Create a new item using the provided data.

        Args:
            data (dict): Data required to create a new item (reference, name, description, price, tax, etc.).

        Returns:
            Item: The created item.
        """
        item = Item(**data)
        return self.item_repository.create(item)
