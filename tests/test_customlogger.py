# tests/test_customlogger.py

import pytest

from logging import INFO
from typing import NoReturn

from loggerLogs.customlogger import CustomLogger
from loggerLogs.singletons import Singleton


def test_init_customlogger() -> NoReturn:
    try:
        resp = CustomLogger()
    except Exception:
        raise Exception
    finally:
        Singleton.destroy(resp)
    assert isinstance(resp, CustomLogger)


def test_bad_loglevel_values_on_init() -> NoReturn:
    with pytest.raises(AttributeError):
        try:    
            resp = CustomLogger(log_level=1)
        except AttributeError:
            raise AttributeError


def test_bad_path_on_init() -> NoReturn:
    with pytest.raises(FileNotFoundError):
        PATH_BAD: str = "/home/javi/aNonExistantFolder"
        try:    
            resp = CustomLogger(file_log=True, file_log_level=INFO, file_log_path=PATH_BAD)
        except FileNotFoundError:
            raise FileNotFoundError


def test_null_path_on_init() -> NoReturn:
    with pytest.raises((FileNotFoundError, ValueError)):
        try:
            resp = CustomLogger(
                file_log=True,
                file_log_level=INFO,
                file_log_path=None,
            )
        except FileNotFoundError:
            raise FileNotFoundError
        except ValueError:
            raise ValueError


def test_wrong_combination_of_file_log_parameters() -> NoReturn:
    with pytest.raises(RuntimeError):
        PATH_TEST: str = "/home/javithompson/projects/loggerLogs"
        try:
            resp = CustomLogger(
                file_log=False,
                file_log_level=INFO,
                file_log_path=PATH_TEST,
            )
        except RuntimeError:
            raise RuntimeError
