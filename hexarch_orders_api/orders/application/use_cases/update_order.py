from ...domain.entities.order import Order
from ...domain.entities.order_item import OrderItem
from ...infrastructure.repositories.order_repository import OrderRepository
from hexarch_orders_api.items.infrastructure.adapters.item_repository import ItemRepository

class UpdateOrderUseCase:
    def __init__(self, order_repository: OrderRepository, item_repository: ItemRepository):
        self.order_repository = order_repository
        self.item_repository = item_repository

    def execute(self, order_id, order_data):
        order = self.order_repository.get(order_id)
        
        if not order:
            raise ValueError("Order not found")

        items_data = order_data.get('items', [])
        order_items = []
        total_price_without_tax = 0
        total_price_with_tax = 0
        
        for item_data in items_data:
            reference = item_data.get('reference')
            quantity = item_data.get('quantity', 0)
            
            item = self.item_repository.get_by_reference(reference)
            if not item:
                raise ValueError(f"Item with reference {reference} not found")

            total_price_without_tax += item.price_without_tax * quantity
            total_price_with_tax += (item.price_without_tax * (1 + item.tax / 100)) * quantity

            order_items.append(OrderItem(
                quantity=quantity,
                reference=reference
            ))

        order.items = order_items
        order.total_price_without_tax = total_price_without_tax
        order.total_price_with_tax = total_price_with_tax
        
        return self.order_repository.update(order)