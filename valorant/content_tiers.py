"""Content tiers"""

from .assets import Media
from .types.content_tiers import ContentTierPayload


class ContentTier:
    """Represents a content tier

    Attributes
    ----------
    uuid: :class:`str`
        The UUID of the tier.
    name: :class:`str`
        The name of the tier
    dev_name: :class:`str`
        The developer name of the tier.
    rank: :class:`int`
        The tier's ranking.
    juice_value: :class:`int`
        The tier's juice value.
    juice_cost: :class:`int`
        The tier's juice cost.
    highlight_color: :class:`str`
        The tier's highlight color.
    display_icon: :class:`valorant.Media`
        The tier's icon.
    asset_path: :class:`str`
        The asset_path on the API
    """

    __slots__ = (
        "uuid",
        "name",
        "dev_name",
        "rank",
        "juice_value",
        "juice_cost",
        "highlight_color",
        "display_icon",
        "asset_path",
    )

    def __init__(self, data: ContentTierPayload) -> None:
        self.uuid: str = data["uuid"]
        self.name: str = data["displayName"]
        self.dev_name: str = data["devName"]
        self.rank: int = data["rank"]
        self.juice_value: int = data["juiceValue"]
        self.juice_cost: int = data["juiceCost"]
        self.highlight_color: str = data["highlightColor"]
        self.display_icon: Media = Media(data["displayIcon"])
        self.asset_path: str = data["assetPath"]

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.name}>"
