from .assets import Media
from .types.ability import AbilityPayload


class Ability:
    """This represents a valorant agent ability."""

    __slots__ = (
        "slot",
        "name",
        "description",
        "display_icon"
    )

    slot: str
    displayame: str
    description: str
    display_icon: Media

    def __init__(self, data: AbilityPayload) -> None:
        self.slot = data["slot"]
        self.name = data["displayName"]
        self.description = data["description"]
        self.display_icon: Media = Media(data["displayIcon"])

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<Ability {self.name}>"
