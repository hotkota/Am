import sqlite3
import discord
from discord.ext import commands
from importlib import import_module

class Profile(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["profile", "account"])
    async def профиль(self, ctx, member: discord.Member):
        if member.bot:
            await ctx.send("У ботов нет профиля")
        else:
            am = import_module("database")
            data = am.stat(member.id)
            emb = discord.Embed(title = f"Профиль {member.name}",colour = discord.Color.red())
            if data["desc"] == " ":
                emb.description = 'Для дополнительной информации напишите "/осебе"'
            else:
                emb.description = data["desc"]
            emb.set_thumbnail(url = member.avatar_url)
            emb.add_field(name = "Основаная информация:", value = f'Баланс: **{data["money"]}**\nУровень: **{data["lvl"]}**\nОпыт: **{data["xp"]}**\nДо нового уровня: **{(5*data["lvl"]**2+50*data["lvl"]+100) - data["xp"]}** xp')
            await ctx.send(embed = emb)

    @профиль.error
    async def Profile_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            am = import_module("database")
            data = am.stat(ctx.message.author.id)
            emb = discord.Embed(title = f"Профиль {ctx.message.author.name}",colour = discord.Color.red())
            if data["desc"] == " ":
                emb.description = 'Для дополнительной информации напишите "/осебе"'
            else:
                emb.description = data["desc"]
            emb.set_thumbnail(url = ctx.message.author.avatar_url)
            emb.add_field(name = "Основаная информация:", value = f'Баланс: **{data["money"]}**\nУровень: **{data["lvl"]}**\nОпыт: **{data["xp"]}**\nДо нового уровня: **{(5*data["lvl"]**2+50*data["lvl"]+100) - data["xp"]}** xp')
            await ctx.send(embed = emb)

def setup(client):
    client.add_cog(Profile(client))