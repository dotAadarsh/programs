import tomlkit
with open("tic-tac-toe-config.toml", mode = "rt", encoding = "UTF-8") as fp:
    config = tomlkit.load(fp)


print(config, type(config))

print(config["user"]["player_o"]["color"])

print(config["user"]["player_o"]["color"].upper())


config.add("app_name", "Tic-Tac-Toe")
print(config)