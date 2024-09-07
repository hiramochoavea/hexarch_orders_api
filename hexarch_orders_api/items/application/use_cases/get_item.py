from ...infrastructure.adapters.item_repository import ItemRepository

class GetItemUseCase:
    def __init__(self, item_repository: ItemRepository):
        self.item_repository = item_repository

    def execute(self, item_id):
        return self.item_repository.get_by_id(item_id)
