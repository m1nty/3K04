import serial
import serial.tools.list_ports
import struct

def list_ports():
    for i in serial.tools.list_ports.comports():
        print(i)

list_ports()

# ser = serial.Serial('COM4', timeout=0)

string3 = (1).to_bytes(1, byteorder='big')
string3 += (60).to_bytes(2, byteorder='big')
print(string3)
string3 += (120).to_bytes(2, byteorder='big')
string3 += (120).to_bytes(2, byteorder='big')
string3 += (150).to_bytes(2, byteorder='big')
string3 += (5.0).to_bytes(2, byteorder='big')
string3 += (5.0).to_bytes(2, byteorder='big')
string3 += (0.4).to_bytes(2, byteorder='big')
string3 += (0.4).to_bytes(2, byteorder='big')
string3 += (320).to_bytes(2, byteorder='big')
string3 += (250).to_bytes(2, byteorder='big')
string3 += (1).to_bytes(2, byteorder='big')
string3 += (20).to_bytes(2, byteorder='big')
string3 += (1).to_bytes(2, byteorder='big')
string3 += (120).to_bytes(2, byteorder='big')


print(string3)

final = b'\\x16\\x55\\'

# ser.write(mode)
# s = ser.read(10)
# print(s)

ser.close()
