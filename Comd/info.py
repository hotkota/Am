import discord
import requests
import memory_profiler
from discord.ext import commands
from importlib import import_module

cfg = import_module("config").prefix

class Infa(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["info", "Info", "Инфо"])
    async def инфа(self, ctx, *, arg):
        emb = discord.Embed(title = f"{self.client.user.name}", colour = discord.Color.red())
        emb.description = f"Я **{self.client.user.name}**!"
        emb.add_field(name = "Мои команды можно узнать написав", value = f"`{cfg}хелп` или `{cfg}help`")
        emb.add_field(name = "Создатель", value = 'Hot_kota#4267')
        emb.add_field(name = "Полезные ссылки", value = "[Пригласить бота](https://discord.com/oauth2/authorize?client_id=737987355389984848&scope=bot&permissions=8)\n[Сервер подержки](https://discord.gg/rgsV2AQ)")
        emb.add_field(name = "Использует модули", value = f"[Discord.py {discord.__version__}](https://github.com/Rapptz/discord.py)\n[Memory-profiler 0.57.0](https://github.com/pythonprofilers/memory_profiler)\n[requests 2.24.0](https://github.com/psf/requests)")
        await ctx.send(embed = emb)

    @инфа.error
    async def Info_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            emb = discord.Embed(title = f"{self.client.user.name}", colour = discord.Color.red())
            emb.description = f"Я **{self.client.user.name}**!"
            emb.add_field(name = "Мои команды можно узнать написав", value = f"`{cfg}хелп` или `{cfg}help`")
            emb.add_field(name = "Создатель", value = "Hot_kota#4267")
            emb.add_field(name = "Полезные ссылки", value = "[Пригласить бота](https://discord.com/oauth2/authorize?client_id=737987355389984848&scope=bot&permissions=8)\n[Сервер подержки](https://discord.gg/rgsV2AQ)")
            emb.add_field(name = "Использует модули", value = f"[Discord.py {discord.__version__}](https://github.com/Rapptz/discord.py)\n[Memory-profiler {memory_profiler.__version__}](https://github.com/pythonprofilers/memory_profiler)\n[requests {requests.__version__}](https://github.com/psf/requests)")
            await ctx.send(embed = emb)

def setup(client):
    client.add_cog(Infa(client))