"""Example module for the demo package"""

from .logger_config import logger


def hello_world(message):
    """Example function to say Hello world with a message"""
    logger.debug("This is DEBUG level log message")
    logger.info("This is INFO level log message")
    logger.warning("This is WARN level log message")
    logger.error("This is ERROR level log message")
    return f"Hello world!: {message}"


def repeat_three_times(filepath: str) -> str:
    """讀取檔案內容並重複三次。"""
    with open(filepath, mode="r", encoding="utf-8") as f:
        content = f.read().strip()
        
    # 將內容重複 3 次，中間用換行隔開
    return "\n".join([content] * 3)