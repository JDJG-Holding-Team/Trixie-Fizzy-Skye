import discord
import re
from discord.ext import commands
import os

async def get_prefix(client,message):
  extras = ["Soda*","So*","sb!","sb*"]
  comp = re.compile("^(" + "|".join(map(re.escape, extras)) + ").*", flags=re.I)
  match = comp.match(message.content)
  if match is not None:
    extras.append(match.group(1))
  return commands.when_mentioned_or(*extras)(client, message)

bot = commands.Bot(command_prefix=(get_prefix),intents = discord.Intents.all())

bot.load_extension('jishaku')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
      try:
        bot.load_extension(f'cogs.{filename[:-3]}')
      except commands.errors.NoEntryPointError:
        pass
