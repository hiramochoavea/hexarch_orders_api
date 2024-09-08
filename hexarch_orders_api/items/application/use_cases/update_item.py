from ...domain.entities.item import Item
from ...infrastructure.adapters.item_repository import ItemRepository


class UpdateItemUseCase:
    """
    Use case for updating an existing item with new data.

    Attributes:
        item_repository (ItemRepository): The repository for updating the item data.
    """

    def __init__(self, item_repository: ItemRepository) -> None:
        """
        Initialize the UpdateItemUseCase with the given item repository.

        Args:
            item_repository (ItemRepository): The repository for updating the item data.
        """
        self.item_repository = item_repository

    def execute(self, item_id: int, item_data: dict) -> Item:
        """
        Update an existing item using the provided data.

        Args:
            item_id (int): The unique identifier of the item to be updated.
            item_data (dict): The new data to update the item with.

        Returns:
            Item: The updated item.
        """
        return self.item_repository.update(item_id, item_data)
