from ...domain.entities.item import Item
from ...infrastructure.models import ItemModel

class ItemMapper:
    @staticmethod
    def to_domain(item_model: ItemModel) -> Item:
        return Item(
            id=item_model.pk,
            reference=item_model.reference,
            name=item_model.name,
            description=item_model.description,
            price_without_tax=float(item_model.price_without_tax),
            tax=float(item_model.tax),
            created_at=item_model.created_at
        )

    @staticmethod
    def to_model(item: Item) -> ItemModel:
        return ItemModel(
            reference=item.reference,
            name=item.name,
            description=item.description,
            price_without_tax=item.price_without_tax,
            tax=item.tax
        )
