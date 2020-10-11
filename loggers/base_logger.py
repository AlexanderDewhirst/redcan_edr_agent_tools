#!/usr/bin/env python

import sys
import os
import pwd
import psutil
import datetime

class BaseLogger(object):

    def __init__(self, response:bool, output_file = None):
            self.output_file        = output_file
            self.command            = self.__get_command()
            self.abs_file_path      = self.__get_abs_file_path()
            self.user_name          = self.__get_username()
            self.process_name       = self.__get_process()["name"]
            self.process_id         = self.__get_process()["pid"]
            self.process_start_time = self.__get_process()["start_time"]
            self.timestamp          = self.__set_timestamp()
            self.status             = self.__set_status(response)

    def __call__(self):
        if not hasattr(self, 'message'):
            raise BaseException(
                "Logger attribute 'message' not present."
            )
        self.__send_to_file()
        self.__dump_message()

    def __set_status(self, status:bool):
        if status == True:
            return 'info'
        elif status == False:
            return 'error'
        else:
            raise BaseException(
                "{} - Unexpected status: '{}' to initialize Logger".format(
                    self.timestamp,
                    status
                )
            )

    def __dump_message(self):
        """
        This function writes the message using stderr or stdout depending on status.
        """
        if self.status == 'error':
            sys.stderr.write(self.message)
        elif self.status == 'info':
            sys.stdout.write(self.message)

    def __send_to_file(self):
        """
        This function sends the data to the output file.
        """
        if self.output_file:
            with open(self.output_file, 'a') as log_file:
                log_file.write(self.message)
        else:
            sys.stdout.write("No log filename specified.")

    def __set_timestamp(self):
        """
        This function gets the current time.
        Output:
            - str
        """
        time = datetime.datetime.now()
        time = time.isoformat('|')
        return time

    def __get_abs_file_path(self):
        """
        This function gets the absolute path of the output file.
        Output:
            - str
        """
        return os.path.abspath(self.output_file)

    def __get_username(self):
        """
        This function gets the username of the current user.
        Output:
            - str
        """
        return pwd.getpwuid(os.getuid())[0]
    
    def __get_process(self):
        """
        This function gets the Process details (id, name, start_time).
        Output:
            - dict
        """
        pid = os.getpid()
        process = {
            "pid": pid,
            "name": psutil.Process(pid).name(),
            "start_time": datetime.datetime.fromtimestamp(psutil.Process(pid).create_time()).isoformat('|')
        }
        return process

    def __get_command(self):
        """
        This function gets the input command using the 'sys' library.
        Output:
            - str
        """
        return ' '.join(sys.argv)
