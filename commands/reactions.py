from discord.ext import commands
from discord.ext.commands import bot

class Reactions(commands.Cog):
    """Interactions and positions"""
    
    def __init__(self, bot):
        self.bot = bot 

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        print(reaction.emoji)
        if reaction.emoji == "📒":
            role = user.guild.get_role()
            await user.add_roles(role)
        elif reaction.emoji == "📕":
            role = user.guild.get_role()   
            await user.add_roles(role)
        elif reaction.emoji == "📗":
            role = user.guild.get_role()
            await user.add_roles(role)


def setup(bot):
    bot.add_cog(Reactions(bot )) 