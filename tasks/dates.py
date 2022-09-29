from discord.ext import commands, tasks
import datetime



class Dates(commands.Cog):
    """Clock and Exercises"""
    
    def __init__(self, bot):
        self.bot = bot 

    @commands.Cog.listener()
    async def on_ready(self):
        self.current_time.start()

    @tasks.loop(seconds=10)
    async def current_date(self):
        now = datetime.datetime.now()

        now = now.strftime("%d/%m/%Y ás %H:%M:%S")

        channel = self.bot.get_channel()

        await channel.send("Atividades para o próximo encontro dia 00/00/00 - 19:00 ! \n Ler o livro Tal \n Todos os dias CTD")



    @tasks.loop(seconds=60)
    async def current_time(self):
        now = datetime.datetime.now()

        now = now.strftime("%d/%m/%Y ás %H:%M:%S")

        channel = self.bot.get_channel(878749103100690507)

        await channel.send('Hora atual ' + now)

def setup(bot):
    bot.add_cog(Dates(bot)) 