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

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
#magic, version = struct.unpack("<LL", data[0:8])

# track location in the file
offset = 0

magic_length = 4
version_length = 4
magic,version = struct.unpack("<LL", data[offset:magic_length + version_length])
offset += magic_length
offset += version_length


if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

# version: 32 bits (4 bytes): 0x1
if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

timestamp_length = 4
timestamp, = struct.unpack("<L", data[offset:offset + timestamp_length])
offset += timestamp_length

timestamp = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

# timestamp 32 bits, 4 bytes
if not is_date(str(timestamp)):
    bork("Bad timestamp! %s is not a valid UNIX timestamp" % timestamp)

author_length = 8
author = struct.unpack(">Q", data[offset:offset + author_length])[0]
offset += author_length

sectioncount_length = 4
sectioncount = struct.unpack("<L", data[offset:offset + sectioncount_length])[0]
if not sectioncount > 0:
    bork("Bad section count! %d must be greater than 0" % sectioncount)
offset += sectioncount_length

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

section_number = 1
while section_number <= int(sectioncount)+2:

    stype_length = 4
    slen_length = 4
    stype, slen = struct.unpack("<LL", data[offset:(offset + stype_length + slen_length)])

    offset += stype_length
    offset += slen_length

    # `SECTION_PNG` (`0x1`) -- Embedded PNG image.
    if stype == 0x1:

        section_type = "SECTION_PNG"
        index = 0
        svalue = 0x89504E470D0A1A0AL
        while index < slen:

            svalue_1 = struct.unpack("<B", data[offset:offset+1])[0]
            svalue = svalue << 8 | svalue_1
            index += 1
            offset += 1

        filename = "Section" + str(section_number) + ".png"
        f = open(filename,"w+")
        f.write(hex(svalue)[2:-1].decode("hex"))
        f.close()

        svalue = "Outputted to " + filename

    # `SECTION_DWORDS` (`0x2`) -- Array of dwords.
    elif stype == 0x2:
        section_type = "SECTION_DWORDS"

        index = 1
        svalue = []

        while index <= (slen/8):

            svalue_1 = struct.unpack("<LL", data[offset:offset+8])[0]
            svalue = svalue + [svalue_1]
            index += 1
            offset += 8

    # `SECTION_UTF8` (`0x3`) -- [UTF-8-encoded](https://en.wikipedia.org/wiki/UTF-8) text.
    elif stype == 0x3:
        section_type = "SECTION_UTF8"

        index = 1
        svalue = 0

        while index < slen:

            svalue_1 = struct.unpack("<B", data[offset:offset+1])[0]
            svalue = svalue << 8 | svalue_1
            index += 1
            offset += 1

        svalue = svalue.decode("utf8")

    # `SECTION_DOUBLES` (`0x4`) -- Array of doubles.
    elif stype == 0x4:
        section_type = "SECTION_DOUBLES"
        index = 1
        svalue = 0

        while index <= (slen/8):

            svalue_1 = struct.unpack("<d", data[offset:offset+8])[0]
            svalue = svalue + [svalue_1]
            index += 1
            offset += 8

    # `SECTION_WORDS` (`0x5`) -- Array of words.
    elif stype == 0x5:
        section_type = "SECTION_WORDS"

        index = 1
        svalue = []

        while index <= (slen/4):

            svalue_1 = struct.unpack("<L", data[offset:offset+4])[0]
            svalue = svalue + [svalue_1]
            index += 1
            offset += 4

    # `SECTION_COORD` (`0x6`) -- (Latitude, longitude) tuple of doubles.
    elif stype == 0x6:
        section_type = "SECTION_COORD"
        if slen == 16:
            coor = struct.unpack("<dd", data[offset:offset+16])
            offset += 16
            svalue = str(coor)
        else:
            bork("Bad Coordinates! Got %d, expected 16" % slen)

    # `SECTION_REFERENCE` (`0x7`) -- The index of another section.
    elif stype == 0x7:
        section_type = "SECTION_REFERENCE"

        if slen == 4:
            svalue = struct.unpack("<L", data[offset:offset+4])[0]
            offset += 4
            if (int(svalue)) in range(0,(int(sectioncount)-1)):
                svalue = "Section Number: " + str(int(svalue))
            else:
                bork("Invalid Section Reference Index! %d is nothing in the range [0, nsects(%d) - 1]" % (int(svalue), sectioncount))
        else:
            bork("Bad Section Reference Length! Got %d, expected 16" % slen)

    # `SECTION_ASCII` (`0x9`)
    elif stype == 0x9:
        section_type = "SECTION_ASCII"

        index = 0
        svalue = 0

        while index < slen:

            svalue_1 = struct.unpack("<B", data[offset:offset+1])[0]
            svalue = svalue << 8 | svalue_1
            index += 1
            offset += 1

        svalue = bytearray.fromhex(hex(svalue)[2:-1]).decode()

    print("SECTION %d" % section_number)
    print("TYPE: %s (%s)" %  (section_type, hex(stype))),
    print("LENGTH: %d (%s)" % (int(slen), hex(slen)))
    print("%s" % svalue)
    print("\n"),

    section_number += 1
