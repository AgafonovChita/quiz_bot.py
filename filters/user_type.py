from aiogram.dispatcher.filters import BaseFilter
from aiogram import types

from typing import Union, List, Dict, Any
from db.db_engine import DB_engine


class UserTypeFilter(BaseFilter):
    user_type: Union[str, List[str]]

    async def __call__(self, message: types.Message, pool:Any) -> bool:
        db_engine = DB_engine(pool)
        check = await db_engine.check_user(message.chat.id)
        if check:
            status_user = 'auth'
        else:
            status_user = 'new'

        return status_user == self.user_type
