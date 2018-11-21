#!/usr/bin/env python2
# from the git repo
import md5py
import struct
import socket, time

host = '142.93.118.186'
port = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the notary
s.connect((host, port))

# Get the initial prompt
data = s.recv(1024)
#print(data)

#####################################
### STEP 1: Calculate forged hash ###
#####################################

# Request some data to be signed
s.send('1\n')

# Get instructions
data = s.recv(1024)
# print(data)

message = 'CMSC389R Rocks!'    # original message here

# Send message to be signed
s.send(message + '\n')

data = s.recv(1024)
# print(data)

# Your data sent was: CMSC389R Rocks!
# Your hash: <legit>
legit = data.split()[-1]      # a legit hash of secret + message goes here, obtained from signing a message
# print("LEGIT:")
# print (legit)

# initialize hash object with state of a vulnerable hash
fake_md5 = md5py.new('A' * 64)
fake_md5.A, fake_md5.B, fake_md5.C, fake_md5.D = md5py._bytelist2long(legit.decode('hex'))

malicious = 'malicious'  # put your malicious message here

# update legit hash with malicious message
fake_md5.update(malicious)

# fake_hash is the hash for md5(secret + message + padding + malicious)
fake_hash = fake_md5.hexdigest()
# print(fake_hash)

#############################
### STEP 2: Craft payload ###
#############################

# TODO: calculate proper padding based on secret + message
# secret is <redacted> bytes long (48 bits)
# each block in MD5 is 512 bits long
# secret + message is followed by bit 1 then bit 0's (i.e. \x80\x00\x00...)
# after the 0's is a bye with message length in bits, little endian style
# (i.e. 20 char msg = 160 bits = 0xa0 = '\xa0\x00\x00\x00\x00\x00\x00\x00\x00')
# craft padding to align the block as MD5 would do it
# (i.e. len(secret + message + padding) = 64 bytes = 512 bits

# clear buffer
data = s.recv(1024)

for i in range(6,16):
    padding = ''
    padding += '\x80'
    padding += ('\x00' * (64 - len(message) - i - 8 - 1))
    padding += struct.pack('<Q', ((i+len(message))*8))

    payload = message + padding + malicious

    s.send('2\n')
    data = s.recv(1024)
    # print("Send 2: " + data)

    s.send(fake_hash + '\n')
    data = s.recv(1024)
    # print("Fake Hash: " + data)

    print("Sending Payload: %s" %str(payload))
    s.send(payload + '\n')

    time.sleep(1)
    data = s.recv(2048)

    if 'Wow...' in data:
        break

# include hash from which you based your crafted hash, your crafted hash,
# and the payload sent to the notary
print('\n'),
print(data)
print("Hash From Which I Used to Craft My Crafted Hash: %s" % legit)
print("Crafted Hash: %s" % fake_hash)
print("Payload Sent to Notary: %s" % payload)

# send `fake_hash` and `payload` to server (manually or with sockets)
# REMEMBER: every time you sign new data, you will regenerate a new secret!
