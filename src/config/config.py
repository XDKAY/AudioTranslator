from os import getenv
from dataclasses import dataclass
from dotenv import load_dotenv


load_dotenv()


__all__ = ('load_config',)


@dataclass
class Bot:
    token: str


@dataclass
class Config:
    bot: Bot


def load_config() -> Config:
    return Config(
        bot=Bot(token=getenv('TOKEN'))
    )