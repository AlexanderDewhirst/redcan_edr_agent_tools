#!/usr/bin/env python

import argparse

class Parser(object):

    def __init__(self, description = None):
        self.description = description
        self.parser = self._init_parser()
        self.status = True

    def __call__(self):
        self.parsed_args = self.parser.parse_args()
        self.validate_args()
        return self

    def _init_parser(self):
        """
        This function is called in the __init__ method and will create the parser
        and subparsers to store the command for us to access
        Output:
            - Namespace (argparse object)
        """
        parser = argparse.ArgumentParser(description = "Process file create/send/replace/delete and network connect/send/close actions.")
        subparsers = parser.add_subparsers(dest = 'command')
        file_parser = subparsers.add_parser('file_manager', help = "Process file actions.")
        file_parser.add_argument('-a', '--action', dest = 'action', type = str, action = 'store', help = 'Action.')
        file_parser.add_argument('-f', '--filename', dest = 'file', type = str, default = 'output.txt', action = 'store', help = 'Output file.')
        file_parser.add_argument('-d', '--data', dest = 'data', type = str, action = 'store', help = 'Data to store.')
        file_parser.add_argument('-rd', '--replace_data', dest = 'replace_data', action = 'store', help = 'Data to replace.')
        file_parser.add_argument('-r', '--row', dest = 'row', type = int, action = 'store', help = 'Select row.')
        file_parser.add_argument('-c', '--column', dest = 'column', type = int, action = 'store', help = 'Select column.')
        file_parser.add_argument('-l', '--log_filename', dest = 'log_file', type = str, default = 'logfile.txt', action = 'store', help = 'Output log file.')
        file_parser.add_argument('--new-line', dest = 'new_line', action = 'store_true', help = 'Insert new line to csv.')

        network_parser = subparsers.add_parser('network_manager', help = "Process network actions.")
        network_parser.add_argument('-a', '--action', dest = 'action', type = str, action = 'store', help = 'Action.')
        network_parser.add_argument('--host', dest = 'host', type = str, action = 'store', help = 'Remote host.')
        network_parser.add_argument('--port', dest = 'port', type = int, action = 'store', help = 'Server port.')
        network_parser.add_argument('-d', '--data', dest = 'data', type = str, action = 'store', help = 'Data to send.')
        network_parser.add_argument('-l', '--log_filename', dest = 'log_file', type = str, default = 'logfile.txt', action = 'store', help = 'Output log file.')
        return parser

    def validate_args(self):
        if self.parsed_args.command not in ['file_manager', 'network_manager']:

            self.parser.error("Command invalid. Must use file manager or network manager")
        elif self.parsed_args.command == 'file_manager':
            
            if self.parsed_args.action == 'send' and not self.parsed_args.data:
                self.parser.error("Must specify data to send.")

            if self.parsed_args.action != "send" and self.parsed_args.new_line:
                self.parser.error("Cannot enter new line using this action.")

            if self.parsed_args.action == "replace" and self.parsed_args.file.split('.')[1] == 'csv':
                if not self.parsed_args.replace_data or not self.parsed_args.data or not self.parsed_args.row or not self.parsed_args.column:
                    self.parser.error("Must specify row, column, data to replace with, and data being replaced in csv file.")
            elif self.parsed_args.action == "replace" and self.parsed_args.file.split('.')[1] == 'txt':
                if not self.parsed_args.replace_data or not self.parsed_args.data:
                    self.parser.error("Must specify data to replace with and data being replaced in txt file.")

        elif self.parsed_args.command == 'network_manager':

            if not self.parsed_args.host or not self.parsed_args.port:
                self.parser.error("Must specify host and port.")

            if self.parsed_args.action == 'send' and not self.parsed_args.data:
                self.parser.error("Must specify data to send.")
            