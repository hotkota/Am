import discord
from discord.ext import commands

emb = discord.Embed(title = 'Команда "/голосование"',colour = discord.Color.red())
emb.description = "Отправляет сообщение от лица бота и прикрепляет реакции"
emb.add_field(name = "Пример:", value = "`/голосование ам`\n    ам")

class Pool(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["poll", "Poll", "Голосование"])
    async def голосование(self, ctx, *, arg):
        if arg == "?":
            await ctx.send(embed = emb)
        else:
            await ctx.message.delete()
            message = await ctx.send(f"**{arg}**")
            await message.add_reaction("👍")
            await message.add_reaction("👎")

    @голосование.error
    async def Poll_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed = emb)

def setup(client):
    client.add_cog(Pool(client))