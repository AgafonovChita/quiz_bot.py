from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from aiogram.dispatcher.filters.callback_data import CallbackData


# generate keyboard Builder
# -> admin keyboard
async def generate_admin_key():
    keyboard_admin = InlineKeyboardBuilder()
    keyboard_admin.add(
        InlineKeyboardButton(text="Add new topic", callback_data="add_topic"),
        InlineKeyboardButton(text="Add questions", callback_data="add_questions"),
        InlineKeyboardButton(text="Edit topic", callback_data="edit_topic"),
        InlineKeyboardButton(text="Delete topic", callback_data="delete_topic"),
    )
    keyboard_admin.adjust(2, repeat=True)
    return keyboard_admin.as_markup()