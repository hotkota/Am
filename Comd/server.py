import discord
from discord.ext import commands

class Server(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["server"])
    async def сервер(self, ctx):
        bot, human = 0, 0
        for member in  ctx.message.guild.members:
            if member.bot:
                bot += 1
            else:
                human += 1
        text, voice = len(ctx.message.guild.text_channels), len(ctx.message.guild.voice_channels)
        emb = discord.Embed(title = "Инфо о сервере", colour = discord.Color.red())
        emb.set_thumbnail(url = ctx.message.guild.icon_url)
        emb.description = f"Название: **{ctx.message.guild.name}**"
        emb.add_field(name = "Участники:", value = f"Всего: **{bot + human}**\nЛюдей: **{human}**\nБотов: **{bot}**")
        emb.add_field(name = "Каналы:", value = f"Всего: **{text + voice}**\nТекстовых: **{text}**\nГолосовых: **{voice}**")
        emb.add_field(name = "Владелец:", value = ctx.message.guild.owner)
        emb.add_field(name = "Регион:", value = ctx.message.guild.region)
        emb.add_field(name = "Уровень проверки:", value = ctx.message.guild.verification_level)
        emb.set_footer(text = f"ID: {ctx.message.guild.id}")
        await ctx.send(embed = emb)

def setup(client):
    client.add_cog(Server(client))