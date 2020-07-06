import socket
import time
import sys
import os

class master:
    soc = ""
    host = ""
    port = ""
    command = ""
    connection = ""
    address = ""
    data = ""
    
    def __init__(self, command, soc, host, port):
        self.command = command
        self.soc = soc
        self.host = host
        self.port = port
        
    def init_connection_to_slave_server(self):
        print("Waiting for any available connections")
        
    def send_command_to_slave_server(self):
        print(self.host)
        
        self.connection, self.address = self.soc.accept()

        print(self.address, "- Has Connected to the slave server")

        # send & encode a connection and the command respectively
        send_connection = self.connection.send(self.command.encode())

        print("Command has been sent successfully, waiting for confirmation!")

    def receive_dispaly_confirmation_message(self):
        # receive the confirmation message from the slave server
        self.data = self.connection.recv(1024)

        # condtion
        if self.data:
            print("Shutdown command has been sent and executed")
