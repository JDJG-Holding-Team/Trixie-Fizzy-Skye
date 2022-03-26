import discord
from discord.ext import commands


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def credits(self, ctx):
        embed = discord.Embed(title="Credits")
        embed.add_field(name="Programmer:", value="JDJG Inc. Official#3493")
        embed.add_field(name="Pfp maker:", value="Dutchy#6127")
        await ctx.send(embed=embed)

    @commands.command()
    async def list_prefixes(self, ctx):
        for x in await self.bot.command_prefix(self.bot, ctx.message):
            await ctx.send(x)


async def setup(bot):
    await bot.add_cog(Commands(bot))
