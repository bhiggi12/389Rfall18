#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib
import re

host = "142.93.117.193" # IP address or URL
port = 7331 # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# receive some data
data = s.recv(1024)
print(data),

while data:
    if 'win' in data:
        break
    question = re.findall("Find me the (?P<encoding_requested>\S*) hash of (?P<value>\S*)", data)
    #
    h = hashlib.new(question[0][0])
    h.update(question[0][1])
    answer = h.hexdigest()
    print(answer)
    s.send(answer + '\n')
    data = s.recv(1024)
    print(data),

# close the connection
s.close()
