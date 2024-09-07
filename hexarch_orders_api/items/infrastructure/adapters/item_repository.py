from ...domain.entities.item import Item
from ...domain.ports.item_repository_port import ItemRepositoryPort
from ...infrastructure.models import ItemModel
from .item_mapper import ItemMapper

class ItemRepository(ItemRepositoryPort):
    def __init__(self):
        self.model_class = ItemModel

    def list_all(self) -> list:
        items = self.model_class.objects.all()
        return [ItemMapper.to_domain(item) for item in items]
    
    def get_by_id(self, item_id: int) -> Item:
        try:
            item_model = self.model_class.objects.get(id=item_id)
        except ItemModel.DoesNotExist:
            return None
        return ItemMapper.to_domain(item_model)

    def get_by_reference(self, reference: str) -> Item:
        try:
            item_model = self.model_class.objects.get(reference=reference)
        except ItemModel.DoesNotExist:
            return None
        return ItemMapper.to_domain(item_model)

    def create(self, item: Item) -> Item:
        item_model = ItemMapper.to_model(item)
        item_model.save()
        return ItemMapper.to_domain(item_model)
    
    def update(self, item_id: int, item_data: dict) -> ItemModel:
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
