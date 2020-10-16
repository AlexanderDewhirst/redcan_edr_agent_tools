#!/usr/bin/env python

from loggers.base_logger import BaseLogger
from helpers.file_helper import FileHelper

class RequestLogger(BaseLogger):

    def __init__(self, response:bool, log_file:str):
        BaseLogger.__init__(self, response, log_file)
        self.message = self.format_message(log_file)

    def __call__(self):
        super().__call__()

    def format_message(self, log_file:str) -> str:
        """
        This function formats the log message.
        Input:
            - str
        Output:
            - str
        """
        logfile_ext = FileHelper.get_ext(log_file)
        if logfile_ext == 'txt':
            base = "{} - {} {}:{} [{}] - {}: {}"
        elif logfile_ext == 'csv':
            base = "{},{},{},{},{},{},{}"
        message = base.format(
            self.user_name,
            self.timestamp,
            self.process_name,
            self.process_id,
            self.command,
            self.status.upper(),
            self.set_message(),
        )
        return message
    
    def set_message(self) -> str:
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