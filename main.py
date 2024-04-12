import discord
import random
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
    
@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)



@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def mem(ctx):
    images = os.listdir("images")
    img_name = random.choice(images)
    with open(f'images/{img_name}', 'rb') as f:

       picture = discord.File(f)
    await ctx.send(file=picture)
    images = (os.listdir('images'))
@bot.command()
async def mem2(ctx):
    a = random.randint(0, 40)
    if a > 0 and a < 5:
        with open('images/mem1.jpg', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    elif a > 6 and a < 14:
        with open('images/mem2.jpg', 'rb') as f:тут
            picture = discord.File(f)
        await ctx.send(file=picture)
    elif a > 15 and a < 20:
        with open('images/mem3.jpg', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    elif a > 21 and a < 40:
        with open('images/mem4.jpg', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


bot.run("")
