from .assets import Media
from .types.role import RolePayload


class Role:
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
        return f"<Role {self.name}>"
