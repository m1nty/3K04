import serial
import serial.tools.list_ports
import struct

def list_ports():
    for i in serial.tools.list_ports.comports():
        print(i)

list_ports()

ser = serial.Serial('COM3', timeout=0)
mode = b''
mode += struct.pack('!B', 3)
print(mode)

ser.write(mode)
# s = ser.read(10)
# print(s)

ser.close()
