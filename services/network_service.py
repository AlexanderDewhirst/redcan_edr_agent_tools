#!/usr/bin/env python

import socket

class NetworkService(object):

    def __init__(self, host: str, port: int, **kwargs):
        self.host = host
        self.port = port
        self.args = kwargs
        self.sock = self.__init_sock()

    def connect(self) -> dict:
        """
        This function establishes a connection to a server using the 'socket' Python library.
        Output:
            - dict
        """
        data = {'sock': {'source': {}, 'destination': {}}}
        try:
            self._establish_connection()
            data['sock']['source']['host'], data['sock']['source']['port'] = self.__get_socket_source()
            data['sock']['destination']['host'], data['sock']['destination']['port'] = self.__get_socket_destination()
            self.sock.close()
            status = True
        except:
            status = False
        finally:
            return self._construct_response(status, data)

    def send(self) -> dict:
        """
        This function sends data to a server using the 'socket' Python library.
        Output:
            - dict
        """
        # NOTE: Python requires keys to be constructed beforehand. Otherwise is throws a KeyError
        data = {'sock': {'source': {}, 'destination': {}}, 'message': ''}
        try:
            self._establish_connection()
            data['sock']['source']['host'], data['sock']['source']['port'] = self.__get_socket_source()
            data['sock']['destination']['host'], data['sock']['destination']['port'] = self.__get_socket_destination()
            data['message'] = self.args['data']
            self.sock.sendall(self.args['data'].encode())
            self.sock.close()
            status = True
        except:
            status = False
        finally:
            return self._construct_response(status, data)

    def close(self) -> dict:
        """
        This function closes a connection using the 'socket' Python library.
        Output:
            - dict
        """
        data = {'sock': {'source': {}, 'destination': {}}}
        try:
            self._establish_connection()
            data['sock']['source']['host'], data['socket']['source']['port'] = self.__get_socket_source()
            data['sock']['destination']['host'], data['socket']['destination']['port'] = self.__get_socket_destination()
            self.sock.close()
            status = True
        except:
            status = False
        finally:
            return self._construct_response(status, data)

    
    def _establish_connection(self):
        """
        This function establishes the connection to the socket.
        """
        self.sock.connect((self.host, self.port))

    def __init_sock(self):
        """
        This function creates an open socket if none is present.
        """
        if 'sock' not in self.args:
            return socket.socket(
                socket.AF_INET, socket.SOCK_STREAM
            )
        else:
            return self.args['sock']

    def _construct_response(self, status:bool, data:dict = None) -> dict:
        """
        This function constructs the data object for the Logger
        Input:
            - bool
            - dict (opt.)
        Output:
            - dict
        """
        response = {
            'status': status,
            'data': data
        }
        return response

    def __get_socket_source(self):
        """
        This function gets the source host and port
        Outpuf:
            - tuple
        """
        return self.sock.getsockname()

    def __get_socket_destination(self):
        """
        This function gets the destination host and port
        Output:
            - tuple
        """
        return self.sock.getpeername()
