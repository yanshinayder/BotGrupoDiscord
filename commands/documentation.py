from discord.ext import commands
from discord.ext.commands import bot
import discord


class Doc(commands.Cog):
    """ Return documentation"""
    
    def __init__(self, bot):
        self.bot = bot 


    @commands.command(name='python')
    async def send_python(self, ctx):
        name = ctx.author.name

        response = name  + (" Aqui está a documentação do Python https://docs.python.org/pt-br/3/")

        await ctx.send(response)    



    #Documentação php
    @commands.command(name='php')
    async def send_php(self, ctx):
        name = ctx.author.name

        response = name  + (" Aqui está a documentação de PHP https://www.php.net/manual/pt_BR/index.php")

        await ctx.send(response)    


    #Documentação sql
    @commands.command(name='sql')
    async def send_sql(self, ctx):
        name = ctx.author.name

        response = name  + (" Aqui está a documentação de SQL https://docs.microsoft.com/pt-br/sql/?view=sql-server-ver15")

        await ctx.channel.send(response)  

    #Documentação git
    @commands.command(name='git')
    async def send_git(self, ctx):
        name = ctx.author.name

        response = name  + (" Aqui está a documentação de GIT https://git-scm.com/doc")

        await ctx.channel.send(response)  

    #Documentação Java
    @commands.command(name='java')
    async def send_java(self, ctx):
        name = ctx.author.name

        response = name  + (" Aqui está a documentação de JAVA https://docs.oracle.com/en/java/")

        await ctx.channel.send(response) 

    #Documentação Mobile
    @commands.command(name='kotlin')
    async def send_kotlin(self, ctx):
        name = ctx.author.name

        response = name  + (" Aqui está a documentação de KOTLIN https://kotlinlang.org/docs/home.html")

        await ctx.channel.send(response) 

    @commands.command(name='flutter')
    async def send_flutter(self, ctx):
        name = ctx.author.name

        response = name  + (" Aqui está a documentação de FLUTTER https://flutter.dev/docs")

        await ctx.channel.send(response) 


    @commands.command(name='node')
    async def send_node(self, ctx):
        name = ctx.author.name

        response = name  + (" Aqui está a documentação de NODE https://nodejs.org/en/docs/")

        await ctx.channel.send(response) 


def setup(bot):
    bot.add_cog(Doc(bot)) 