#!/usr/bin/env python

from .file_controller import FileController
from .network_controller import NetworkController

class BaseController(object):

    def __init__(self, namespace_args):
        self.command = namespace_args.command
        self.action = namespace_args.action
        if is_network_manager(self.command):
            namespace_controller, response, status = NetworkController().map_action(self.action, namespace_args)
        elif is_file_manager(self.command):
            namespace_controller, response, status = FileController().map_action(self.action, namespace_args)
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


def is_network_manager(command) -> bool:
    """
    This function checks if the subparser command was 'network_manager'
    Output:
        - bool
    """
    return command == "network_manager"

def is_file_manager(command) -> bool:
    """
    This function checks if the subparser command was 'file_manager'
    Output:
        - bool
    """
    return command == "file_manager"