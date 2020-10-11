#!/usr/bin/env python

import argparse

from parsers.parser import Parser
from controllers.base_controller import BaseController
from utils.logger import Logger


# python3 ./main.py file_manager -a "create" -l "log.txt" -f "output.txt"
# python3 ./main.py file_manager -a "send" -l "log.txt" -f "output.txt" -d "My initial data."
# python3 ./main.py file_manager -a "replace" -l "log.txt" -f "output.txt" -d "updated data." -rd "initial data." -r 1 -c 1
# python3 ./main.py file_manager -a "delete" -l "log.txt" -f "output.txt"
# python3 ./main.py network_manager -a "connect" -l "log.txt" -h "localhost" -p "4000"
# python3 ./main.py network_manager -a "send" -l "log.txt" -h "localhost" -p "4000" -d "Send my data."
# python3 ./main.py network_manager -a "close" -l "log.txt"


# Parser
parser = Parser()
args = parser()

# Controller
controller = BaseController(args)
Logger(controller.response[1], controller.response[0], args.log_file).create_log()





