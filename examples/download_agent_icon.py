from valorant import ValClient

v = ValClient()

# fetch agents
for i in v.fetch_agents():
    
    # save the icons to an existing directory
    print(i.display_icon_small.save(fr"{i.name}.png"))