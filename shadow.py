import discord
import os
import random
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

def ra_em():
    emoji = ["😀", "😋", "😭", "🎈", "✨", "🎮", "👻", "🐱‍👤"]
    return random.choice(emoji)

def flip_coin():
    flip = random.randint(1, 2)
    if flip == 1:
        return "YAZI"
    else:
        return "TURA"
    
def ra_sa():
    a = random.randint(0, 10)
    return a

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba, benim adım {bot.user}! Ben bir botum!')

@bot.command()
async def shadow(ctx):
    await ctx.send(f"Komutlar: !hello !shadow !sayı !heh !emoji !coin !mem !duck !dog")

@bot.command()
async def sayı(ctx):
    await ctx.send(ra_sa())

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def emoji(ctx):
    await ctx.send(ra_em())

@bot.command()
async def coin(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def mem(ctx):
    resimler_listesi = os.listdir('images') #['resim1.jpeg', 'resim2.jpeg', 'resim3.jpeg']
    with open(f'images/{random.choice(resimler_listesi)}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)

bot.run("TOKEN")
