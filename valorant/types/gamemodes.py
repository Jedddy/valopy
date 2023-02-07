from typing import TypedDict, Union


class GameRuleBoolOverridePayload(TypedDict):
    ruleName: str
    state: bool


class GameFeatureOverridePayload(TypedDict):
    featureName: str
    state: bool


class GameModePayload(TypedDict):
    uuid: str
    displayName: str
    duration: Union[str, None]
    allowsMatchTimeouts: bool
    isTeamVoiceAllowed: bool
    isMinimapHidden: bool
    orbCount: int
    roundsPerHalf: int
    teamRoles: Union[list[str], None]
    gameFeatureOverrides: Union[list[GameFeatureOverridePayload], None]
    gameRuleBoolOverrides: Union[list[GameRuleBoolOverridePayload], None]
    displayIcon: Union[str, None]
    assetPath: str


class GameModeEquippablePayload(TypedDict):
    uuid: str
    displayName: str
    category: str
    displayIcon: str
    killStreamIcon: str
    assetPath: str
