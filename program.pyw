import socket
import time
import master_server
import slave_server

soc = socket.socket()
host = socket.gethostname()
port = 8080
soc.bind((host, port))
soc.listen(1)

# command from the user(manually)
master_server_command = "shutdown"
slave_server_command = "Command Received"
command = " "

#initialize connection
master_slave_connection = master_server.master(master_server_command, soc, host, port)
master_slave_connection.init_connection_to_slave_server()

time.sleep(5)

#on the slave server
slave_connection_on = slave_server.slave_server(master_server_command)
slave_connection_on.receive_connection_from_master_server()

time.sleep(5)

#execute the master server if the command is received by slave server successfully
master_slave_connection.send_command_to_slave_server()

# execute the shutdown command
slave_connection_on.execute_sent_command()

# display confirmation message for command execution if true or false
master_slave_connection.receive_dispaly_confirmation_message()





