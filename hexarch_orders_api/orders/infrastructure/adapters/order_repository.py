from typing import List

from hexarch_orders_api.items.infrastructure.models import ItemModel

from ...domain.entities.order import Order
from ...domain.ports.order_repository_port import OrderRepositoryPort
from ...infrastructure.models import OrderItemModel, OrderModel
from .order_mapper import OrderMapper


class OrderRepository(OrderRepositoryPort):
    """
    Repository for managing Order entities.

    Methods:
        get_by_id(order_id: int) -> Order: Retrieves an Order by its ID.
        list_all() -> List[Order]: Lists all Orders.
        create(order: Order) -> Order: Creates a new Order.
        update(order: Order) -> Order: Updates an existing Order.
        remove_items(order_id: int): Removes all items from an Order.
        add_item(order_id: int, item_reference: str, quantity: int): Adds an item to an Order.
    """

    def __init__(self):
        """
        Initializes the OrderRepository with the OrderModel.
        """
        self.model_class = OrderModel

    def get_by_id(self, order_id: int) -> Order:
        """
        Retrieves an Order by its ID.

        Args:
            order_id: The ID of the order to retrieve.

        Returns:
            An Order instance or None if not found.
        """
        try:
            order_model = self.model_class.objects.get(id=order_id)
        except OrderModel.DoesNotExist:
            return None
        return OrderMapper.to_domain(order_model)

    def list_all(self) -> List[Order]:
        """
        Lists all Orders.

        Returns:
            A list of Order instances.
        """
        orders = self.model_class.objects.all()
        return [OrderMapper.to_domain(order) for order in orders]

    def create(self, order: Order) -> Order:
        """
        Creates a new Order.

        Args:
            order: The Order instance to create.

        Returns:
            The created Order instance.
        """
        order_model = OrderMapper.to_model(order)
        order_model.save()

        for item in order.items:
            item_model = ItemModel.objects.get(reference=item.reference)
            OrderItemModel.objects.create(
                order=order_model, item=item_model, quantity=item.quantity
            )
        return OrderMapper.to_domain(order_model)

    def update(self, order: Order) -> Order:
        """
        Updates an existing Order.

        Args:
            order: The Order instance with updated data.

        Returns:
            The updated Order instance or None if not found.
        """
        try:
            order_model = self.model_class.objects.get(id=order.id)
        except OrderModel.DoesNotExist:
            return None

        order_model.total_price_without_tax = order.total_price_without_tax
        order_model.total_price_with_tax = order.total_price_with_tax
        order_model.save()

        OrderItemModel.objects.filter(order=order_model).delete()

        for item in order.items:
            item_model = ItemModel.objects.get(reference=item.reference)
            OrderItemModel.objects.create(
                order=order_model, item=item_model, quantity=item.quantity
            )
        return OrderMapper.to_domain(order_model)

    def remove_items(self, order_id: int):
        """
        Removes all items from an Order.

        Args:
            order_id: The ID of the order from which to remove items.
        """
        try:
            order_model = self.model_class.objects.get(id=order_id)
        except OrderModel.DoesNotExist:
            return
        OrderItemModel.objects.filter(order=order_model).delete()

    def add_item(self, order_id: int, item_reference: str, quantity: int):
        """
        Adds an item to an Order.

        Args:
            order_id: The ID of the order to which to add the item.
            item_reference: The reference of the item to add.
            quantity: The quantity of the item to add.
        """
        try:
            order_model = self.model_class.objects.get(id=order_id)
            item_model = ItemModel.objects.get(reference=item_reference)
        except (OrderModel.DoesNotExist, ItemModel.DoesNotExist):
            return
        OrderItemModel.objects.create(
            order=order_model, item=item_model, quantity=quantity
        )
