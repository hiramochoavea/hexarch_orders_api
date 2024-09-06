# from django.utils import timezone
# from domain.entities import Order
# from domain.services import OrderService

# class CreateOrderUseCase:
#     def __init__(self, order_repository):
#         self.order_repository = order_repository

#     def execute(self, items):
#         # Create the order
#         new_order = Order(items=items, creation_date=timezone.now())

#         # Save the order in the repository
#         self.order_repository.save(new_order)
        
#         return new_order