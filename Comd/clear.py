import discord
from discord.ext import commands

emb = discord.Embed(title = "Очистка чата",colour = discord.Color.red())
emb.description = "Удаляет сообщения в чате"
emb.add_field(name = "Пример:", value = "`/очистить 10\n\tУдалит 10 сообщений не старше 2 недель")

class Clear(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["clear", "Clear", "Очистить"])
    @commands.has_permissions(administrator = True)
    async def очистить(self, ctx, amount: int):
        if amount is None:
            await ctx.send(embed = emb)
        elif amount <= 0:
            await ctx.send(embed = emb)
        else:
            await ctx.channel.purge(limit = amount + 1)
            emb = discord.Embed(title = "Очистка чата",colour = discord.Color.red())
            emb.description = f"**{ctx.message.author.name}** очистил чат\nУдалено **{amount}** сообщений"
            await ctx.send(embed = emb)

    @очистить.error
    async def Clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed = emb)

def setup(client):
    client.add_cog(Clear(client))