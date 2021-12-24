from aiogram import types
from aiogram.dispatcher.router import Router
from aiogram.dispatcher.filters.command import Command


from keyboards import main_keyboards


async def cmd_start(message: types.Message):
    await message.answer(f"Здравствуй, дорогой друг!", reply_markup=main_keyboards.keyboard_start)


def register_commands(router: Router):
    router.message.register(cmd_start, Command(commands="main"), user_type='auth')
