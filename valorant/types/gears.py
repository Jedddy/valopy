from typing import TypedDict

from .shop_data import ShopDataPayload


class GearPayload(TypedDict):
    uuid: str
    displayName: str
    description: str
    displayIcon: str
    assetPath: str
    shopData: ShopDataPayload
