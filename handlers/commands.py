from aiogram import types
from aiogram.dispatcher.router import Router
from aiogram import types
from aiogram.dispatcher.router import Router
from aiogram.dispatcher.filters.command import Command

from services.db_engine import DB_engine

from keyboards import main_keyboards


async def cmd_start(message: types.Message, db_engine: DB_engine):
    name_user = await db_engine.get_name(message.chat.id)
    print('я тут')
    await message.answer(f"Hello, "+name_user, reply_markup=main_keyboards.generate_main_keyboard())


def register_commands(router: Router):
    router.message.register(cmd_start, Command(commands="start"), user_type='auth')
