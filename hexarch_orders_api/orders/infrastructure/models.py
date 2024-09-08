from django.db import models
from hexarch_orders_api.items.infrastructure.models import ItemModel

class OrderModel(models.Model):
    """
    Model representing an order.

    Attributes:
        items: A many-to-many relationship with ItemModel through OrderItemModel.
        total_price_without_tax: The total price of the order excluding tax.
        total_price_with_tax: The total price of the order including tax.
        created_at: The timestamp when the order was created.
    """    
    items = models.ManyToManyField(ItemModel, through='OrderItemModel')
    total_price_without_tax = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    total_price_with_tax = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - Created on {self.created_at}"

    class Meta:
        db_table = 'order'


class OrderItemModel(models.Model):
    """
    Model representing an item in an order.

    Attributes:
        order: A foreign key to the OrderModel.
        item: A foreign key to the ItemModel.
        quantity: The quantity of the item in the order.
    """    
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name='order_items')
    item = models.ForeignKey(ItemModel, on_delete=models.CASCADE, related_name='item_orders')
    quantity = models.PositiveIntegerField()

    class Meta:
        db_table = 'order_item'
        unique_together = ('order', 'item')