from typing import TypedDict


class EventPayload(TypedDict):
    uuid: str
    displayName: str
    shortDisplayName: str
    startTime: str
    endTime: str
    assetPath: str
