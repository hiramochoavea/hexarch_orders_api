from ...domain.entities.order import Order
from ...domain.entities.order_item import OrderItem
from ...infrastructure.repositories.order_repository import OrderRepository
from hexarch_orders_api.items.infrastructure.adapters.item_repository import ItemRepository

class CreateOrderUseCase:
    def __init__(self, order_repository: OrderRepository, item_repository: ItemRepository):
        self.order_repository = order_repository
        self.item_repository = item_repository

    def execute(self, data):
        items_data = data.get('items', [])

        total_price_without_tax = 0
        total_price_with_tax = 0

        order_items = []
        for item_data in items_data:
            item = item_data.get('item')
            reference = item_data.get('reference')
            quantity = item_data.get('quantity', 0)            

            item = self.item_repository.get_by_reference(reference)

            if quantity == 0:
                continue

            total_price_without_tax += item.price_without_tax * quantity
            total_price_with_tax += (item.price_without_tax * (1 + item.tax / 100)) * quantity

            new_order_item = OrderItem(
                quantity=quantity,
                reference=reference
            )

            order_items.append(new_order_item)
        
        order = Order(
            items=order_items,
            total_price_without_tax=total_price_without_tax,
            total_price_with_tax=total_price_with_tax
        )
        
        return self.order_repository.save(order)