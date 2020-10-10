#!/usr/bin/env python

import sys

class Logger(object):

    def __init__(self, message:str, response:bool, output_file = None):
        self.log_type = self._set_log_type(response)
        self.output_file = output_file
        self.message = self._format_message(message)

    def create_log(self):
        """
        This function prints a formatted log message with stderr or stoud
        depending on message type.
        """
        self.__dump_message()
        self.__send_to_file()

    def _format_message(self, message:str):
        """
        This function overwrites the message to format message type
        for user.
        """
        if self.log_type == "error":
            message = "{}: {}\n".format(
                self.log_type.upper(),
                message
            )
        elif self.log_type == "info":
            message = "{}: {}\n".format(
                self.log_type.upper(),
                message
            )
        else:
            raise BaseException(
                "Unexpected type: '{}'".format(
                    self.log_type
                )
            )
        return message

    def _set_log_type(self, log_type:bool):
        if log_type == True:
            return 'info'
        elif log_type == False:
            return 'error'
        else:
            raise BaseException(
                "Unexpected log_type: '{}' to initialize Logger".format(
                    log_type
                )
            )

    def __dump_message(self):
        if self.log_type == 'error':
            sys.stderr.write(self.message)
        elif self.log_type == 'info':
            sys.stdout.write(self.message)

    def __send_to_file(self):
        if self.output_file:
            with open(self.output_file, 'w') as log_file:
                log_file.write(self.message)
        else:
            sys.stdout.write("No log filename specified.")