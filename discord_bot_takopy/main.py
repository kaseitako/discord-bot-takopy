import os

import nextcord
from dotenv import load_dotenv
from nextcord.ext import commands

load_dotenv()
server_id = int(os.environ.get("SERVER_ID"))
token = os.environ.get("DISCORD_BOT_TOKEN")

bot = commands.Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.slash_command(description="お返事するッピ！", guild_ids=[server_id])
async def ping(interaction: nextcord.Interaction):
    await interaction.send("pongッピ！")


bot.run(token)
