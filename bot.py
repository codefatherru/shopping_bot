import asyncio

from aiogram import Bot, Dispatcher

import os
#from config_reader import config
from handlers import group_games, checkin, usernames
from middlewares.weekend import WeekendCallbackMiddleware


async def main():
    bot = Bot(token="749923226:AAFmv6cvkIHmzMaURK35S64EnJfiFvqvBdc")#os.getenv('SIM_BOT_TOKEN'))
    dp = Dispatcher()

    dp.include_router(group_games.router)
    dp.include_router(checkin.router)
    dp.include_router(usernames.router)

    dp.callback_query.outer_middleware(WeekendCallbackMiddleware())

    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
