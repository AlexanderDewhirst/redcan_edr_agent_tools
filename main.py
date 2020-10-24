#!/usr/bin/env python

from parsers.parser import Parser
from controllers.base_controller import BaseController
from loggers.controller_logger import ControllerLogger
from loggers.request_logger import RequestLogger

# Parser
parser = Parser()
request = parser()
print(request)
# TODO: Check if connection to socket has already been established.

# RequestLogger
RequestLogger(request.status, request.parsed_args.log_file)()

# Controller
base_controller = BaseController(request.parsed_args)
controller = base_controller()

# Logger
controller_logger = ControllerLogger(
    controller.subcontroller.__class__.__name__,
    controller.subcontroller.action,
    controller.subcontroller.status,
    controller.subcontroller.data,
    request.parsed_args.log_file
)
controller_logger()
