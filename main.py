from asyncio import run
from src.services.bot import bot

from src.core.app import dispatcher
from src.utils.logger import logger


log = logger(__name__)


async def main():
    log.info('Бот запущен')
    await dispatcher.start_polling(bot)


if __name__ == '__main__':
    run(main())
