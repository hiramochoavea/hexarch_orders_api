class Item:
    """
    Represents an item entity with its attributes.
    """

    def __init__(self, reference, name, description, price_without_tax, tax, id=None, created_at=None) -> None:
        """
        Initialize an Item entity.

        Args:
            reference (str): The reference code of the item.
            name (str): The name of the item.
            description (str): The description of the item.
            price_without_tax (float): The price of the item excluding tax.
            tax (float): The applicable tax rate for the item.
            id (int, optional): The unique identifier of the item. Defaults to None.
            created_at (str, optional): The timestamp when the item was created. Defaults to None.
        """
        self.id = id
        self.reference = reference
        self.name = name
        self.description = description
        self.price_without_tax = price_without_tax
        self.tax = tax
        self.created_at = created_at
