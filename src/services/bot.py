from aiogram import Bot
from src.config import load_config


config = load_config()


if __name__ != '__main__':
    bot = Bot(token=config.bot.token)