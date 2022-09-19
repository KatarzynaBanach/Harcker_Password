##  Harcker Password
The program guesses login and password and send it to to the host using socket, trying to break in the website. At each stage another method of guessing login and password was applied (simulating improving security of website by the admin). Created while doing a course on hyperskill.org, based on general schema and guidelines provided by course author (but solutions designed on my own). It was a lot of fun and possibility to practice using of **_socket module, generators, loops, dictionaries, json files._**

**Technologies used:**
- python
- libraries: socket, json, sys, itertools, time






**Stages:**

**Stage 1:**
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



**Stage 2:**
The admin noticed someone sneaking around the site with admin rights and came up with a password.  The admin of the server doesn’t hide the information that passwords vary in length and may include letters from a to z and numbers from 0 to 9. You should start with a,b,c,....,z,0,1,..aa,ab,ac,ad and continue until your password is correct. If the password is correct, you will receive the Connection success! message. Otherwise, you will see the Wrong password! message. The server cannot receive more than a million attempts, so if your program works indefinitely, you will see the unfortunate message Too many attempts.

Objectives:
In this stage, you should write a program that:
- Parses the command line and gets two arguments that are IP address and port.
- Tries different passwords until it finds the correct one.
- Prints the password it found.

**Stage 3:**
The situation gets more complicated: the admin improves the server and our simple brute force attack is no longer working. Well, this shouldn't hold you back: you can provide your program with a prepared dictionary of typical passwords (it was generated using a database with over a million real-life passwords). That's not all: the admin decided to outsmart us and changed the case of some letters in the new password so that we could not crack it using the password dictionary.

Objectives:
In this stage, you should write a program that:
- Parses the command line and gets two arguments that are IP address and port.
- Finds the correct password using the list of typical passwords.
- Prints the password it found.

**Stage 4:**
Now the admin has implemented a security system by login and password. In order to access the site with admin privileges, you need to know the admin's login and password. Fortunately, we have a dictionary of different logins and a very interesting vulnerability. Now the admin has made a complex password that is guaranteed to be absent in the databases since it's randomly generated from several characters. The server now uses JSON to send messages. 
Use an empty password while searching for the correct login. It matters because you will know that the login is correct the moment you get the ‘wrong password’ result instead of ‘wrong login’.

Objectives:
-Try all logins with an empty password.
- When you find the login, try out every possible password of length 1.
- When an exception occurs, you know that you found the first letter of the password.
- Use the found login and the found letter to find the second letter of the password.
- Repeat until you receive the ‘success’ message.
- Finally, your program should print the combination of login and password in JSON format. The examples show two ways of what the output can look like.

**Stage 5:**
The program now catches the exception and sends a simple ‘wrong password’ message to the client even when the real password starts with current symbols.
We know that catching an exception takes the computer a long time, so there should be a delay in the server response when this exception takes place. 
You can use it to hack the system: count the time period in which the response comes and find out which starting symbols work out for the password.

Objectives:
In this stage, you should write a program that uses the time vulnerability to find the password.
- Use the list of logins from the previous stage.
- Output the result as you did this in the previous stage.
