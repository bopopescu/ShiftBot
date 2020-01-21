import logging
from logging import getLogger, StreamHandler, Formatter, FileHandler

# class LoggingFilter():
    # def __init__(self, level):
    #    self.__level = level
    
    # def filter(self, record):
    #     return record.levelno <= self.__level

class LogHandler:
    sep = '########################'

    logger = getLogger(__name__)
    logger.setLevel(logging.INFO)

    logFormat = logging.Formatter(sep+'\n%(asctime)s\n\t%(levelname)s - %(message)s\n')

    def setLogHandler(self, level, filename):
        handler = logging.FileHandler(filename)
        handler.setLevel(level)
        handler.setFormatter(logFormat)
        logger.addHandler(handler)

    setLogHandler(logging.ERROR, './error.log')
    setLogHandler(logging.WARNING, './warning.log')
    setLogHandler(logging.INFO, './info.log')

    def logInfo(self, text):
        logger.info(text)

    def logWarning(self, text):
        logger.warn(text)

    def logException(self, text):
        logger.exception(text)
