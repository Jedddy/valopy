from valorant import ValClient


client = ValClient()

# loop over the fetched agents
for agent in client.fetch_agents():

    # print the name of the agent
    print(agent.name)
