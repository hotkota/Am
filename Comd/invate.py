import discord
from discord.ext import commands

emb = discord.Embed(title = "Пригласить", colour = discord.Color.red())
emb.add_field(name = "Ссылки", value = "[Пригласить бота](https://discord.com/oauth2/authorize?client_id=737987355389984848&scope=bot&permissions=8)\n[Сервер подержки](https://discord.gg/rgsV2AQ)")

class Invate(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["invate", "инвайт"])
    async def пригласить(self, ctx, *, arg):
        if arg[0] == "?":
            await ctx.send(embed = emb)
        else:
            await ctx.send(embed = emb)

    @пригласить.error
    async def Invate_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed = emb)

def setup(client):
    client.add_cog(Invate(client))