import discord
from discord.ext import commands

class Congress(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.members = {}

    @commands.command(name='register')
    async def register_member(self, ctx, *, member_name: str):
        """Register a new member."""
        if member_name in self.members:
            await ctx.send(f"{member_name} is already registered.")
        else:
            self.members[member_name] = {'name': member_name, 'registered_by': str(ctx.author)}
            await ctx.send(f"{member_name} has been registered!")

    @commands.command(name='profile')
    async def member_profile(self, ctx, *, member_name: str):
        """View a member's profile."""
        member_info = self.members.get(member_name)
        if member_info:
            await ctx.send(f"Profile of {member_name}: Registered by {member_info['registered_by']}.")
        else:
            await ctx.send(f"{member_name} is not registered.")


def setup(bot):
    bot.add_cog(Congress(bot))