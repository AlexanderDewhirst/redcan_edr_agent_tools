#!/usr/bin/env python

from .logger import Logger

class RequestLogger(Logger):

    def __init__(self, response:bool, namespace_args:object):
        Logger.__init__(self, response, namespace_args.log_file)
        self.message = self.format_message()

    def __call__(self):
        super().__call__()

    def format_message(self) -> str:
        message = "{} - {} {}:{} [{}] - {}: {}\n".format(
            self.user_name,
            self.timestamp,
            self.process_name,
            self.process_id,
            self.command,
            self.status.upper(),
            self.set_message(),
        )
        return message
    
    def set_message(self):
        if self.status == 'info':
            message = "Process started."
        else:
            message = "Process failed."
        return message