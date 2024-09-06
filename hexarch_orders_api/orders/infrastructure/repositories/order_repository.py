from django.shortcuts import get_object_or_404
from ...domain.entities.order import Order
from ...infrastructure.models import OrderModel, OrderItemModel
from hexarch_orders_api.items.infrastructure.models import ItemModel

class OrderRepository:
    def __init__(self):
        self.model_class = OrderModel

    def get(self, order_id: int) -> Order:
        order = get_object_or_404(OrderModel, id=order_id)

        return Order(
            pk=order.id,
            items=[
                {
                    'reference': order_item.item.reference,
                    'quantity': order_item.quantity
                }
                for order_item in order.orderitemmodel_set.all()
            ],
            total_price_without_tax=float(order.total_price_without_tax),
            total_price_with_tax=float(order.total_price_with_tax),
            creation_date=order.created_at
        )
        
    def list_all(self) -> list:
        orders = OrderModel.objects.all()
        
        return [
            Order(
                pk=order.id,
                items=[
                    {
                        'reference': order_item.item.reference,
                        'quantity': order_item.quantity
                    }
                    for order_item in order.orderitemmodel_set.all()
                ],
                total_price_without_tax=order.total_price_without_tax,
                total_price_with_tax=order.total_price_with_tax,
                creation_date=order.created_at
            )
            for order in orders
        ]
    
    def save(self, order: Order):
        order_model = OrderModel(
            total_price_without_tax=order.total_price_without_tax,
            total_price_with_tax=order.total_price_with_tax
        )
        order_model.save()

        for item in order.items:

            item_model = get_object_or_404(ItemModel, reference=item.reference)
            OrderItemModel.objects.create(
                order=order_model,
                item=item_model,
                quantity=item.quantity
            )

        return Order(
            pk=order_model.pk,
            items=order.items,
            total_price_without_tax=float(order_model.total_price_without_tax),
            total_price_with_tax=float(order_model.total_price_with_tax),
            creation_date=order_model.created_at
        )    