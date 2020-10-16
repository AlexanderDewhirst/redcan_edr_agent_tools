#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 4000


def serve():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        while True:
            conn, addr = s.accept()
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if data:
                    conn.sendall(data)
                    print('Data:', data.decode())


serve()