import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart

from config import token


bot = Bot(token)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message):
    await message.answer('Start')


# @dp.message()
# async def echo(message):
#     await message.answer(message.text)


@dp.message()
async def welcome_message(message):
    text = message.text.lower()
    if text in ['привет', 'здравствуйте', 'hello', 'hi']:
        await message.answer('Hello!')
    elif text in ['пока', 'досвидания', 'while']:
        await message.answer('Пока!')
    else:
        await message.answer(message.text)


async def main():
    await dp.start_polling(bot)

asyncio.run(main())
