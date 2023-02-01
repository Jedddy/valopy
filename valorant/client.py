from .agents import Agent
from .http_client import HTTPClient, Route
from .langs import Language


class ValClient:
    """Represents the main val client"""

    def __init__(self, lang: Language = Language.english) -> None:
        self.lang = lang.value
        self.http_client = HTTPClient(self.lang)

    def fetch_agents(self) -> list[Agent]:
        """Fetches all agents in the game.

        Returns:
            list[:class:`valopy.Agents`]
        """

        agents = []
        data = self.http_client.request(
            Route("/agents"),
            **{"isPlayableCharacter": True}
        )

        for agent in data:
            agents.append(Agent(agent))

        return agents

    def fetch_agent(self, uuid: str, /):
        """Fetches an agent by their uuid."""

        data = self.http_client.request(
            Route(f"/agents/{uuid}")
        )

        return Agent(data)
