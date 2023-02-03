"""Ceremonies"""

from .types.ceremonies import CeremonyPayload


class Ceremony:
    """Represents a valorant kill ceremony.

    Attributes
    ----------
    uuid: :class:`str`
        The ceremony UUID.
    name: :class:`str`
        The ceremony name.
    asset_path: :class:`str`
        The asset path on the API.
    """

    __slots__ = (
        "uuid",
        "name",
        "asset_path",
    )

    uuid: str
    name: str
    asset_path: str

    def __init__(self, data: CeremonyPayload):
        self.uuid: str = data["uuid"]
        self.name: str = data["displayName"]
        self.asset_path: str = data["assetPath"]
