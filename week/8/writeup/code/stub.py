#!/usr/bin/env python2

import sys
import struct
from dateutil.parser import parse
from datetime import datetime

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)

# From: https://stackoverflow.com/questions/25341945/check-if-string-has-date-any-format
def is_date(string):
    try:
        parse(string)
        return True
    except ValueError:
        return False


# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# track location in the file
offset = 0
# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
#magic, version = struct.unpack("<LL", data[0:8])

# magic: 32 bits (4 bytes): 0xDEADBEEF
magic_length = 4
version_length = 4
magic,version = struct.unpack("<LL", data[offset:magic_length+version_length])
if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

# version: 32 bits (4 bytes): 0x1
if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

offset = offset + magic_length + version_length
timestamp_length = 4

# timestamp 32 bits, 4 bytes
timestamp, = struct.unpack("<L", data[offset:offset + timestamp_length])
#print ("Timestamp %s" % str(timestamp))
timestamp = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

if not is_date(str(timestamp)):
    bork("Bad timestamp! %s is not a valid UNIX timestamp" % timestamp)

offset = offset + timestamp_length
author_length = 8
author = struct.unpack(">Q", data[offset:offset+author_length])[0]

#print("Author: %s" % (str(author[0]), str(author[1])))
#offset = offset + 8
# print("Part 1: %s" % hex(author))
# author = hex(author)[2:]
#author += struct.unpack("<LL", data[offset:offset+8])
#print("Part 2: %s" %str(author))
#author = hex((author[1]<<32) | author[0])# | (author[2]<<32) | author[0])
#author = author[2:]

sectioncount_length = 4
offset = offset + author_length
sectioncount = struct.unpack("<L", data[offset:offset+sectioncount_length])
if not sectioncount > 0:
    bork("Bad section count! %d must be greater than 0" % sectioncount)

# Header Layout
# Magic: 0xDEADBEEF Version: version Timestamp: timestamp Author: author Section count: sectioncount

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %s" % timestamp)
print("AUTHOR: %s" % bytearray.fromhex(hex(author)[2:]).decode())
print("SECTION COUNT: %s" % sectioncount)

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")
headersize = magic_length + version_length + timestamp_length + author_length + sectioncount_length
print("Header Size: %d" % headersize)
#print("Temp: %s" % temp)
bodyoffset = headersize


section_number = 1
while section_number <= sectioncount:#int(sectioncount[0]):
    stype, slen = struct.unpack("<LL", data[bodyoffset:bodyoffset+8])
    print("SECTION %d: " % section_number)
    print("Section Type: %s" %  hex(stype))
    print("Section Length: %s" % hex(slen))

    bodyoffset = bodyoffset + 8

    # index = 1
    # svalue = 0
    # while index <= slen:
    #     svalue_1 = struct.unpack(">B", data[bodyoffset:bodyoffset+1])[0]
    #     svalue = svalue << 8 | svalue_1
    #     index += 1
    #     bodyoffset += 1
        #print("SVALUE[%d]: %s" % (index, hex(svalue)))

    # svalue = ()
    # while slen > 7:
    #     print("Loop Length: %d" % slen)
    #     svalue += struct.unpack(">B", data[bodyoffset:bodyoffset+1])
    #     bodyoffset += 8
    #     slen -= 8
    # extra = struct.unpack("<LL", data[bodyoffset:bodyoffset+8])
    # extra = extra[0] << 16 | extra[1]
    # print("EXTRA: %s" % hex(extra))
    # index = len(svalue) - 2
    # svalue_1 = svalue[0]
    # svalue_move = 32
    # index = 1
    # while index < len(svalue):
    #     svalue_1 = svalue_1 << svalue_move | svalue[index]
    #     index += 1
    # `SECTION_PNG` (`0x1`) -- Embedded PNG image.
    if stype == 0x1:
        print ("SECTION_PNG")
        print("Offset: %s" % hex(bodyoffset))
        print("Ending: %s" % hex(bodyoffset+slen))
        index = 0
        svalue = 0x89504E470D0A1A0AL
        while index < slen:
            svalue_1 = struct.unpack(">B", data[bodyoffset:bodyoffset+1])[0]
            svalue = svalue << 8 | svalue_1
            index += 1
            bodyoffset += 1
            #print("SVALUE[%d]: %s" % (index, hex(svalue)))
        # print("Offset: %d" % bodyoffset)
        #print("SVALUE: %s" % str(svalue)[20])
        #print("SVALUE: %s" % hex(svalue))
        #print("Svalue: %s" % hex(svalue))
        #print("Svalue: %s" % hex(svalue)[2:-1].decode("hex"))
        filename = "Section" + str(section_number) + ".png"
        f = open(filename,"w+")
        #f.write(chr(svalue))
        f.write(hex(svalue)[2:-1].decode("hex"))
        f.close()
        # with open(filename, 'rb') as f:
        #     for chunk in iter(lambda: f.read(32), b''):
        #         print chunk.encode('hex')

    # `SECTION_DWORDS` (`0x2`) -- Array of dwords.
    elif stype == 0x2:
        print ("SECTION_DWORDS")
        index = 1
        svalue = 0
        while index <= (slen/8):
            svalue_1 = struct.unpack("<LL", data[bodyoffset:bodyoffset+8])[0]
            svalue = svalue << 8 | svalue_1
            index += 1
            bodyoffset += 8
        #print("SVALUE: %s" % svalue)
        print("SVALUE: %s" % hex(svalue))
    # `SECTION_UTF8` (`0x3`) -- [UTF-8-encoded](https://en.wikipedia.org/wiki/UTF-8) text.
    elif stype == 0x3:
        print ("SECTION_UTF8")
    # `SECTION_DOUBLES` (`0x4`) -- Array of doubles.
    elif stype == 0x4:
        print ("SECTION_DOUBLES")
    # `SECTION_WORDS` (`0x5`) -- Array of words.
    elif stype == 0x5:
        print ("SECTION_WORDS")
        index = 1
        svalue = 0
        while index <= (slen/4):
            svalue_1 = struct.unpack(">L", data[bodyoffset:bodyoffset+4])[0]
            svalue = svalue << 4 | svalue_1
            index += 1
            bodyoffset += 4
        #print("SVALUE: %s" % svalue)
        print("SVALUE: %s" % hex(svalue))
        #print("Value: %s" % bytearray.fromhex(hex(svalue)[2:-1]).decode())
    # `SECTION_COORD` (`0x6`) -- (Latitude, longitude) tuple of doubles.
    elif stype == 0x6:
        print ("SECTION_COORD")
        #latitude,longitude = struct.unpack("<dd", data[bodyoffset:bodyoffset+64])
        coor = struct.unpack("<dd", data[bodyoffset:bodyoffset+16])
        print("Coordinates: %s" % str(coor))
        bodyoffset += 16
    # `SECTION_REFERENCE` (`0x7`) -- The index of another section.
    elif stype == 0x7:
        print ("SECTION_REFERENCE")
        svalue = struct.unpack("<L", data[bodyoffset:bodyoffset+4])[0]
        print ("SVALUE: %s" % hex(svalue))
        bodyoffset += 4

    # `SECTION_ASCII` (`0x9`)
    elif stype == 0x9:
        print ("SECTION_ASCII")
        index = 0
        svalue = 0
        while index < slen:
            svalue_1 = struct.unpack(">B", data[bodyoffset:bodyoffset+1])[0]
            svalue = svalue << 8 | svalue_1
            index += 1
            bodyoffset += 1
        # svalue = ()
        # while slen > 0:
        #     svalue += struct.unpack("<LL", data[bodyoffset:bodyoffset+8])
        #     bodyoffset += 8
        #     slen -= 8
        # index = len(svalue) - 2
        # svalue_1 = svalue[0]
        # svalue_move = 32
        # index = 1
        # while index < len(svalue):
        #     svalue_1 = svalue_1 << svalue_move | svalue[index]
        #     index += 1
        # #print("Value: %s" % str(svalue))

        print("Value: %s" % bytearray.fromhex(hex(svalue)[2:-1]).decode())
        #print("Value: %s" % bytearray.fromhex(str(svalue_1)).decode())
    section_number += 1
