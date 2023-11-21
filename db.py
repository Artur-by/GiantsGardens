import asyncpg
import config

# Устанавливаем соединение с базой данных
async def connect_to_db():
    return await asyncpg.connect(database=config.DATABASE, user=config.PGUSER,
                                 password=config.PGPASSWORD, host=config.PGHOST)

# Создаем таблицу пользователей, если её еще нет
async def create_user_table():
    conn = await connect_to_db()
    await conn.execute('''
        CREATE TABLE IF NOT EXISTS our_users(
            user_id BIGINT PRIMARY KEY,
            user_name TEXT,
            user_full_name TEXT
        )
    ''')
    await conn.close()

# Создаем таблицу с записями о проблемах
async def create_send_problems():
    conn = await connect_to_db()
    await conn.execute('''
        CREATE TABLE IF NOT EXISTS tasks(
            user_id BIGINT,
            cur_date DATE,
            cur_time TIME,
            problem TEXT,
            status BOOL
        )
    ''')
    await conn.close()

# Функция, чтобы проверить, существует ли пользователь
async def check_user_exists(user_id):
    conn = await connect_to_db()
    result = await conn.fetchval('SELECT user_id FROM our_users WHERE user_id = $1', user_id)
    await conn.close()
    return result is not None


# Функция, чтобы добавить нового пользователя
async def add_new_user(user_id, user_name, user_full_name):
    conn = await connect_to_db()
    await conn.execute('INSERT INTO our_users(user_id, user_name,  user_full_name) VALUES($1, $2, $3)',
                       user_id, user_name, user_full_name)
    await conn.close()

# Функция, чтобы записать новую проблему
async def add_new_problem(user_id, cur_date, cur_time, problem, status=True ):
    conn = await connect_to_db()
    await conn.execute('INSERT INTO tasks(user_id, cur_date, cur_time, problem, status) VALUES($1, $2, $3,$4, $5)',
                       user_id, cur_date, cur_time, problem, status)
    await conn.close()
