from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

# generate keyboard -> Markup
# buttons_start = [
#     InlineKeyboardButton(text="Go to quiz", callback_data="start_quiz"),
#     InlineKeyboardButton(text="Рейтинг участников", callback_data="get_rating")
# keyboard_start = InlineKeyboardMarkup(inline_keyboard=[buttons_start])


# generate keyboard -> Builder
def generate_main_keyboard():
    keyboard_start = InlineKeyboardBuilder()
    keyboard_start.add(
        InlineKeyboardButton(text="Go to quiz", callback_data="start_quiz"),
        InlineKeyboardButton(text="Рейтинг участников", callback_data="get_rating")
    )

    keyboard_start.adjust(1, repeat=True)
    return keyboard_start.as_markup()


