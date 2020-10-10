#!/usr/bin/env python

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '/', 'controllers'))

from utils.file_util import FileUtil
from utils.network_util import NetworkUtil

class BaseController(object):

    def __init__(self, namespace_args):
        self.command = namespace_args.command
        self.action = namespace_args.action
        rest_args = self.__map_args(namespace_args)
        if self.is_network_manager():
            self.response = NetworkController().map_action(self.action, rest_args)
        elif self.is_file_manager():
            self.response = FileController().map_action(self.action, rest_args)
        else:
            raise BaseException(
                "Unexpected controller: '{}' does not map to controller."
                .format(
                    self.command
                )
            )

    def is_network_manager(self):
        return self.command == "network_manager"

    def is_file_manager(self):
        return self.command == "file_manager"

    def __map_args(self, namespace_args):
        args = {}
        for key, value in vars(namespace_args).items():
            args[key] = value
        return args

class FileController:

    def map_action(self, action, args):
        file_util = FileUtil(args['file'])
        print(action)
        print(args)
        if action == 'new':
            response, log = file_util.create_file()
            print(response)
        elif action == 'create':
            response, log = file_util.write_data(args['data'])
        elif action == 'update':
            response, log = file_util.replace_data(args['data'], args['replace_data'], args['row'], args['column'])
        elif action == 'delete':
            response, log = file_util.delete_file()
        else:
            raise BaseException(
                "Unexpected action: '{}' does not map to controller"
                .format(
                    action
                )
            )
        return response, log

class NetworkController:

    def map_action(self, action, args):
        network_util = NetworkUtil(args.host, args.port)
        if action == 'connect':
            response, log = network_util.connect()
        elif action == 'send':
            response, log = network_util.send(args.data)
        elif action == 'close':
            response, log = network_util.close()
        else:
            raise BaseException(
                "Unexpected action: '{}' does not map to controller"
                .format(
                    action
                )
            )
        return response, log