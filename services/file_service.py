#!/usr/bin/env python

import sys
import os
import csv

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
            return log, True
        except:
            return log, False

    def send(self) -> (str, bool):
        """
        This function sends data to a file.
        Output:
            - str
            - bool
        """
        log = self._send_log()
        # NOTE: hotfix to handle extensions.
            
        if self.filename.split('.')[1] == 'txt': # Condition is weak
            response = self._send_txt()
        elif self.filename.split('.')[1] == 'csv': # Condition is weak
            response = self._send_csv()
        return log, response

    def replace(self) -> (str, bool):
        """
        This function determines how to replace data.
        Output:
            - str
            - bool
        """
        if self.filename.split('.')[1] == 'csv': # Condition is weak
            log = self._replace_csv_log()
            response = self._replace_csv()
        elif self.filename.split('.')[1] == 'txt': # Condition is weak
            log = self._replace_txt_log()
            response = self._replace_txt()
        return log, response

    def _send_csv(self) -> bool:
        """
        This function sends data to a csv file.
        Output:
            - bool
        """
        try:
            with open(self.filename, 'a') as file:
                if self.args['new_line']: # Sloppy way to create new line
                    file.write(
                        '\n{},'.format(self.args['data'])
                    )
                else:
                    file.write(
                        "{},".format(self.args['data'])
                    )
            return True
        except:
            return False

    def _send_txt(self) -> bool:
        """
        This function sends data to a txt file.
        Output:
            - bool
        """
        try:
            with open(self.filename, 'a') as file:
                if self.args['new_line']:
                    file.write(
                        '\n{}'.format(self.args['data'])
                    )
                else:
                    file.write(
                        "{}".format(self.args['data'])
                    )
        
            return True
        except:
            return False

    def _replace_csv(self) -> bool:
        """
        This function replaces data in a csv using the 'row' and 'column' arguments provided.
        Output:
            - bool
        # TODO: Fix double open file..
        """
        try:
            content = None
            with open(self.filename, newline = '') as file:
                content = list(csv.reader(file))
                content[self.args['row'] - 1][self.args['column'] - 1] = content[self.args['row'] - 1][self.args['column'] - 1].replace(self.args['replace_data'], self.args['data'])
            with open(self.filename, 'w') as file:
                writer = csv.writer(file)
                writer.writerows(content)
            return True
        except:
            return False

    def _replace_txt(self) -> bool:
        """
        This function replaces data in a txt file.
        Output:
            - bool
        # TODO: Fix double open file..
        """
        try:
            content = None
            with open(self.filename, 'r') as file:
                content = file.read()
                content = content.replace(self.args['replace_data'], self.args['data'])
            with open(self.filename, 'w+') as file:
                file.write(content)
            return True
        except:
            return False

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
            return log, True
        except:
            return log, False

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

    def _replace_csv_log(self) -> str:
        """
        This function formats a message when replacing data in a csv.
        Output:
            - str
        """
        logger_msg = "Replacing {} to {} at ({}, {}) in {}".format(
            self.args['replace_data'],
            self.args['data'],
            self.args['row'],
            self.args['column'],
            self.filename
        )
        return logger_msg

    def _replace_txt_log(self) -> str:
        """
        This function formats a message when replacing data in a txt file.
        Output:
            - str
        """
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
