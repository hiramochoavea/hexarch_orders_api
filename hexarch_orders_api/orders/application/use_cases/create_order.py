from ...domain.entities.order import Order
from ...domain.entities.order_item import OrderItem
from ...infrastructure.adapters.order_repository import OrderRepository
from hexarch_orders_api.items.infrastructure.adapters.item_repository import ItemRepository
from ...domain.exceptions import ItemNotFoundException
from ...domain.utils import calculate_price_totals

class CreateOrderUseCase:
    def __init__(self, order_repository: OrderRepository, item_repository: ItemRepository):
        """
        Initialize the CreateOrderUseCase with the given repositories.

        Args:
            order_repository (OrderRepository): The repository for handling orders.
            item_repository (ItemRepository): The repository for handling items.
        """        
        self.order_repository = order_repository
        self.item_repository = item_repository

    def execute(self, data):
        """
        Create a new order with the provided data.

        Args:
            data (dict): Data for creating the order, including items and their quantities.

        Returns:
            Order: The created order instance.
        """        
        items_data = data.get('items', [])
        order_items = []
        
        items_info = []
        for item_data in items_data:
            reference = item_data.get('reference')
            quantity = item_data.get('quantity', 0)
            
            item = self.item_repository.get_by_reference(reference)
            if item is None:
                raise ItemNotFoundException(f"Item with reference {reference} does not exist.")

            if quantity == 0:
                continue

            items_info.append({
                'price_without_tax': item.price_without_tax,
                'tax': item.tax,
                'quantity': quantity
            })

            new_order_item = OrderItem(
                quantity=quantity,
                reference=reference
            )
            order_items.append(new_order_item)

        total_price_without_tax, total_price_with_tax = calculate_price_totals(items_info)

        order = Order(
            items=order_items,
            total_price_without_tax=total_price_without_tax,
            total_price_with_tax=total_price_with_tax
        )

        return self.order_repository.create(order)