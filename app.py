import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode


from hendlers.user_private import user_private_router
from hendlers.user_group import user_group_router
from hendlers.admin_private import admin_router
from config import token
from database.engine import create_db, drop_db, session_maker
from common.bot_cmds_list import private
from middlewares.db import DataBaseSession

bot = Bot(token, parse_mode=ParseMode.HTML)
dp = Dispatcher()


dp.include_router(user_private_router)
dp.include_router(user_group_router)
dp.include_router(admin_router)


async def on_startup(bot):
    run_param = False
    if run_param:
        await drop_db()
    await create_db()


async def on_shutdown(bot):
    print('бот лег')


async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    dp.update.middleware(DataBaseSession(session_pool=session_maker))

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    # await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())

    await bot.set_my_commands(
        commands=private, scope=types.BotCommandScopeAllPrivateChats())


asyncio.run(main())
