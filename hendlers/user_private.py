from aiogram import Router
from aiogram.filters import CommandStart, Command

user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message):
    await message.answer('Start')


# @user_private_router.message()
# async def echo(message):
#     await message.answer(message.text)


@user_private_router.message(Command('menu'))
async def menu_cmd(message):
    await message.answer('menu pizza')


@user_private_router.message()
async def welcome_message(message):
    text = message.text.lower()
    if text in ['привет', 'здравствуйте', 'hello', 'hi']:
        await message.answer('Hello!')
    elif text in ['пока', 'досвидания', 'while']:
        await message.answer('Пока!')
    else:
        await message.answer(message.text)
