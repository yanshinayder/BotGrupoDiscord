from discord.ext import commands
from discord.ext.commands import bot
import discord

class Talks(commands.Cog):
    """Talks with user"""
    
    def __init__(self, bot):
        self.bot = bot 



    @commands.command(name='oi')
    async def send_hello(self, ctx):
        name = ctx.author.name

        response = "Olá, " + name

        await ctx.send(response)



    '''@commands.command(name='contato')
    async def secret(self, ctx):
        try:
            await ctx.author.send("Linkedin - teste ")
            await ctx.author.send("Grupo no Telegram - exemplo")
            await ctx.author.send("Link para o Nutror - https://www.nutror.com/")
        except discord.errors.Forbidden:
            await ctx.send("Por favor Habilite a Opção para receber mensagens de qualquer pessoa do servidor (Opções -> Privacidade e Segurança)")'''

    @commands.command(name='comando')
    async def send_commands(self, ctx):
        name = ctx.author.name

        response = name + ('''
        !oi - Boas vindas
        !contato - Contatos dos administradores
        !python - Documentação Python
        !php - Documentação PHP
        !sql - Documentação SQL
        !git - Documentação Git
        !java - Documentação Java
        !kotlin - Documentação kotlin
        !flutter - Documentação Flutter
        !node - Documentação Node     
        !Delphi - Documentação Delphi
        !Golang - Documentação Golang  
        !Javascript - Documentação Javascript 
        ''')

        await ctx.send(response)

def setup(bot):
    bot.add_cog(Talks(bot )) 