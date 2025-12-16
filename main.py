from asyncio import run

from aiogram import Bot

from src.config import load_config
from src.core.app import dispatcher
from src.utils.logger import logger


config = load_config()
log = logger(__name__)


async def main():
    bot = Bot(token=config.bot.token)

    log.info('Бот запущен')

    await dispatcher.start_polling(bot)


if __name__ == '__main__':
    run(main())