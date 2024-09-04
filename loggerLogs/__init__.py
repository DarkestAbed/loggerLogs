# loggerLogs/__init__.py

from os import environ

from loggerLogs.convenient import logs


environ.update({"ENVIRON": "dev"})

__all__ = []
