import datetime
from typing_extensions import TypeAlias

import discord
from discord import message   
from discord.ext import commands, tasks 


bot = commands.Bot("!")

@bot.event
async def on_ready():
    print(f"Estou pronto! Estou conectado como {bot.user} ")
    current_time.start()    

@bot.event
async def on_message(message):
    
    if message.author == bot.user:
        return 
    
    if 'palavrao' in message.content:
        await message.channel.send (f"Por favor, {message.author.name}, não ofenda os demais usuários! ")

        await message.delete()

    await bot.process_commands(message) 

@bot.command(name='oi')
async def send_hello(ctx):
    name = ctx.author.name

    response = "Olá, " + name

    await ctx.send(response)


##########Documentação############


#aDocumentaçãopython
@bot.command(name='python')
async def send_link(ctx):
    name = ctx.author.name

    response = name  + (" Aqui está a documentação do Python https://docs.python.org/pt-br/3/")

    await ctx.send(response)    

#Documentação php
@bot.command(name='php')
async def send_link(ctx):
    name = ctx.author.name

    response = name  + (" Aqui está a documentação de PHP https://www.php.net/manual/pt_BR/index.php")

    await ctx.send(response)    

#Documentação sql
@bot.command(name='sql')
async def send_link(ctx):
    name = ctx.author.name

    response = name  + (" Aqui está a documentação de SQL https://docs.microsoft.com/pt-br/sql/?view=sql-server-ver15")

    await ctx.channel.send(response)  

#Documentação git
@bot.command(name='git')
async def send_link(ctx):
    name = ctx.author.name

    response = name  + (" Aqui está a documentação de GIT https://git-scm.com/doc")

    await ctx.channel.send(response)  

#Documentação Java
@bot.command(name='java')
async def send_link(ctx):
    name = ctx.author.name

    response = name  + (" Aqui está a documentação de JAVA https://docs.oracle.com/en/java/")

    await ctx.channel.send(response) 

#Documentação Mobile
@bot.command(name='kotlin')
async def send_link(ctx):
    name = ctx.author.name

    response = name  + (" Aqui está a documentação de KOTLIN https://kotlinlang.org/docs/home.html")

    await ctx.channel.send(response) 

@bot.command(name='flutter')
async def send_link(ctx):
    name = ctx.author.name

    response = name  + (" Aqui está a documentação de FLUTTER https://flutter.dev/docs")

    await ctx.channel.send(response) 


##########Documentação############


@bot.command(name='contato')
async def secret(ctx):
    try:
        await ctx.author.send("Linkedin - teste ")
        await ctx.author.send("Grupo no Telegram - exemplo")
        await ctx.author.send("Link para o Nutror - https://www.nutror.com/")
    except discord.errors.Forbidden:
        await ctx.send("Por favor Habilite a Opção para receber mensagens de qualquer pessoa do servidor (Opções -> Privacidade e Segurança)")

@tasks.loop(seconds=30)
async def current_time():
    now = datetime.datetime.now()

    now = now.strftime("%d/%m/%Y ás %H:%M:%S")

    channel = bot.get_channel(879393059308175370)

    await channel.send("Atividades para o próximo encontro dia 00/00/00 - 19:00 ! \n Ler o livro Tal \n Assistir ao video 1 \n Assistir apresentação pessoal no nutror \n Todos os dias CTD")
                        


bot.run("ODc4NzQ3NTc4MzI0Mzc3NjEx.YSFrdQ.EtPSE1UBVnCn5KNOpxi7e5O0AUo")
