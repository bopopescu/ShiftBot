import logging
from logging import getLogger, StreamHandler, Formatter, FileHandler

sep = '########################'

class LoggingFilter(level):
    def __init__(self, level):
        self.__level = level
    
    def filter(self, record):
        return record.levelno <= self.__level


logger = getLogger(__name__)


def setLogHandler(level, filename):
    logFormat = logging.Formatter(sep+'\n%(asctime)s\n\t%(levelname)s - %(message)s\n')
    handler = logging.FileHandler(filename)
    handler.setLevel(level)
    handler.setFormatter(logFormat)
    handler.addFilter(LoggingFilter(level))
    logger.addHandler(handler)

logger.setLevel(logging.DEBUG)
setLogHandler(logging.INFO, './info.log')
setLogHandler(logging.WARNING, './warning.log')
setLogHandler(logging.ERROR, './error.log')

def logInfo(text):
    logger.info(text)

def logWarning(text):
    logger.warn(text)

def logException(text):
    logger.exception(text)