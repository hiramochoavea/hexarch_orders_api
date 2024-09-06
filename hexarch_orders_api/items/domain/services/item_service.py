from ..entities.item import Item
from ...infrastructure.repositories.item_repository import ItemRepository
from ...application.use_cases import create_item, update_item, list_item, get_item

class ItemService:
    def __init__(self, repository: ItemRepository):
        self.repository = repository
        self.create_item_use_case = create_item.CreateItemUseCase(repository)
        self.update_item_use_case = update_item.UpdateItemUseCase(repository)
        self.list_items_use_case = list_item.ListItemsUseCase(repository)
        self.get_item_use_case = get_item.GetItemUseCase(repository)

    def create_item(self, data):
        return self.create_item_use_case.execute(data)

    def update_item(self, item_id, item_data):
        return self.update_item_use_case.execute(item_id, item_data)

    def get_item(self, item_id):
        return self.get_item_use_case.execute(item_id)

    def list_items(self):
        return self.list_items_use_case.execute()
