import struct
import os

ub_size = os.path.getsize("u-boot.imx")
file_in = open("u-boot.imx", "rb")
hdr, =struct.unpack("I",file_in.read(4))
ivt_ent, =struct.unpack("I",file_in.read(4))
res1, =struct.unpack("I",file_in.read(4))
dcd, =struct.unpack("I",file_in.read(4))
boot, =struct.unpack("I",file_in.read(4))
self, =struct.unpack("I",file_in.read(4))
csf, =struct.unpack("I",file_in.read(4))
res2, =struct.unpack("I",file_in.read(4))
start, =struct.unpack("I",file_in.read(4))
length, =struct.unpack("I",file_in.read(4))
plugin, =struct.unpack("I",file_in.read(4))
pos = file_in.tell()
dcdhdr, =struct.unpack("B",file_in.read(1))
dcdsiz, =struct.unpack(">H",file_in.read(2))
dcdver, =struct.unpack("B",file_in.read(1))


print("ivt_entry (uboot code start) ".ljust(30),"=", format(ivt_ent, "#08x"))
print("self pointer ".ljust(30),"=", format(self, "#08x"))
print("uboot file size ".ljust(30),"=", format(ub_size, "#08x"), ub_size)
print("load address ".ljust(30),"=", format(start, "#08x"))
print("DCD addr ".ljust(30),"=", format(dcd, "#08x"))
print("length  ".ljust(30),"=", format(length, "#08x"), length)
print("DCD (hdr,len,ver)".ljust(30),"=", format(dcdhdr, '#02x'), format(dcdsiz, '#04x'), format(dcdver, '#02x'))

print("--------------------------------------------------------------------------")

print("csf check ",format(csf, "#08x"), format(self+ub_size, "#08x"))
# pad-to size for proper HAB alignment upon load to memory
print("calculated uboot pad-to value =", format(ub_size+(ub_size+self)%4096, "#08x"))

#end of the DCD will be the starting position of the DCD header + length
# this will be used for the DCD authentication section of the CSF
print("dest address, read offset and length of authenticated section =", format(self, '#08x'),format(0, '#02x'), format(pos+dcdsiz, '#04x'))

#size of the uboot portion of the imx file to be used for encryption section of CSF
print("dest address, read offset and length of encrypted section =", format(ivt_ent, '#08x'), format((ivt_ent-self), '#04x'), format(ub_size-(ivt_ent-self), '#08x'))

