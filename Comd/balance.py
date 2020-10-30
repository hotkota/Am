import sqlite3
import discord
from discord.ext import commands

class Balance(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["money", "balance"])
    async def баланс(self, ctx, *, arg):
        if len(arg) == 18:
            try:
                arg = int(arg)
                if isinstance(arg, int):
                    member = ctx.message.guild.get_member(arg)
                    print(member, arg, type(arg))
                    if member is None:
                        if member.bot:
                            await ctx.send("У ботов нет профиля")
                        else:
                            with sqlite3.connect("../am/data/DB/Database.db") as conn:
                                cursor = conn.cursor()
                                if cursor.execute(f"SELECT id FROM users WHERE id = {member.id}").fetchone() is not None:
                                    for row in cursor.execute(f"SELECT money, name FROM users where id={member.id}").fetchall():
                                        emb = discord.Embed(title = f"Профиль {row[1]}",colour = discord.Color.red())
                                        emb.description = f"Баланс: **{row[0]}**"
                                    await ctx.send(embed = emb)
                                else:
                                    await ctx.send("Данного пользователя нет в базе данных")
                            conn.close()
                    else:
                        with sqlite3.connect("../am/data/DB/Database.db") as conn:
                            cursor = conn.cursor()
                            if cursor.execute(f"SELECT id FROM users WHERE id = {arg}").fetchone() is not None:
                                for row in cursor.execute(f"SELECT money, name FROM users where id={member.id}").fetchall():
                                    emb = discord.Embed(title = f"Профиль {row[1]}",colour = discord.Color.red())
                                    emb.description = f"Баланс: **{row[0]}**"
                                await ctx.send(embed = emb)
                            else:
                                await ctx.send("Данного пользователя нет в базе данных")
                        conn.close()
            except:
                await ctx.send("Укажите id пользователя")

    #@commands.command(aliases = ["money", "balance"])
    #async def баланс(self, ctx, member: discord.Member):
    #    if member.bot:
    #        await ctx.send("У ботов нет профиля")
    #    else:
    #        with sqlite3.connect("../am/data/DB/Database.db") as conn:
    #            cursor = conn.cursor()
    #            for row in cursor.execute(f"SELECT money FROM users where id={member.id}").fetchall():
    #                emb = discord.Embed(title = f"Профиль {member.name}",colour = discord.Color.red())
    #                emb.set_thumbnail(url = member.avatar_url)
    #                emb.description = f"Баланс: **{row[0]}**"
    #                await ctx.send(embed = emb)
    #        conn.close()
                
    @баланс.error
    async def Balance_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            with sqlite3.connect("../am/data/DB/Database.db") as conn:
                cursor = conn.cursor()
                for row in cursor.execute(f"SELECT money FROM users where id={ctx.message.author.id}").fetchall():
                    emb = discord.Embed(title = f"Профиль {ctx.message.author.name}",colour = discord.Color.red())
                    emb.set_thumbnail(url = ctx.message.author.avatar_url)
                    emb.description = f"Баланс: **{row[0]}**"
                    await ctx.send(embed = emb)
            conn.close()

def setup(client):
    client.add_cog(Balance(client))