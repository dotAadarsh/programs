'''Create a directory named config/ and save tic_tac_toe.toml inside that directory.
config/
├── __init__.py
└── tic_tac_toe.toml
'''

import config

print(config.path)
print( config.tic_tac_toe)
print(config.tic_tac_toe["server"]["url"])
print(config.tic_tac_toe["constant"]["board_size"])

# You can now integrate a configuration into your existing projects by copying the config/ directory into your project and replacing the tic-tac-toe configuration with your own settings.