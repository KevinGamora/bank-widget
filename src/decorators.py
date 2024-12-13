
import functools
import logging
from typing import Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger = logging.getLogger(func.__name__)
            handler = logging.FileHandler(filename) if filename else logging.StreamHandler()
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)

            try:
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} ok")
                return result
            except Exception as e:
                logger.error(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise
            finally:
                logger.removeHandler(handler)

        return wrapper
    return decorator
