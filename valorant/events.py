"""Events"""

from datetime import datetime

from .types.events import EventPayload


class Event:
    """Represents a valorant event.

    Attributes
    ----------
    uuid: :class:`str`
        The event uuid.
    name: :class:`str`
        The event name.
    short_name: :class:`str`
        The short name.
    start_time: :class`datetime.datetime`
        The start time of the event.
    end_time: :class:`datetime.datetime`
        The end time of the event.
    asset_path: :class:`str`
        The asset_path on the API.
    """

    __slots__ = (
        "uuid",
        "name",
        "short_name",
        "start_time",
        "end_time",
        "asset_path",
    )

    def __init__(self, data: EventPayload) -> None:
        self.uuid: str = data["uuid"]
        self.name: str = data["displayName"]
        self.short_name: str = data["shortDisplayName"]
        self.asset_path: str = data["assetPath"]
        self.start_time: datetime = datetime.fromisoformat(data["startTime"].replace("Z", "+00:00"))
        self.end_time: datetime = datetime.fromisoformat(data["endTime"].replace("Z", "+00:00"))

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.name}>"
