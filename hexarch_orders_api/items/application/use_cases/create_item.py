from ...domain.entities.item import Item
from ...infrastructure.adapters.item_repository import ItemRepository

class CreateItemUseCase:
    def __init__(self, item_repository: ItemRepository):
        self.item_repository = item_repository

    def execute(self, data):
        item = Item(**data)
        return self.item_repository.create(item)