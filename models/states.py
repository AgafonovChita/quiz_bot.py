from aiogram.dispatcher.fsm.state import State, StatesGroup


class RegisterUser(StatesGroup):
    user_nickname = State()

