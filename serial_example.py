import serial
import struct

packets = []
packets.append(struct.pack('<B', 22)) # Initialization code
packets.append(struct.pack('<B', 85)) # Set-parameter code
packets.append(struct.pack('<B', 1)) # param_dict['mode']
packets.append(struct.pack('<H', 60)) # param_dict['LRL']
packets.append(struct.pack('<H', 120)) # param_dict['URL']
packets.append(struct.pack('<B', 120)) # param_dict['MSR']
packets.append(struct.pack('<H', 150)) # param_dict['FAD']
packets.append(struct.pack('<d', 5)) # param_dict['AA']
packets.append(struct.pack('<d', 5)) # param_dict['VA']
packets.append(struct.pack('<f', 0.4)) # param_dict['APW']
packets.append(struct.pack('<f', 0.4)) # param_dict['VPW']
packets.append(struct.pack('<H', 320)) # param_dict['VRP']
packets.append(struct.pack('<H', 250)) # param_dict['ARP']
packets.append(struct.pack('<f', 1)) # param_dict['AT']
packets.append(struct.pack('<B', 20)) # param_dict['REAT']
packets.append(struct.pack('<B', 1)) # param_dict['RF']
packets.append(struct.pack('<B', 120)) # param_dict['RT']

string = b''

for packet in packets:
    string += packet

with serial.Serial(port='COM4', baudrate=115200) as ser:
    for packet in packets:
        ser.write(packet)


# with serial.Serial(port='COM4', baudrate=115200) as ser:

#     packets[1] = b'\x44'
#     for packet in packets:
#         ser.write(packet)

packets[1] = b'\x33'

count = 0
with serial.Serial(port='COM4', baudrate=115200) as ser:
    for packet in packets:
        ser.write(packet)
    while True:
        data = ser.read(59)
        atrial = struct.unpack('<d', data[43:51])
        ventrical = struct.unpack('<d', data[51:59])
        print('atrial: {} | ventrical: {}'.format(atrial, ventrical))
        if count == 100: break
        count += 1
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    packets[1] = b'\x44'
    for packet in packets:
        ser.write(packet)

# with serial.Serial(port='COM4', baudrate=115200) as ser:
#     while data:
#         data = ser.read(59)



