#!/usr/bin/env python

from parsers.parser import Parser
from controllers.base_controller import BaseController
from loggers.network_logger import NetworkLogger
from loggers.file_logger import FileLogger
from loggers.request_logger import RequestLogger

# Parser
parser = Parser()
request = parser()

# RequestLogger()
RequestLogger(request.status, request.parsed_args)()

# Controller
controller = BaseController(request.parsed_args)
if controller.controller == 'FileController':
    FileLogger(controller.response, controller.status, request.parsed_args)()
elif controller.controller == 'NetworkController':
    NetworkLogger(controller.response, controller.status, request.parsed_args)()





