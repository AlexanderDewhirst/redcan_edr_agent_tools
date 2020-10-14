#!/usr/bin/env python

import socket

class NetworkUtil(object):

    def __init__(self, host: str, port: int, **kwargs):
        self.host = host
        self.port = port
        self.args = kwargs
        self.__init_sock()

    def connect(self) -> (str, bool):
        """
        This function establishes a connection to a server using the 'socket' Python library.
        Output:
            - str
            - bool
        """
        log = self._connect_log()
        try:
            self._establish_connection()
            self.args['sock'].close()
            return log, True
        except:
            return log, False

    def send(self) -> (str, bool):
        """
        This function sends data to a server using the 'socket' Python library.
        Output:
            - str
            - bool
        """
        log = self._send_log()
        try:
            self._establish_connection()
            self.args['sock'].sendall(self.args['data'].encode())
            data = self.args['sock'].recv(1024)
            print(data)
            # self.args['sock'].close()
            return log, True
        except:
            return log, False

    def close(self) -> (str, bool):
        """
        This function closes a connection using the 'socket' Python library.
        Output:
            - str
            - bool
        """
        log = self._close_log()
        try:
            self._establish_connection()
            self.args['sock'].close()
            return log, True
        except:
            return log, False

    def _connect_log(self) -> str:
        """
        This function formats a log message when connecting to a server.
        Output:
            - str
        """
        logger_msg = "Establishing connection to host '{}' and port '{}'".format(
            self.host,
            self.port
        )
        return logger_msg

    def _send_log(self) -> str:
        """
        This function formats a log message when sending data to a server.
        Output:
            - str
        """
        logger_msg = "Sending '{}' to socket at host '{}' and port '{}'".format(
            self.args['data'],
            self.host,
            self.port
        )
        return logger_msg

    def _close_log(self) -> str:
        """
        This function formats a log message when closing a connection.
        Output:
            - str
        """
        logger_msg = "Closing connection to host '{}' and port '{}'".format(
            self.host,
            self.port
        )
        return logger_msg

    def _establish_connection(self):
        self.args['sock'].connect((self.host, self.port))

    def __init_sock(self):
        """
        This function creates an open socket if none is present.
        """
        if 'sock' not in self.args:
            self.args['sock'] = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM
            )
