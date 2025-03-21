import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
client = discord.Client(intents=intents)
slash = discord.app_commands.CommandTree(client)

@client.event
async def on_ready():
    await slash.sync()
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print(f'Slash commands synced.')


@slash.command(name="ping", description="Replies with latency and status info")
async def ping(interaction: discord.Interaction):
    latency_ms = round(client.latency * 1000)  # latency in ms
    await interaction.response.send_message(
        f"🏓 Pong!\n"
        f"📡 Latency: `{latency_ms}ms`\n"
        f"✅ Bot is online and responding."
    )

client.run(TOKEN)
