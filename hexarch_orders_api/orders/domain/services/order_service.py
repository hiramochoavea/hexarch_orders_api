class OrderService:
    @staticmethod
    def calculate_total_price_excluding_taxes(order):
        return sum(item.price for item in order.items)

    @staticmethod
    def calculate_total_price_including_taxes(order):
        return sum(item.price + (item.price * item.tax) for item in order.items)