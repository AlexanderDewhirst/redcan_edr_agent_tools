#!/usr/bin/env python

import sys
import os
from helpers.file_helper import FileHelper

class FileService(object):

    def __init__(self, filename:str, **kwargs):
        self.filename  = filename
        self.args      = kwargs 

    def create(self) -> dict:
        """
        This function creates a file.
        Output:
            - dict
        """
        try:
            with open(self.filename, 'w') as file:
                pass
            data = {'filename': self.filename}
            status = True
        except:
            status = False
        finally:
            return self._construct_response(status, data)

    def send(self) -> dict:
        """
        This function sends data to a file.
        Output:
            - dict
        """
        # NOTE: potentially move 'try' block to this method
        data = {'message': self.args['data'], 'filename': self.filename}
        file_ext = self.filename.split('.')[1]
        status = FileHelper.send_to_file(
            self.filename,
            self.args['data'],
            file_ext,
            self.args['new_line']
        )
        return self._construct_response(status, data)

    def replace(self) -> dict:
        """
        This function determines how to replace data.
        Output:
            - dict
        """
        data = {'message': self.args['data'], 'replace_message': self.args['replace_data'], 'row': '', 'column': '', 'filename': self.filename}
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
            
            data['row'] = self.args['row']
            data['column'] = self.args['column']
        elif file_ext == 'txt':
            status = FileHelper.replace_in_file(
                self.filename,
                self.args['data'],
                self.args['replace_data'], 
                file_ext
            )
        return self._construct_response(status)

    def delete(self) -> dict:
        """
        This function deletes the file.
        Output:
            - dict
        """
        data = {'filename': self.filename}
        try:
            os.remove(self.filename)
            status = True
        except:
            status = False
        finally:
            return self._construct_response(status, data)    

    def _construct_response(self, status:bool, data:dict = None) -> dict:
        """
        This function constructs the data object for the Logger
        Input:
            - bool
            - dict (opt.)
        Output:
            - dict
        """
        response = {
            'status': status,
            'data': data
        }
        return response
