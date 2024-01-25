from typing import Any
from aiogram.filters import Filter
from aiogram import types


class ChatTypeFilter(Filter):
    def __init__(self, chat_typs: list[str]) -> None:
        self.chat_pyps = chat_typs

    async def __call__(self, message: types.Message) -> bool:
        return message.chat.type in self.chat_pyps
