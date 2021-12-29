from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from aiogram.dispatcher.filters.callback_data import CallbackData


#CallbackData  - TopicKeyboards
class DataTopic(CallbackData, prefix="topic"):
    topic_id: int
    topic_name: str


# generate keyboard Builder
# -> main keyboard
async def generate_main_key():
    keyboard_start = InlineKeyboardBuilder()
    keyboard_start.add(
        InlineKeyboardButton(text="Go to quiz", callback_data="start_quiz"),
        InlineKeyboardButton(text="Рейтинг участников", callback_data="get_rating")
    )
    keyboard_start.adjust(1, repeat=True)
    return keyboard_start.as_markup()


# -> topic keyboard
async def generate_topic_key(db_engine):
    list_topics = [[47001, 'Маматика'], [47002, 'Информатика'], [47003, 'Всё обо всём']]

    keyboard_topic = InlineKeyboardBuilder()
    for topic in list_topics:
        keyboard_topic.add(InlineKeyboardButton(text=topic[1],
                                                callback_data=DataTopic(topic_id=topic[0], topic_name=topic[1]).pack()))

    keyboard_topic.adjust(3, repeat=True)
    return keyboard_topic.as_markup()


# -> let's go keyboard
async def generate_goquiz_key():
    keyboard_topic = InlineKeyboardBuilder()
    keyboard_topic.add(
        InlineKeyboardButton(text='Погнали', callback_data="go_quiz")
    )
    keyboard_topic.adjust(1, repeat=False)
    return keyboard_topic.as_markup()









"""
#generate keyboard -> Markup
buttons_start = [
    InlineKeyboardButton(text="Go to quiz", callback_data="start_quiz"),
    InlineKeyboardButton(text="Рейтинг участников", callback_data="get_rating")
keyboard_start = InlineKeyboardMarkup(inline_keyboard=[buttons_start])
"""
