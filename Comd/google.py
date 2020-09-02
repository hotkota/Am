import discord
from discord.ext import commands

class Google(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["Гугл", "google", "Google"])
    async def гугл(self, ctx, *arg):
        emb = discord.Embed(title = "Google",colour = discord.Color.red())
        emb.description = "Так как кому то лень искать в гугле я сделаю это вместо него\n[{}]({})".format(" ".join(arg), f'https://google.gik-team.com/?q={"+".join(arg)}')
        emb.set_footer(text = f"Вызвал {ctx.message.author.name}")
        await ctx.send(embed = emb)

    @гугл.error
    async def Google_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Ведите вопрос")

def setup(client):
    client.add_cog(Google(client))