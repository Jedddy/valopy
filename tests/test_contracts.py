from valorant import ValClient


client = ValClient()


def test_contract():
    for contract in client.fetch_contracts():
        assert isinstance(contract.ship_it, bool)

def test_contract_fade():
    contract = client.fetch_contract("7ae5ad85-400b-beba-989d-42924ccf39be")

    assert contract.display_icon.save("test.png") is None
    assert contract.ship_it == False
    assert len(contract.content.chapters) > 1
    assert contract.content.relation_type == "Agent"
    assert contract.content.premium_vp_cost == -1
    assert contract.name == "Fade Contract"


def test_contract_act():
    contract = client.fetch_contract("7b06d4ce-e09a-48d5-8215-df9901376fa7")

    for reward in contract.content.chapters:
        assert reward.free_rewards is not None
        assert isinstance(reward.free_rewards, list)
