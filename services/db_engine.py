from typing import List
import asyncpg
import config


async def create_pool():
    pool = await asyncpg.create_pool(host=config.db_host,
                                     port=config.db_port, user=config.db_user, password=config.db_pass,
                                     database=config.db_type)
    return pool

class DB_engine:
    def __init__(self, conn):
        self.conn = conn

    async def execute(self, query, params, ans):
        if ans:
            result = await self.conn.fetch(query, *params)
            return result
        else:
            await self.conn.execute(query, *params)

    async def check_user(self, id_user):
        query = '''SELECT id_user FROM users WHERE id_user=$1'''
        check = await self.conn.fetch(query, id_user)
        if check:
            return True

    async def get_name(self, id_user):
        query = '''SELECT nickname_bot FROM users WHERE id_user=$1'''
        name_user = await self.conn.fetch(query, id_user)
        if name_user:
            return name_user[0][0]
        return 'Name_user errors'

    async def add_user(self, id_user, nickname_bot, name_tg, nickname_tg, date_register):
        query = '''INSERT INTO users 
                           (id_user, nickname_bot, name_tg, nickname_tg, date_register) VALUES ($1, $2, $3, $4, $5)'''
        params = id_user, nickname_bot, name_tg, nickname_tg, date_register
        await self.conn.execute(query, *params)

    async def get_topic_info(self, id_topic):
        query = '''SELECT * FROM topics WHERE id_topic=$1'''
        topic_data = await self.conn.fetch(query, id_topic)
        if topic_data:
            return topic_data
        return ['Topic not found', 'Topic not found', 'Topic not found', 'Topic not found', 'Topic not found', 'Topic not found', ]