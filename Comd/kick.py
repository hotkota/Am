import discord
from discord.ext import commands

class Kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['kick'])
    @commands.has_permissions(administrator = True)
    async def кик(self,ctx, member: discord.Member, *,reason = None):
        if member == None or member == ctx.message.author:
            await ctx.send('Нельзя себя банить')
        if reason == None:
            reason = 'Машинам тут не место'
        await member.kick(reason = reason)
        await ctx.send(f'{member.name} был кикнут')

def setup(client):
    client.add_cog(Kick(client))