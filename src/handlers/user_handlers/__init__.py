from aiogram import Router

from .user_handlers import *


__all__ = ('router_user_handlers',)


router_user_handlers = Router(name=__name__)
router_user_handlers.include_router(router)