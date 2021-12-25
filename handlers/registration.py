from aiogram import types
from aiogram.dispatcher.router import Router
from aiogram.dispatcher.filters.command import Command
from aiogram.dispatcher.fsm.context import FSMContext

from models.states import RegisterUser
from handlers.commands import cmd_start

from db.db_engine import DB_engine


async def register_user(message: types.Message, state=FSMContext):
    await message.answer("Друг, кажестя мы ещё не знакомы!\nКак я могу к тебе обращатсья?")
    await state.set_state(RegisterUser.user_nickname)


async def get_nickname_user(message:types.Message, db_engine:DB_engine, state=FSMContext, ):
    await message.answer('Очень приятно, '+message.text)
    await state.clear()
    await db_engine.add_user(message.chat.id, message.text, message.chat.first_name+' '+message.chat.last_name, message.chat.username, message.date)
    await cmd_start(message, db_engine)


def register_commands_new_user(router:Router):
    router.message.register(register_user, Command(commands="start"), user_type='new')
    router.message.register(get_nickname_user, state=RegisterUser.user_nickname, user_type='new')