import asyncio
import logging
import os
from aiogram import Bot, Dispatcher

#from config_reader import config
from handlers import group_games, checkin, usernames, questions, different_types
from middlewares.weekend import WeekendCallbackMiddleware


async def main():
    bot = Bot(token=os.getenv('SIM_BOT_TOKEN'))
    dp = Dispatcher()
    logging.basicConfig(level=logging.INFO)
    dp.include_router(questions.router)
    dp.include_router(different_types.router)
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
