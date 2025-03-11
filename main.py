import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

task_points = {}

@bot.event
async def on_ready():
    print(f'Bot {bot.user} olarak giriş yaptı!')

@bot.command()
async def craft(ctx, *, item: str):
    crafts = {
        "plastik şişe": "Kalemlik, saksı, mumluk yapabilirsiniz. 🎨",
        "pet şişe kapakları": "Mozaik sanat eserleri veya oyun materyalleri yapabilirsiniz. 🖌️",
        "plastik kaşık": "Dekoratif çiçekler veya avizeler yapabilirsiniz. ✨"
    }
    await ctx.send(crafts.get(item.lower(), "Bu eşya için elimde fikir yok. 😕"))

@bot.command()
async def recycle(ctx, *, item: str):
    recycle_guide = {
        "cam şişe": "Geri dönüşüm kutusuna atılmalı. ♻️",
        "plastik şişe": "Plastik geri dönüşüm kutusuna atılmalı. 🥤",
        "pil": "Atık pil toplama kutularına bırakılmalı. ⚡",
        "kağıt": "Kağıt geri dönüşüm kutusuna atılmalı. 📄",
        "metal kutu": "Metal geri dönüşüm kutusuna atılmalı. 🥫"
    }
    user = ctx.author.name
    task_points[user] = task_points.get(user, 0) + random.randint(1, 5)
    await ctx.send(recycle_guide.get(item.lower(), "Bu eşya için bir bilgi bulunamadı, yerel yönetiminizden bilgi alabilirsiniz."))
    await ctx.send(f"Tebrikler {user}! 🎉 Geri dönüşüm yaptığın için {task_points[user]} puan kazandın! 💚")

@bot.command()
async def decomposition(ctx, *, item: str):
    decomposition_time = {
        "plastik şişe": "450 yıl ⏳",
        "cam şişe": "1 milyon yıl ⏳",
        "kağıt": "2-6 hafta 📜",
        "muz kabuğu": "2-5 hafta 🍌",
        "metal kutu": "50 yıl ⏳"
    }
    await ctx.send(decomposition_time.get(item.lower(), "Bu eşya için elimde veri yok. 😕"))

@bot.command()
async def my_points(ctx):
    user = ctx.author.name
    points = task_points.get(user, 0)
    await ctx.send(f"{user}, şu ana kadar {points} geri dönüşüm puanı topladın! 🌿")

@bot.command()
async def help_me(ctx):
    help_text = (
        "**Komut Listesi:**\n"
        "$craft <eşya>: Plastik el işleri için fikir verir. 🎨\n"
        "$recycle <eşya>: Eşyanın nasıl geri dönüştürüleceğini söyler ve puan kazandırır. ♻️\n"
        "$decomposition <eşya>: Eşyanın doğada ne kadar sürede yok olduğunu söyler. ⏳\n"
        "$my_points: Geri dönüşümden kazandığın puanları gösterir. 🌱\n"
        "$help_me: Bu yardım mesajını gösterir. 📖"
    )
    await ctx.send(help_text)
    
    
bot.run("token")
