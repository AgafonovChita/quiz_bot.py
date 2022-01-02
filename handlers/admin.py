from aiogram import Bot
import random
from aiogram import types
from aiogram.dispatcher.router import Router
from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters.command import Command
from keyboards.admin_keyboards import generate_admin_key
from aiogram.dispatcher.fsm.context import FSMContext
from models.states import AddNewTopic
from keyboards.main_keyboards import DataTopic
from services.db_engine import DB_engine

from magic_filter import F


# /start
async def cmd_start_admin(message: types.Message, db_engine: DB_engine):
    await message.answer(f"Приветствую тебя,господин", reply_markup=await generate_admin_key())


async def add_topic(callback: CallbackQuery, db_engine: DB_engine, state: FSMContext):
    await callback.answer()
    await callback.message.answer("Type topic info\n\nFormat:\nname::descript::author::timer::count::active")
    await state.set_state(AddNewTopic.add_topic)


async def save_new_topic(message: types.Message, db_engine: DB_engine, state: FSMContext):
    data = message.text.split("::")
    id_topic = random.randint(1, 100000)
    print(data)
    await db_engine.add_topic(id_topic, data[0], data[1], data[2], data[3], data[4], data[5])
    await state.clear()


# register command - main Router
def register_admin(router: Router):
    router.message.register(cmd_start_admin, Command(commands="start"), user_type="admin")
    router.callback_query.register(add_topic, F.data == "add_topic")
    router.message.register(save_new_topic, user_type='admin', state=AddNewTopic.add_topic)
