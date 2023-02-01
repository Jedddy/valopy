from typing import TypedDict


class MediaVoicePayload(TypedDict):
    id: int
    wwise: str
    wave: str


class VoiceLinePayload(TypedDict):
    """Represents a valorant agent voice line."""
    minDuration: float
    maxDuration: float
    mediaList: list[MediaVoicePayload]
