#!/usr/bin/env python

from parsers.parser import Parser
from controllers.base_controller import BaseController
from loggers.network_logger import NetworkLogger
from loggers.file_logger import FileLogger
from loggers.request_logger import RequestLogger


# python3 ./main.py file_manager -a "create" -l "log.txt" -f "output.txt"
# python3 ./main.py file_manager -a "send" -l "log.txt" -f "output.txt" -d "My initial data."
# python3 ./main.py file_manager -a "replace" -l "log.txt" -f "output.txt" -d "updated data." -rd "initial data." -r 1 -c 1
# python3 ./main.py file_manager -a "delete" -l "log.txt" -f "output.txt"
# python3 ./main.py network_manager -a "connect" -l "log.txt" -h "localhost" -p "4000"
# python3 ./main.py network_manager -a "send" -l "log.txt" -h "localhost" -p "4000" -d "Send my data."
# python3 ./main.py network_manager -a "close" -l "log.txt"


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





