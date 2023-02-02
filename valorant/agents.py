from .abilities import Ability
from .assets import Media, VoiceLine
from .role import Role
from .types.agents import AgentPayload


class Agent:
    """Represents a valorant agent."""

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
        self._update_abilities(data)

    def _update_abilities(self, data: AgentPayload) -> None:
        self.abilities = []

        for ability in data["abilities"]:
            self.abilities.append(Ability(ability))

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<Agent {self.name}>"

    def __eq__(self, other) -> bool:
        return self.uuid == other.uuid

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)
