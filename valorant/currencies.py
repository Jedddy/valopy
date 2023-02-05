"""Currencies"""

from .assets import Media
from .types.currencies import CurrencyPayload


class Currency:
    """Represents a valorant currency

    Attributes
    ----------
    uuid: :class:`str`
        The currency's UUID.
    name: :class:`str`
        The currency's name.
    name_singular: :class:`str`
        The singular name.
    display_icon: :class:`valorant.Media`
        The display icon of this currency.
    large_icon: :class:`valorant.Media`
        The large icon of this currency.
    asset_path: :class:`str`
        The asset path on the API.
    """

    __slots__ = (
        "uuid",
        "name",
        "name_singular",
        "display_icon",
        "large_icon",
        "asset_path",
    )

    def __init__(self, data: CurrencyPayload) -> None:
        self.uuid: str = data["uuid"]
        self.name: str = data["displayName"]
        self.name_singular: str = data["displayNameSingular"]
        self.display_icon: Media = Media(data["displayIcon"])
        self.large_icon: Media = Media(data["largeIcon"])
        self.asset_path: str = data["assetPath"]

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<Currency {self.name}>"
