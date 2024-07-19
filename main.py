import asyncio
import os
import re
import sys
import traceback

import discord
import dotenv
from discord.ext import commands

from cogs import EXTENSIONS

async def get_prefix(client, message):
    extras = ["Soda*", "So*", "sb!", "sb*"]
    comp = re.compile("^(" + "|".join(map(re.escape, extras)) + ").*", flags=re.I)
    match = comp.match(message.content)
    if match is not None:
        extras.append(match.group(1))
    return commands.when_mentioned_or(*extras)(client, message)


async def status_task(self):
    await self.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(type=discord.ActivityType.listening, name="Orders for Soda"),
    )
    await asyncio.sleep(40)
    await self.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(
            type=discord.ActivityType.listening, name="Bot PFP made by Dutchy#6127(thank you) :D"
        ),
    )
    await asyncio.sleep(40)


async def startup(self):
    await self.wait_until_ready()
    await status_task(self)


class TrixieSkye(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def setup_hook(self):
        await bot.load_extension("jishaku")

        for cog in EXTENSIONS:
            try:
                await self.load_extension(f"{cog}")
            except commands.errors.ExtensionError:
                traceback.print_exc()

        self.loop.create_task(startup(self))


bot = TrixieSkye(command_prefix=(get_prefix), intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Bot is Ready")
    print(f"Logged in as {bot.user}")
    print(f"Id: {bot.user.id}")


@bot.event
async def on_error(event, *args, **kwargs):
    more_information = sys.exc_info()
    error_wanted = traceback.format_exc()
    traceback.print_exc()

    # print(more_information[0])


dotenv.load_dotenv()
bot.run(os.environ["TOKEN"])
