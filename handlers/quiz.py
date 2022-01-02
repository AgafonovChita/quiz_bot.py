from aiogram.dispatcher.router import Router
from aiogram.types import CallbackQuery, PollAnswer
from aiogram import Bot
from handlers.main import select_topic
from services.db_engine import DB_engine
from aiogram.dispatcher.fsm.context import FSMContext

from magic_filter import F

from keyboards.main_keyboards import DataTopic

"""Должен быть калбек-хендлер, который среагирвет на go_quiz"""


async def go_quiz(callback: CallbackQuery, bot: Bot, db_engine: DB_engine, state: FSMContext):
    await callback.answer()
    await callback.message.answer('Тут типо вопросы по квизу')
    data = await state.get_data()
    quest = await db_engine.get_quest(id_topic=data["id_topic"], list_quest_old=data["list_quest_old"])
    print(data)
    print(quest)


async def stop_quiz(callback: CallbackQuery, bot: Bot, db_engine: DB_engine):
    await callback.answer()
    await select_topic(callback, bot, db_engine)
    await callback.message.delete()


async def poll_answer(answer: PollAnswer):
    print(answer)


async def send_poll(bot: Bot, user_id, question_text, answers, correct_id, open_time):
    await bot.send_poll(chat_id=user_id, question='Как дела?',
                        options=['ok', 'no'], type='quiz', correct_option_id=1, open_period=10)


# Register handlers callbacks
def register_quiz_engine(router: Router):
    router.callback_query.register(go_quiz, F.data == "start_quiz")
    router.callback_query.register(stop_quiz, F.data == "cancel_quiz")
