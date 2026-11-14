import logging


def setup_logger(name, logfile, fmt="%(asctime)s | %(message)s"):
    """Створює/повертає логер з ім'ям `name`, що пише у файл `logfile`."""
    logger = logging.getLogger(name)

    if not logger.handlers:
        handler = logging.FileHandler(logfile, encoding="utf-8")
        handler.setFormatter(logging.Formatter(fmt))
        logger.addHandler(handler)

    return logger
