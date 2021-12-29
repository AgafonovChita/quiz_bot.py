from aiogram.dispatcher.router import Router
from aiogram.types import CallbackQuery, PollAnswer
from aiogram import Bot
from services.db_engine import DB_engine

from magic_filter import F

from keyboards.quiz_keyboards import generate_type_quiz_keyboard
from keyboards.main_keyboards import DataTopic

"""Должен быть калбек-хендлер, который среагирвет на go_quiz"""


async def go_quiz(callback: CallbackQuery):
    await callback.answer()
    await callback.answer('Тут типо вопросы по квизу')
    """генерируем вопрос - отправляем - ждем ответ - проверяем правильность/кол-во вопросов - отправляем след.вопрос"""


async def poll_answer(answer: PollAnswer):
    print(answer)


async def send_poll(bot: Bot, user_id, question_text, answers, correct_id, open_time):
    await bot.send_poll(chat_id=user_id, question='Как дела?',
                        options=['ok', 'no'], type='quiz', correct_option_id=1, open_period=10)


# Register handlers callbacks
def register_quiz_engine(router: Router):
    router.callback_query.register(go_quiz, F.data == "go_quiz")
