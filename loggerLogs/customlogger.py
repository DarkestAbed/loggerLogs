# loggerLogs/module.py
"""
## `loggerLogs` module
A custom, tailor-made implementation of the Logger library.

Classes:
    CustomLogger

Methods:
    __init__()
"""

from dataclasses import dataclass
from datetime import datetime
from logging import (
    Logger,
    StreamHandler,
    FileHandler,
    Formatter,
    getLogger,
    DEBUG,
    INFO,
    WARNING,
    ERROR,
)
from os.path import exists, join

from loggerLogs.configs import (
    DATE_FMT,
    LEVELS,
    LOGGING_LEVEL_LOGGER,
    LOGGING_LEVEL_CONSOLE,
    LOGGING_FORMAT,
)


@dataclass
class CustomLogger:
    """
    ## `CustomLogger` class


    Methods:
        __init__()

    Args:
        metaclass (_type_, optional): _description_. Defaults to Singleton.
    """
    def __init__(
            self,
            log_level: int = LOGGING_LEVEL_LOGGER,
            console_log: bool = True,
            console_log_level: int = LOGGING_LEVEL_CONSOLE,
            file_log: bool = False,
            file_log_path: str | None = None,
            file_log_level: int | None = None,
        ) -> None:
        """
        ## Constructor method

        Args:
            log_level (int, optional): _description_. Defaults to LOGGING_LEVEL_LOGGER.
            console_log (bool, optional): _description_. Defaults to True.
            console_log_level (int, optional): _description_. Defaults to LOGGING_LEVEL_CONSOLE.
            file_log (bool, optional): _description_. Defaults to False.
            file_log_path (str, optional): _description_. Defaults to `$PWD/logs`.
            file_log_level (int, optional): _description_. Defaults to LOGGING_LEVEL_FILE.

        Returns:
            None
        """
        LOGGING_LEVELS_INT: list[int] = [DEBUG, INFO, WARNING, ERROR]
        date: str = datetime.strftime(datetime.now(), DATE_FMT)
        # guardrails
        if log_level not in LOGGING_LEVELS_INT:
            print("Log level not allowed")
            raise AttributeError
        if console_log_level not in LOGGING_LEVELS_INT:
            print("Console log level not allowed")
            raise AttributeError
        if file_log is True and file_log_level not in LOGGING_LEVELS_INT:
            print("File log level not allowed")
            raise AttributeError
        if file_log is True:
            if file_log_path is None:
                print("Path cannot be 'None'")
                raise ValueError
            if not exists(file_log_path):
                print("File log path unavailable")
                raise FileNotFoundError
        if file_log is False:
            if file_log_level is not None or file_log_path is not None:
                print("File log config error")
                raise RuntimeError
        # logger setup
        print(f"Initializing logger on level {LEVELS.get(log_level)}.")
        self.logger: Logger = getLogger(__name__)
        self.logger.setLevel(level=log_level)
        formatter = Formatter(LOGGING_FORMAT)
        if console_log:
            ## console logger
            self.console_log = StreamHandler()
            self.console_log.setLevel(level=console_log_level)
            self.console_log.setFormatter(formatter)
            self.logger.addHandler(self.console_log)
        if file_log:
            ## file logger
            log_path = join(file_log_path, f"{date}-execution.log")
            self.file_log = FileHandler(filename=log_path, mode="w", encoding="latin-1", delay=False)
            self.file_log.setLevel(level=file_log_level)
            self.file_log.setFormatter(formatter)
            self.logger.addHandler(self.file_log)
        return None

    def debug(self, txt: str) -> None:
        self.logger.debug(txt)
        return None

    def info(self, txt: str) -> None:
        self.logger.info(txt)
        return None

    def warning(self, txt: str) -> None:
        self.logger.warning(txt)
        return None

    def error(self, txt: str) -> None:
        self.logger.error(txt)
        return None

    def exception(self, txt: str) -> None:
        self.logger.exception(txt, stack_info=True)
        return None


def main() -> None:
    return None


if __name__ == "__main__":
    main()
else:
    pass
