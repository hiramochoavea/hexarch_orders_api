class Item:
    def __init__(self, reference, name, description, price_without_tax, tax, created_at=None, pk=None):
        self.id = pk        
        self.reference = reference
        self.name = name
        self.description = description
        self.price_without_tax = price_without_tax
        self.tax = tax
        self.created_at = created_at