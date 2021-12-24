from aiogram import types
from aiogram.dispatcher.router import Router
from aiogram.dispatcher.filters.command import Command
from aiogram.dispatcher.fsm.context import FSMContext

from models.states import RegisterUser


async def register_user(message:types.Message, state=FSMContext):
    await message.answer("Друг, кажестя мы ещё не знакомы!\nКак я могу к тебе обращатсья?")
    await state.set_state(RegisterUser.user_nickname)


async def get_nickname_user(message:types.Message, state=FSMContext):
    print(message)
    await message.answer('Очень приятно, '+message.text)
    await state.clear()

    nickname = message.text
    data_register = message.date
    id_tg = message.chat.id
    name_tg = message.chat.first_name + ' ' + message.chat.last_name
    nickname_tg = message.chat.username


def register_commands_new_user(router:Router):
    router.message.register(register_user, Command(commands="main"), user_type='new')
    router.message.register(get_nickname_user, state=RegisterUser.user_nickname)