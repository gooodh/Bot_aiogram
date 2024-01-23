import asyncio
from aiogram import Bot, Dispatcher

from hendlers.user_private import user_private_router
from config import token, ALLOWED_UPDATES

bot = Bot(token)
dp = Dispatcher()
dp.include_router(user_private_router)


async def main():
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

asyncio.run(main())
