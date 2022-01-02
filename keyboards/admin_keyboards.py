from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from aiogram.dispatcher.filters.callback_data import CallbackData


# generate keyboard Builder
# -> main keyboard
async def generate_admin_key():
    keyboard_start = InlineKeyboardBuilder()
    keyboard_start.add(
        InlineKeyboardButton(text="Add new topic", callback_data="add_topic"),
        InlineKeyboardButton(text="Add questions", callback_data="add_questions"),
        InlineKeyboardButton(text="Edit topic", callback_data="edit_topic"),
        InlineKeyboardButton(text="Delete topic", callback_data="delete_topic"),
    )
    keyboard_start.adjust(2, repeat=True)
    return keyboard_start.as_markup()