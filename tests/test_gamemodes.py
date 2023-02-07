import pytest

from valorant import ValClient
from valorant.errors import NotFound


client = ValClient()


def test_gamemodes():
    modes = client.fetch_gamemodes()

    assert len(modes) > 1


def test_gamemode():
    mode = client.fetch_gamemode("e921d1e6-416b-c31f-1291-74930c330b7b")

    assert mode.name == "Spike Rush"
    assert mode.team_roles is None


def test_equippables():
    eq = client.fetch_gamemode_equippables()

    assert len(eq) > 1

def test_equippable():
    eq = client.fetch_gamemode_equippable("c5de005c-4bdc-26a7-a47d-c295eaaae9d8")

    assert eq.name == "Classic"

