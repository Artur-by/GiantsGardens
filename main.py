import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import config
import db
from handlers import router

async def main():

    # Создаем таблицу telegram_user
    await db.create_user_table()
    # Объект бота:
    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    # Диспетчер:
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(router)
    #  <- подключает к нашему диспетчеру все обработчики, которые используют router

    await bot.delete_webhook(drop_pending_updates=True)
    # - удаляет все обновления, которые произошли после последнего завершения работы бота

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    #- запуск процесса поллинга новых апдейтов



if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, filename="log.log", filemode="a")
    asyncio.run(main())