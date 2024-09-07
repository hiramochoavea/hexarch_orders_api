class Order:
    def __init__(self, id=None, items=None, total_price_without_tax=0.00, 
                 total_price_with_tax=0.00, created_at=None):
        self.id = id
        self.items = items if items is not None else []
        self.total_price_without_tax = total_price_without_tax
        self.total_price_with_tax = total_price_with_tax
        self.created_at = created_at
