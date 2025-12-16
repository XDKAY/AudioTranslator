from logging import Logger, basicConfig, getLogger, INFO


def logger(filename: str) -> Logger:
    basicConfig(
        level=INFO,
        format='%(asctime)s - %(module)s - %(levelname)s - %(message)s',
        datefmt='%H:%M:%S'
    )
    return getLogger(filename)