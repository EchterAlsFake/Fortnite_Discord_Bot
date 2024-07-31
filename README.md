> [!WARNING]
> This Bot is currently deprecated, because the API which I used won't support most of the endpoints anymore. I'll update it at some times, but now it won't work.
> Please wait for my upodate, and then you can use it again :)

> [!IMPORTANT]
> This repository may seem dead, but it isn't. If I don't tell otherwise above everything should be working from the codebase. It's just, that I may not always host the Bot.
<p align="center">
  <img src="https://github.com/EchterAlsFake/Fortnite_Discord_Bot/blob/657bc9b6d758f4649a9730ada9aa77e45c02b118/assets/Fortnite.png" alt="Fortnite Discord Bot Logo" width="200"/>
</p>

<h1 align="center">Fortnite Discord Bot</h1>
<p align="center">
<a href="https://github.com/EchterAlsFake/Porn_Fetch/workflows/CodeQL"><img src="https://github.com/EchterAlsFake/Porn_Fetch/workflows/CodeQL/badge.svg" alt="CodeQL Analysis"/></a>
</p>

<p align="center">
  <a href="https://discord.com/api/oauth2/authorize?client_id=1187896849739288749&scope=applications.commands"><strong>Invite to your server</strong></a>

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Setup](#setup)
   - [Requirements](#requirements)
   - [Installation](#installation)
   - [Running the Bot](#running-the-bot)
4. [Commands](#commands)
5. [License](#license)

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

# License
Licensed under GPL 3 
Copyright (C) 2023 Johannes Habel
