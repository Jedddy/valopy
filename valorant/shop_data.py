"""Shop Data"""

from typing import Union

from .assets import Media
from .types.shop_data import ShopDataPayload, GridPositionPayload


class GridPosition:
    """Represents an item's grid position

    Attributes
    ----------
    row: class:`int`
        The row.
    column: class:`int`
        The column.
    """

    __slots__ = (
        "row",
        "column",
    )

    def __init__(self, data: GridPositionPayload) -> None:
        self.row: int = data["row"]
        self.column: int = data["column"]


class ShopData:
    """Represents a valorant item's shop data.

    Attributes
    ----------
    cost: :class:`int`
        The item's cost.
    category: :class:`str`
        The category.
    category_text: :class:`str`
        The category text.
    grid_position: :class:`valorant.GridPosition`
        The grid position of the item on the shop.
    can_be_trashed: :class:`bool`
        Indicates if the item can be trashed or not.
    image: :class:`valorant.Media`
        The item's image
    new_image: :class:`valorant.Media`
        The item's new image.
    new_image2: :class:`valorant.Media`
        The item's new image.
    asset_path: :class:`str`
        The asset path on the API
    """

    __slots__ = (
        "cost",
        "category",
        "category_text",
        "grid_position",
        "can_be_trashed",
        "image",
        "new_image",
        "new_image2",
        "asset_path",
    )

    def __init__(self, data: ShopDataPayload) -> None:
        self.cost: int = data["cost"]
        self.category: str = data["category"]
        self.category_text: str = data["categoryText"]

        if data["gridPosition"]:
            self.grid_position: GridPosition = GridPosition(data["gridPosition"])
        else:
            self.grid_position = None

        self.can_be_trashed: bool = data["canBeTrashed"]
        self.image: Media = Media(data["image"])
        self.new_image: Media = Media(data["newImage"])
        self.new_image2: Media = Media(data["newImage2"])
        self.asset_path: str = data["assetPath"]
