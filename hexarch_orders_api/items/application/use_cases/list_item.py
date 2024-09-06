from ...infrastructure.repositories.item_repository import ItemRepository

class ListItemsUseCase:
    def __init__(self, item_repository: ItemRepository):
        self.item_repository = item_repository

    def execute(self):
        return self.item_repository.list_all()
    