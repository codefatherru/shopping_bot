import asyncio
import logging
import os
from aiogram import Bot, Dispatcher

#from config_reader import config
from handlers import in_pm, bot_in_group, admin_changes_in_group, events_in_group, group_games, checkin, usernames, questions, different_types
from middlewares.weekend import WeekendCallbackMiddleware

async def main():
    bot = Bot(token=os.getenv('SIM_BOT_TOKEN'))
    dp = Dispatcher()
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    dp.include_router(group_games.router)
    dp.include_router(checkin.router)
    dp.include_router(usernames.router)
    dp.include_router(in_pm.router)
    dp.include_router(events_in_group.router)
    dp.include_router(bot_in_group.router)
    dp.include_router(admin_changes_in_group.router)

    dp.callback_query.outer_middleware(WeekendCallbackMiddleware())

    admins = await bot.get_chat_administrators(os.getenv('MAIN_CHAT_ID'))
    admin_ids = {admin.user.id for admin in admins}

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types(), admins=admin_ids)


if __name__ == "__main__":
    asyncio.run(main())
