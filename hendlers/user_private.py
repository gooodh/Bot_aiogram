from aiogram import F, Router, types
from aiogram.filters import CommandStart, Command, or_f

from filters.chat_types import ChatTypeFilter

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())
async def start_cmd(message):
    await message.answer('Start')


@user_private_router.message(or_f(Command("menu"), (F.text.lower() == "меню")))
async def menu_cmd(message: types.Message):
    await message.answer("Вот меню:")


@user_private_router.message(F.text.lower() == "о нас")
@user_private_router.message(Command("about"))
async def about_cmd(message: types.Message):
    await message.answer("О нас:")


@user_private_router.message(F.text.lower() == "варианты оплаты")
@user_private_router.message(Command("payment"))
async def payment_cmd(message: types.Message):
    await message.answer("Варианты оплаты:")


# @user_private_router.message((F.text.lower().contains('доставк')) | (F.text.lower() == 'варианты доставки'))
@user_private_router.message(F.text.lower().contains('доставк'))
@user_private_router.message(Command("shipping"))
async def shipping_cmd(message: types.Message):
    await message.answer("Варианты доставки:")



# @user_private_router.message()
# async def echo(message):
#     await message.answer(message.text)


# @user_private_router.message()
# async def welcome_message(message):
#     text = message.text.lower()
#     if text in ['привет', 'здравствуйте', 'hello', 'hi']:
#         await message.answer('Hello!')
#     elif text in ['пока', 'досвидания', 'while']:
#         await message.answer('Пока!')
#     else:
#         await message.answer(message.text)
