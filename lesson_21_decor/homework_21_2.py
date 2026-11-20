import functools
import logging
from hw_log import setup_logger

logger = setup_logger("GuardLogger", "guard.log")
logger.setLevel(logging.INFO)


def guard(secret):
    """Декоратор @guard(secret) — захищає функцію паролем.

    Перед кожним викликом питає пароль. Правильний — функція виконується
    (INFO у лог). Неправильний — виводить повідомлення про відмову,
    логує WARNING і повертає None без виклику функції.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            password = input("Назви пароль: ")

            if password == secret:
                logger.info(f"Доступ надано: {func.__name__}")
                return func(*args, **kwargs)

            logger.warning(f"Невдала спроба доступу до: {func.__name__}")
            print("Стій! Доступ заборонено.")
            return None
        return wrapper
    return decorator


@guard(secret="Мамай")
def open_treasury():
    print("Скарбниця відчинена!")
    return "золото, срібло, зброя"


result = open_treasury()
print(result)
