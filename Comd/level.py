import sqlite3
import discord
from discord.ext import commands

conn = sqlite3.connect("../am/data/DB/Database.db")
cursor = conn.cursor()

class Level(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["level", "lvl", "xp", "опыт"])
    async def уровень(self, ctx, *, arg):
        if arg != 18:
            pass
        else:
            if member.bot:
                await ctx.send("У ботов нет профиля")
            else:
                for row in cursor.execute(f"SELECT lvl, xp, name FROM users where id={arg}").fetchall():
                    emb = discord.Embed(title = f"Профиль {row[1]}",colour = discord.Color.red())
                    emb.description = f"Уровень: **{row[0]}**\nопыт: **{row[1]}**\nДо нового уровня: **{(5*row[0]**2+50*row[0]+100)-row[1]}**"
                    await ctx.send(embed = emb)
                    del row, emb


    @commands.command(aliases = ["level", "lvl", "xp", "опыт"])
    async def уровень(self, ctx, member: discord.Member):
        if member.bot:
            await ctx.send("У ботов нет профиля")
        else:
            for row in cursor.execute(f"SELECT lvl, xp FROM users where id={member.id}").fetchall():
                emb = discord.Embed(title = f"Профиль {ctx.message.author.name}",colour = discord.Color.red())
                emb.set_thumbnail(url = ctx.message.author.avatar_url)
                emb.description = f"Уровень: **{row[0]}**\nопыт: **{row[1]}**\nДо нового уровня: **{(5*row[0]**2+50*row[0]+100)-row[1]}**"
                await ctx.send(embed = emb)

    @уровень.error
    async def Level_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            for row in cursor.execute(f"SELECT lvl, xp FROM users where id={ctx.message.author.id}").fetchall():
                emb = discord.Embed(title = f"Профиль {ctx.message.author.name}",colour = discord.Color.red())
                emb.set_thumbnail(url = ctx.message.author.avatar_url)
                emb.description = f"Уровень: **{row[0]}**\nУровень: **{row[0]}**\nопыт: **{row[1]}**\nДо нового уровня: **{(5*row[0]**2+50*row[0]+100)-row[1]}**"
                await ctx.send(embed = emb)

def setup(client):
    client.add_cog(Level(client))