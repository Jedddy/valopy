from typing import TypedDict


class RolePayload(TypedDict):
    uuid: str
    displayName: str
    description: str
    displayIcon: str
    assetPath: str
