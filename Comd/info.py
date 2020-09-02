import discord
from discord.ext import commands

class Infa(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["info", "Info", "Инфо"])
    async def инфа(self, ctx, *, arg):
        if arg == "?":
            emb = discord.Embed(title = f'Команда "/инфа"',colour = discord.Color.red())
            emb.description = "Показывает основную информацию о боте"
            emb.add_field(name = "**Создатель**", value = "Разработчик бота")
            emb.add_field(name = "**Использует модули**", value = "Модули которые использует бот")
            await ctx.send(embed = emb)
        else:
            emb = discord.Embed(title = f"{self.client.user.name}",colour = discord.Color.red())
            emb.description = f"Я **{self.client.user.name}**!"
            emb.add_field(name = "Мои команды можно узнать написав `/хелп`",value = "или `/help`")
            emb.add_field(name = "**Создатель**",value = 'Hot_kota#4267')
            emb.add_field(name = "**Полезные ссылки**",value = "[Пригласить бота](https://discord.com/oauth2/authorize?client_id=737987355389984848&scope=bot&permissions=8)\n[Сервер подержки](https://discord.gg/rgsV2AQ)")
            emb.add_field(name = "**Использует модули**",value = f"[Discord.py {discord.__version__}](https://github.com/Rapptz/discord.py)\n[Memory-profiler](https://github.com/pythonprofilers/memory_profiler)")
            await ctx.send(embed = emb)

    @инфа.error
    async def Info_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            emb = discord.Embed(title = f"{self.client.user.name}",colour = discord.Color.red())
            emb.description = f"Я **{self.client.user.name}**!"
            emb.add_field(name = "Мои команды можно узнать написав `/хелп`",value = "или `/help`")
            emb.add_field(name = "**Создатель**",value = "Hot_kota#4267")
            emb.add_field(name = "**Полезные ссылки**",value = "[Пригласить бота](https://discord.com/oauth2/authorize?client_id=737987355389984848&scope=bot&permissions=8)\n[Сервер подержки](https://discord.gg/rgsV2AQ)")
            emb.add_field(name = "**Использует модули**",value = f"[Discord.py {discord.__version__}](https://github.com/Rapptz/discord.py)\n[Memory-profiler](https://github.com/pythonprofilers/memory_profiler)")
            await ctx.send(embed = emb)

def setup(client):
    client.add_cog(Infa(client))