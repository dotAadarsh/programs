import tomli

with open("tic_tac_toe.toml", mode="rb") as fp:
  config = tomli.load(fp) # using load() to read the file

print(config)

print(config["user"]["player_o"])

print(config["server"]["url"])


# If you already have the TOML document represented as a string, then you can use loads() instead of load().
toml_str = """
    offset_date-time_utc = 2021-01-12 00:23:45Z
    potpourri = ["flower", 1749, { symbol = "X", color = "blue" }, 1994-02-14]
    """

print(tomli.loads(toml_str))

# Both load() and loads() convert TOML documents to Python dictionaries, and you can use them interchangably. 
