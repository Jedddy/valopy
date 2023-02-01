from valorant import ValClient


client = ValClient()


def test_buddies():
    buddies = [i for i in client.fetch_buddies()]

    assert len(buddies) > 1


def test_buddy():
    buddy = client.fetch_buddy("f2f07eae-4518-15eb-546b-018961e0dd60")

    assert buddy.name == "Task Force 809 Buddy"
    assert buddy.hidden_if_not_owned == False
    assert buddy.theme_uuid == None

def test_buddy_level():
    buddylevel = client.fetch_buddy_level("6c3b1a9e-4067-7ed6-fc6c-fea61e0a057c")
    buddylevel2 = client.fetch_buddy_level("b1fa66b4-4401-415a-03fd-d2862fae97ab")

    assert buddylevel.name == "809"
    assert buddylevel2.name == "A21"
