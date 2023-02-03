import pytest

from valorant import ValClient
from valorant.errors import NotFound


client = ValClient()


def test_agent_error():
    with pytest.raises(NotFound):
        client.fetch_agent("nothing to see here.")

def test_ceremony_error():
    with pytest.raises(NotFound):
        client.fetch_agent("Testing")
