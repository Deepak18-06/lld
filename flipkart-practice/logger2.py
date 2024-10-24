from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
import json
import os
import threading
from queue import Queue

# Single Responsibility Principle - Each class has one responsibility
# Open/Closed Principle - Easy to extend with new log levels and handlers

class LogLevel(Enum):
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    CRITICAL = 5

@dataclass
class LogRecord:
    timestamp: datetime
    level: LogLevel
    message: str
    context: Dict[str, Any]
    logger_name: str

# Interface Segregation Principle - Separate interfaces for different logging concerns
class LogFormatter(ABC):
    @abstractmethod
    def format(self, record: LogRecord) -> str:
        pass

class LogHandler(ABC):
    @abstractmethod
    def handle(self, record: LogRecord) -> None:
        pass

class LogFilter(ABC):
    @abstractmethod
    def should_log(self, record: LogRecord) -> bool:
        pass

# Concrete implementations of formatters
class JsonFormatter(LogFormatter):
    def format(self, record: LogRecord) -> str:
        return json.dumps({
            'timestamp': record.timestamp.isoformat(),
            'level': record.level.name,
            'message': record.message,
            'context': record.context,
            'logger_name': record.logger_name
        })

class TextFormatter(LogFormatter):
    def format(self, record: LogRecord) -> str:
        return f"[{record.timestamp.isoformat()}] {record.level.name}: {record.message} " \
               f"Context: {record.context} Logger: {record.logger_name}"

# Concrete implementations of handlers
class ConsoleHandler(LogHandler):
    def __init__(self, formatter: LogFormatter):
        self.formatter = formatter

    def handle(self, record: LogRecord) -> None:
        formatted_message = self.formatter.format(record)
        print(formatted_message)

class FileHandler(LogHandler):
    def __init__(self, formatter: LogFormatter, filename: str):
        self.formatter = formatter
        self.filename = filename

    def handle(self, record: LogRecord) -> None:
        formatted_message = self.formatter.format(record)
        with open(self.filename, 'a') as f:
            f.write(formatted_message + '\n')

# Concrete implementations of filters
class LevelFilter(LogFilter):
    def __init__(self, min_level: LogLevel):
        self.min_level = min_level

    def should_log(self, record: LogRecord) -> bool:
        return record.level.value >= self.min_level.value

class ContextFilter(LogFilter):
    def __init__(self, required_fields: List[str]):
        self.required_fields = required_fields

    def should_log(self, record: LogRecord) -> bool:
        return all(field in record.context for field in self.required_fields)

# Observer Pattern - Handlers observe the logger
# Factory Pattern - Creates different types of loggers
class LoggerFactory:
    _loggers: Dict[str, 'Logger'] = {}

    @classmethod
    def get_logger(cls, name: str) -> 'Logger':
        if name not in cls._loggers:
            cls._loggers[name] = Logger(name)
        return cls._loggers[name]

# Singleton Pattern with Thread Safety
class AsyncLogProcessor:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.initialize()
        return cls._instance

    def initialize(self):
        self.queue = Queue()
        self.running = True
        self.worker_thread = threading.Thread(target=self._process_logs)
        self.worker_thread.daemon = True
        self.worker_thread.start()

    def _process_logs(self):
        while self.running:
            try:
                logger, record = self.queue.get()
                if record is None:
                    break
                logger._do_log(record)
                self.queue.task_done()
            except Exception as e:
                print(f"Error processing log: {e}")

    def submit_log(self, logger: 'Logger', record: LogRecord):
        self.queue.put((logger, record))

    def shutdown(self):
        self.running = False
        self.queue.put((None, None))
        self.worker_thread.join()

# Builder Pattern for logger configuration
class LoggerBuilder:
    def __init__(self, name: str):
        self.logger = Logger(name)

    def with_handler(self, handler: LogHandler) -> 'LoggerBuilder':
        self.logger.add_handler(handler)
        return self

    def with_filter(self, log_filter: LogFilter) -> 'LoggerBuilder':
        self.logger.add_filter(log_filter)
        return self

    def with_async_processing(self) -> 'LoggerBuilder':
        self.logger.enable_async_processing()
        return self

    def build(self) -> 'Logger':
        return self.logger

# Main Logger class
class Logger:
    def __init__(self, name: str):
        self.name = name
        self.handlers: List[LogHandler] = []
        self.filters: List[LogFilter] = []
        self.async_processor: Optional[AsyncLogProcessor] = None

    def add_handler(self, handler: LogHandler) -> None:
        self.handlers.append(handler)

    def add_filter(self, log_filter: LogFilter) -> None:
        self.filters.append(log_filter)

    def enable_async_processing(self) -> None:
        self.async_processor = AsyncLogProcessor()

    def _do_log(self, record: LogRecord) -> None:
        if all(f.should_log(record) for f in self.filters):
            for handler in self.handlers:
                handler.handle(record)

    def log(self, level: LogLevel, message: str, context: Dict[str, Any] = None) -> None:
        if context is None:
            context = {}

        record = LogRecord(
            timestamp=datetime.now(),
            level=level,
            message=message,
            context=context,
            logger_name=self.name
        )

        if self.async_processor:
            self.async_processor.submit_log(self, record)
        else:
            self._do_log(record)

    def debug(self, message: str, context: Dict[str, Any] = None) -> None:
        self.log(LogLevel.DEBUG, message, context)

    def info(self, message: str, context: Dict[str, Any] = None) -> None:
        self.log(LogLevel.INFO, message, context)

    def warning(self, message: str, context: Dict[str, Any] = None) -> None:
        self.log(LogLevel.WARNING, message, context)

    def error(self, message: str, context: Dict[str, Any] = None) -> None:
        self.log(LogLevel.ERROR, message, context)

    def critical(self, message: str, context: Dict[str, Any] = None) -> None:
        self.log(LogLevel.CRITICAL, message, context)

# Example usage
def example_usage():
    # Create logger using builder pattern
    logger = (LoggerBuilder("app_logger")
             .with_handler(ConsoleHandler(TextFormatter()))
             .with_handler(FileHandler(JsonFormatter(), "app.log"))
             .with_filter(LevelFilter(LogLevel.INFO))
             .with_filter(ContextFilter(["request_id"]))
             .with_async_processing()
             .build())

    # Log some messages
    logger.info("Application started", {"request_id": "123", "user": "admin"})
    logger.error("Database connection failed", {
        "request_id": "124",
        "error_code": "DB_001"
    })

    # Get same logger instance using factory
    same_logger = LoggerFactory.get_logger("app_logger")
    same_logger.warning("Duplicate request detected", {
        "request_id": "125",
        "duplicate_key": "user_123"
    })

# Decorator for method logging
def log_method(logger_name: str):
    def decorator(func):
        logger = LoggerFactory.get_logger(logger_name)

        def wrapper(*args, **kwargs):
            context = {
                "function": func.__name__,
                "args": str(args),
                "kwargs": str(kwargs)
            }
            
            logger.debug(f"Entering {func.__name__}", context)
            try:
                result = func(*args, **kwargs)
                logger.debug(f"Exiting {func.__name__}", {
                    **context,
                    "result": str(result)
                })
                return result
            except Exception as e:
                logger.error(f"Error in {func.__name__}: {str(e)}", context)
                raise
        return wrapper
    return decorator

# Example usage with decorator
@log_method("math_logger")
def calculate_sum(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    # Basic usage example
    example_usage()

    # Decorator usage example
    result = calculate_sum(5, 3)
    print(f"Sum result: {result}")

    # Cleanup
    AsyncLogProcessor().shutdown()