import os
import discord


intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True
intents.members = True

client = discord.Client(intents=intents)
prefix = os.getenv("BOT_PREFIX", "s")


@client.event
async def on_ready():
    print(f"✅ Logged in as: {client.user}")
    await client.change_presence(
        activity=discord.Streaming(
            name="shelp | by snoopixx",
            url="https://www.twitch.tv/twitch"
        )
    )


async def handle_ping(message: discord.Message, client: discord.Client):
    latency = round(client.latency * 1000)
    await message.reply(f"🏓 **Pong!** `{latency}ms`")


@client.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    if message.content.strip().lower() == f"{prefix.lower()}ping":
        await handle_ping(message, client)


def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise SystemExit("❌ No Bot Token found")
    client.run(token)


if __name__ == "__main__":
    main()
