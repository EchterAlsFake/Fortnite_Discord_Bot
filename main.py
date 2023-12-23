import fortnite_api
import discord.app_commands

from configparser import ConfigParser
from discord.ext import commands
from hue_shift import return_color, reset

conf = ConfigParser()
conf.read('config.ini')
api_key = conf.get("bot", "fortnite_api_key")
discord_secret = conf.get("bot", "client_secret")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
api = fortnite_api.FortniteAPI(api_key)


def get_player_information(player_name, gamemode, input) -> dict:
    """
    :param player_name:
    :param gamemode:
    :param input:
    :return:
    """
    stats = api.stats.fetch_by_name(name=player_name)

    input_stats = getattr(stats.stats, input)
    mode_stats = getattr(input_stats, gamemode)

    return {
        "kills": mode_stats.kills,
        "deaths": mode_stats.deaths,
        "kd": mode_stats.kd,
        "players_outlived": mode_stats.players_outlived,
        "minutes_played": mode_stats.minutes_played,
        "matches": mode_stats.matches,
        "kills_per_match": mode_stats.kills_per_match,
        "top_5": mode_stats.top5,
        "top_12": mode_stats.top12,
        "winrate": mode_stats.win_rate,
        "score_per_match": mode_stats.scorePerMatch,
        "score": mode_stats.score,
        "score_per_min": mode_stats.score_per_min,
        "last_updated": mode_stats.last_modified,
        "kills_per_min": mode_stats.kills_per_min
    }


def get_aes_key() -> list[str]:
    aes_key = api.aes.fetch()
    aes_build = aes_key.build
    aes_main = aes_key.main_key
    return [aes_build, aes_main]


def get_creator_code(name):
    if api.creator_code.exists(name):
        information = api.creator_code.fetch(name)
        account_name = information.user.name
        account_id = information.user.id
        code = information.code
        data = [account_name, account_id, code]
        return data

    else:
        return False


def get_map_locations():
    map_object = api.map.fetch()
    for pois in map_object.pois:
        yield [pois.name, pois.id, pois.location.y, pois.location.x, pois.location.z]


def get_map_image():
    map_object = api.map.fetch()
    return map_object.poi_image


@bot.tree.command()
@discord.app_commands.describe(player_name="The name of the player", gamemode="The game mode", input_method="The input method")
@discord.app_commands.choices(gamemode=[
    discord.app_commands.Choice(name="Solo", value="solo"),
    discord.app_commands.Choice(name="Duo", value="duo"),
    discord.app_commands.Choice(name="Trio", value="trio")
],
    input_method=[
        discord.app_commands.Choice(name="Keyboard & Mouse", value="keyboard_mouse"),
        discord.app_commands.Choice(name="Touch", value="touch"),
        discord.app_commands.Choice(name="Gamepad", value="gamepad")
    ])
async def player_stats(interaction: discord.Interaction, player_name : str, gamemode : str, input_method : str):
    stats = get_player_information(player_name, input=input_method, gamemode=gamemode)

    await interaction.response.send_message(f"""
Name: {player_name}
Kills: {stats.get("kills")}
KD: {stats.get("kd")}
Deaths: {stats.get("deaths")}
Players outlived: {stats.get("players_outlived")}
Minutes played: {stats.get("minutes_played")}
Matches: {stats.get("matches")}
Kills per match: {stats.get("kills_per_match")}
Top 5: {stats.get("top_5")}
Top 12: {stats.get("top_12")}
Winrate: {stats.get("winrate")}
Score per match: {stats.get("score_per_match")}
Score: {stats.get("score")}
Score per min: {stats.get("score_per_min")}
Kills per min: {stats.get("kills_per_min")}
Last Modified: {stats.get("last_updated")}""")
    print(f"{return_color()}Responded player stats{reset()}")


@bot.tree.command(name="get_creator_code_info", description="The Creator Code")
async def get_creator_code(interaction: discord.Interaction, creator_code : str):
        data = get_creator_code(creator_code)
        if data is False:
            await interaction.response.send_message("Invalid Creator Code!")

        account_name = data[0]
        account_id = data[1]
        code = data[2]
        await interaction.response.send_message(f"""
Account Name: {account_name}
Account ID: {account_id}
Creator Code: {code}""")
        print(f"{return_color()}Responded a Creator Code{reset()}")

@bot.tree.command(name="get_aes_key", description="Returns AES key")
async def return_aes_key(interaction: discord.Interaction):
    aes = get_aes_key()
    build = aes[0]
    key = aes[1]
    await interaction.response.send_message(f"""
    Build: {build}
    Key: {key}""")
    print(f"{return_color()}Responded AES Key{reset()}")


@bot.tree.command(name="get_map_locations", description="Returns the exact coordinates for each city")
async def get_map_locations_(interaction: discord.Interaction):
    current_message = ""
    messages = []
    await interaction.response.send_message("Please wait...")
    for item in get_map_locations():
        name, id, y, x, z = item
        formatted_item = f"""Name: {name}, ID: {id} 
        Location: X: {x} 
        Location: Y: {y} 
        Location: Z: {z}\n"""

        # Check if adding this item will exceed the limit
        if len(current_message) + len(formatted_item) > 2000:
            messages.append(current_message)
            current_message = formatted_item
        else:
            current_message += formatted_item

    # Add the last message if it's not empty
    if current_message:
        messages.append(current_message)

    # Send each message
    for msg in messages:
        await interaction.followup.send(msg)

    print(f"{return_color()}Responded Location{reset()}")


@bot.tree.command(name="get_map_image", description="Shows the Fortnite Map Image")
async def get_map_image_(interaction: discord):
    await interaction.response.send_message(get_map_image())
    print(f"{return_color()}Responded an Image{reset()}")


@bot.event
async def on_ready():
    print(f"{return_color()}Bot is ready{reset()}")
    try:
        await bot.tree.sync()
        print(f"{return_color()}Synced application commands{reset()}")

    except Exception as e:
        print(e)

bot.run(discord_secret)
