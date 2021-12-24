from aiogram.dispatcher.router import Router
from aiogram.types import CallbackQuery
from magic_filter import F


async def start_quiz(callback: CallbackQuery):
    await callback.message.edit_text("Мы начинаем КВН", reply_markup=None)
    await callback.answer()


# Register handlers callbacks (buttons)
def register_callbacks(router: Router):
    router.callback_query.register(start_quiz, F.data == "start_quiz")