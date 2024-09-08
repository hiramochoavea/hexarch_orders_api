from django.apps import AppConfig


class ItemsConfig(AppConfig):
    """
    Django application configuration for the Items app.

    Attributes:
        default_auto_field (str): The default field type for auto-generated primary keys.
        name (str): The name of the Django app.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hexarch_orders_api.items'
