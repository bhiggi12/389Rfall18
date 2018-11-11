#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

# this will work if you place this script in your writeup folder
wordlist = open("./probable-v2-top1575.txt", 'r').read().split('\n')

hashes = open("./hashes", 'r').read().split('\r\n')

# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase

for salt in salts:
    # do stuff
    for word in wordlist:
        curr = salt + word
        
        curr_hash = hashlib.sha512(curr).hexdigest()

        if str(curr_hash) in (hashes):
            print("Hash: %s" % str(curr_hash))
            print("Salt: %s" % salt),
            print("Password: %s" % word)
