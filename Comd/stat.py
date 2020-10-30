import os
import time
import sqlite3
import discord
from discord.ext import commands
from importlib import import_module
from memory_profiler import memory_usage

def comd():
    am = import_module("database")
    return am.commands_view()

def started():
    with open("./data/TXT/startTime.txt", "r") as file:
        im = file.readline()

    elapsed_time = time.time() - float(im)
    return str(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))

commands_num = 0
symbols = 4777

for i in os.listdir("../am/Comd"):
    if i.endswith(".py"):
        infile = open(f"../am/Comd/{i}", "r", encoding = "utf-8")
        commands_num += 1
        symbols += len(infile.read())

class Stat(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["stat", "Stat", "Стат"])
    async def стат(self, ctx, *, arg):
        if arg[0] == "?":
            emb = discord.Embed(title = 'Команда "/статистика"',colour = discord.Color.red())
            emb.add_field(name = "Основаная:",value = "Серверов: **на скольких серверах есть бот**\nУчастников: **количество участников на всех серверах**")
            emb.add_field(name = "Сервер:",value = "Задержка: **время которое занимает обработка и отправка сообщения**\nПотребление памяти: **сколько бот потребляет**")
            emb.add_field(name = "Бот:",value = "Команд: **Количество команд в боте**\nСимволов: **Общее количество символов в файлах бота**")
            await ctx.send(embed = emb)
        else:
            ama = 0
            for guild in self.client.guilds:
                ama += len([i for i in guild.members if not i.bot])
            am = memory_usage()
            guilds = await self.client.fetch_guilds(limit = None).flatten()
            emb = discord.Embed(title = "Статистика",colour = discord.Color.red())
            emb.add_field(name = "Основная:", value = f"Серверов: **{len(guilds)}**\nУчастников: **{ama}**")
            emb.add_field(name = "Сервер:", value = f"Задержка: **{int(self.client.latency * 1000)} мс**\nПотребление памяти: **{int(am[0])}** МБ\nВремя работы **{started()}**")
            emb.add_field(name = "Бот:", value = f"Команд: **{commands_num}**\nСимволов: **{symbols}**\nОбработано команд: **{comd()}**")
            await ctx.send(embed = emb)

    @стат.error
    async def Stat_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            ama = 0
            for guild in self.client.guilds:
                ama += len([i for i in guild.members if not i.bot])
            am = memory_usage()
            guilds = await self.client.fetch_guilds(limit = None).flatten()
            emb = discord.Embed(title = "Статистика",colour = discord.Color.red())
            emb.add_field(name = "Основная:", value = f"Серверов: **{len(guilds)}**\nУчастников: **{ama}**")
            emb.add_field(name = "Сервер:", value = f"Задержка: **{int(self.client.latency * 1000)} мс**\nПотребление памяти: **{int(am[0])}** МБ\nВремя работы **{started()}**")
            emb.add_field(name = "Бот:", value = f"Команд: **{commands_num}**\nСимволов: **{symbols}**\nОбработано команд: **{comd()}**")
            await ctx.send(embed = emb)

def setup(client):
    client.add_cog(Stat(client))