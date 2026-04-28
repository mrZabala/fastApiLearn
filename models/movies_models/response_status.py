from enum import Enum

class ResponseStatus(str, Enum):
    SUCCESS = "SUCCESS"
    EMPTY = "EMPTY"
    ERROR = "ERROR"