#!/usr/bin/env python

from .base_logger import BaseLogger

class NetworkLogger(BaseLogger):

    def __init__(self, action:str, status:bool, data:dict, log_file:str):
        BaseLogger.__init__(self, status, log_file)
        self.data = data
        self.message = self.format_message(action)

    def __call__(self):
        super().__call__()

    def format_message(self, action:str) -> str:
        """
        This function formats the log message.
        Input:
            - str
        Output:
            - str
        """
        log = getattr(self, "_{}_log".format(action))()
        message = "{} - {} {}:{} [{}] - {}: {} (Source - {}:{}) (Destination - {}:{})".format(
            self.user_name,
            self.timestamp,
            self.process_name,
            self.process_id,
            self.command,
            self.status.upper(),
            log,
            self.data['sock']['source']['host'],
            self.data['sock']['source']['port'],
            self.data['sock']['destination']['host'],
            self.data['sock']['destination']['port'],
            # Size of Data
            # Protocol of Data,
        )

        return message

    def _connect_log(self) -> str:
        """
        This function formats a log message when connecting to a server.
        Output:
            - str
        """
        logger_msg = "Establishing connection."
        return logger_msg

    def _send_log(self) -> str:
        """
        This function formats a log message when sending data to a server.
        Output:
            - str
        """
        logger_msg = "Sending '{}' to socket.".format(
            self.data['sock']['message'],
        )
        return logger_msg

    def _close_log(self) -> str:
        """
        This function formats a log message when closing a connection.
        Output:
            - str
        """
        logger_msg = "Closing connection."
        return logger_msg
