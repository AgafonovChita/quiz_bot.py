from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats, BotCommandScopeAllGroupChats


async def set_bot_commands(bot: Bot):
    data = [
        # Commands in private chats (English and Russian)
        (
            [
                BotCommand(command="main", description="Главное меню"),
                BotCommand(command="mess_admin", description="Обратная связь"),
            ],
            BotCommandScopeAllPrivateChats(),
            "en"
        ),
        (
            [
                BotCommand(command="main", description="Главное меню"),
                BotCommand(command="call_admin", description="Обратная связь"),
            ],
            BotCommandScopeAllPrivateChats(),
            "ru"
        ),
    ]

    for commands_list, commands_scope, language in data:
        await bot.set_my_commands(commands=commands_list, scope=commands_scope, language_code=language)