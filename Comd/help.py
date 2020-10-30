import discord
from discord.ext import commands
from importlib import import_module

cfg = import_module("config").prefix

emb = discord.Embed(title = "Команды",colour = discord.Color.red())
emb.description = f"Для дополнительной информации напиши после команды `?`.\nНапример `{cfg}хелп ?`"
emb.add_field(name = "Информация:", value = f"`{cfg}хелп` `{cfg}инфа` `{cfg}стат` `{cfg}юзер` `{cfg}инвайт`")
emb.add_field(name = "Модерация:", value = f"`{cfg}очистить`")
emb.add_field(name = "Экономика:", value = f"`{cfg}профиль` `{cfg}баланс` `{cfg}уровень` `{cfg}казино` `{cfg}передать`")
emb.add_field(name = "Сообщения:", value = f"`{cfg}скажи` `{cfg}голосование`")
emb.add_field(name = "Развлечение:", value = f"`{cfg}ам` `{cfg}шар`")
emb.add_field(name = "API:", value = f"`{cfg}гугл` `{cfg}ии` `{cfg}фото`")
emb.add_field(name = "Утилиты:", value = f"`{cfg}эмоция` `{cfg}аватар` `{cfg}ранд` `{cfg}t`")
emb.set_footer(text = "Команды также доступны на английском")

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["help", "Help", "Хелп"])
    async def хелп(self, ctx, *, arg):
        arg = arg.lower()
        if arg == "?":
            emb = discord.Embed(title = "Команды", colour = discord.Color.red())
            emb.description = f"Для дополнительной информации напиши после команды `?`.\nНапример `{cfg}хелп ?`"
            emb.add_field(name = "Информация", value = "Полезная информация о боте")
            emb.add_field(name = "Модерация", value = "**Данный раздел еще сырой**\nКоманды для администраторации")
            emb.add_field(name = "Экономика", value = "Команды для просмотра своей и чужой статистики активности")
            emb.add_field(name = "Сообщения", value = "Команды для отправки сообщений ботом")
            emb.add_field(name = "Развлечения", value = "Команды для поднятия настроения")
            emb.add_field(name = "API", value = "Команды которые используют другие сайты для работы")
            emb.add_field(name = "Утилиты", value = "Просто полезные команды")
        elif arg == "информация":
            emb = discord.Embed(title = 'Раздел "Информация"' ,colour = discord.Color.red())
            emb.description = f"Для дополнительной информации напиши после команды `?`.\nНапример `{cfg}хелп ?`"
            emb.add_field(name = f"{cfg}хелп", value = "```Список всех доступных команд```")
            emb.add_field(name = f"{cfg}инфа", value = "```Вся информация о боте```")
            emb.add_field(name = f"{cfg}стат", value = "```Статистика бота```")
            emb.add_field(name = f"{cfg}юзер", value = "```Информация о участнике```")
            emb.add_field(name = f"{cfg}инвайт", value = "```Ссылки на приглашение бота и на сервер подержки```")
        elif arg == "модерация":
            emb = discord.Embed(title = 'Раздел "Модерация"',colour = discord.Color.red())
            emb.description = f"Для дополнительной информации напиши после команды `?`.\nНапример `{cfg}хелп ?`"
            emb.add_field(name = f"{cfg}очистить", value = "```Удаляет указаное количество сообщений```")
        elif arg == "экономика":
            emb = discord.Embed(title = 'Раздел "Экономика"' ,colour = discord.Color.red())
            emb.description = f"Для дополнительной информации напиши после команды `?`.\nНапример `{cfg}хелп ?`"
            emb.add_field(name = f"{cfg}профиль", value = "```Профиль участника```")
            emb.add_field(name = f"{cfg}баланс", value = "```Баланс указаного пользователя```")
            emb.add_field(name = f"{cfg}уровень", value = "```Уровень и опыт пользователя```")
            emb.add_field(name = f"{cfg}казино", value = "```Способ потратить свои деньги```")
            emb.add_field(name = f"{cfg}передать", value = "```Передача денег другому пользователю```")
        elif arg == "сообщения":
            emb = discord.Embed(title = 'Раздел "Сообщения"' ,colour = discord.Color.red())
            emb.description = f"Для дополнительной информации напиши после команды `?`.\nНапример `{cfg}хелп ?`"
            emb.add_field(name = f"{cfg}скажи", value = "```Отправляет сообщение от лица бота```")
            emb.add_field(name = f"{cfg}голосование", value = "```Отправляет сообщение и добаляет реакции```")
        elif arg == "развлечения" or arg == "развлечение":
            emb = discord.Embed(title = 'Раздел "Развелечения"' ,colour = discord.Color.red())
            emb.description = f"Для дополнительной информации напиши после команды `?`.\nНапример `{cfg}хелп ?`"
            emb.add_field(name = f"{cfg}ам", value = "```Ам...```")
            emb.add_field(name = f"{cfg}шар", value = "```Отвечает на вопрос```")
        elif (arg == "api") or (arg == "апи"):
            emb = discord.Embed(title = 'Раздел "API"',colour = discord.Color.red())
            emb.description = f"Для дополнительной информации напиши после команды `?`.\nНапример `{cfg}хелп ?`"
            emb.add_field(name = f"{cfg}гугл", value = "```Ссылка на гугл с нужным вопросом```")
            emb.add_field(name = f"{cfg}ии", value = "```Просто чат бот```")
            emb.add_field(name = f"{cfg}фото", value = "```Случайная картинка```")
        elif arg == "утилиты":
            emb = discord.Embed(title = 'Раздел "Утилиты"',colour = discord.Color.red())
            emb.description = f"Для дополнительной информации напиши после команды `?`.\nНапример `{cfg}хелп ?`"
            emb.add_field(name = f"{cfg}эмоция", value = "```Преврашает эмодзи в картинку```")
            emb.add_field(name = f"{cfg}аватар", value = "```Отправляет аватар участника```")
            emb.add_field(name = f"{cfg}ранд", value = "```Случайное число в диапазоне```")
            emb.add_field(name = f"{cfg}t", value = "```Перевод введеного текста```")
        await ctx.send(embed = emb)

    @хелп.error
    async def Help_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed = emb)

def setup(client):
    client.add_cog(Help(client))