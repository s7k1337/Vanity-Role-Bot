import discord
from discord.ext import commands
import json

with open("config.json") as f:
    config = json.load(f)

TOKEN = config["TOKEN"]
GUILD_ID = int(config["GUILD_ID"])
SUPPORTER_ROLE_ID = int(config["SUPPORTER_ROLE_ID"])
LOG_CHANNEL_ID = int(config["LOG_CHANNEL_ID"])
KEYWORDS = config["KEYWORDS"]

EMBED_AUTHOR_ICON = "image_link"  # Custom Author Icon
EMBED_COLOR_ROLE_ADDED = discord.Color(0xFA78D9)  # Embed color if the role was given
EMBED_COLOR_ROLE_REMOVED = discord.Color(0x6E1858)  # Embed color if the role was removed

intents = discord.Intents.default()
intents.presences = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is running! | Made by github.com/s7k1")

@bot.event
async def on_presence_update(before, after):
    if after.guild.id != GUILD_ID:
        return
    
    supporter_role = after.guild.get_role(SUPPORTER_ROLE_ID)
    log_channel = after.guild.get_channel(LOG_CHANNEL_ID)
    if not supporter_role or not log_channel:
        return

    status = ""
    if after.activity and isinstance(after.activity, discord.CustomActivity):
        status = after.activity.name.lower() if after.activity.name else ""
    
    has_keyword = any(kw in status for kw in KEYWORDS)

    if has_keyword:
        if supporter_role not in after.roles:
            await after.add_roles(supporter_role)
            embed = discord.Embed(color=EMBED_COLOR_ROLE_ADDED)
            embed.set_author(name=f"Author_name", icon_url=EMBED_AUTHOR_ICON)
            embed.description = f" Your Description"
            await log_channel.send(embed=embed)
            print(f"Added role - {after.name}")
    else:
        if supporter_role in after.roles:
            await after.remove_roles(supporter_role)
            embed = discord.Embed(color=EMBED_COLOR_ROLE_REMOVED)
            embed.set_author(name=f"Author_name", icon_url=EMBED_AUTHOR_ICON) 
            embed.description = f" Your Description "
            await log_channel.send(embed=embed)
            print(f"Removed role - {after.name}")

bot.run(TOKEN)
