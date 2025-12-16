from aiogram import Router
from aiogram.types import Message


__all__ = ('router_regular_message_handler',)


router_regular_message_handler = Router(name=__name__)


@router_regular_message_handler.message()
async def handler_regular_message(message: Message):
    await message.answer('I do not know of such a command.')