#!/usr/bin/env python

from .base_logger import BaseLogger

class RequestLogger(BaseLogger):

    def __init__(self, response:bool, namespace_args:object):
        print("Logfile:", namespace_args.log_file)
        BaseLogger.__init__(self, response, namespace_args.log_file)
        self.message = self.format_message()

    def __call__(self):
        super().__call__()

    def format_message(self) -> str:
        """
        This function formats the log message.
        Output:
            - str
        """
        message = "{} - {} {}:{} [{}] - {}: {}".format(
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
        """
        This function sets the message given the status.
        Output:
            - str
        # TODO: Add better description
        """
        if self.status == 'info':
            message = "Process started."
        else:
            message = "Process failed."
        return message