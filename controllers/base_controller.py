#!/usr/bin/env python

from controllers.network_controller import NetworkController
from controllers.file_controller import FileController

class BaseController(object):

    def __init__(self, namespace_args):
        self.command = namespace_args.command
        self.args = namespace_args
        self.subcontroller = None

    def __call__(self):
        if self.command == 'network_manager':
            controller = NetworkController(self.args)()
        elif self.command == 'file_manager':
            controller = FileController(self.args)()
        self.subcontroller = controller
        return self
