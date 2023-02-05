"""Agents"""

from .abilities import Ability
from .assets import Media, VoiceLine
from .role import Role
from .types.agents import AgentPayload


class Agent:
    """Represents a valorant agent.

    Attributes
    ----------
    uuid: :class:`str`
        The UUID of the agent.
    name: :class:`str`
        The name of the agent.
    description: :class:`str`
        The description about the agent.
    dev_name: :class:`str`
        The agent's developer name.
    tags: List[:class:`str`]
        The agent's tags.
    is_playable: :class:`bool`
        Indicates if the agent is playable.
    is_base_content: :class:`bool`
        Indicates if the agent is base content.
    is_available_for_test: :class:`bool`
        Indicates if the agent is available for testing.
    role: :class:`valorant.Role`
        The agent's role.
    abilities: :class:`valorant.Ability`
        The agent's abilities.
    display_icon: :class:`valorant.Media`
        The agent's display icon.
    display_icon_small: :class:`valorant.Media`
        A small version of the agent's display icon.
    bust_portrait: :class:`valorant.Media`
        A bust portrait of the agent.
    full_portrait: :class:`valorant.Media`
        A full portrait of the agent.
    full_portrait_v2: :class:`valorant.Media`
        A v2 full portrait of the agent.
    kill_feed_portrait: :class:`valorant.Media`
        The agent's kill feed portrait
    background: :class:`valorant.Media`
        The agent's background image.
    background_gradient_colors: List[:class:`str`]
        The agent's background gradient colors.
    asset_path: :class:`str`
        The agent's asset path on the API.
    is_full_portrait_right_facing: :class:`bool`
        Indicates if the full portrait is right facing.
    voice_line: :class:`valorant.VoiceLine`
        The agent's voicelines.
    """

    __slots__ = (
        "uuid",
        "name",
        "description",
        "dev_name",
        "tags",
        "is_playable",
        "is_base_content",
        "available_for_test",
        "role",
        "abilities",
        "display_icon",
        "display_icon_small",
        "bust_portrait",
        "full_portrait",
        "full_portrait_v2",
        "kill_feed_portrait",
        "background",
        "background_gradient_colors",
        "asset_path",
        "is_full_portrait_right_facing",
        "voice_line"
    )

    uuid: str
    name: str
    description: str
    dev_name: str
    tags: list[str]  # some results return `None`
    display_icon: Media
    display_icon_small: Media
    bust_portrait: Media
    full_portrait: Media
    full_portrait_v2: Media
    kill_feed_portrait: Media
    background: Media
    background_gradient_colors: list[str]
    asset_path: str
    is_full_portrait_right_facing: bool
    voice_line: VoiceLine
    is_playable: bool
    is_base_content: bool
    available_for_test: bool
    role: Role
    abilities: list[Ability]

    def __init__(self, data: AgentPayload) -> None:
        self.uuid: str = data["uuid"]
        self.name: str = data["displayName"]
        self.description: str = data["description"]
        self.dev_name: str = data["developerName"]
        self.tags: list[str] = data.get("characterTags", [])
        self.is_playable: bool = data["isPlayableCharacter"]
        self.available_for_test: bool = data["isAvailableForTest"]
        self.is_base_content: bool = data["isBaseContent"]
        self.display_icon: Media = Media(data["displayIcon"])
        self.display_icon_small: Media = Media(data["displayIconSmall"])
        self.bust_portrait: Media = Media(data["bustPortrait"])
        self.full_portrait: Media = Media(data["fullPortrait"])
        self.full_portrait_v2: Media = Media(data["fullPortraitV2"])
        self.kill_feed_portrait: Media = Media(data["killfeedPortrait"])
        self.background: Media = Media(data["background"])
        self.background_gradient_colors: list[str] = data["backgroundGradientColors"]
        self.asset_path: str = data["assetPath"]
        self.is_full_portrait_right_facing: bool = data["isFullPortraitRightFacing"]
        self.role: Role = Role(data["role"])
        self.voice_line: VoiceLine = VoiceLine(data["voiceLine"])
        self._update(data)

    def _update(self, data: AgentPayload) -> None:
        self.abilities = []

        for ability in data["abilities"]:
            self.abilities.append(Ability(ability))

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.name}>"

    def __eq__(self, other) -> bool:
        return self.uuid == other.uuid

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)
