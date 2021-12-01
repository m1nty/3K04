# Imports
import PySimpleGUI as sg
import serial
import struct
from dcm_layouts import make_a_v_egram_layout, make_a_egram_layout, make_v_egram_layout

class SerialDCM:
    def __init__(self, port='COM4', baudrate=115200):
        self.port = port
        self.baudrate = baudrate
        self.packets = []

        self.AT_map = {'V-Low': 1,
                       'Low': 1.2,
                       'Med-Low': 1.4,
                       'Med': 1.6,
                       'Med-High': 1.8,
                       'High': 2.0,
                       'V-High': 2.3}
        
    def send_params(self, param_dict):
        self.packets.append(struct.pack('<B', 22)) # Initialization code
        self.packets.append(struct.pack('<B', 85)) # Set-parameter code
        self.packets.append(struct.pack('<B', int(param_dict['mode']))) # param_dict['mode']
        self.packets.append(struct.pack('<H', int(param_dict['LRL']))) # param_dict['LRL']
        self.packets.append(struct.pack('<H', int(param_dict['URL']))) # param_dict['URL']
        self.packets.append(struct.pack('<B', int(param_dict['MSR']))) # param_dict['MSR']
        self.packets.append(struct.pack('<H', int(param_dict['FAD']))) # param_dict['FAD']
        self.packets.append(struct.pack('<d', float(param_dict['AA']))) # param_dict['AA']
        self.packets.append(struct.pack('<d', float(param_dict['VA']))) # param_dict['VA']
        self.packets.append(struct.pack('<f', float(param_dict['APW']))) # param_dict['APW']
        self.packets.append(struct.pack('<f', float(param_dict['VPW']))) # param_dict['VPW']
        self.packets.append(struct.pack('<H', int(param_dict['VRP']))) # param_dict['VRP']
        self.packets.append(struct.pack('<H', int(param_dict['ARP']))) # param_dict['ARP']
        self.packets.append(struct.pack('<f', self.AT_map[param_dict['AT']])) # param_dict['AT']
        self.packets.append(struct.pack('<B', int(param_dict['REAT']))) # param_dict['REAT']
        self.packets.append(struct.pack('<B', int(param_dict['RF']))) # param_dict['RF']
        self.packets.append(struct.pack('<B', int(param_dict['RT']))) # param_dict['RT']
        print(self.packets)
        with serial.Serial(port=self.port, baudrate=self.baudrate) as ser:
            
            for packet in self.packets:
                ser.write(packet)
        

    def verify_params(self):
        self.packets[1] = b'\x22'

        with serial.Serial(port=self.port, baudrate=self.baudrate) as ser:
            for packet in self.packets:
                ser.write(packet)

            self.params_byte_string = ser.read(59)

        byte_string = b''
        for packet in self.packets:
            byte_string += packet

        if byte_string[2:] == self.params_byte_string[:43]:
            sg.popup("The parameters are verified!")
        else:
            sg.popup("The parameters are incorrect!")

    # TO-DO: Need to allow for two different graphs, one for atrial, one for ventrical, and option for both to be showing as well
    def get_all_egram_data(self):
        # if len(self.packets) < 47:
        #     raise Exception('Please submit parameters prior to requesting egram data!')
  
        self.packets[1] = b'\x22'
        
        GRAPH_SIZE_X = 800
        x = lastx = lasty1 = lasty2 = 0
        step_size, delay = 1, 1
        
        self.window3 = make_a_v_egram_layout()
        
        with serial.Serial(port=self.port, baudrate=self.baudrate) as ser:
            while True:
                for packet in self.packets:
                    ser.write(packet)
                self.egram_byte_string = ser.read(59)
                atrial = struct.unpack('<d', self.egram_byte_string[43:51])
                ventrical = struct.unpack('<d', self.egram_byte_string[51:59])

                event, values = self.window3.read(timeout=delay)
                
                if event == "Exit" or event == sg.WIN_CLOSED:
                    break

                y1 = 10*ventrical[0]/0.6 - 5 # determine the atrial/ventrical size (convert from byte string) and place here
                y2 = 130 + 10*atrial[0]/0.6 - 5
                if x < GRAPH_SIZE_X:               # if still drawing initial width of graph
                    self.window3['A-GRAPH'].DrawLine((lastx, lasty2), (x, y2), width=1)
                    self.window3['V-GRAPH'].DrawLine((lastx, lasty1), (x, y1), width=1)
                else:                               # finished drawing full graph width so move each time to make room
                    x = lastx = lasty1 = lasty2 = 0
                    self.window3['A-GRAPH'].erase()
                    self.window3['V-GRAPH'].erase()
                    self.window3['A-GRAPH'].DrawLine((lastx, lasty2), (x, y2), width=1)
                    self.window3['V-GRAPH'].DrawLine((lastx, lasty1), (x, y1), width=1)
                    

                lastx, lasty1, lasty2 = x, y1, y2
                x += step_size


        self.window3.close()

    def get_a_egram_data(self):
        self.packets[1] = b'\x22'
        
        GRAPH_SIZE_X = 800
        x = lastx = lasty = 0
        step_size, delay = 1, 1
        
        self.window3 = make_a_egram_layout()

        with serial.Serial(port=self.port, baudrate=self.baudrate) as ser:

            while True:
                for packet in self.packets:
                    ser.write(packet)
                self.egram_byte_string = ser.read(59)
                atrial = struct.unpack('<d', self.egram_byte_string[43:51])

                event, values = self.window3.read(timeout=delay)

                if event == "Exit" or event == sg.WIN_CLOSED:
                    break
                
                y = 10*atrial[0]/0.6 - 5 # determine the atrial/ventrical size (convert from byte string) and place here

                if x < GRAPH_SIZE_X:        # if still drawing initial width of graph
                    self.window3['A-GRAPH'].DrawLine((lastx, lasty), (x, y), width=1)
                else:                               # finished drawing full graph width so move each time to make room
                    x = lastx = lasty = 0
                    self.window3['A-GRAPH'].erase()
                    self.window3['A-GRAPH'].DrawLine((lastx, lasty), (x, y), width=1)

                lastx, lasty = x, y
                x += step_size

        self.window3.close()

    def get_v_egram_data(self):
        self.packets[1] = b'\x22'
        
        GRAPH_SIZE_X = 800
        x = lastx = lasty = 0
        step_size, delay = 1, 1
        
        self.window3 = make_v_egram_layout()

        with serial.Serial(port=self.port, baudrate=self.baudrate) as ser:
            
            while True:
                for packet in self.packets:
                    ser.write(packet)
                self.egram_byte_string = ser.read(59)
                ventrical = struct.unpack('<d', self.egram_byte_string[51:59])

                event, values = self.window3.read(timeout=delay)

                if event == "Exit" or event == sg.WIN_CLOSED:
                    break
                
                y = 10*ventrical[0]/0.6 - 5 # determine the atrial/ventrical size (convert from byte string) and place here

                if x < GRAPH_SIZE_X:             # if still drawing initial width of graph
                    self.window3['V-GRAPH'].DrawLine((lastx, lasty), (x, y), width=1)
                else:                               # finished drawing full graph width so move each time to make room
                    x = lastx = lasty = 0
                    self.window3['V-GRAPH'].erase()
                    self.window3['V-GRAPH'].DrawLine((lastx, lasty), (x, y), width=1)

                lastx, lasty = x, y
                x += step_size

        self.window3.close()



        