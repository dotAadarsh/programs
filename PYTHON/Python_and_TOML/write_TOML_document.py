import tomli_w

config = {
         "user": {
         "player_x": {"symbol": "X", "color": "blue", "ai": True},
         "player_o": {"symbol": "O", "color": "green", "ai": False},
         "ai_skill": 0.85,
        },
        "board_size": 3,
        "server": {"url": "https://tictactoe.example.com"},
}

print(tomli_w.dumps(config))

# dumps() writes to a string that you can continue to process. If you want to store your new TOML document directly to disk, then you can call dump() instead.
