import random
import discord
from config import *
from time import time
from os import listdir
from asyncio import sleep
from pymongo import MongoClient
from discord.ext import commands

cluster = MongoClient(f"mongodb+srv://{password_db}@main.3magc.mongodb.net/users?retryWrites=true&w=majority")
db = cluster["one_db"]

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
    client.loop.create_task(status_task())
    print("готов")

@client.event
async def on_message(message):
    if message.author.bot is False:
        if message.content:
            collection = db["users"]
            if collection.count_documents({"_id": message.author.id}) == 0:
                collection.insert_one({
                    "_id": message.author.id,
                    "balance": 500,
                    "description": 'Для дополнительной информации напишите "/осебе"',
                    "inventory": {},
                    "xp": 0,
                    "level": 1
                })
            else:
                xp, level = collection.find_one({"_id": message.author.id})["xp"], collection.find_one({"_id": message.author.id})["level"]
                collection.update_one({"_id": message.author.id}, {"$set": {"xp": xp + random.randint(15, 25)}})
                if xp >= (5*level**2 + 50*level + 100):
                    coin = collection.find_one({"_id": message.author.id})["balance"]
                    collection.update_one({"_id": message.author.id}, {"$set": {"xp": 0, "level": level + 1, "balance": coin + 500*level}})
    await client.process_commands(message)

for file in listdir("./Comd"):
    if file.endswith(".py"):
        client.load_extension(f"Comd.{file[:-3]}")

@client.event
async def on_command(ctx):
    collection = db["commands"]
    comd = collection.find_one({"bot_id": client.user.id})["command"]
    collection.update_one({"bot_id": client.user.id}, {"$set": {"command": comd + 1}})

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pass

client.run(token)
