import discord
from discord.ext import commands

emb = discord.Embed(title = "Команды",colour = discord.Color.red())
emb.description = "Для дополнительной информации напиши после команды `?`.\nНапример `/хелп ?`"
emb.add_field(name = "Информация:", value = "`/хелп` `/инфа` `/стат` `/юзер` `/инвайт`")
emb.add_field(name = "Модерация:", value = "`/очистить`")
emb.add_field(name = "Экономика:", value = "`/профиль` `/баланс` `/уровень`")
emb.add_field(name = "Сообщения:", value = "`/скажи` `/голосование`")
emb.add_field(name = "Развлечение:", value = "`/ам` `/шар`")
emb.add_field(name = "API:", value = "`/гугл` `/ии` `/фото`")
emb.add_field(name = "Утилиты:", value = "`/эмоция` `/аватар` `/ранд` `/t`")
emb.set_footer(text = "Команды также доступны на английском")

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["help", "Help", "Хелп"])
    async def хелп(self, ctx, *, arg):
        arg = arg.lower()
        if arg == "?":
            emb = discord.Embed(title = "Команды", colour = discord.Color.red())
            emb.description = "Для дополнительной информации напиши после команды `?`.\nНапример `/хелп ?`"
            emb.add_field(name = "Информация", value = "Полезная информация о боте")
            emb.add_field(name = "Модерация", value = "**Данный раздел еще сырой**\nКоманды для администраторации")
            emb.add_field(name = "Экономика", value = "Команды для просмотра своей и чужой статистики активности")
            emb.add_field(name = "Сообщения", value = "Команды для отправки сообщений ботом")
            emb.add_field(name = "Развлечения", value = "Команды для поднятия настроения")
            emb.add_field(name = "API", value = "Команды которые используют другие сайты для работы")
            emb.add_field(name = "Утилиты", value = "Просто полезные команды")
        elif arg == "информация":
            emb = discord.Embed(title = 'Раздел "Информация"' ,colour = discord.Color.red())
            emb.description = "Для дополнительной информации напиши после команды `?`.\nНапример `/хелп ?`"
            emb.add_field(name = "/хелп", value = "```Список всех доступных команд```")
            emb.add_field(name = "/инфа", value = "```Вся информация о боте```")
            emb.add_field(name = "/стат", value = "```Статистика бота```")
            emb.add_field(name = "/юзер", value = "```Информация о участнике```")
            emb.add_field(name = "/инвайт", value = "```Ссылки на приглашение бота и на сервер подержки```")
        elif arg == "модерация":
            emb = discord.Embed(title = 'Раздел "Модерация"',colour = discord.Color.red())
            emb.description = "Для дополнительной информации напиши после команды `?`.\nНапример `/хелп ?`"
            emb.add_field(name = "/очистить", value = "```Удаляет указаное количество сообщений```")
        elif arg == "экономика":
            emb = discord.Embed(title = 'Раздел "Экономика"' ,colour = discord.Color.red())
            emb.description = "Для дополнительной информации напиши после команды `?`.\nНапример `/хелп ?`"
            emb.add_field(name = "/профиль", value = "```Профиль участника```")
            emb.add_field(name = "/баланс", value = "```Баланс указаного пользователя```")
            emb.add_field(name = "/уровень", value = "```Уровень и опыт пользователя```")
        elif arg == "сообщения":
            emb = discord.Embed(title = 'Раздел "Сообщения"' ,colour = discord.Color.red())
            emb.description = "Для дополнительной информации напиши после команды `?`.\nНапример `/хелп ?`"
            emb.add_field(name = "/скажи", value = "```Отправляет сообщение от лица бота```")
            emb.add_field(name = "/голосование", value = "```Отправляет сообщение и добаляет реакции```")
        elif arg == "развлечения" or arg == "развлечение":
            emb = discord.Embed(title = 'Раздел "Развелечения"' ,colour = discord.Color.red())
            emb.description = "Для дополнительной информации напиши после команды `?`.\nНапример `/хелп ?`"
            emb.add_field(name = "/ам", value = "```Ам...```")
            emb.add_field(name = "/шар", value = "```Отвечает на вопрос```")
        elif (arg == "api") or (arg == "апи"):
            emb = discord.Embed(title = 'Раздел "API"',colour = discord.Color.red())
            emb.description = "Для дополнительной информации напиши после команды `?`.\nНапример `/хелп ?`"
            emb.add_field(name = "/гугл", value = "```Ссылка на гугл с нужным вопросом```")
            emb.add_field(name = "/ии", value = "```Просто чат бот```")
            emb.add_field(name = "/фото", value = "```Случайная картинка```")
        elif arg == "утилиты":
            emb = discord.Embed(title = 'Раздел "Утилиты"',colour = discord.Color.red())
            emb.description = "Для дополнительной информации напиши после команды `?`.\nНапример `/хелп ?`"
            emb.add_field(name = "/эмоция", value = "```Преврашает эмодзи в картинку```")
            emb.add_field(name = "/аватар", value = "```Отправляет аватар участника```")
            emb.add_field(name = "/ранд", value = "```Случайное число в диапазоне```")
            emb.add_field(name = "/t", value = "```Перевод введеного текста```")
        await ctx.send(embed = emb)

    @хелп.error
    async def Help_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed = emb)

def setup(client):
    client.add_cog(Help(client))