from typing import TypedDict

from .assets import VoiceLinePayload
from .role import RolePayload
from .ability import AbilityPayload


class AgentPayload(TypedDict):
    uuid: str
    displayName: str
    description: str
    developerName: str
    characterTags: list[str]  # i have no idea how to parse this, some results return `None`
    isPlayableCharacter: bool
    isBaseContent: bool
    isAvailableForTest: bool
    role: RolePayload
    abilities: list[AbilityPayload]
    displayIcon: str
    displayIconSmall: str
    bustPortrait: str
    fullPortrait: str
    fullPortraitV2: str
    killfeedPortrait: str
    background: str
    backgroundGradientColors: list[str]
    assetPath: str
    isFullPortraitRightFacing: bool
    voiceLine: VoiceLinePayload
