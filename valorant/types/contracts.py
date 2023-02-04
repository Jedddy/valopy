from typing import TypedDict, Union


class ContractRewardPayload(TypedDict):
    type: str
    uuid: str
    amount: int
    isHighlighted: bool


class ContractLevelPayload(TypedDict):
    reward: ContractRewardPayload
    xp: int
    vpCost: int
    isPurchasableWithVP: bool


class ContractChapterPayload(TypedDict):
    isEpilogue: bool
    levels: list[ContractLevelPayload]
    freeRewards: Union[list[ContractRewardPayload], None]


class ContractContentPayload(TypedDict):
    relationType: str
    relationUuid: str
    chapters: list[ContractChapterPayload]
    premiumRewardScheduleUuid: str
    premiumVPCost: int


class ContractPayload(TypedDict):
    uuid: str
    displayName: str
    displayIcon: str
    shipIt: bool
    freeRewardScheduleUuid: str
    content: ContractContentPayload
    assetPath: str
