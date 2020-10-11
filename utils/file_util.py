#!/usr/bin/env python

import sys
import os

class FileUtil(object):

    def __init__(self, filename:str, **kwargs):
        self.filename  = filename
        self.args      = kwargs 

    def create(self) -> (bool, str):
        log = self._create_log()
        try:
            with open(self.filename, 'w') as file:
                pass
            return log, True
        except:
            return log, False

    def send(self) -> (bool, str):
        log = self._send_log()
        try:
            with open(self.filename, 'a') as file:
                file.write(
                    "{}\n".format(self.args['data'])
                )
            return log, True
        except:
            return log, False

    def replace(self):
        if self.args['replace_cell']:
            log = self._replace_csv_log()
            response = self._replace_csv()
        else:
            log = self._replace_txt_log()
            response = self._replace_txt()
        return log, response

    def _replace_csv(self) -> (bool, str):
        try:
            with open(self.filename, 'w') as file:
                content = file.readlines()
                content[self.args['row'] - 1][self.args['column'] - 1].replace(self.args['replace_data'], self.args['data'])
            return True
        except:
            return False

    def _replace_txt(self) -> (bool, str):
        try:
            with open(self.filename, 'w') as file:
                content = file.read()
                content.replace(self.args['replace_data'], self.args['data'])
            return True
        except:
            return False

    def delete(self) -> (bool, str):
        log = self._delete_log()
        try:
            os.remove(self.filename)
            return log, True
        except:
            return log, False

    def _create_log(self) -> str:
        logger_msg = "Creating file {}".format(
            self.filename
        )
        return logger_msg

    def _send_log(self) -> str:
        logger_msg = "Sending {} to {}".format(
            self.args['data'],
            self.filename
        )
        return logger_msg

    def _replace_csv_log(self) -> str:
        logger_msg = "Replacing {} to {} at ({}, {}) in {}".format(
            self.args['replace_data'],
            self.args['data'],
            self.args['row'],
            self.args['column'],
            self.filename
        )
        return logger_msg

    def _replace_txt_log(self) -> str:
        logger_msg = "Replacing {} to {} in {}".format(
            self.args['replace_data'],
            self.args['data'],
            self.filename
        )
        return logger_msg

    def _delete_log(self) -> str:
        logger_msg = "Deleting {}".format(
            self.filename
        )
        return logger_msg
