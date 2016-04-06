imxfile = open("u-boot.imx", "rb")
addr = 0x0
try:
    while (addr <= 0xc00):
            dword = imxfile.read(1)
            dword += imxfile.read(1)
            dword += imxfile.read(1)
            dword += imxfile.read(1)
            print "0x%0.4X : 0x%s" % (addr, dword.encode('hex'))
            addr += 4
finally:
        imxfile.close()

import struct

# This example demonstrates how to read a binary file, by reading the width and
# height information from a bitmap file. First, the bytes are read, and then
# they are converted to integers.

# When reading a binary file, always add a 'b' to the file open mode
with open('u-boot.imx', 'rb') as f:

    f.seek(0)

    # The width and height are 4 bytes each, so read 8 bytes to get both of them
    bytes = f.read(32)

    # Here, we decode the byte array from the last step. The width and height
    # are each unsigned, little endian, 4 byte integers, so they have the format
    # code '<II'. See http://docs.python.org/3/library/struct.html for more info
    size = struct.unpack('<LLLLLLLL', bytes)

    # Print the width and height of the image
    print 'header:   0x%08x' % (size[0])
    print 'header:   0x%08x' % (size[1])
    print 'header:   0x%08x' % (size[2])
    print 'header:   0x%08x' % (size[3])
    print 'header:   0x%08x' % (size[4])
    print 'header:   0x%08x' % (size[5])
    print 'header:   0x%08x' % (size[6])
    print 'header:   0x%08x' % (size[7])
