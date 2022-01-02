from aiogram import Bot
from aiogram import types
from aiogram.dispatcher.router import Router
from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters.command import Command
from keyboards.admin_keyboards import generate_admin_key
from aiogram.dispatcher.fsm.context import FSMContext

from keyboards.main_keyboards import DataTopic
from services.db_engine import DB_engine

from magic_filter import F


# /start
async def cmd_start_admin(message: types.Message, db_engine: DB_engine):
    await message.answer(f"Приветствую тебя,господин", reply_markup=await generate_admin_key())


# register command - main Router
def register_admin(router: Router):
    router.message.register(cmd_start_admin, Command(commands="start"), user_type='admin')