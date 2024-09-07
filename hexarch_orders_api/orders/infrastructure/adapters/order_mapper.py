from ...domain.entities.order import Order
from ...infrastructure.models import OrderModel, OrderItemModel
from hexarch_orders_api.items.infrastructure.models import ItemModel

class OrderMapper:
    @staticmethod
    def to_domain(order_model: OrderModel) -> Order:
        return Order(
            id=order_model.pk,
            items=[
                {
                    'reference': order_item.item.reference,
                    'quantity': order_item.quantity
                }
                for order_item in order_model.orderitemmodel_set.all()
            ],
            total_price_without_tax=float(order_model.total_price_without_tax),
            total_price_with_tax=float(order_model.total_price_with_tax),
            creation_date=order_model.created_at
        )

    @staticmethod
    def to_model(order: Order) -> OrderModel:
        return OrderModel(
            total_price_without_tax=order.total_price_without_tax,
            total_price_with_tax=order.total_price_with_tax
        )
