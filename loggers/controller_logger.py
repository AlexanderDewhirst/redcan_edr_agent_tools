#!/usr/bin/env python

from .file_logger import FileLogger
from .network_logger import NetworkLogger


class ControllerLogger:
    
    def __init__(self, controller:str, action:str, status:bool, data:dict, log_file:str):
        self.controller = controller
        self.action     = action
        self.status     = status
        self.log_file   = log_file
        self.data       = data
        self.message    = None

    def __call__(self):
        if self.controller == 'FileController':
            logger = FileLogger(self.action, self.status, self.data, self.log_file)()
        elif self.controller == 'NetworkController':
            logger = NetworkLogger(self.action, self.status, self.data, self.log_file)()
        self.message = logger.message
        return self
