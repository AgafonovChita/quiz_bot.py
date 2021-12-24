async def insert_user(message, nickname, name_tg, nickname_tg, date_register):
    query = '''INSERT INTO users 
                (id_user, nickname_bot, name_tg, nickname_tg, date_register) VALUES ($1, $2, $3, $4, $5)'''
    params = message.chat.id, nickname, name_tg, nickname_tg, date_register
    status = await db_engine.execute(query, params, False)
    return status
