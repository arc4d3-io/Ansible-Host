import datetime
import socket
import os

class Logger:
    
    def __init__(self, log_format="%b %d %H:%M:%S", process_name="myapp"):
        self.log_format = log_format
        self.process_name = process_name
        self.hostname = socket.gethostname()
        self.pid = os.getpid()

    def _get_timestamp(self):
        return datetime.datetime.now().strftime(self.log_format)

    def log(self, message):
        timestamp = self._get_timestamp()
        log_entry = f"{timestamp} {self.hostname} {self.process_name}[{self.pid}]: {message}"
        print(log_entry)
