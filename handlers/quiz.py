from aiogram.dispatcher.router import Router
from aiogram.types import CallbackQuery, PollAnswer
from aiogram import Bot
from services.db_engine import DB_engine

from keyboards.quiz_keyboards import generate_type_quiz_keyboard
from keyboards.main_keyboards import DataTopic




async def poll_answer(answer: PollAnswer):
    print(answer)


async def send_poll(bot: Bot):
    await bot.send_poll(chat_id=callback.from_user.id, question='Как дела?',
                        options=['ok', 'no'], type='quiz', correct_option_id=1, open_period=10)



# Register handlers callbacks
def register_callbacks(router: Router):
    router.callback_query.register(start_quiz, F.data == "start_quiz")
    router.poll.register(poll_answer)