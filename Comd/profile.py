import sqlite3
import discord
from discord.ext import commands

class Profile(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["profile", "account"])
    async def профиль(self, ctx, *, arg):
        if arg != 18:
            pass
        else:
            if member.bot:
                await ctx.send("У ботов нет профиля")
            else:
                with sqlite3.connect("../am/data/DB/Database.db") as conn:
                    cursor = conn.cursor()
                    for row in cursor.execute(f"SELECT money, lvl, xp, desc, name FROM users where id={arg}").fetchall():
                        emb = discord.Embed(title = f"Профиль {row[4]}",colour = discord.Color.red())
                    if row[3] == " ":
                        emb.description = 'Для дополнительной информации напишите "/осебе"'
                    else:
                        emb.description = row[3]
                    emb.add_field(name = "Основная информация:", value = f"Баланс: **{row[0]}**\nУровень: **{row[1]}**\nОпыт: **{row[2]}**\nДо нового уровня: **{(5*row[1]**2+50*row[1]+100)-row[2]}** xp")
                    await ctx.send(embed = emb)


    @commands.command(aliases = ["profile", "account"])
    async def профиль(self, ctx, member: discord.Member):
        if member.bot:
            await ctx.send("У ботов нет профиля")
        else:
            with sqlite3.connect("../am/data/DB/Database.db") as conn:
                cursor = conn.cursor()
                for row in cursor.execute(f"SELECT money,lvl,xp,desc FROM users where id={member.id}").fetchall():
                    emb = discord.Embed(title = f"Профиль {member.name}",colour = discord.Color.red())
                    if row[3] == " ":
                        emb.description = 'Для дополнительной информации напишите "/осебе"'
                    else:
                        emb.description = row[3]
                    emb.set_thumbnail(url = member.avatar_url)
                    emb.add_field(name = "Основная информация:", value = f"Баланс: **{row[0]}**\nУровень: **{row[1]}**\nОпыт: **{row[2]}**\nДо нового уровня: **{(5*row[1]**2+50*row[1]+100) - row[2]}** xp")
                    await ctx.send(embed = emb)

    @профиль.error
    async def Profile_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            with sqlite3.connect("../am/data/DB/Database.db") as conn:
                cursor = conn.cursor()
                for row in cursor.execute(f"SELECT money,lvl,xp,desc FROM users where id={ctx.message.author.id}").fetchall():
                    emb = discord.Embed(title = f"Профиль {ctx.message.author.name}",colour = discord.Color.red())
                    if row[3] == " ":
                        emb.description = 'Для дополнительной информации напишите "/осебе"'
                    else:
                        emb.description = row[3]
                    emb.set_thumbnail(url = ctx.message.author.avatar_url)
                    emb.add_field(name = "Основаная информация:", value = f"Баланс: **{row[0]}**\nУровень: **{row[1]}**\nОпыт: **{row[2]}**\nДо нового уровня: **{(5*row[1]**2+50*row[1]+100) - row[2]}** xp")
                    await ctx.send(embed = emb)

def setup(client):
    client.add_cog(Profile(client))