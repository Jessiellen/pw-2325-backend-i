import discord
from discord.ext import commands


intents = discord.Intents().all()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print("Estou pronto! Conectado como o {bot.user}")

@bot.command(name="Hello")
async def send_hi(ctx):
    name = ctx.author.name

    response ="Hi," + name
    await ctx.send(response)
    
bot.run()