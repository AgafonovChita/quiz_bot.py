import asyncio
import logging
import config

from services import db_engine

from aiogram import Bot, Dispatcher
from aiogram.dispatcher.router import Router

from models.bot_commands import set_bot_commands
from handlers.commands import register_commands_main
from handlers.registration import register_commands_new_user
from filters.chat_type import ChatTypeFilter
from filters.user_type import UserTypeFilter
from middlewares.db_pool import DBPool


logger = logging.getLogger(__name__)


async def main():
    bot = Bot(config.bot_token, parse_mode="HTML")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    logger.error("Starting bot")

    # get pool connect to db (asyncpg)
    pool = await db_engine.create_pool()

    # define the only router
    start_router = Router()
    main_router = Router()

    dp = Dispatcher()
    dp.include_router(start_router)
    dp.include_router(main_router)

    # Register filters
    # default_router.message.bind_filter(ChatTypeFilter)
    # default_router.callback_query.bind_filter(UserTypeFilter)
    start_router.message.bind_filter(UserTypeFilter)
    main_router.message.bind_filter(UserTypeFilter)

    # DB pool-connection forward middlewares
    start_router.message.outer_middleware(DBPool(pool=pool))
    start_router.callback_query.outer_middleware(DBPool(pool=pool))
    main_router.message.outer_middleware(DBPool(pool=pool))
    main_router.callback_query.outer_middleware(DBPool(pool=pool))

    # register handlers to start_router
    register_commands_new_user(start_router)
    # register handlers to quiz_router
    register_commands_main(main_router)


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