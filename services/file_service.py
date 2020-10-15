#!/usr/bin/env python

import sys
import os
from helpers.file_helper import FileHelper

class FileService(object):

    def __init__(self, filename:str, **kwargs):
        self.filename  = filename
        self.args      = kwargs 

    def create(self) -> (str, bool):
        """
        This function creates a file.
        Output:
            - str
            - bool
        """
        log = self._create_log()
        try:
            with open(self.filename, 'w') as file:
                pass
            status = True
        except:
            status = False
        finally:
            return self._construct_response(log, status)

    def send(self) -> (str, bool):
        """
        This function sends data to a file.
        Output:
            - str
            - bool
        """
        log = self._send_log()
        # NOTE: potentially move 'try' block to this method
        file_ext = self.filename.split('.')[1]
        status = FileHelper.send_to_file(
            self.filename,
            self.args['data'],
            file_ext,
            self.args['new_line']
        )
        return self._construct_response(log, status)

    def replace(self) -> (str, bool):
        """
        This function determines how to replace data.
        Output:
            - str
            - bool
        """
        file_ext = self.filename.split('.')[1]
        if file_ext == 'csv':
            status = FileHelper.replace_in_file(
                self.filename,
                self.args['data'],
                self.args['replace_data'], 
                file_ext,
                self.args['row'],
                self.args['column'],
            )
        elif file_ext == 'txt':
            status = FileHelper.replace_in_file(
                self.filename,
                self.args['data'],
                self.args['replace_data'], 
                file_ext
            )
        log = self._replace_log(file_ext)
        return self._construct_response(log, status)

    def delete(self) -> (str, bool):
        """
        This function deletes the file.
        Output:
            - str
            - bool
        """
        log = self._delete_log()
        try:
            os.remove(self.filename)
            status = True
        except:
            status = False
        finally:
            return self._construct_response(log, status)

    def _create_log(self) -> str:
        """
        This function formats a message when creating a file.
        Output:
            - str
        """
        logger_msg = "Creating file {}".format(
            self.filename
        )
        return logger_msg

    def _send_log(self) -> str:
        """
        This function formats a message when sending data to a file.
        Output:
            - str
        """
        logger_msg = "Sending {} to {}".format(
            self.args['data'],
            self.filename
        )
        return logger_msg

    def _replace_log(self, file_ext:str) -> str:
        """
        This function formats a message when replacing data in a file.
        Output:
            - str
        """
        if file_ext == 'csv':
            logger_msg = "Replacing {} to {} at ({}, {}) in {}".format(
                self.args['replace_data'],
                self.args['data'],
                self.args['row'],
                self.args['column'],
                self.filename
            )
        elif file_ext == 'txt':
            logger_msg = "Replacing {} to {} in {}".format(
                self.args['replace_data'],
                self.args['data'],
                self.filename
            )
        return logger_msg

    def _delete_log(self) -> str:
        """
        This function formats a message when deleting a file.
        Output:
            - str
        """
        logger_msg = "Deleting {}".format(
            self.filename
        )
        return logger_msg

    def _construct_response(self, log:str, status:bool, data:dict = None) -> dict:
        response = {
            'log': log,
            'status': status,
            'data': data
        }
        return response
