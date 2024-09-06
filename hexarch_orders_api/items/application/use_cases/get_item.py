from ...infrastructure.repositories.item_repository import ItemRepository
from django.shortcuts import get_object_or_404

class GetItemUseCase:
    def __init__(self, item_repository: ItemRepository):
        self.item_repository = item_repository

    def execute(self, item_id):
        return get_object_or_404(self.item_repository.model_class, pk=item_id)
