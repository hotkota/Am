from asyncio import sleep
import discord
from discord.ext import commands

class Mute(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["mute"])
    @commands.has_permissions(administrator = True)
    async def мут(self, ctx, member: discord.Member, TIME: int):
        mute_role = discord.utils.get(ctx.message.guild.roles, name = 'Am_mute')
        if mute_role:
            await member.add_roles(mute_role)
            await ctx.send(f'{member.mention} был замьючен')
            await sleep(TIME * 60)
            await member.remove_roles(mute_role)
        else:
            guilds = ctx.guild
            perms = discord.Permissions(send_messages = False, read_messages = True)
            await guilds.create_role(name = 'Am_mute', permissions = perms)
            muted = discord.utils.get(ctx.message.guild.roles, name = 'Am_mute')

            for channel in ctx.message.guild.channels:
                await channel.set_permissions(muted, send_messages = False, read_messages = True, read_message_history = True)

            await member.add_roles(muted)
            await ctx.send(f'{member.mention} был замьючен')
            await sleep(TIME * 60)
            await member.remove_roles(muted)

def setup(client):
    client.add_cog(Mute(client))