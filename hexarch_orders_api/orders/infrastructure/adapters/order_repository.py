from typing import List
from ...domain.entities.order import Order
from ...domain.ports.order_repository_port import OrderRepositoryPort
from ...infrastructure.models import OrderModel, OrderItemModel
from hexarch_orders_api.items.infrastructure.models import ItemModel
from .order_mapper import OrderMapper

class OrderRepository(OrderRepositoryPort):
    def __init__(self):
        self.model_class = OrderModel

    def get_by_id(self, order_id: int) -> Order:
        try:
            order_model = self.model_class.objects.get(id=order_id)
        except OrderModel.DoesNotExist:
            return None
        return OrderMapper.to_domain(order_model)
    
    def list_all(self) -> List[Order]:
        orders = self.model_class.objects.all()
        return [OrderMapper.to_domain(order) for order in orders]
    
    def create(self, order: Order) -> Order:
        order_model = OrderMapper.to_model(order)
        order_model.save()

        for item in order.items:
            item_model = ItemModel.objects.get(reference=item.reference)
            OrderItemModel.objects.create(
                order=order_model,
                item=item_model,
                quantity=item.quantity
            )
        return OrderMapper.to_domain(order_model)

    def update(self, order: Order) -> Order:
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
                order=order_model,
                item=item_model,
                quantity=item.quantity
            )
        return OrderMapper.to_domain(order_model)

    def remove_items(self, order_id: int):
        try:
            order_model = self.model_class.objects.get(id=order_id)
        except OrderModel.DoesNotExist:
            return
        OrderItemModel.objects.filter(order=order_model).delete()

    def add_item(self, order_id: int, item_reference: str, quantity: int):
        try:
            order_model = self.model_class.objects.get(id=order_id)
            item_model = ItemModel.objects.get(reference=item_reference)
        except (OrderModel.DoesNotExist, ItemModel.DoesNotExist):
            return
        OrderItemModel.objects.create(
            order=order_model,
            item=item_model,
            quantity=quantity
        )
