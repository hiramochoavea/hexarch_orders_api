from ...domain.entities.item import Item
from ...infrastructure.models import ItemModel


class ItemMapper:
    """
    Mapper class for converting between domain Item and ItemModel instances.

    Methods:
        to_domain(item_model: ItemModel) -> Item: Converts an ItemModel instance to a domain Item instance.
        to_model(item: Item) -> ItemModel: Converts a domain Item instance to an ItemModel instance.
    """

    @staticmethod
    def to_domain(item_model: ItemModel) -> Item:
        """
        Convert an ItemModel instance to a domain Item instance.

        Args:
            item_model (ItemModel): The ItemModel instance to convert.

        Returns:
            Item: The domain Item instance.
        """
        return Item(
            id=item_model.pk,
            reference=item_model.reference,
            name=item_model.name,
            description=item_model.description,
            price_without_tax=float(item_model.price_without_tax),
            tax=float(item_model.tax),
            created_at=item_model.created_at
        )

    @staticmethod
    def to_model(item: Item) -> ItemModel:
        """
        Convert a domain Item instance to an ItemModel instance.

        Args:
            item (Item): The domain Item instance to convert.

        Returns:
            ItemModel: The ItemModel instance.
        """
        return ItemModel(
            reference=item.reference,
            name=item.name,
            description=item.description,
            price_without_tax=item.price_without_tax,
            tax=item.tax
        )
