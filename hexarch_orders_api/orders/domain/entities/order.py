class Order:
    """
    Represents an order.
    """

    def __init__(self, id=None, items=None, total_price_without_tax=0.00, 
                 total_price_with_tax=0.00, created_at=None):
        """
        Initialize an Order.

        Args:
            id (int, optional): The unique identifier of the order.
            items (List[OrderItem], optional): The list of items in the order.
            total_price_without_tax (float, optional): The total price without tax.
            total_price_with_tax (float, optional): The total price with tax.
            created_at (datetime, optional): The creation date of the order.
        """        
        self.id = id
        self.items = items if items is not None else []
        self.total_price_without_tax = total_price_without_tax
        self.total_price_with_tax = total_price_with_tax
        self.created_at = created_at
