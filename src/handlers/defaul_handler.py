from aiogram import Router
from aiogram.types import Message
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state


__all__ = ('router_regular_message_handler',)


router_regular_message_handler = Router(name=__name__)


@router_regular_message_handler.message(StateFilter(default_state))
async def handler_regular_message(message: Message):
    await message.answer('I do not know of such a command.')