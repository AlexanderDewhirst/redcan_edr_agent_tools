#!/usr/bin/env python

import argparse

class Parser(object):

    def __init__(self, description = None):
        self.description = description
        self.parser = self._init_parser()

    def __call__(self):
        parsed_args = self.parser.parse_args()
        return parsed_args

    def _init_parser(self):
        parser = argparse.ArgumentParser()
        subparsers = parser.add_subparsers(help = 'Subparsers', dest = 'command')
        file_parser = subparsers.add_parser('file_manager')
        file_parser.add_argument('-a', '--action', dest = 'action', type = str, action = 'store', help = 'Action.')
        file_parser.add_argument('-f', '--filename', dest = 'file', type = str, action = 'store', help = 'Output file.')
        file_parser.add_argument('-d', '--data', dest = 'data', type = str, action = 'store', help = 'Data to store.')
        file_parser.add_argument('-r', '--row', dest = 'row', type = int, action = 'store', help = 'Select row.')
        file_parser.add_argument('-c', '--column', dest = 'column', type = int, action = 'store', help = 'Select column.')
        file_parser.add_argument('-l', '--log_filename', dest = 'log_file', type = str, action = 'store', help = 'Output log file.')

        network_parser = subparsers.add_parser('network_manager')
        network_parser.add_argument('-a', '--action', dest = 'action', type = str, action = 'store', help = 'Action.')
        network_parser.add_argument('--host', dest = 'host', type = str, action = 'store', help = 'Remote host.')
        network_parser.add_argument('--port', dest = 'port', type = int, action = 'store', help = 'Server port.')
        network_parser.add_argument('-d', '--data', dest = 'data', type = str, action = 'store', help = 'Data to send.')
        network_parser.add_argument('-l', '--log_filename', dest = 'log_file', type = str, action = 'store', help = 'Output log file.')
        return parser