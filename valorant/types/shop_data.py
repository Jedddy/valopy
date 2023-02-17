from typing import TypedDict, Union


class GridPositionPayload(TypedDict):
    row: int
    column: int


class ShopDataPayload(TypedDict):
    cost: int
    category: str
    categoryText: str
    gridPosition: GridPositionPayload
    canBeTrashed: bool
    image: Union[str, None]
    newImage: Union[str, None]
    newImage2: Union[str, None]
    assetPath: str
