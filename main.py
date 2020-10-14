#!/usr/bin/env python

from parsers.parser import Parser
from controllers.base_controller import BaseController
from loggers.network_logger import NetworkLogger
from loggers.file_logger import FileLogger
from loggers.request_logger import RequestLogger

# Parser
parser = Parser()
request = parser()
# TODO: Check if connection to socket has already been established.

# RequestLogger
RequestLogger(request.status, request.parsed_args)()

# Controller
base_controller = BaseController(request.parsed_args)
controller = base_controller()
if controller.subcontroller.__class__.__name__ == 'FileController':
    FileLogger(controller.subcontroller.response, controller.subcontroller.status, request.parsed_args)()
elif controller.subcontroller.__class__.__name__ == 'NetworkController':
    NetworkLogger(controller.subcontroller.response, controller.subcontroller.status, request.parsed_args)()
