import discord
from discord.ext import commands

emb = discord.Embed(title = 'Команда "/скажи"',colour = discord.Color.red())
emb.description = "Оправляет сообщение от лица бота"
emb.add_field(name = "Пример:", value = "`/скажи ам`")
emb.add_field(name = "Результат:", value = "`ам`")

class Say(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["say", "Say", "Скажи"])
    async def скажи(self, ctx, *, arg):
        if arg == "?":
            await ctx.send(embed = emb)
        else:
            await ctx.message.delete()
            await ctx.send(arg)

    @скажи.error
    async def Say_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed = emb)

def setup(client):
    client.add_cog(Say(client)) 