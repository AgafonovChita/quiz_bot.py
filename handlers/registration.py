from aiogram import types
from aiogram.dispatcher.router import Router
from aiogram.dispatcher.filters.command import Command
from aiogram.dispatcher.fsm.context import FSMContext

from models.states import RegisterUser

from db.db_engine import DB_engine


async def register_user(message:types.Message, state=FSMContext):
    await message.answer("Друг, кажестя мы ещё не знакомы!\nКак я могу к тебе обращатсья?")
    await state.set_state(RegisterUser.user_nickname)


async def get_nickname_user(message:types.Message, db_engine: DB_engine, state=FSMContext):
    await message.answer('Очень приятно, '+message.text)
    await state.clear()
    query = '''INSERT INTO users 
                   (id_user, nickname_bot, name_tg, nickname_tg, date_register) VALUES ($1, $2, $3, $4, $5)'''
    params = message.chat.id, message.text, message.chat.first_name+' '+message.chat.last_name, message.chat.username, message.date
    await db_engine.execute(query, params, False)


def register_commands_new_user(router:Router):
    router.message.register(register_user, Command(commands="main"), user_type='new')
    router.message.register(get_nickname_user, state=RegisterUser.user_nickname)