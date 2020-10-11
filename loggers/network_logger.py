#!/usr/bin/env python

from .base_logger import BaseLogger

class NetworkLogger(BaseLogger):

    def __init__(self, message:str, response:bool, namespace_args:object):
        BaseLogger.__init__(self, response, namespace_args.log_file)
        self.host = namespace_args.host
        self.port = namespace_args.port
        self.message = self.format_message(message)
        

    def __call__(self):
        super().__call__()

    def format_message(self, message:str) -> str:
        """
        This function formats the log message.
        Output:
            - str
        """
        message = "{} - {} {}:{} [{}] - {}: {} ({}:{})\n".format(
            self.user_name,
            self.timestamp,
            self.process_name,
            self.process_id,
            self.command,
            self.status.upper(),
            message,
            self.host,
            self.port
            # Destination Address and Port
            # Source Address and Port
            # Size of Data
            # Protocol of Data,
        )

        return message