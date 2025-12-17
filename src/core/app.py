from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from src.handlers import handlers_router

storage = MemoryStorage()

dispatcher = Dispatcher(storage=storage)
dispatcher.include_router(handlers_router)