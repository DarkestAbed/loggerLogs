# tests/test_customlogger.py

import pytest

from logging import INFO
from typing import NoReturn

from loggerLogs.customlogger import CustomLogger


@pytest.fixture(scope="function")
def customlogger_empty():
    tmp_class: CustomLogger = CustomLogger()
    # return tmp_class
    yield tmp_class
    del tmp_class


@pytest.fixture(scope="class")
def customlogger_bad_values():
    tmp_class: CustomLogger = CustomLogger(log_level=1)
    return tmp_class
    # yield tmp_class
    # del tmp_class


@pytest.fixture(scope="session")
def customlogger_bad_path():
    PATH_BAD: str = "/home/javi/aNonExistantFolder"
    tmp_class: CustomLogger = CustomLogger(
        file_log=True,
        file_log_level=INFO,
        file_log_path=PATH_BAD,
    )
    return tmp_class
    # yield tmp_class
    # del tmp_class


@pytest.fixture(scope="session")
def customlogger_null_path():
    tmp_class: CustomLogger = CustomLogger(
        file_log=True,
        file_log_level=INFO,
        file_log_path=None,
    )
    return tmp_class
    # yield tmp_class
    # del tmp_class


@pytest.fixture(scope="session")
def customlogger_wrong_inputs():
    PATH_TEST: str = "/home/javithompson/projects/loggerLogs"
    tmp_class: CustomLogger = CustomLogger(
        file_log=False,
        file_log_level=INFO,
        file_log_path=PATH_TEST,
    )
    return tmp_class
    # yield tmp_class
    # del tmp_class


def test_init_customlogger(customlogger_empty) -> NoReturn:
    resp = customlogger_empty
    assert isinstance(resp, CustomLogger)


def test_bad_loglevel_values_on_init(customlogger_bad_values) -> NoReturn:
    with pytest.raises(AttributeError):
        resp = customlogger_bad_values


def test_bad_path_on_init(customlogger_bad_path) -> NoReturn:
    with pytest.raises(FileNotFoundError):
        resp = customlogger_bad_path


def test_null_path_on_init(customlogger_null_path) -> NoReturn:
    with pytest.raises((FileNotFoundError, ValueError)):
        resp = customlogger_null_path


def test_wrong_combination_of_file_log_parameters(customlogger_wrong_inputs) -> NoReturn:
    with pytest.raises(RuntimeError):
        resp = customlogger_wrong_inputs
