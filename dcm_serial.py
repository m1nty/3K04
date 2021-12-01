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

        # A map to convert the text-representation of activity threshold
        self.AT_map = {'V-Low': 1,
                       'Low': 1.2,
                       'Med-Low': 1.4,
                       'Med': 1.6,
                       'Med-High': 1.8,
                       'High': 2.0,
                       'V-High': 2.3}
        
    def send_params(self, param_dict):
        # Pack each parameter into a byte string and append it onto the packets list
        self.packets.append(struct.pack('<B', 22)) # Initialization code
        self.packets.append(struct.pack('<B', 85)) # Set-parameter code
        self.packets.append(struct.pack('<B', int(param_dict['mode']))) 
        self.packets.append(struct.pack('<H', int(param_dict['LRL']))) 
        self.packets.append(struct.pack('<H', int(param_dict['URL']))) 
        self.packets.append(struct.pack('<B', int(param_dict['MSR']))) 
        self.packets.append(struct.pack('<H', int(param_dict['FAD']))) 
        self.packets.append(struct.pack('<d', float(param_dict['AA']))) 
        self.packets.append(struct.pack('<d', float(param_dict['VA']))) 
        self.packets.append(struct.pack('<f', float(param_dict['APW']))) 
        self.packets.append(struct.pack('<f', float(param_dict['VPW']))) 
        self.packets.append(struct.pack('<H', int(param_dict['VRP']))) 
        self.packets.append(struct.pack('<H', int(param_dict['ARP']))) 
        self.packets.append(struct.pack('<f', self.AT_map[param_dict['AT']])) 
        self.packets.append(struct.pack('<B', int(param_dict['REAT']))) 
        self.packets.append(struct.pack('<B', int(param_dict['RF'])))
        self.packets.append(struct.pack('<B', int(param_dict['RT'])))
        
        # Open the serial comm and write each packet one by one, total of 45 bytes
        with serial.Serial(port=self.port, baudrate=self.baudrate) as ser:
            for packet in self.packets:
                ser.write(packet)
        

    def verify_params(self):
        # Switch flag to return params instead of setting
        self.packets[1] = b'\x22'

        # Open the serial comm and write each packet one by one, total of 45 bytes
        with serial.Serial(port=self.port, baudrate=self.baudrate) as ser:
            for packet in self.packets:
                ser.write(packet)

            # The pacemaker will return a bytestring of 59 bytes, composed of parameters and heartbeat data
            self.params_byte_string = ser.read(59)

        # Construct a bytestring from the DCM parameter data
        byte_string = b''
        for packet in self.packets:
            byte_string += packet
        
        # Compare the DCM parameters with the pacemaker parameters
        if byte_string[2:] == self.params_byte_string[:43]:
            sg.popup("The parameters are verified!")
        else:
            sg.popup("The parameters are incorrect!")

    # TO-DO: Need to allow for two different graphs, one for atrial, one for ventrical, and option for both to be showing as well
    def get_all_egram_data(self):
        # Switch flag to return signals
        self.packets[1] = b'\x22'
        
        # Initialize graph properties
        GRAPH_SIZE_X = 800
        x = lastx = lasty1 = lasty2 = 0
        step_size, delay = 1, 1
        
        # Open window
        self.window3 = make_a_v_egram_layout()
        
        with serial.Serial(port=self.port, baudrate=self.baudrate) as ser:
            while True:
                # Send trigger and read back signal data
                for packet in self.packets:
                    ser.write(packet)
                self.egram_byte_string = ser.read(59)

                # Extract the atrial and ventricle singals from the byte string and unpack them
                atrial = struct.unpack('<d', self.egram_byte_string[43:51])
                ventrical = struct.unpack('<d', self.egram_byte_string[51:59])

                event, values = self.window3.read(timeout=delay)
                
                if event == "Exit" or event == sg.WIN_CLOSED:
                    break
                    
                # Scale the values to the appropriate range
                y1 = 10*ventrical[0]/0.6 - 5
                y2 = 130 + 10*atrial[0]/0.6 - 5

                # If still drawing initial width of graph
                if x < GRAPH_SIZE_X:               
                    self.window3['A-GRAPH'].DrawLine((lastx, lasty2), (x, y2), width=1)
                    self.window3['V-GRAPH'].DrawLine((lastx, lasty1), (x, y1), width=1)
                # Finished drawing full graph width so erase and start from 0
                else:                               
                    x = lastx = lasty1 = lasty2 = 0
                    self.window3['A-GRAPH'].erase()
                    self.window3['V-GRAPH'].erase()
                    self.window3['A-GRAPH'].DrawLine((lastx, lasty2), (x, y2), width=1)
                    self.window3['V-GRAPH'].DrawLine((lastx, lasty1), (x, y1), width=1)
                
                # Update values
                lastx, lasty1, lasty2 = x, y1, y2
                x += step_size

        self.window3.close()

    def get_a_egram_data(self):
        # Switch flag to return signals
        self.packets[1] = b'\x22'
        
        # Initialize graph properties
        GRAPH_SIZE_X = 800
        x = lastx = lasty = 0
        step_size, delay = 1, 1
        
        self.window3 = make_a_egram_layout()

        with serial.Serial(port=self.port, baudrate=self.baudrate) as ser:
            while True:
                # Send trigger and read back signal data
                for packet in self.packets:
                    ser.write(packet)
                self.egram_byte_string = ser.read(59)

                # Extract the atrial singals from the byte string and unpack them
                atrial = struct.unpack('<d', self.egram_byte_string[43:51])

                event, values = self.window3.read(timeout=delay)

                if event == "Exit" or event == sg.WIN_CLOSED:
                    break
                
                # Scale the values to the appropriate range
                y = 10*atrial[0]/0.6 - 5 

                # If still drawing initial width of graph
                if x < GRAPH_SIZE_X:
                    self.window3['A-GRAPH'].DrawLine((lastx, lasty), (x, y), width=1)
                # Finished drawing full graph width so erase and start from 0
                else:
                    x = lastx = lasty = 0
                    self.window3['A-GRAPH'].erase()
                    self.window3['A-GRAPH'].DrawLine((lastx, lasty), (x, y), width=1)

                # Update values
                lastx, lasty = x, y
                x += step_size

        self.window3.close()

    def get_v_egram_data(self):
        # Switch flag to return signals
        self.packets[1] = b'\x22'
        
        # Initialize graph properties
        GRAPH_SIZE_X = 800
        x = lastx = lasty = 0
        step_size, delay = 1, 1
        
        self.window3 = make_v_egram_layout()

        with serial.Serial(port=self.port, baudrate=self.baudrate) as ser:
            while True:
                # Send trigger and read back signal data
                for packet in self.packets:
                    ser.write(packet)
                self.egram_byte_string = ser.read(59)

                # Extract the ventricle singals from the byte string and unpack them
                ventrical = struct.unpack('<d', self.egram_byte_string[51:59])

                event, values = self.window3.read(timeout=delay)

                if event == "Exit" or event == sg.WIN_CLOSED:
                    break
                
                # Scale the values to the appropriate range
                y = 10*ventrical[0]/0.6 - 5

                # If still drawing initial width of graph
                if x < GRAPH_SIZE_X:
                    self.window3['V-GRAPH'].DrawLine((lastx, lasty), (x, y), width=1)

                # Finished drawing full graph width so erase and start from 0
                else:
                    x = lastx = lasty = 0
                    self.window3['V-GRAPH'].erase()
                    self.window3['V-GRAPH'].DrawLine((lastx, lasty), (x, y), width=1)

                # Update values
                lastx, lasty = x, y
                x += step_size

        self.window3.close()



        