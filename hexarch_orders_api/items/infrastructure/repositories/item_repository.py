from django.shortcuts import get_object_or_404
from ...domain.entities.item import Item
from ...infrastructure.models import ItemModel

class ItemRepository:
    def __init__(self):
        self.model_class = ItemModel

    def save(self, item: Item):
        item_model = ItemModel(
            reference=item.reference,
            name=item.name,
            description=item.description,
            price_without_tax=item.price_without_tax,
            tax=item.tax
        )
        
        item_model.save()

        return Item(
            reference=item_model.reference,
            name=item_model.name,
            description=item_model.description,
            price_without_tax=float(item_model.price_without_tax),
            tax=float(item_model.tax),
            created_at=item_model.created_at
        )
    
    def update(self, item_id, item_data):
        item_model = get_object_or_404(ItemModel, id=item_id)
        
        item_model.reference = item_data.get('reference', item_model.reference)
        item_model.name = item_data.get('name', item_model.name)
        item_model.description = item_data.get('description', item_model.description)
        item_model.price_without_tax = item_data.get('price_without_tax', item_model.price_without_tax)
        item_model.tax = item_data.get('tax', item_model.tax)
        item_model.save()
        
        return item_model    
    

    def get(self, item_id: int) -> Item:
        item_model = get_object_or_404(ItemModel, id=item_id)

        return Item(
            reference=item_model.reference,
            name=item_model.name,
            description=item_model.description,
            price_without_tax=float(item_model.price_without_tax),
            tax=float(item_model.tax),
            created_at=item_model.created_at
        )

    def list_all(self) -> list:
        items = ItemModel.objects.all()
        
        return [
            Item(
                reference=item.reference,
                name=item.name,
                description=item.description,
                price_without_tax=float(item.price_without_tax),
                tax=float(item.tax),
                created_at=item.created_at
            )
            for item in items
        ]
    
    def get_by_reference(self, reference: str) -> Item:
        item_model = get_object_or_404(ItemModel, reference=reference)

        return Item(
            reference=item_model.reference,
            name=item_model.name,
            description=item_model.description,
            price_without_tax=float(item_model.price_without_tax),
            tax=float(item_model.tax),
            created_at=item_model.created_at
        )