from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from db.db_engine import DB_engine


class DBPool(BaseMiddleware):
    def __init__(self, pool) -> None:
        super().__init__()
        self.pool = pool

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        async with self.pool.acquire() as session:
            data['db_connect'] = session
            data['db_engine'] = DB_engine(session)

            result = await handler(event, data)

            data.pop('db_connect')
            data.pop('db_engine')
            db_connect = data.get("db_connect")
            db_engine = data.get("db_engine")

            if db_connect:
                await db_connect.close()

            if db_engine:
                await db_engine.close()

            return result
