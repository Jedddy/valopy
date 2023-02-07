"""Gamemodes"""

from typing import Union

from .types.gamemodes import (
    GameFeatureOverridePayload,
    GameModeEquippablePayload,
    GameModePayload,
    GameRuleBoolOverridePayload,
)
from .assets import Media


class GameRuleBoolOverride:

    __slots__ = (
        "rule_name",
        "state",
    )

    def __init__(self, data: GameRuleBoolOverridePayload):
        self.rule_name: str = data["ruleName"]
        self.state: bool = data["state"]


class GameFeatureOverride:

    __slots__ = (
        "feature_name",
        "state",
    )

    def __init__(self, data: GameFeatureOverridePayload) -> None:
        self.feature_name: str = data["featureName"]
        self.state: bool = data["state"]


class GameMode:
    """Represents a valorant game mode.

    Attributes
    ----------
    uuid: :class:`str`
        The game mode's UUID.
    name: :class:`str`
        The game mode name.
    duration: Optional[:class:`str`]
        The duration.
    allows_match_timeouts: :class:`bool`
        Indicates if this mode allows match timeouts.
    is_team_voice_allowed: :class:`bool`
        Indicates if this mode allows team voice.
    is_minimap_hidden :class:`bool`
        Indicates if the minimap is hidden.
    orb_count: :class:`int`
        The game mode orb count.
    rounds_per_half: :class:`int`
        The rounds per half of the game.
    team_roles: Optional[:class:`bool`]
        The team roles of this mode.
    game_feature_overrides: Optional[:class:`valorant.GameFeatureOverride`]
        The overridden game features.
    game_rule_bool_overrides: Optional[:class:`valorant.GameRuleOverride`]
        The overridden game rules.
    display_icon: Optional[:class:`valorant.Media`]
        The game mode's display icon.
    asset_path: :class:`str`
        The asset path on the API.
    """

    __slots__ = (
        "uuid",
        "name",
        "duration",
        "allows_match_timeouts",
        "is_team_voice_allowed",
        "is_minimap_hidden",
        "orb_count",
        "rounds_per_half",
        "team_roles",
        "game_feature_overrides",
        "game_rule_bool_overrides",
        "display_icon",
        "asset_path",
    )

    def __init__(self, data: GameModePayload) -> None:
        self.uuid: str = data["uuid"]
        self.name: str = data["displayName"]
        self.duration: Union[str, None] = data["duration"]
        self.allows_match_timeouts: bool = data["allowsMatchTimeouts"]
        self.is_team_voice_allowed: bool = data["isTeamVoiceAllowed"]
        self.is_minimap_hidden: bool = data["isMinimapHidden"]
        self.orb_count: int = data["orbCount"]
        self.rounds_per_half: int = data["roundsPerHalf"]
        self.team_roles: Union[list[str], None] = data["teamRoles"]
        self.game_feature_overrides: Union[list[GameFeatureOverride], None] = None
        self.game_rule_bool_overrides: Union[list[GameRuleBoolOverride], None] = None
        self.display_icon: Media = Media(data["displayIcon"])
        self.asset_path: str = data["assetPath"]

    def _update(self, data: GameModePayload):

        game_feat_override = data["gameFeatureOverrides"]
        game_rule_override = data["gameRuleBoolOverrides"]

        if game_feat_override:
            self.game_feature_overrides = []

            for game_feat in game_feat_override:
                self.game_feature_overrides.append(GameFeatureOverride(game_feat))

        if game_rule_override:
            self.game_rule_bool_overrides = []

            for game_rule in game_rule_override:
                self.game_rule_bool_overrides.append(GameRuleBoolOverride(game_rule))

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<{self.__class__.name} {self.name}>"


class GameModeEquippable:
    """Represents a game mode equippable

    Attributes
    ----------
    uuid: :class:`str`
        The equippables UUID.
    name: :class:`str`
        The name.
    category: :class:`str`
        The equippable's category
    display_icon: :class:`valorant.Media`
        The display icon.
    kill_stream_icon: :class:`valorant.Media`
        The kill stream icon.
    asset_path: :class:`str`
        The asset path on the API.
    """

    __slots__ = (
        "uuid",
        "name",
        "category",
        "display_icon",
        "kill_stream_icon",
        "asset_path",
    )

    def __init__(self, data: GameModeEquippablePayload) -> None:
        self.uuid: str = data["uuid"]
        self.name: str = data["displayName"]
        self.category: str = data["category"]
        self.display_icon: Media = Media(data["displayIcon"])
        self.kill_stream_icon: Media = Media(data["killStreamIcon"])
        self.asset_path: str = data["assetPath"]

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<{self.__class__.name} {self.name}>"
