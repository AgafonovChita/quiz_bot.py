from aiogram import Bot
from aiogram import types
from aiogram.dispatcher.router import Router
from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters.command import Command
from aiogram.dispatcher.fsm.context import FSMContext

from keyboards.main_keyboards import DataTopic
from services.db_engine import DB_engine

from magic_filter import F

from keyboards.main_keyboards import generate_topic_key, generate_main_key, generate_goquiz_key


# /start
async def cmd_start(message: types.Message, db_engine: DB_engine):
    name_user = await db_engine.get_name(message.chat.id)
    await message.answer(f"Приветствую тебя, " + name_user, reply_markup=await generate_main_key())


# callback "start_quiz"
async def select_topic(callback: CallbackQuery, bot: Bot, db_engine: DB_engine):
    await callback.answer()
    type_quiz_keyboard = await generate_topic_key(db_engine)
    await callback.message.edit_text("Выбери QUIZ который хочешь пройти", reply_markup=type_quiz_keyboard)


# check topic
async def check_topic(callback: CallbackQuery, callback_data: DataTopic, db_engine: DB_engine, state:FSMContext ):
    await callback.answer()
    topic_data = await db_engine.get_topic_info(callback_data.topic_id)
    await callback.message.answer(text='ID quiz: ' + topic_data[0] + '\n' +
                                       'Quiz_topic: ' + topic_data[1] + '\n' +
                                       'Описание: ' + topic_data[2] + '\n' +
                                       'Автор: ' + topic_data[3] + '\n' +
                                       'Кол-во вопросов: ' + str(topic_data[4]) + '\n' +
                                       'Время на ответ: ' + str(topic_data[5] + ' секунд \n'),
                                  reply_markup=await generate_goquiz_key(topic_data[0]))
    await state.update_data(id_topic=topic_data[0], count_quest=topic_data[4], time_out=topic_data[5], list_quest_old=[])



# register command - main Router
def register_commands_main(router: Router):
    router.callback_query.register(select_topic, F.data == "go_main_quiz")
    router.callback_query.register(check_topic, DataTopic.filter())

    router.message.register(cmd_start, Command(commands="start"), user_type='auth')
