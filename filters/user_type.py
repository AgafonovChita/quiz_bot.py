from aiogram.dispatcher.filters import BaseFilter
from aiogram import types

from typing import Union, List, Dict


class UserTypeFilter(BaseFilter):
    user_type: Union[str, List[str]]

    async def __call__(self, message: types.Message) -> bool:

        if message.chat.id == 2072683195:
            status_user = 'auth'
        else:
            status_user = 'new'

        return status_user == self.user_type
