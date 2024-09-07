def calculate_price_totals(items):
    """
    Calculate the total price without tax and with tax for a list of items.
    
    Args:
        items (list of dict): List of items where each item is a dictionary with keys 'price_without_tax', 'tax', and 'quantity'.
    
    Returns:
        tuple: A tuple containing total price without tax and total price with tax.
    """
    total_price_without_tax = 0
    total_price_with_tax = 0

    for item in items:
        price_without_tax = item.get('price_without_tax', 0)
        tax = item.get('tax', 0)
        quantity = item.get('quantity', 0)

        total_price_without_tax += price_without_tax * quantity
        total_price_with_tax += (price_without_tax * (1 + tax / 100)) * quantity

    return total_price_without_tax, total_price_with_tax
