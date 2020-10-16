#!/usr/bin/env python

from loggers.base_logger import BaseLogger
from helpers.file_helper import FileHelper

class FileLogger(BaseLogger):

    def __init__(self, action:str, status:bool, data:dict, log_file:str):
        BaseLogger.__init__(self, status, log_file)
        self.data = data
        self.message = self.format_message(action, log_file)

    def __call__(self):
        super().__call__()
        return self

    def format_message(self, action:str, log_file:str) -> str:
        """
        This function formats the log message.
        Input:
            - str
            - str
        Output:
            - str
        """
        log = getattr(self, "_{}_log".format(action))()
        logfile_ext = FileHelper.get_ext(log_file)
        if logfile_ext == 'txt':
            base = "{} - {} {}:{} [{}] - {}: {} ({})"
        elif logfile_ext == 'csv':
            base = "{},{},{},{},{},{},{},{}"
        message = base.format(
            self.user_name,
            self.timestamp,
            self.process_name,
            self.process_id,
            self.command,
            self.status.upper(),
            log,
            self.abs_file_path,
        )
        return message

    def _create_log(self) -> str:
        """
        This function formats a message when creating a file.
        Output:
            - str
        """
        logger_msg = "Creating file {}".format(
            self.data['filename']
        )
        return logger_msg

    def _send_log(self) -> str:
        """
        This function formats a message when sending data to a file.
        Output:
            - str
        """
        logger_msg = "Sending {} to {}".format(
            self.data['message'],
            self.data['filename']
        )
        return logger_msg

    def _replace_log(self) -> str:
        """
        This function formats a message when replacing data in a file.
        Output:
            - str
        """
        file_ext = FileHelper.get_ext(self.data['filename'])
        if file_ext == 'csv':
            logger_msg = "Replacing {} to {} at ({}, {}) in {}".format(
                self.data['replace_message'],
                self.data['message'],
                self.data['row'],
                self.data['column'],
                self.data['filename']
            )
        elif file_ext == 'txt':
            logger_msg = "Replacing {} to {} in {}".format(
                self.data['replace_data'],
                self.data['data'],
                self.data['filename']
            )
        return logger_msg

    def _delete_log(self) -> str:
        """
        This function formats a message when deleting a file.
        Output:
            - str
        """
        logger_msg = "Deleting {}".format(
            self.data['filename']
        )
        return logger_msg
    