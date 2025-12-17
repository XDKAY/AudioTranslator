from aiogram import Router
from .base_handlers import router_base_handlers
from .defaul_handler import router_regular_message_handler
from .user_handlers import *


__all__ = ('handlers_router', )


handlers_router = Router(name=__name__)

handlers_router.include_routers(
    router_base_handlers,
    router_user_handlers,
    router_regular_message_handler
)