from ...domain.entities.order import Order
from ...domain.entities.order_item import OrderItem
from ...infrastructure.adapters.order_repository import OrderRepository
from hexarch_orders_api.items.infrastructure.adapters.item_repository import ItemRepository
from ...domain.utils import calculate_price_totals

class UpdateOrderUseCase:
    def __init__(self, order_repository: OrderRepository, item_repository: ItemRepository):
        self.order_repository = order_repository
        self.item_repository = item_repository

    def execute(self, order_id, order_data):
        order = self.order_repository.get_by_id(order_id)
        if not order:
            raise ValueError("Order not found")

        items_data = order_data.get('items', [])
        order_items = []

        items_info = []
        for item_data in items_data:
            reference = item_data.get('reference')
            quantity = item_data.get('quantity', 0)
            
            item = self.item_repository.get_by_reference(reference)
            if not item:
                raise ValueError(f"Item with reference {reference} not found")

            items_info.append({
                'price_without_tax': item.price_without_tax,
                'tax': item.tax,
                'quantity': quantity
            })

            order_items.append(OrderItem(
                quantity=quantity,
                reference=reference
            ))

        total_price_without_tax, total_price_with_tax = calculate_price_totals(items_info)

        order.items = order_items
        order.total_price_without_tax = total_price_without_tax
        order.total_price_with_tax = total_price_with_tax
        
        return self.order_repository.update(order)