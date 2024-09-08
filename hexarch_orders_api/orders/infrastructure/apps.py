from django.apps import AppConfig


class OrdersConfig(AppConfig):
    """
    Django application configuration for the Orders app.

    Attributes:
        default_auto_field (str): The default field type for auto-generated primary keys.
        name (str): The name of the Django app.
    """
        
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hexarch_orders_api.orders'