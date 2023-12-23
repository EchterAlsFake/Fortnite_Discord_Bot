# Fortnite Discord Bot

## Table of Contents
1. Introduction
2. Features
3. Setup
   - Requirements
   - Installation
   - Running the Bot
4. Commands
5. Contribution
6. License
7. Contact

## Introduction
This Fortnite Discord Bot provides various functionalities related to Fortnite game statistics and information retrieval. It utilizes the [Fortnite API](https://fortnite-api.com) to fetch player stats, AES keys, creator codes, map locations, and map images. The bot is integrated with Discord using `discord.py` and `discord.app_commands`.

## Features
- Fetch player statistics for different input methods and game modes.
- Retrieve AES key information.
- Get Fortnite creator code details.
- Provide map locations and coordinates.
- Display the Fortnite map image.

## Setup

> [!IMPORTANT] 
> The Setup is only required, if you want to run the Bot locally. Otherwise, you can just invite it to the server and that's it

### Requirements
- Python 3.x
- Discord.py library
- Fortnite API access

### Installation
1. Clone the repository:
`git clone https://github.com/EchterAlsFake/Fortnite_Discord_Bot`
2. Install dependencies: `pip install discord hue_shift fortnite-api`
3. Create a `config.ini` file with your Fortnite API key and Discord Bot token:
```ini
[bot]
fortnite_api_key = YOUR_FORTNITE_API_KEY
client_secret = YOUR_DISCORD_BOT_TOKEN
```

### Running the Bot
Run the bot using the following command: `python main.py`


## Commands
- `/player_stats <player_name> <gamemode> <input_method>`: Fetches and displays statistics for a specified Fortnite player.
- `/get_creator_code_info <creator_code>`: Retrieves information related to a given Fortnite creator code.
- `/get_aes_key`: Returns the current AES key used in Fortnite.
- `/get_map_locations`: Provides a list of map locations with coordinates.
- `/get_map_image`: Displays the current Fortnite map image.
