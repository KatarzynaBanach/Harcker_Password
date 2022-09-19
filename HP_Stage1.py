# Project: Password Hacker - hyperskills
# STAGE 1 
import socket
import sys

data = sys.argv
hostname = data[1]
port = int(data[2])
message = data[3]


my_socket = socket.socket()
my_socket.connect((hostname, port))
message = message.encode()
my_socket.send(message)
response = my_socket.recv(1024)
response = response.decode()
print(response)
my_socket.close()
