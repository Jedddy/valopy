"""Contracts"""

from typing import Union

from .assets import Media
from .types.contracts import (
    ContractRewardPayload,
    ContractChapterPayload,
    ContractLevelPayload,
    ContractContentPayload,
    ContractPayload,
)


class ContractReward:
    """Represents a contract reward.

    Attributes
    ----------
    reward_type: :class:`str`
        The reward type.
    uuid: :class:`str`
        The UUID of the reward.
    amount: :class:`int`
        The amount of the rewards.
    is_highlighted: :class:`bool`
        Indicates if the reward is highlighted
    """

    __slots__ = (
        "reward_type",
        "uuid",
        "amount",
        "is_highlighted",
    )

    def __init__(self, data: ContractRewardPayload) -> None:
        self.reward_type: str = data["type"]
        self.uuid: str = data["uuid"]
        self.amount: int = data["amount"]
        self.is_highlighted: bool = data["isHighlighted"]


class ContractLevel:
    """Represents a contract level.

    Attributes
    ----------
    reward: List[:class:`valorant.ContractReward`]
        The reward for this level.
    xp: :class:`int`
        The exp for this level.
    vp_cost: :class:`int`
        The vp cost of this level.
    is_purchasable_with_vp: :class:`bool`
        Indicates if this level is purchasable with VP
    """

    __slots__ = (
        "reward",
        "xp",
        "vp_cost",
        "is_purchasable_with_vp",
    )

    def __init__(self, data: ContractLevelPayload) -> None:
        self.reward: ContractReward = ContractReward(data["reward"])
        self.xp: int = data["xp"]
        self.vp_cost: int = data["vpCost"]
        self.is_purchasable_with_vp: bool = data["isPurchasableWithVP"]


class ContractChapter:
    """Represents a contract chapter.

    Attributes
    ----------
    is_epilogue: :class:`bool`
        Indicates if the chapter is epilogue.
    levels: List[:class:`valorant.ContractLevel`]
    free_rewards: Optional[List[:class:`valorant.ContractReward`]]
    """

    __slots__ = (
        "is_epilogue",
        "levels",
        "free_rewards",
    )

    def __init__(self, data: ContractChapterPayload) -> None:
        self.is_epilogue: bool = data["isEpilogue"]
        self.levels: list[ContractLevel] = []
        self.free_rewards: Union[list[ContractReward], None] = None
        self._update(data)

    def _update(self, data: ContractChapterPayload) -> None:
        for level in data["levels"]:
            self.levels.append(ContractLevel(level))

        if data["freeRewards"]:
            self.free_rewards = []
            for reward in data["freeRewards"]:
                self.free_rewards.append(ContractReward(reward))


class ContractContent:
    """Represents a contract content.

    Attributes
    ----------
    relation_type: :class:`str`
        The content's relation type.
    relation_uuid: :class:`str`
        The relation UUID.
    chapters: :class:`valorant.ContractChapter`
        The contract chapters.
    premium_reward_schedule_uuid: Optional[:class:`str`]
        ...
    premium_vp_cost: :class:`bool`
        The premium vp cost.
    """

    __slots__ = (
        "relation_type",
        "relation_uuid",
        "chapters",
        "premium_reward_schedule_uuid",
        "premium_vp_cost",
    )

    def __init__(self, data: ContractContentPayload) -> None:
        self.relation_type: str = data["relationType"]
        self.relation_uuid: str = data["relationUuid"]
        self.chapters: list[ContractChapter] = []
        self.premium_reward_schedule_uuid: str = data["premiumRewardScheduleUuid"]
        self.premium_vp_cost: int = data["premiumVPCost"]
        self._update(data)

    def _update(self, data: ContractContentPayload) -> None:
        for chapter in data["chapters"]:
            self.chapters.append(ContractChapter(chapter))


class Contract:
    """Represents a valorant contract

    Attributes
    ----------
    uuid: :class:`str`
        The UUID of the contract.
    name: :class:`str`
        The name of the contract.
    display_icon: Optional[:class:`valorant.Media`]
        The display icon.
    ship_it: :class:`bool`
        ...
    free_reward_schedule_uuid: :class:`str`
        ...
    content: :class:`valorant.Content`
        The contract's content.
    asset_path: :class:`str`
        The asset path on the API.
    """

    __slots__ = (
        "uuid",
        "name",
        "display_icon",
        "ship_it",
        "free_reward_schedule_uuid",
        "content",
        "asset_path",
    )

    def __init__(self, data: ContractPayload) -> None:
        self.uuid: str = data["uuid"]
        self.name: str = data["displayName"]
        self.display_icon: Media = Media(data["displayIcon"])
        self.ship_it: bool = data["shipIt"]
        self.free_reward_schedule_uuid: str = data["freeRewardScheduleUuid"]
        self.content: ContractContent = ContractContent(data["content"])
        self.asset_path: str = data["assetPath"]
