from aiogram import Router
from .base_handlers import router


__all__ = ('router_base_handlers',)


router_base_handlers = Router(name=__name__)

router_base_handlers.include_router(router)