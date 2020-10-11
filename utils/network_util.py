#!/usr/bin/env python

import socket

class NetworkUtil(object):

    def __init__(self, host: str, port: int, **kwargs):
        self.host = host
        self.port = port
        self.args = kwargs
        self.__init_sock()

    def connect(self) -> (bool, str):
        log = self._connect_log()
        try:
            self.args['sock'].connect((self.host, self.port))
            return True, log
        except:
            return False, log

    def send(self) -> (bool, str):
        log = self._send_log()
        try:
            self.args['sock'].send(self.args['data'].encode())
            return True, log
        except:
            return False, log

    def close(self) -> (bool, str):
        log = self._close_log()
        try:
            self.args['sock'].close()
            return True, log
        except:
            return False, log

    def _connect_log(self) -> str:
        logger_msg = "Establishing connection to host '{}' and port '{}'".format(
            self.host,
            self.port
        )
        return logger_msg

    def _send_log(self) -> str:
        logger_msg = "Sending '{}' to socket at host '{}' and port '{}'".format(
            self.args['data'],
            self.host,
            self.port
        )
        return logger_msg

    def _close_log(self) -> str:
        logger_msg = "Closing connection to host '{}' and port '{}'".format(
            self.host,
            self.port
        )
        return logger_msg

        
    def __init_sock(self):
        if self.args['sock'] == None:
            self.args['sock'] = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM
            )
