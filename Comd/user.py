import discord
from discord.ext import commands

class User(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["user", "User", "Юзер"])
    async def юзер(self, ctx):
        if ctx.message.author.status == discord.Status.online:
            status = "Онлайн"
        elif ctx.message.author.status == discord.Status.idle:
            status = "Не активен"
        elif ctx.message.author.status == discord.Status.dnd:
            status = "Не беспокоить"
        elif ctx.message.author.status == discord.Status.offline:
            castom_status = "Не известно"
            status = "Офлайн"
        
        if ctx.message.author.activity == None:
            castom_status = "Отсутствует"
        else:
            castom_status = ctx.message.author.activity
        emb = discord.Embed(title = f"Информация о {ctx.message.author.name}",colour = discord.Color.red())
        emb.set_thumbnail(url = ctx.message.author.avatar_url)
        emb.add_field(name = "Основная", value = f"Ник: **{ctx.message.author.name}#{ctx.message.author.discriminator}**\nСтатус: **{status}**\n Пользовательский статус: **{castom_status}**\nРегистрация: **{ctx.message.author.created_at.date()}**\nПрисоединился: **{ctx.message.author.joined_at.date()}**")
        emb.set_footer(text = f"ID: {ctx.message.author.id}")
        await ctx.send(embed = emb)

def setup(client):
    client.add_cog(User(client))