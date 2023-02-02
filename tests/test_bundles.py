from valorant import ValClient


client = ValClient()


def test_bundles():
    for bundle in client.fetch_bundles():
        assert bundle.uuid is not None
        assert bundle.display_icon.url is not None

