import datetime

import discord   
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
        await message.channel.send(f"Por favor, {message.author.name}, não ofenda os demais usuários! ")

        await message.delete()

    await bot.process_commands(message) 

@bot.command(name='oi')
async def send_hello(ctx):
    name = ctx.author.name

    response = "Olá, " + name

    await ctx.send(response)

#ajuda para python
@bot.command(name='python')
async def send_link(ctx):
    name = ctx.author.name

    response = name  + (" Aqui está a documentação do Python https://docs.python.org/pt-br/3/")

    channel = bot.get_channel(878757566874808320)

    await ctx.send(response)    

#ajuda para php

@bot.command(name='php')
async def send_link(ctx):
    name = ctx.author.name

    response = name  + (" Aqui está a documentação de PHP https://www.php.net/manual/pt_BR/index.php")

    channel = bot.get_channel(879141986349764648)

    await ctx.send(response)    

#ajuda sql
@bot.command(name='sql')
async def send_link(ctx):
    name = ctx.author.name

    response = name  + (" Aqui está a documentação de SQL https://docs.microsoft.com/pt-br/sql/?view=sql-server-ver15")

    channel = bot.get_channel(879144228603703346)

    await ctx.channel.send(response)    

@bot.command(name='contato')
async def secret(ctx):
    try:
        await ctx.author.send("Linkedin - teste ")
        await ctx.author.send("Grupo no Telegram - exemplo")
        await ctx.author.send("blablablablabla")
    except discord.errors.Forbidden:
        await ctx.send("Por favor Habilite a Opção para receber mensagens de qualquer pessoa do servidor (Opções -> Privacidade e Segurança)")

@tasks.loop(minutes=10)
async def current_time():
    now = datetime.datetime.now()

    now = now.strftime("%d/%m/%Y ás %H:%M:%S")

    channel = bot.get_channel(878749103100690507)

    await channel.send("Data atual: " + now )


bot.run("ODc4NzQ3NTc4MzI0Mzc3NjEx.YSFrdQ.EtPSE1UBVnCn5KNOpxi7e5O0AUo")
