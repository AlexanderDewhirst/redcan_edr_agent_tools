#!/usr/bin/env python

import sys
import os

class FileUtil(object):

    def __init__(self, filename:str):
        self.filename = filename

    def create_file(self) -> (bool, str):
        log = self._create_log()
        try:
            with open(self.filename, 'w') as file:
                pass
            return True, log
        except:
            return False, log

    def send(self, data:str) -> (bool, str):
        log = self._send_log(data)
        try:
            with open(self.filename, 'w') as file:
                file.write(
                    "{}\n".format(data)
                )
            return True, log
        except:
            return False, log

    def replace(self, data:str, replace_data:str, row:int, column:int) -> (bool, str):
        log = self._replace_log(data, replace_data, row, column)
        try:
            with open(self.filename, 'w') as file:
                # if kwargs['row'] and kwargs['column']:
                content = file.readlines()
                content[row - 1][column - 1].replace(replace_data, data)
                # else:
                #     content = file.read()
                #     content.replace(replace_data, data)
            return True, log
        except:
            return False, log

    def delete(self) -> (bool, str):
        log = self._delete_log()
        try:
            os.remove(self.filename)
            return True, log
        except:
            return False, log

    def _create_log(self) -> str:
        logger_msg = "Creating file {}".format(
            self.filename
        )
        return logger_msg

    def _send_log(self, data:str) -> str:
        logger_msg = "Sending {} to {}".format(
            data,
            self.filename
        )
        return logger_msg

    def _replace_log(self, data:str, replace_data:str, row:int, column:int) -> str:
        # if row and column:
        logger_msg = "Replacing {} to {} at ({}, {}) in {}".format(
            replace_data,
            data,
            row,
            column,
            self.filename
        )
        # else:
        #     logger_msg = "Replacing {} to {} in {}".format(
        #         replace_data,
        #         data,
        #         self.filename
        #     )
        return logger_msg

    def _delete_log(self) -> str:
        logger_msg = "Deleting {}".format(
            self.filename
        )
        return logger_msg