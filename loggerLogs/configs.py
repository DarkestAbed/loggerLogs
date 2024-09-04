# loggerLogs/configs.py

from logging import DEBUG, INFO
from os import environ

# logging formats
LOGGING_LEVEL_LOGGER: int = (lambda: DEBUG if environ.get("ENVIRON") == "dev" else INFO)()  # debug: 10, info: 20
LOGGING_LEVEL_CONSOLE: int = LOGGING_LEVEL_LOGGER
LOGGING_LEVEL_FILE: int = LOGGING_LEVEL_LOGGER
LOGGING_FORMAT: str = "%(asctime)s || %(filename)s::%(module)s - %(funcName)s (%(lineno)d) || %(process)d::%(processName)s :: %(levelname)s :: %(message)s"
# date formats
DATE_FMT: str = "%Y%m%d"
DATETIME_FMT: str = "%Y%m%d%H%M%S"
TIMESTAMP_FMT: str = "%Y-%m-%d %H:%M:%S.%f"
