import asyncio
import logging
import config

import asyncpg

from aiogram import Bot, Dispatcher
from aiogram.dispatcher.router import Router


from models.bot_commands import set_bot_commands
from handlers.commands import register_commands
from handlers.callbacks import register_callbacks
from handlers.registration import register_commands_new_user
from filters.chat_type import ChatTypeFilter
from filters.user_type import UserTypeFilter
from middlewares.db_pool import DBPool

logger = logging.getLogger(__name__)


async def create_pool():
    pool = await asyncpg.create_pool(host=config.db_host,
                                     port=config.db_port, user=config.db_user, password=config.db_pass,
                                     database=config.db_type)
    return pool


async def main():
    bot = Bot(config.bot_token, parse_mode="HTML")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    logger.error("Starting bot")

    # get pool connect to db (asyncpg)
    pool = await create_pool()


    # Define the only router
    start_router = Router()
    quiz_router = Router()

    dp = Dispatcher()
    dp.include_router(start_router)
    dp.include_router(quiz_router)

    # Register filters
    # default_router.message.bind_filter(ChatTypeFilter)
    # default_router.callback_query.bind_filter(UserTypeFilter)
    start_router.message.bind_filter(UserTypeFilter)
    quiz_router.message.bind_filter(UserTypeFilter)


    # DB pool-connection forward middlewares
    quiz_router.message.outer_middleware(DBPool(pool=pool))
    quiz_router.callback_query.outer_middleware(DBPool(pool=pool))


    start_router.message.outer_middleware(DBPool(pool=pool))
    start_router.callback_query.outer_middleware(DBPool(pool=pool))


    # Register handlers
    register_commands(quiz_router)
    register_callbacks(quiz_router)
    register_commands_new_user(start_router)


    try:
        await set_bot_commands(bot)
        await bot.get_updates(offset=-1)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types(), pool=pool)
    finally:
        pass


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.warning("Exit")