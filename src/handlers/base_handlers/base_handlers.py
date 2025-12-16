from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart


__all__ = ('router_base_handlers',)


router = Router(name=__name__)


@router.message(CommandStart())
async def handler_start_message(message: Message):
    await message.answer('start')


@router.message(Command('help'))
async def handler_help_message(message: Message):
    await message.answer('help')