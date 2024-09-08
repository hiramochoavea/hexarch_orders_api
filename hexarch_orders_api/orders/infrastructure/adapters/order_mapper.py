from ...domain.entities.order import Order
from ...domain.entities.order_item import OrderItem
from ...infrastructure.models import OrderModel, OrderItemModel
from hexarch_orders_api.items.infrastructure.models import ItemModel


class OrderMapper:
    """
    Mapper for converting between Order and OrderModel.

    Methods:
        to_domain(order_model: OrderModel) -> Order: Converts an OrderModel instance to an Order instance.
        to_model(order: Order) -> OrderModel: Converts an Order instance to an OrderModel instance.
    """
    @staticmethod
    def to_domain(order_model: OrderModel) -> Order:
        """
        Converts an OrderModel instance to an Order instance.

        Args:
            order_model: The OrderModel instance to convert.

        Returns:
            An Order instance.
        """
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
        """
        Converts an Order instance to an OrderModel instance.

        Args:
            order: The Order instance to convert.

        Returns:
            An OrderModel instance.
        """
        return OrderModel(
            total_price_without_tax=order.total_price_without_tax,
            total_price_with_tax=order.total_price_with_tax
        )
