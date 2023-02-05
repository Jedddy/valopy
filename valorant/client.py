from typing import Generator

from .agents import Agent
from .buddies import Buddy, BuddyLevel
from .bundles import Bundle
from .ceremonies import Ceremony
from .content_tiers import ContentTier
from .contracts import Contract
from .currencies import Currency
from .competitive_tiers import Episode
from .http_client import HTTPClient, Route
from .langs import Language


class ValClient:
    """Represents the main val client

    Parameters
    ----------
    lang: Optional[:class:`valorant.Language`]
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

        data = self._http_client.request(
            Route("/agents"),
            **{"isPlayableCharacter": True}
        )

        return [Agent(agent) for agent in data]

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

    def fetch_ceremonies(self) -> list[Ceremony]:
        """Fetches valorant kill ceremonies.

        Returns
        ----------
        List[:class:`valorant.Ceremony`]
            A valorant kill ceremony.
        """

        data = self._http_client.request(
            Route("/ceremonies")
        )

        return [Ceremony(ceremony) for ceremony in data]

    def fetch_ceremony(self, uuid: str, /) -> Ceremony:
        """Fetches a valorant kill ceremony.

        Parameters
        ----------
        uuid: :class:`str`
            The UUID of the ceremony to search for.

        Returns
        ----------
        :class:`valorant.Ceremony`
            A valorant kill ceremony.

        Raises
        ----------
        NotFound:
            If the UUID provided does not match a ceremony
        """

        data = self._http_client.request(
            Route(f"/ceremonies/{uuid}")
        )

        return Ceremony(data)

    def fetch_episodes(self) -> list[Episode]:
        """Fetches all valorant competitive episodes.

        Returns
        ----------
        List[:class:`valorant.Episode`]
        """

        data = self._http_client.request(
            Route("/competitivetiers")
        )

        return [Episode(episode) for episode in data]

    def fetch_episode(self, uuid: str, /) -> Episode:
        """Fetches a valorant episode.

        Parameters
        ----------
        uuid: :class:`str`
            The UUID of the episode to search for.

        Returns
        ----------
        :class:`valorant.Episode`
            A valorant episode.

        Raises
        ----------
        NotFound:
            If the UUID provided does not match an episode.
        """

        data = self._http_client.request(
            Route(f"/competitivetiers/{uuid}")
        )

        return Episode(data)

    def fetch_content_tiers(self) -> list[ContentTier]:
        """Fetches all valorant content tiers.

        Returns
        ----------
        List[:class:`valorant.ContentTier`]
        """

        data = self._http_client.request(
            Route("/contenttiers")
        )

        return [ContentTier(tier) for tier in data]

    def fetch_content_tier(self, uuid: str, /) -> ContentTier:
        """Fetches a valorant content tier.

        Parameters
        ----------
        uuid: :class:`str`
            The UUID of the content tier to search for.

        Returns
        ----------
        :class:`valorant.ContentTier`
            A valorant content tier.

        Raises
        ----------
        NotFound:
            If the UUID provided does not match a content tier.
        """

        data = self._http_client.request(
            Route(f"/contenttiers/{uuid}")
        )

        return ContentTier(data)

    def fetch_contracts(self) -> Generator[Contract, None, None]:
        """Fetches all valorant contracts.

        Yields
        ----------
        :class:`valorant.Contract`
            A valorant contract.
        """

        data = self._http_client.request(
            Route("/contracts")
        )

        for contract in data:
            yield Contract(contract)

    def fetch_contract(self, uuid: str, /) -> Contract:
        """Fetches a valorant contract.

        Parameters
        ----------
        uuid: :class:`str`
            The UUID of the contract to search for.

        Returns
        ----------
        :class:`valorant.Contract`
            A valorant contract.

        Raises
        ----------
        NotFound:
            If the UUID provided does not match a contract.
        """

        data = self._http_client.request(
            Route(f"/contracts/{uuid}")
        )

        return Contract(data)

    def fetch_currencies(self) -> list[Currency]:
        """Fetches all valorant currencies.

        
        Returns
        ----------
        List[:class:`valorant.Currency`]
            A valorant courrency.
        """

        data = self._http_client.request(
            Route("/currencies")
        )

        return [Currency(currency) for currency in data]

    def fetch_currency(self, uuid: str, /) -> Currency:
        """Fetches a valorant currency.

        Parameters
        ----------
        uuid: :class:`str`
            The UUID of the currency to search for.

        Returns
        ----------
        :class:`valorant.Currency`
            A valorant currency.

        Raises
        ----------
        NotFound:
            If the UUID provided does not match a currency.
        """

        data = self._http_client.request(
            Route(f"/currencies/{uuid}")
        )

        return Currency(data)
