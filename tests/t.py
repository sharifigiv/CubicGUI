import struct

myNum = 121080111
myHex = '0x{0:04X}'.format(myNum)
print(myHex)
mylist = list(struct.pack('>I',myNum))
print(mylist)
print(list(map(hex, mylist)))