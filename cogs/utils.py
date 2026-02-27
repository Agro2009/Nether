import discord
from discord.ext import commands

class Utils(commands.Cog):
    """Utility commands for Discord bot"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping')
    async def ping(self, ctx):
        """Returns Pong!"""
        await ctx.send('Pong!')

    @commands.command(name='say')
    async def say(self, ctx, *, message: str):
        """Repeats the message provided."""
        await ctx.send(message)

    @commands.command(name='info')
    async def info(self, ctx):
        """Provides information about the bot."""
        await ctx.send('This is a utility command bot.')


def setup(bot):
    bot.add_cog(Utils(bot))