import os
import discord
from config import *
from time import time
import database as DB
from os import listdir
from asyncio import sleep
from discord.ext import commands

client = commands.Bot(command_prefix = (prefix, f"<@{id_client}> "), intents = discord.Intents.all())
client.remove_command("help")

async def status_task():
    while True:
        await client.change_presence(activity = discord.Game("AM"))
        await sleep(10)
        await client.change_presence(activity = discord.Game("/help"))
        await sleep(30)

@client.event
async def on_ready():
    am = 0
    for guild in client.guilds:
        am += len([i for i in guild.members if not i.bot])
        print(guild.name, guild.id, guild.owner, len(guild.members), len([i for i in guild.members if i.bot]))
    print(am)
    with open("./data/TXT/startTime.txt", "w") as file:
        file.write(str(time()))
    DB.start_database()
    client.loop.create_task(status_task())
    print("готов")

@client.event
async def on_message(message):
    if message.author.bot is False:
        DB.proverka(message.author.id, message.author.name)
        #DB.economy(message.author.id)
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
