# loggerLogs/convenient.py

from logging import Logger

from loggerLogs.configs import (
    LOGGING_LEVEL_LOGGER,
    LOGGING_LEVEL_CONSOLE,
    LEVELS,
)
from loggerLogs.customlogger import CustomLogger


custom_logger: CustomLogger = CustomLogger(
    log_level=LOGGING_LEVEL_LOGGER,
    console_log=True,
    console_log_level=LOGGING_LEVEL_CONSOLE,
    file_log=False,
    file_log_level=None,
)
print(f"Initializing simple logger on level {LEVELS.get(LOGGING_LEVEL_LOGGER)}.")
logs: Logger = custom_logger.logger
