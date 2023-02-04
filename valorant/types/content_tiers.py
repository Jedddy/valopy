from typing import TypedDict


class ContentTierPayload(TypedDict):
    uuid: str
    displayName: str
    devName: str
    rank: int
    juiceValue: int
    juiceCost: int
    highlightColor: str
    displayIcon: str
    assetPath: str
