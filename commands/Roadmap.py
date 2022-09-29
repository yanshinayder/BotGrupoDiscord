from discord.ext import commands
from discord.ext.commands import bot
import discord

class Line(commands.Cog):
    """Return Roadmap for Users"""

    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='RoadMap')
    async def send_RmBack(self, ctx):
        name = ctx.author.name

        response = name + ("https://roadmap.sh/")    

        await ctx.channel.send(response)

def setup(bot):
    bot.add_cog(Line(bot))        