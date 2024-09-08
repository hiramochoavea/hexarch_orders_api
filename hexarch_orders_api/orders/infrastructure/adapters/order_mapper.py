from ...domain.entities.order import Order
from ...domain.entities.order_item import OrderItem
from ...infrastructure.models import OrderModel, OrderItemModel
from hexarch_orders_api.items.infrastructure.models import ItemModel

class OrderMapper:
    @staticmethod
    def to_domain(order_model: OrderModel) -> Order:
        return Order(
            id=order_model.pk,
            items=[
                OrderItem(
                    quantity=order_item.quantity,
                    reference=order_item.item.reference,
                )
                for order_item in order_model.order_items.all()
            ],
            total_price_without_tax=float(order_model.total_price_without_tax),
            total_price_with_tax=float(order_model.total_price_with_tax),
            created_at=order_model.created_at
        )

    @staticmethod
    def to_model(order: Order) -> OrderModel:
        return OrderModel(
            total_price_without_tax=order.total_price_without_tax,
            total_price_with_tax=order.total_price_with_tax
        )
