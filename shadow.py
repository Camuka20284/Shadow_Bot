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

def ra_is():
    sekil = ["('‿')", "(★‿★)", "♪(´▽｀)", "(ツ)", "(⓿_⓿)", "(＞︿＜)"]
    return random.choice(sekil)

def flip_coin():
    flip = random.randint(1, 2)
    if flip == 1:
        return "YAZI"
    else:
        return "TURA"
    
def ra_sa():
    a = random.randint(0,100000)
    return a

def ra_re():
    renk = ["🔴","🟠","🟡","🟢","🔵","🟣","⚫"]
    return random.choice(renk)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba, benim adım {bot.user}! Ben bir botum!')

@bot.command()
async def yardım(ctx):
    await ctx.send(f"Komutlar: !hello !yardım !sayı !işaret !heh !topla !çıkar !çarp !böl !emoji !renk !para !mem !duck !dog")

@bot.command()
async def sayı(ctx):
    await ctx.send(ra_sa())

@bot.command()
async def işaret(ctx):
    await ctx.send(ra_is())

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def topla(ctx, toplanan_1 = 5, toplanan_2 = 5):
    await ctx.send(toplanan_1 + toplanan_2)

@bot.command()
async def çıkar(ctx, eksilen = 5, çıkan = 5):
    await ctx.send(eksilen - çıkan)

@bot.command()
async def çarp(ctx, çarpan_1 = 5, çarpan_2 = 5):
    await ctx.send(çarpan_1 * çarpan_2)

@bot.command()
async def böl(ctx, bölünen = 5, bölen = 5):
    await ctx.send(bölünen // bölen)

@bot.command()
async def emoji(ctx):
    await ctx.send(ra_em())

@bot.command()
async def renk(ctx):
    await ctx.send(ra_re())

@bot.command()
async def para(ctx):
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
