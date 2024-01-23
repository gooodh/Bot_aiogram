import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart

from config import token


bot = Bot(token)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message):
    await message.answer('Start')


async def main():
    await dp.start_polling(bot)

asyncio.run(main())
