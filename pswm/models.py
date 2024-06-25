from enum import Enum


class Field(Enum):
    NAME = 0
    URL = 1
    USER = 2
    PASS = 3


class Mode(Enum):
    MANUAL = ["M", "m"]
    AUTO = ["A", "a"]
    QUIT = ["Q", "q"]
