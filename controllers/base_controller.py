#!/usr/bin/env python

from .file_controller import FileController
from .network_controller import NetworkController

class BaseController(object):

    def __init__(self, namespace_args):
        self.command = namespace_args.command
        self.action = namespace_args.action
        rest_args = self.__map_args(namespace_args)
        if self.is_network_manager():
            namespace_controller, response, status = NetworkController().map_action(self.action, rest_args)
        elif self.is_file_manager():
            namespace_controller, response, status = FileController().map_action(self.action, rest_args)
        else:
            raise BaseException(
                "Unexpected controller: '{}' does not map to controller."
                .format(
                    self.command
                )
            )
        self.controller = namespace_controller
        self.response = response
        self.status = status

    def __call__(self):
        return self

    def is_network_manager(self) -> bool:
        """
        This function checks if the subparser command was 'network_manager'
        Output:
            - bool
        """
        return self.command == "network_manager"

    def is_file_manager(self):
        """
        This function checks if the subparser command was 'file_manager'
        Output:
            - bool
        """
        return self.command == "file_manager"

    def __map_args(self, namespace_args):
        """
        This function maps Namespace to a dict.
        ## TODO: exclude 'action' and 'command'
        Output:
            - dict
        """
        args = {}
        for key, value in vars(namespace_args).items():
            args[key] = value
        return args
