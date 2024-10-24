class LogEntry:
    def __init__(self, timestamp, level, message, source):
        self.timestamp = timestamp  # DateTime when the log was generated
        self.level = level          # INFO, DEBUG, WARN, ERROR
        self.message = message      # Log message
        self.source = source        # Service/module generating the log

from collections import Queue
from time import time, datetime
from enum import Enum

class Level(Enum):
    INFO = 1
    DEBUG = 2
    ERROR = 3
    WARN = 4

import threading
from queue import Queue

class Logger:
    def __init__(self):
        self.log_queue = Queue()  # Asynchronous log writing
        self.log_levels = ["DEBUG", "INFO", "WARN", "ERROR"]
        self.log_writer_thread = threading.Thread(target=self.write_logs)
        self.log_writer_thread.start()

    def log(self, level, message, source):
        if level in self.log_levels:
            log_entry = LogEntry(timestamp=datetime.now(), level=level, message=message, source=source)
            self.log_queue.put(log_entry)  # Add log to the queue for asynchronous writing

    def write_logs(self):
        while True:
            log_entry = self.log_queue.get()
            # Writing log to storage, could be a file, a database, etc.
            self.write_to_storage(log_entry)

    def write_to_storage(self, log_entry):
        # Example: Write to a local file
        with open('app.log', 'a') as log_file:
            log_file.write(f"{log_entry.timestamp} [{log_entry.level}] {log_entry.source}: {log_entry.message}\n")
