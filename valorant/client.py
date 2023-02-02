from typing import Generator

from .agents import Agent
from .buddies import Buddy, BuddyLevel
from .bundles import Bundle
from .http_client import HTTPClient, Route
from .langs import Language


class ValClient:
    """Represents the main val client

    Parameters
    ----------
    lang: :class:`valorant.Language`
        The language to use for data fetching.
    """

    def __init__(self, lang: Language = Language.english) -> None:
        self.lang = lang.value
        self._http_client = HTTPClient(self.lang)

    def fetch_agents(self) -> list[Agent]:
        """Fetches all agents in the game.

        Returns:
            list[:class:`valopy.Agents`]
        """

        agents = []
        data = self._http_client.request(
            Route("/agents"),
            **{"isPlayableCharacter": True}
        )

        for agent in data:
            agents.append(Agent(agent))

        return agents

    def fetch_agent(self, uuid: str, /) -> Agent:
        """Fetches an agent by their UUID.

        Parameters
        ----------
        uuid: :class:`str`
            The UUID of the agent to search for.

        Returns
        ----------
        :class:`valorant.Agent`
            A valorant agent.

        Raises
        ----------
        NotFound:
            If the UUID provided does not match an agent.
        """

        data = self._http_client.request(
            Route(f"/agents/{uuid}")
        )

        return Agent(data)

    def fetch_buddies(self) -> Generator[Buddy, None, None]:
        """Fetches all gun buddies

        Yields
        ----------
        :class:`valorant.Buddy`
            A valorant gun buddy.
        """

        data = self._http_client.request(
            Route("/buddies")
        )

        for buddy in data:
            yield Buddy(buddy)

    def fetch_buddy(self, uuid: str, /) -> Buddy:
        """Fetches a gun buddy by its UUID

        Parameters
        ----------
        uuid: :class:`str`
            The UUID of the buddy to search for.

        Returns
        ----------
        :class:`valorant.Buddy`
            A valorant gun buddy.

        Raises
        ----------
        NotFound:
           If the UUID provided does not match a gun buddy.
        """

        data = self._http_client.request(
            Route(f"/buddies/{uuid}")
        )

        return Buddy(data)

    def fetch_buddy_levels(self) -> Generator[BuddyLevel, None, None]:
        """Fetches all gun buddies

        Yields
        ----------
        :class:`valorant.BuddyLevel`
            A valorant gun buddy level.
        """

        data = self._http_client.request(
            Route("/buddies/levels")
        )

        for level in data:
            yield BuddyLevel(level)

    def fetch_buddy_level(self, uuid: str, /) -> BuddyLevel:
        """Fetches a gun buddy level by its UUID

        Parameters
        ----------
        uuid: :class:`str`
            The UUID of the buddy level to search for.

        Returns
        ----------
        :class:`valorant.Buddy`
            A valorant gun buddy.

        Raises
        ----------
        NotFound:
           If the UUID provided does not match a buddy level.
        """

        data = self._http_client.request(
            Route(f"/buddies/levels/{uuid}")
        )

        return BuddyLevel(data)

    def fetch_bundles(self) -> Generator[Bundle, None, None]:
        """Fetches valorant bundles.

        Yields
        ----------
        :class:`valorant.Bundle`
            A valorant bundle.
        """

        data = self._http_client.request(
            Route("/bundles")
        )

        for bundle in data:
            yield Bundle(bundle)

    def fetch_bundle(self, uuid: str, /) -> Bundle:
        """Fetches a valorant bundle.

        Parameters
        ----------
        uuid: :class:`str`
            The UUID of the bundle to search for.

        Returns
        ----------
        :class:`valorant.Bundle`
            A valorant bundle.

        Raises
        ----------
        NotFound:
            If the UUID provided does not match a bundle.
        """

        data = self._http_client.request(
            Route(f"/bundles/{uuid}")
        )

        return Bundle(data)
