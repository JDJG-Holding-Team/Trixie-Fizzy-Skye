import discord, os , asyncio,traceback
import ClientConfig, B

bot=ClientConfig.bot

async def status_task():
  await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="Orders for Soda"))
  await asyncio.sleep(40)
  await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="Bot PFP made by Dutchy#6127(thank you) :D"))
  await asyncio.sleep(40)

async def startup():
  await bot.wait_until_ready()
  await status_task()

@bot.event
async def on_ready():
  print("Bot is Ready")
  print(f"Logged in as {bot.user}")
  print(f"Id: {bot.user.id}")


@bot.event
async def on_error(event,*args,**kwargs):
  more_information=os.sys.exc_info()
  error_wanted=traceback.format_exc()
  traceback.print_exc()
  
  #print(more_information[0])

B.b()
bot.loop.create_task(startup())
bot.run(os.environ["TOKEN"])
