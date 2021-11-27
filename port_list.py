import serial
import struct

# ser = serial.Serial('COM4', timeout=0)
string = struct.pack('<BBBHHBHddffHHfBBB', 22, 85, 1, 60, 120, 120, 150, 5, 5, 0.4, 0.4, 320, 250, 1, 20, 1, 120)
print(len(string))

# ser.write(mode)
# s = ser.read(10)
# print(s)

#ser.close()
