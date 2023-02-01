from typing import TypedDict, Union


class BaseBuddyPayload(TypedDict):
    uuid: str
    displayName: str
    displayIcon: str
    assetPath: str


class BuddyLevelPayload(BaseBuddyPayload):
    charmLevel: int


class BuddyPayload(BaseBuddyPayload):
    isHiddenIfNotOwned: bool
    themeUuid: Union[str, None]
    levels: list[BuddyLevelPayload]
