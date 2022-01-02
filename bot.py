import asyncio
import logging
import config

from services import db_engine

from aiogram import Bot, Dispatcher
from aiogram.dispatcher.router import Router

from models.bot_commands import set_bot_commands
from handlers.main import register_commands_main
from handlers.registration import register_commands_new_user
from handlers.quiz import register_quiz_engine
from handlers.admin import register_admin

from filters.chat_type import ChatTypeFilter
from filters.user_type import UserTypeFilter
from keyboards.main_keyboards import DataTopic
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

    # dregistration the only router
    registration_router = Router()
    main_router = Router()
    quiz_router = Router()
    admin_router = Router()

    dp = Dispatcher()
    dp.include_router(quiz_router)
    dp.include_router(registration_router)
    dp.include_router(main_router)
    dp.include_router(admin_router)


    # Register filters
    # default_router.message.bind_filter(ChatTypeFilter)
    # default_router.callback_query.bind_filter(UserTypeFilter)
    registration_router.message.bind_filter(UserTypeFilter)
    main_router.message.bind_filter(UserTypeFilter)
    admin_router.message.bind_filter(UserTypeFilter)

    # DB pool-connection forward middlewares
    quiz_router.message.outer_middleware(DBPool(pool=pool))
    quiz_router.callback_query.outer_middleware(DBPool(pool=pool))
    registration_router.message.outer_middleware(DBPool(pool=pool))
    registration_router.callback_query.outer_middleware(DBPool(pool=pool))
    main_router.message.outer_middleware(DBPool(pool=pool))
    main_router.callback_query.outer_middleware(DBPool(pool=pool))
    admin_router.message.outer_middleware(DBPool(pool=pool))
    admin_router.callback_query.middlewares(DBPool(pool=pool))


    # register handlers to start_router, main_router, quiz_router
    register_quiz_engine(quiz_router)
    register_commands_new_user(registration_router)
    register_commands_main(main_router)
    register_admin(admin_router)



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