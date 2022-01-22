"""warnings.py

Contains custom Errors attached to the Agent model which trigger
warnings to be registered in our system. These warnings do not
disrupt the system, but rather are storaged in memory to be queried
and logged.
"""
import typing as t
from enum import Enum
from unicodedata import category
import warnings


class WarningEnum(str, Enum):
    close_to_memory_limit = "close to memory limit"
    over_memory_limit = "over memory limit"


def warn_close_to_memory_limit(
    agent_name: str, current_storage_useage: int, total_storage: int
) -> None:
    warnings.simplefilter("always")
    msg = f"""{agent_name} is approaching its storage limit. 
        Current storage useage: {current_storage_useage}. 
        Total storage usage: {total_storage}"""

    warnings.warn(msg)


class OverMemoryLimitError(Exception):
    """Error that is raised when an Agents current storage useage reported
    exceeds its set storage limit.
    """

    def __init__(self, value: int, message: str) -> None:
        self.value = value
        self.message = message

        super().__init__(message)


class StorageLimitOutOfRangeError(Exception):
    """Error that is raised when an Agent sets its storage limit to a
    values outside of the range 0 - 100.
    """

    def __init__(self, value: int, message: str) -> None:
        self.value = value
        self.message = message

        super().__init__(message)
