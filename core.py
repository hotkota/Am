import discord
from config import *
from time import time
import database as DB
from os import listdir
from asyncio import sleep
from discord.ext import commands

client = commands.Bot(command_prefix = (prefix, f"<@{id_client}> "))
client.remove_command("help")

async def status_task():
    while True:
        await client.change_presence(activity = discord.Game("AM"))
        await sleep(10)
        await client.change_presence(activity = discord.Game("/help"))
        await sleep(30)

@client.event
async def on_ready():
    with open("./data/TXT/startTime.txt", "w") as file:
        file.write(str(time()))
    print("Проверка DB")
    DB.start_database()
    print("Проверка завершена")
    client.loop.create_task(status_task())
    print("готов")

@client.event
async def on_message(message):
    if message.author.bot is False:
        if message.content:
            if message.content.startswith(f"{prefix}премиум"):
                DB.premium(message.guild.id, message.author.id)
            elif message.content.startswith(f"{prefix}осебе") or message.content.startswith(f"{prefix}desc"):
                DB.desc(message.author.id, message.content[7:])
            DB.proverka(message.guild.id, message.author.id, message.author.name)
            DB.economy(message.author.id)
    await client.process_commands(message)

for file in listdir("./Comd"):
    if file.endswith(".py"):
        client.load_extension(f"Comd.{file[:-3]}")

@client.event
async def on_command(ctx):
    DB.commands()

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pass

client.run(token)
