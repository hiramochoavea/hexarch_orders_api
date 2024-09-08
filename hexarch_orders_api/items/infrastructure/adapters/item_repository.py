from typing import List
from ...domain.entities.item import Item
from ...domain.ports.item_repository_port import ItemRepositoryPort
from ...infrastructure.models import ItemModel
from .item_mapper import ItemMapper

class ItemRepository(ItemRepositoryPort):
    """
    Repository for managing item persistence.

    Inherits from:
        ItemRepositoryPort: The port defining the interface for item repositories.

    Attributes:
        model_class (Type[ItemModel]): The model class used for item persistence.
    """
        
    def __init__(self):
        """
        Initialize the ItemRepository with the ItemModel class.

        Args:
            None
        """        
        self.model_class = ItemModel

    def list_all(self) -> List[Item]:
        """
        Retrieve all items from the repository.

        Returns:
            List: A list of domain Item instances.
        """        
        items = self.model_class.objects.all()
        return [ItemMapper.to_domain(item) for item in items]
    
    def get_by_id(self, item_id: int) -> Item:
        """
        Retrieve an item by its unique identifier.

        Args:
            item_id (int): The unique identifier of the item.

        Returns:
            Item: The domain Item instance, or None if not found.
        """        
        try:
            item_model = self.model_class.objects.get(id=item_id)
        except ItemModel.DoesNotExist:
            return None
        return ItemMapper.to_domain(item_model)

    def get_by_reference(self, reference: str) -> Item:
        """
        Retrieve an item by its reference.

        Args:
            reference (str): The reference code of the item.

        Returns:
            Item: The domain Item instance, or None if not found.
        """        
        try:
            item_model = self.model_class.objects.get(reference=reference)
        except ItemModel.DoesNotExist:
            return None
        return ItemMapper.to_domain(item_model)

    def create(self, item: Item) -> Item:
        """
        Create a new item in the repository.

        Args:
            item (Item): The domain Item instance to create.

        Returns:
            Item: The created domain Item instance.
        """        
        item_model = ItemMapper.to_model(item)
        item_model.save()
        return ItemMapper.to_domain(item_model)
    
    def update(self, item_id: int, item_data: dict) -> ItemModel:
        """
        Update an existing item with new data.

        Args:
            item_id (int): The unique identifier of the item to update.
            item_data (dict): The new data to update the item with.

        Returns:
            Item: The updated domain Item instance, or None if not found.
        """        
        try:
            item_model = self.model_class.objects.get(id=item_id)
        except ItemModel.DoesNotExist:
            return None

        item_model.reference = item_data.get('reference', item_model.reference)
        item_model.name = item_data.get('name', item_model.name)
        item_model.description = item_data.get('description', item_model.description)
        item_model.price_without_tax = item_data.get('price_without_tax', item_model.price_without_tax)
        item_model.tax = item_data.get('tax', item_model.tax)
        item_model.save()

        return ItemMapper.to_domain(item_model)
