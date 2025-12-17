from aiogram.fsm.state import StatesGroup, State


__all__ = ('StateGetVoiceMessage',)


class StateGetVoiceMessage(StatesGroup):
    get_voice_message = State()