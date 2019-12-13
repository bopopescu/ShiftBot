import logging
from logging import getLogger, StreamHandler, Formatter, FileHandler

logger = getLogger("ShiftBotLog")

# ハンドラに渡すエラーメッセージのレベル
logger.setLevel(logging.INFO)

logHandler = StreamHandler()
logfileHandler = FileHandler(filename="ShiftBotLog.log", mode="a")

# ハンドラが出力するエラーメッセージのレベル
logHandler.setLevel(logging.DEBUG)
logfileHandler.setLevel(logging.INFO)

# ログ出力のフォーマット設定
logFormat = Formatter("%(asctime)s - %(name)s\n\t%(levelname)s - %(message)s")
logHandler.setFormatter(logFormat)
logfileHandler.setFormatter(logFormat)

logger.addHandler(logHandler)
logger.addHandler(logfileHandler)

def logInfo(text):
    logger.info(text)

def logException(text):
    logger.exception(text)