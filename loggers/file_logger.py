#!/usr/bin/env python

from .logger import Logger

class FileLogger(Logger):

    def __init__(self, message:str, response:bool, namespace_args:object):
        Logger.__init__(self, response, namespace_args.log_file)
        self.message = self.format_message(message)

    def __call__(self):
        """
        This function prints a formatted log message with stderr or stoud
        depending on message type.
        """
        super().__call__()

    def format_message(self, message:str) -> str:
        """
        This function overwrites the message to format message type
        for user.
        """
        message = "{} - {} {}:{} [{}] - {}: {} ({})\n".format(
            self.user_name,
            self.timestamp,
            self.process_name,
            self.process_id,
            self.command,
            self.status.upper(),
            message,
            self.abs_file_path,
        )
        return message
    