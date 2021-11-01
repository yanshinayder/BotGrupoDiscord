from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound

class Manager(commands.Cog):
    """Manage the bot"""
    
    def __init__(self, bot):
        self.bot = bot 


    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Estou pronto! Estou conectado como {self.bot.user} ")
        

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error,CommandNotFound):
            await ctx.send("Use um comando existente, para saber todos os comandos digite !comando ")

        else:
            raise error    


def setup(bot):
    bot.add_cog(Manager(bot))         