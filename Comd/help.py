import discord
from discord.ext import commands

emb = discord.Embed(title = "Команды",colour = discord.Color.red())
emb.description = "Для дополнительной информации напиши после команды `?`.\nНапример `/хелп ?`"
emb.add_field(name = "Информация:", value = "`/хелп /инфа /стат /юзер /инвайт`")
emb.add_field(name = "Модерация:", value = "`/бан /кик /мут /очистить`")
emb.add_field(name = "Экономика:", value = "`/профиль /баланс /уровень`")
emb.add_field(name = "Сообщения:", value = "`/скажи /голосование`")
emb.add_field(name = "Развлечение:", value = "`/ам /шар /лиса /кот /пес`")
emb.add_field(name = "Утилиты:", value = "`/эмоция /аватар /ранд`")
emb.set_footer(text = "Команды также доступны на английском")

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["help"])
    async def хелп(self, ctx, *, arg):
        if arg[0] == "?":
            emb = discord.Embed(title = "Команды",colour = discord.Color.red())
            emb.description = "Для дополнительной информации напиши после команды `?`.\nНапример `/хелп ?`"
            emb.add_field(name = "Информация", value = "Содержит полезную информацию")
            emb.add_field(name = "Модерация", value = "**Данный раздел еще сырой**\nСодержит команды для администраторов")
            emb.add_field(name = "Экономика", value = "Содержит команды для просмотра своей и чужой статистики активности")
            emb.add_field(name = "Сообщения", value = "Команды для отправки сообщений ботом")
            emb.add_field(name = "Развлечения", value = "Команды для поднятия настроения")
            emb.add_field(name = "Утилиты", value = "Просто полезные команды")
            await ctx.send(embed = emb)
        elif (arg == "Информация") or (arg == "информация"):
            emb = discord.Embed(title = 'Раздел "Информация"' ,colour = discord.Color.red())
            emb.description = "Для дополнительной информации напиши после команды `?`.\nНапример `/хелп ?`"
            emb.add_field(name = "/хелп", value = "Список всех доступных команд")
            emb.add_field(name = "/инфа", value = "Вся информация о боте")
            emb.add_field(name = "/стат", value = "Статистика бота")
            emb.add_field(name = "/юзер", value = "Информация о участнике")
            emb.add_field(name = "/инвайт", value = "Ссылки на приглашение бота и на сервер подержки")
            await ctx.send(embed = emb)
        elif (arg == "Модерация") or (arg == "модерация"):
            emb = discord.Embed(title = 'Раздел "Модерация"',colour = discord.Color.red())
            emb.description = "Для дополнительной информации напиши после команды `?`.\nНапример `/хелп ?`\n**Данные команды еще сырые**"
            emb.add_field(name = "/бан", value = "Банит указаного участника")
            emb.add_field(name = "/кик", value = "Кик указаного участника")
            emb.add_field(name = "/мут", value = "Выдает мут на определеное время")
            emb.add_field(name = "/очистить", value = "Удаляет указаное количество сообщений")
            await ctx.send(embed = emb)
        elif (arg == "Экономика") or (arg == "экономика"):
            emb = discord.Embed(title = 'Раздел "Экономика"' ,colour = discord.Color.red())
            emb.description = "Для дополнительной информации напиши после команды `?`.\nНапример `/хелп ?`"
            emb.add_field(name = "/профиль", value = "Профиль участника")
            emb.add_field(name = "/баланс", value = "Баланс указаного пользователя")
            emb.add_field(name = "/уровень", value = "Уровень и опыт пользователя")
            await ctx.send(embed = emb)
        elif (arg == "Сообщения") or (arg == "сообщения"):
            emb = discord.Embed(title = 'Раздел "Сообщения"' ,colour = discord.Color.red())
            emb.description = "Для дополнительной информации напиши после команды `?`.\nНапример `/хелп ?`"
            emb.add_field(name = "/скажи", value = "Отправляет сообщение от лица бота")
            emb.add_field(name = "/голосование", value = "Отправляет сообщение и добаляет реакции")
            await ctx.send(embed = emb)
        elif (arg == "Развлечения") or (arg == "развлечения"):
            emb = discord.Embed(title = 'Раздел "Развелечения"' ,colour = discord.Color.red())
            emb.description = "Для дополнительной информации напиши после команды `?`.\nНапример `/хелп ?`"
            emb.add_field(name = "/ам", value = "Ам...")
            emb.add_field(name = "/шар", value = "Отвечает на вопрос")
            emb.add_field(name = "/лиса", value = "Случайная картинка лисы")
            emb.add_field(name = "/кот", value = "Случайная картинка кота")
            emb.add_field(name = "/пес", value = "Случайная картинка собаки")
            await ctx.send(embed = emb)
        elif (arg == "Утилиты") or (arg == "утилиты"):
            emb = discord.Embed(title = 'Раздел "Утилиты"',colour = discord.Color.red())
            emb.description = "Для дополнительной информации напиши после команды `?`.\nНапример `/хелп ?`"
            emb.add_field(name = "/эмоция", value = "Преврашает эмодзи в картинку")
            emb.add_field(name = "/аватар", value = "Отправляет аватар учатсника")
            emb.add_field(name = "/ранд", value = "Случайное число в диапазоне")
            await ctx.send(embed = emb)
        else:
            await ctx.send(embed = emb)

    @хелп.error
    async def Help_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed = emb)

def setup(client):
    client.add_cog(Help(client))