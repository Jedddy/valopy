"""Abilities"""

from .assets import Media
from .types.ability import AbilityPayload


class Ability:
    """This represents a valorant agent ability.

    Attributes
    ----------
    slot: :class:`str`
        The slot of the ability.
    name: :class:`str`
        The name of the ability.
    description: :class:`str`
        The description of the ability.
    display_icon: :class:`valorant.Media`
        A media object of the display icon.
    """

    __slots__ = (
        "slot",
        "name",
        "description",
        "display_icon"
    )

    slot: str
    name: str
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
        return f"<{self.__class__.__name__} {self.name}>"
