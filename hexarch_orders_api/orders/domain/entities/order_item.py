class OrderItem:
    """
    Represents an item in an order.
    """

    def __init__(self, quantity, reference) -> None:
        """
        Initialize an OrderItem.

        Args:
            quantity (int): The quantity of the item.
            reference (str): The reference of the item.
        """
        self.quantity = quantity
        self.reference = reference
