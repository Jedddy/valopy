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

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.name}>"


class Buddy(BaseBuddy):
    """Represents a gun buddy.

    Attributes
    ----------
    uuid: :class:`str`
        The gun buddy's UUID.
    name: :class:`str`
        The gun buddy's display name.
    display_icon: :class:`valorant.Media`
        The display icon.
    asset_path: :class:`str`
        The asset path on the API.
    hidden_if_not_owned: :class:`bool`
        Indicates if the buddy is hidden if it's not owned.
    theme_uuid: Optional[:class:`str`]
        The theme UUID.
    levels: List[:class:`valorant.BuddyLevel`]
        A list of the buddy's levels.
    """

    __slots__ = (
        "uuid",
        "name",
        "display_icon",
        "asset_path",
        "hidden_if_not_owned",
        "theme_uuid",
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
        self._update(data)

    def _update(self, data: BuddyPayload):
        for level in data["levels"]:
            self.levels.append(BuddyLevel(level))

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.name}>"
