import sqlite3
import discord
from discord.ext import commands

conn = sqlite3.connect("../am/data/DB/Database.db")
cursor = conn.cursor()

class Balance(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["money", "balance", "Money", "Balance", "Баланс"])
    async def баланс(self, ctx, *, arg):
        if arg != 18:
            pass
        else:
            if member.bot:
                await ctx.send("У ботов нет профиля")
            else:
                for row in cursor.execute(f"SELECT money, name FROM users where id={arg}").fetchall():
                    emb = discord.Embed(title = f"Профиль {row[1]}",colour = discord.Color.red())
                    emb.description = f"Баланс: **{row[0]}**"
                    await ctx.send(embed = emb)
                    del row, emb

    @commands.command(aliases = ["money", "balance"])
    async def баланс(self, ctx, member: discord.Member):
        if member.bot:
            await ctx.send("У ботов нет профиля")
        else:
            for row in cursor.execute(f"SELECT money FROM users where id={member.id}").fetchall():
                emb = discord.Embed(title = f"Профиль {member.name}",colour = discord.Color.red())
                emb.set_thumbnail(url = member.avatar_url)
                emb.description = f"Баланс: **{row[0]}**"
                await ctx.send(embed = emb)
                

    @баланс.error
    async def Balance_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            for row in cursor.execute(f"SELECT money FROM users where id={ctx.message.author.id}").fetchall():
                emb = discord.Embed(title = f"Профиль {ctx.message.author.name}",colour = discord.Color.red())
                emb.set_thumbnail(url = ctx.message.author.avatar_url)
                emb.description = f"Баланс: **{row[0]}**"
                await ctx.send(embed = emb)

def setup(client):
    client.add_cog(Balance(client))