#!/usr/bin/env python

import sys
import os
import pwd
import psutil
import datetime

class Logger(object):

    def __init__(self, message:str, response:bool, output_file = None):
        self.output_file = output_file
        self.timestamp = self.__set_timestamp()
        self.log_type = self.__set_log_type(response)
        
        self.message = self.format_message(message)
        

    def create_log(self):
        """
        This function prints a formatted log message with stderr or stoud
        depending on message type.
        """
        self.__send_to_file()
        self.__dump_message()

    def format_message(self, message:str):
        """
        This function overwrites the message to format message type
        for user.
        """
        abs_output_file_path = self.__get_abs_file_path()
        user_name         = self.__get_username()
        process           = self.__get_process()
        command           = self.__get_command()
        if self.log_type == "error":
            message = "{} - {} {}:{}:{} [{}] ({}) - {}: {}".format(
                user_name,
                self.timestamp,
                process["name"],
                process["pid"],
                process["start_time"],
                command,
                abs_output_file_path,
                self.log_type.upper(),
                message
            )
        elif self.log_type == "info":
            message = "{} - {} {}:{}:{} [{}] ({}) - {}: {}".format(
                user_name,
                self.timestamp,
                process["name"],
                process["pid"],
                process["start_time"],
                command,
                abs_output_file_path,
                self.log_type.upper(),
                message
            )
        else:
            raise BaseException(
                "{} - {} {}:{}:{} [{}] ({}) - Unexpected type: '{}'".format(
                    user_name,
                    self.timestamp,
                    process["name"],
                    process["pid"],
                    process["start_time"],
                    command,
                    abs_output_file_path,
                    self.log_type
                )
            )
        return message

    def __set_log_type(self, log_type:bool):
        if log_type == True:
            return 'info'
        elif log_type == False:
            return 'error'
        else:
            raise BaseException(
                "{} - Unexpected log_type: '{}' to initialize Logger".format(
                    self.timestamp,
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
            with open(self.output_file, 'a') as log_file:
                log_file.write(
                    "{}\n".format(self.message)
                )
        else:
            sys.stdout.write("No log filename specified.")

    def __set_timestamp(self):
        time = datetime.datetime.now()
        time = time.isoformat('|')
        return time

    def __get_abs_file_path(self):
        return os.path.abspath(self.output_file)

    def __get_username(self):
        return pwd.getpwuid(os.getuid())[0]
    
    def __get_process(self):
        pid = os.getpid()
        process = {
            "pid": pid,
            "name": psutil.Process(pid).name(),
            "start_time": datetime.datetime.fromtimestamp(psutil.Process(pid).create_time()).isoformat('|')
        }
        return process

    def __get_command(self):
        return ' '.join(sys.argv)
