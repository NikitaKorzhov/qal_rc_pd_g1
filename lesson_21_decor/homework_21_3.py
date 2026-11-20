import functools
import logging
import random
import time
from hw_log import setup_logger

logger = setup_logger("RetryLogger", "retry.log")
logger.setLevel(logging.INFO)


def retry(times=3, delay=1.0):
    """Декоратор @retry(times, delay) — повторює виклик функції при помилці.

    Кожна невдала спроба логується як WARNING (номер спроби + текст помилки).
    Якщо всі спроби вичерпано — логується ERROR і виняток піднімається повторно.
    Якщо виклик вдався — логується INFO з номером успішної спроби.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    result = func(*args, **kwargs)
                except Exception as e:
                    logger.warning(f"Спроба {attempt}/{times} не вдалася: {e}")

                    if attempt == times:
                        logger.error(f"Усі спроби вичерпано ({times}/{times}): {e}")
                        raise

                    time.sleep(delay)
                else:
                    logger.info(f"Успіх на спробі {attempt}/{times}")
                    return result
        return wrapper
    return decorator


@retry(times=4, delay=0.5)
def unreliable_scout():
    if random.random() < 0.7:  # 70% шанс провалу
        raise ConnectionError("Розвідник не повернувся")
    return "Ворог за річкою!"


result = unreliable_scout()
print(result)
