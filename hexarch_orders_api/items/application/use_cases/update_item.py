from ...domain.entities.item import Item
from ...infrastructure.repositories.item_repository import ItemRepository

class UpdateItemUseCase:
    def __init__(self, item_repository: ItemRepository):
        self.item_repository = item_repository

    def execute(self, item_id, item_data):
        return self.item_repository.update(item_id, item_data)