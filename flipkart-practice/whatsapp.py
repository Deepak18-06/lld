from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
import json
import os
import threading
from queue import Queue


class LogLevel(Enum):
    DEBUG = 1
    INFOR = 2
    WARNING = 3
    ERROR = 4
    CRITICAL = 5

@dataclass
class LogRecord:
    timestamp: datetime
    level: LogLevel
    message: str
    context: Dict[str, Any]
    logger_name = str


class LogFormatter(ABC):
    @abstractmethod
    def format(self):
        pass

class LogHandler(ABC):
    @abstractmethod
    def handle(self):
        pass
class LogFitler(ABC):
    @abstractmethod
    def should_log(self):
        pass

class JsonFormatter(LogFormatter):
    def format(self, record: LogRecord):
        return json.dump(
            {
                'timestamp': record.timestamp.isf
            }
        )
    
class TextFormatter(LogFormatter):
    def format(self, record: LogRecord):
        return f"{record.timestamp} - {record.message}- "
    

class ConsoleHandler(LogHandler):
    def __init__(self, formatter) -> None:
        self.formatter = formatter

    def handle(self, record: LogRecord):
        formated_message = self.formatter(record)
        print(formated_message)

class FileHandler(LogHandler):
    def __init__(self, formatter, file_name) -> None:
        self.formatter = formatter
        self.file_name = file_name

    def handle(self, record: LogRecord):
        formatted_record = self.formatter(record)


class LevelFilter(LogFitler):
    def __init__(self, min_level: LogLevel):
        self.min_level = min_level

    def should_log(self, record):
        return record.level.value >= self.min.value
    
class ContextFilter(LogFitler):
    def __init__(self) -> None:
        self.requirem