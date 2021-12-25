from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Generate keyboard main
buttons_start = [
    InlineKeyboardButton(text="Go to quiz", callback_data="start_quiz"),
    InlineKeyboardButton(text="Рейтинг участников", callback_data="get_rating")
                    ]

keyboard_start = InlineKeyboardMarkup(inline_keyboard=[buttons_start])
