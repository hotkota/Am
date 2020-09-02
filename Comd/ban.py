import discord
from discord.ext import commands

class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['ban'])
    @commands.has_permissions(administrator = True)
    async def бан(self, ctx , member: discord.Member, *, reason = None):
        if member == None or member == ctx.message.author:
            await ctx.send('Нельзя себя банить')
        if reason == None:
            reason = 'Машинам тут не место'
        await member.ban(reason = reason)
        await ctx.send(f'{member.name} был забанен')

def setup(client):
    client.add_cog(Ban(client))