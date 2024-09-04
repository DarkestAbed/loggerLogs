# loggerLogs/convenient.py

from logging import Logger

from loggerLogs.configs import (
    LOGGING_LEVEL_LOGGER,
    LOGGING_LEVEL_CONSOLE,
    LOGGING_LEVEL_FILE,
)
from loggerLogs.customlogger import CustomLogger

custom_logger: CustomLogger = CustomLogger(
    log_level=LOGGING_LEVEL_LOGGER,
    console_log=True,
    console_log_level=LOGGING_LEVEL_CONSOLE,
    file_log=False,
    file_log_level=None,
)
logs: Logger = custom_logger.logger
