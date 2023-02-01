"""Assets"""

import os
from typing import Union

import requests

from .types.assets import (
    MediaVoicePayload,
    VoiceLinePayload
)


class Media:
    """Represents an Media for the assets."""

    __slots__ = ("url",)

    url: Union[str, None]

    def __init__(self, url: str) -> None:
        self.url = url or None

    def save(self, path: Union[str, os.PathLike]) -> int | None:
        """Saves the media to a file path.

        If the only the filename and extension is supplied,
        save to the root dir of the project.

        Parameters:
            path: Union[:class:`str`, :class`os.PathLike`]
                The path to save the media file to.
        """

        if self.url:
            resp = requests.get(self.url)

            with open(path, "wb") as f:
                return f.write(resp.content)

        return None

    def to_bytes(self) -> bytes | None:
        """Returns the bytes of a media"""

        if self.url:
            resp = requests.get(self.url)
            return resp.content

        return None


class MediaVoice(Media):
    id: int
    wwise: Media
    wave: Media

    def __init__(self, data: MediaVoicePayload) -> None:
        self.id: int = data["id"]
        self.wwise: Media = Media(data["wwise"])
        self.wave: Media = Media(data["wave"])


class VoiceLine:
    """Represents a valorant agent voice line."""
    min_duration: float
    max_duration: float
    media_list: list[MediaVoice]

    def __init__(self, data: VoiceLinePayload) -> None:
        self.min_duration: float = data["minDuration"]
        self.max_duration: float = data["maxDuration"]
        self.media_list: list = []  # Place holder
        self._update_media(data["mediaList"])

    def _update_media(self, data: list[MediaVoicePayload]) -> None:
        for media in data:
            self.media_list.append(MediaVoice(media))
