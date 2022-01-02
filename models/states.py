from aiogram.dispatcher.fsm.state import State, StatesGroup


class RegisterUser(StatesGroup):
    user_nickname = State()


class AddNewTopic(StatesGroup):
    add_topic = State()
