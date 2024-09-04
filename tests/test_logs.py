# test/test_logs.py

from logging import Logger
from typing import NoReturn

from loggerLogs import logs


def test_init_customlogger() -> NoReturn:
    try:
        resp = logs
    except Exception:
        raise Exception
    assert isinstance(resp, Logger)
