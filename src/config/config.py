from os import getenv
from dataclasses import dataclass
from dotenv import load_dotenv


load_dotenv()


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