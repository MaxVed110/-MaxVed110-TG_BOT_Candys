import logging


logger = logging.getLogger('Candis_bot')
logger.setLevel(logging.INFO)
log_save = logging.FileHandler('logger.log')
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_save.setFormatter(formatter)
logger.addHandler(log_save)


def logger_clr():
    with open('logger.log', 'w'):
        pass