from typing import TypedDict, Union


class RankTierPayload(TypedDict):
    tier: int
    tierName: str
    division: str
    divisionName: str
    color: str
    backgroundColor: str
    smallIcon: Union[str, None]
    largeIcon: Union[str, None]
    rankTriangleDownIcon: Union[str, None]
    rankTriangleUpIcon: Union[str, None]


class EpisodePayload(TypedDict):
    uuid: str
    assetObjectName: str
    tiers: list[RankTierPayload]
