from functools import wraps
import logging

logging.basicConfig(filename='logging.log', format='%(asctime)s %(message)s', level='INFO')


def log_message(func):
    @wraps(func)
    def wrapper(update, *args, **kwargs):
        logging.info(update.message)
        return func(update, *args, **kwargs)

    return wrapper
