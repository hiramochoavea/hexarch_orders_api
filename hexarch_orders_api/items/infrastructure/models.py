from django.db import models


class ItemModel(models.Model):
    """
    Django model representing an item in the database.

    Attributes:
        reference (str): The reference code of the item.
        name (str): The name of the item.
        description (str): The description of the item.
        price_without_tax (Decimal): The price of the item excluding tax.
        tax (Decimal): The applicable tax rate for the item.
        created_at (DateTime): The timestamp when the item was created.
    """

    reference = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price_without_tax = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=4, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """
        Return a string representation of the item, which is its name.

        Returns:
            str: The name of the item.
        """
        return self.name

    class Meta:
        db_table = 'item'
