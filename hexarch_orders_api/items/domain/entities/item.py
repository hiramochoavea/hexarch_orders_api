class Item:
    def __init__(self, reference, name, description, price_without_tax, tax, id=None, created_at=None):
        self.id = id
        self.reference = reference
        self.name = name
        self.description = description
        self.price_without_tax = price_without_tax
        self.tax = tax
        self.created_at = created_at
