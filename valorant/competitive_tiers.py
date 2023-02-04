"""Competitive Tiers"""

from .assets import Media
from .types.competitive_tiers import RankTierPayload, EpisodePayload


class RankTier:
    """Represents a Rank tier.

    Attributes
    ----------
    tier: :class:`str`
        The rank tier.
    name: :class:`str`
        The name of the tier.
    division: :class:`str`
        The division of the rank tier.
    division_name: :class:`str`
        The division name.
    color: :class:`str`
        The tier color.
    background_color: :class:`str`
        The background color.
    small_icon: :class:`valorant.Media`
        The tier's small icon.
    large_icon: :class:`valorant.Media`
        The tier's large icon.
    rank_triangle_down_icon: :class:`valorant.Media`
        The tier's rank triangle down icon.
    rank_triangle_up_icon: :class:`valorant.Media`
        The tier's rank triangle up icon.
    """

    __slots__ = (
        "tier",
        "name",
        "division",
        "division_name",
        "color",
        "background_color",
        "small_icon",
        "large_icon",
        "rank_triangle_down_icon",
        "rank_triangle_up_icon",
    )

    tier: int
    name: str
    division: str
    division_name: str
    color: str
    background_color: str
    small_icon: Media
    large_icon: Media
    rank_triangle_down_icon: Media
    rank_triangle_up_icon: Media

    def __init__(self, data: RankTierPayload) -> None:
        self.tier: int = data["tier"]
        self.name: str = data["tierName"]
        self.division: str = data["division"]
        self.division_name: str = data["divisionName"]
        self.color: str = data["color"]
        self.background_color: str = data["backgroundColor"]
        self.small_icon: Media = Media(data["smallIcon"])
        self.large_icon: Media = Media(data["largeIcon"])
        self.rank_triangle_down_icon: Media = Media(data["rankTriangleDownIcon"])
        self.rank_triangle_up_icon: Media = Media(data["rankTriangleUpIcon"])

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<RankTier {self.name}>"


class Episode:
    """Represents a valorant competitive episode.

    Attributes
    ----------
    uuid: :class:`str`
        The episode's UUID.
    asset_object_name: :class:`str`
        The asset's object name.
    tiers: List[:class:`valorant.RankTier`]
    """

    __slots__ = (
        "uuid",
        "asset_object_name",
        "tiers",
    )

    uuid: str
    asset_object_name: str
    tiers: list[RankTier]

    def __init__(self, data: EpisodePayload):
        self.uuid: str = data["uuid"]
        self.asset_object_name: str = data["assetObjectName"]
        self.tiers: list[RankTier] = []
        self._update(data)

    def _update(self, data: EpisodePayload):
        for tier in data["tiers"]:
            self.tiers.append(RankTier(tier))

    def __str__(self) -> str:
        return self.asset_object_name

    def __repr__(self) -> str:
        return f"<Episode {self.asset_object_name}>"
