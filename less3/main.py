import asyncio
import config
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import logging
from handers import common, msg, carrier

async def main():
    #Логирование
    logging.basicConfig(level=logging.INFO)

    # Объект бота и диспетчера
    bot = Bot(token=config.token)
    dp = Dispatcher()

    dp.include_router(carrier.router)
    dp.include_router(common.router)
    dp.include_router(msg.router)

    await dp.start_polling(bot)


if __name__ == '__main__':
   asyncio.run(main())