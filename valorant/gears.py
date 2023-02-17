"""Gears"""

from .shop_data import ShopData
from .types.gears import GearPayload


class Gear:
    """Represents a valorant gear.

    Attributes
    ----------
    uuid: :class:`str`
        The UUID of the gear.
    name: :class:`str`
        The name of the gear.
    description: :class:`str`
        The description.
    asset_path: :class:`str`
        The asset path on the API
    shop_data: :class:`valorant.ShopData`
        The gear's shop data.
    """

    __slots__ = (
        "uuid",
        "name",
        "description",
        "asset_path",
        "shop_data",
    )

    def __init__(self, data: GearPayload) -> None:
        self.uuid: str = data["uuid"]
        self.name: str = data["displayName"]
        self.description: str = data["description"]
        self.asset_path: str = data["assetPath"]
        self.shop_data: ShopData = ShopData(data["shopData"])
