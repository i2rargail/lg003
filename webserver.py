import socket
import threading
import sys


class Webserver:
    def __init__(self,port):
        self.server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server_socket.setsocketopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,TRUE)
        self.server_socket.bind(('',port,))
        self.server_socket.listen(128)

    def server_conn(self):
        new_socket,new_client=self.server_socket.accept()
        print("新用户连接...",new_client)
        
