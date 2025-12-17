from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.state import default_state


__all__ = ('router',)


router = Router(name=__name__)


@router.message(CommandStart(), StateFilter(default_state))
async def handler_start_message(message: Message):
    await message.answer('start')


@router.message(Command('help'), StateFilter(default_state))
async def handler_help_message(message: Message):
    await message.answer('help')