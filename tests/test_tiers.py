from valorant import ValClient
from valorant.errors import NotFound


client = ValClient()


def test_tier():
    episode = client.fetch_episode("03621f52-342b-cf4e-4f86-9350a49c6d04")
    assert episode.asset_object_name == "Episode5_CompetitiveTierDataTable"


def test_tiers():
    for episode in client.fetch_episodes():
        assert len(episode.tiers) > 1
