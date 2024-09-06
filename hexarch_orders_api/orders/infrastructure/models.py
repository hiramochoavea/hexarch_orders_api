from django.db import models
from hexarch_orders_api.items.infrastructure.models import ItemModel

class OrderModel(models.Model):
    items = models.ManyToManyField(ItemModel, through='OrderItem')
    total_price_without_tax = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    total_price_with_tax = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - Created on {self.created_at}"

    class Meta:
        db_table = 'order'


class OrderItem(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    item = models.ForeignKey(ItemModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        db_table = 'order_item'
        unique_together = ('order', 'item')