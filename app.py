import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode


from hendlers.user_private import user_private_router
from hendlers.user_group import user_group_router
from config import token, ALLOWED_UPDATES
from common.bot_cmds_list import private

bot = Bot(token, parse_mode=ParseMode.HTML)
dp = Dispatcher()


dp.include_router(user_private_router)
dp.include_router(user_group_router)


async def main():
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)
    # await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())

    await bot.set_my_commands(
        commands=private, scope=types.BotCommandScopeAllPrivateChats())


asyncio.run(main())
