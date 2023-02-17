from valorant import ValClient


client = ValClient()


def test_gear():
    gear = client.fetch_gear("822bcab2-40a2-324e-c137-e09195ad7692")

    assert gear.name == "Heavy Shields"
    assert gear.shop_data.can_be_trashed == False


def test_gears():
    gears = client.fetch_gears()

    assert len(gears) > 1
