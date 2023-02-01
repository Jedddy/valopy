"""Gun Buddies"""

from typing import Union

from .assets import Media
from .types.buddies import BuddyPayload, BuddyLevelPayload


class BaseBuddy:
    """Base class for gun buddies."""

    uuid: str
    name: str
    display_icon: Media
    asset_path: str


class BuddyLevel(BaseBuddy):
    """Represents buddy level."""

    __slots__ = (
        "uuid",
        "name",
        "display_icon",
        "asset_path",
        "charm_level",
    )

    charm_level: int

    def __init__(self, data: BuddyLevelPayload) -> None:
        self.uuid: str = data["uuid"]
        self.name: str = data["displayName"]
        self.display_icon: Media = Media(data["displayIcon"])
        self.asset_path: str = data["assetPath"]
        self.charm_level: int = data["charmLevel"]


class Buddy(BaseBuddy):
    """Represents a gun buddy."""

    __slots__ = (
        "uuid",
        "name",
        "display_icon",
        "asset_path",
        "hidden_if_not_owned",
        "theme_uuid",
        "asset_path",
        "levels",
    )

    hidden_if_not_owned: bool
    theme_uuid: Union[str, None]
    asset_path: str
    levels: list[BuddyLevel]

    def __init__(self, data: BuddyPayload) -> None:
        self.uuid: str = data["uuid"]
        self.name: str = data["displayName"]
        self.display_icon: Media = Media(data["displayIcon"])
        self.asset_path: str = data["assetPath"]
        self.hidden_if_not_owned: bool = data["isHiddenIfNotOwned"]
        self.theme_uuid: Union[str, None] = data["themeUuid"]
        self.levels: list[BuddyLevel] = []
        self._update_levels(data)

    def _update_levels(self, data: BuddyPayload):
        for level in data["levels"]:
            self.levels.append(BuddyLevel(level))
