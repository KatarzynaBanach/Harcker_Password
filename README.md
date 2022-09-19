# Harcker_Password
The program guesses login and password and send it to to the host using socket, trying to break in the website.At each stage another method of guessing login and password was applied (simulating improving security of website by the admin). Created while doing a course on hyperskill.org, based on general schema and guidelines provided by course author (but solutions designed on my own). It was a lot of fun and possibility to practice using of **socket module, generators, loops, dictionaries, json files.**

**Technologies used:**
- python
- libraries: socket, json, sys, itertools, time





## Stages:

## Stage 1:
Imagine some admin who runs a website on the Internet. The first task of this project is to go to the admin's site; it will immediately give out all the secret information. Remember, as soon as you enter the site as an admin, you will automatically obtain all the private data of the site.  Your program should connect to the server using an IP address and a port from the command line arguments. You can use socket module to create this program.

Objectives:

Your program will receive command line arguments in this order:
- IP address
- port
- message for sending
The algorithm is the following:
- Create a new socket.
- Connect to a host and a port using the socket.
- Send a message from the third command line argument to the host using the socket.
- Receive the server’s response.
- Print the server’s response.
- Close the socket.



## Stage 2:
## Stage 3:
## Stage 4:
## Stage 5:
