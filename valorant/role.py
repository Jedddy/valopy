from .assets import Media
from .types.role import RolePayload


class Role:
    """Represents a valorant agent role.

    Attributes
    ----------
    uuid: :class:`str`
        The role's UUID.
    name: :class:`str`
        The role name.
    description: :class:`str`
        The role's description
    display_icon: :class:`valorant.Media`
        The display icon.
    asset_path: :class:`str`
        The asset path on the API.
    """

    __slots__ = (
        "uuid",
        "name",
        "description",
        "display_icon",
        "asset_path",
    )

    uuid: str
    name: str
    description: str
    display_icon: Media
    asset_path: str

    def __init__(self, data: RolePayload) -> None:
        self.uuid: str = data["uuid"]
        self.name: str = data["displayName"]
        self.description: str = data["description"]
        self.asset_path: str = data["assetPath"]
        self.display_icon: Media = Media(data["displayIcon"])

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.name}>"
