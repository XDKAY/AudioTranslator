from aiogram import Dispatcher
from src.handlers import handlers_router


dispatcher = Dispatcher()
dispatcher.include_router(handlers_router)