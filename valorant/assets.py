"""Assets"""

import os
from typing import Union

import requests

from .types.assets import (
    MediaVoicePayload,
    VoiceLinePayload
)


class Media:
    """Represents a Media for the assets.

    Attributes
    ----------
    url: :class:`str`
        The media's url.
    """

    __slots__ = ("url",)

    url: Union[str, None]

    def __init__(self, url: Union[str, None]) -> None:
        self.url = url

    def save(self, path: Union[str, os.PathLike]) -> int | None:
        """Saves the media to a file path.

        If the only the filename and extension is supplied,
        save to the root dir of the project.

        Parameters
        ----------
        path: Union[:class:`str`, :class`os.PathLike`]
            The path to save the media file to.

        Returns
        ----------
        Optional[:class:`int`]
            The number of characters written.
        """

        if self.url:
            resp = requests.get(self.url)

            with open(path, "wb") as f:
                return f.write(resp.content)

        return None

    def to_bytes(self) -> bytes | None:
        """Returns the bytes of this media object."""

        if self.url:
            resp = requests.get(self.url)
            return resp.content

        return None


class MediaVoice:
    """Represents a voice line media

    Attributes
    ----------
    id: :class:`int`
        The voice line's id.
    wwise: :class:`valorant.Media`
        The wwise version of the voice line.
    wave: :class:`valorant.Media`
        The wave version of the voice line.
    """

    id: int
    wwise: Media
    wave: Media

    def __init__(self, data: MediaVoicePayload) -> None:
        self.id: int = data["id"]
        self.wwise: Media = Media(data["wwise"])
        self.wave: Media = Media(data["wave"])


class VoiceLine:
    """Represents a valorant agent voice line.

    Attributes
    ----------
    min_duration: :class:`float`
        The minimum duration of the voice line.
    max_duration: :class`float`
        The max duration of the voice line.
    media_list: List[:class:`Media`]
        A list of the voice line's media.
    """

    min_duration: float
    max_duration: float
    media_list: list[MediaVoice]

    def __init__(self, data: VoiceLinePayload) -> None:
        self.min_duration: float = data["minDuration"]
        self.max_duration: float = data["maxDuration"]
        self.media_list: list[MediaVoice] = []  # Place holder
        self._update(data["mediaList"])

    def _update(self, data: list[MediaVoicePayload]) -> None:
        for media in data:
            self.media_list.append(MediaVoice(media))
