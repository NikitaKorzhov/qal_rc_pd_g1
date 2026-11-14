import functools
from hw_log import setup_logger
import logging

logger = setup_logger("ChronicleLogger", "chronicle.log")
logger.setLevel(logging.INFO)

def chronicle(chronicler="Анонімний"):
    if callable(chronicler):
        func = chronicler
        chronicler_name = "Анонімний"
        return warper(func, chronicler_name)
    def decorator(func):
        return warper(func, chronicler)
    
    return decorator

def warper(func, chronicler_name):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)

        # Виклик функції через INFO
        logger.info(f"[Літописець: {chronicler_name}] Викликано: {func.__name__}({signature})")
        
        result = func(*args, **kwargs)
        
        # Результат виконання через INFO
        logger.info(f"[Результат]: {result!r}")
        
        return result
    return wrapper


@chronicle("Самійло Величко")
def make_decision(action, target):
    return f"Рішення: {action} → {target}"

@chronicle()
def count_warriors(regiment):
    return 500

make_decision("Атакувати", "Перекоп")
count_warriors("Полтавський")