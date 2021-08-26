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
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if 'palavrao' in message.content:
            await message.channel.send(f"Por favor, {message.author.name}, não ofenda os demais usuários! ")

            await message.delete()
        

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error,CommandNotFound):
            await ctx.send("Por favor, use um comando existente, para saber todos os comandos digite !comando ")

        else:
            raise error    


def setup(bot):
    bot.add_cog(Manager(bot))         