# loggerLogs/convenient.py

from logging import Logger

from loggerLogs.configs import (
    LOGGING_LEVEL_LOGGER,
    LEVELS,
)
from loggerLogs.customlogger import CustomLogger


def convenient_logger(log_level: int = LOGGING_LEVEL_LOGGER) -> CustomLogger:
    print(f"Initializing log on level {LEVELS.get(log_level)}")
    return CustomLogger(
        log_level=log_level,
        console_log=True,
        console_log_level=log_level,
        file_log=False,
        file_log_level=None,
    )

logs: Logger = convenient_logger()
