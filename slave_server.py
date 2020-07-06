import socket
import time
import sys
import os

class slave_server:
    soc = socket.socket()
    host = "Cyber-Ninja"
    port = 8080
    command = ""

    def __init__(self, command):
        self.command = command
        
    def receive_connection_from_master_server(self):
        self.soc.connect((self.host, self.port))
        
        print("Connected to the master server")

    """
    give a condition
    &
    execute the shutdown bat file
    receive & decode a connection and the command respectively
    """
    def execute_sent_command(self):
        self.command = self.soc.recv(1024)
        self.command = self.command.decode()
        
        if (self.command == "shutdown"):
            print("shutdown command")
            self.soc.send(self.command.encode())
            time.sleep(10)
            
            os.system("shutdown_server.bat")
        else:
            print("Unable to complete the execution")
