import asyncio
import logging
import config


from aiogram import Bot, Dispatcher
from aiogram.dispatcher.router import Router

from models.bot_commands import set_bot_commands
from handlers.commands import register_commands
from handlers.callbacks import register_callbacks
from handlers.registration import register_commands_new_user
from filters.chat_type import ChatTypeFilter
from filters.user_type import UserTypeFilter

logger = logging.getLogger(__name__)


async def main():
    bot = Bot(config.bot_token, parse_mode="HTML")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    logger.error("Starting bot")

    # Define the only router
    default_router = Router()

    # Register filters
    default_router.message.bind_filter(ChatTypeFilter)
    #default_router.callback_query.bind_filter(UserTypeFilter)
    default_router.message.bind_filter(UserTypeFilter)


    # Register handlers
    register_commands(default_router)
    register_callbacks(default_router)
    register_commands_new_user(default_router)

    # Setup dispatcher and bind routers to it
    dp = Dispatcher()
    dp.include_router(default_router)

    # список команд бота
    await set_bot_commands(bot)

    # запуск бота
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())