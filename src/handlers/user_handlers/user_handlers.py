from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from src.states import StateGetVoiceMessage
from src.utils.logger import logger


__all__ = ('router', )


log = logger(__name__)

router = Router(name=__name__)


@router.message(Command('voice'))
async def handler_message_get_voice(message: Message, state: FSMContext):
    await message.answer('Отправь мне голосовое сообщение')
    await state.set_state(StateGetVoiceMessage.get_voice_message)


@router.message(StateFilter(StateGetVoiceMessage.get_voice_message), F.voice)
async def get_voice(message: Message, state: FSMContext):
    file_id = message.voice.file_id
    log.info(f'Получено голосовое сообщение с id {file_id}')
    await state.clear()


@router.message(StateFilter(StateGetVoiceMessage.get_voice_message))
async def warning_get_voice(message: Message):
    await message.answer('Ай ай мне нужно голосовое сообщение')