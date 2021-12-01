# Imports
import PySimpleGUI as sg
import json
from dcm_layouts import landing_layout, make_parameters, make_post_submit_layout
from dcm_serial import SerialDCM


# Set theme of GUI
sg.theme('Dark')

class DCM:
    def __init__(self):

        # Initialize landing window layout and run program
        self.window = sg.Window('Pacemaker DCM', landing_layout)
        self.run_welcome_screen()
        
    def run_welcome_screen(self):
        # Infinite loop so that the program stays running until the window is closed
        with open('parameter_data.json') as f:
            param_data = json.load(f)

        param_limits = param_data['param_limits']
        param_keys = param_data['param_keys']
        while True:
            # Read in event and input values
            event, values = self.window.read()
            # Termination
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
            
            # Login process
            if event == "Login":
                if DCM.verify(values["-name-"], values["-password-"]):
                    self.username = values["-name-"]
                    # If login is successful, proceed to pacing screens
                    self.window.close()
                    self.run_pacing_screen()

                else:
                    sg.popup("User doesn't exist. Please register.")

            # Registration process
            elif event == "Register":
                self.username = values["-name-"]
                # Ensure the fields are not empty
                if not values["-name-"] and not values["-password-"]:
                    sg.popup("Credentials cannot be empty.")

                # Avoid duplicate users
                elif DCM.existing_name(values["-name-"]):
                    sg.popup("User already exists.")

                # Max 10 Users
                elif DCM.is_db_full():
                    sg.popup("Max user capacity reached.")

                # Successful registration
                else:
                    DCM.register(values["-name-"], values["-password-"])
                    DCM.default_paramaters(self.username, param_keys, param_limits)
                    sg.popup("User successfully registered.")
                
            if event == 'SUB-VOO':
                DCM.submit_parameters(self.username, values, param_keys, param_limits)

                param_dict = {'mode': 1,
                              'LRL': values['VOO-LRL'],
                              'URL': values['VOO-URL'],
                              'MSR': 1,
                              'FAD': 1,
                              'AA': 1,
                              'VA': values['VOO-VA'],
                              'APW': 1,
                              'VPW': values['VOO-VPW'],
                              'VRP': 1,
                              'ARP': 1,
                              'AT': 'Low',
                              'REAT': 1,
                              'RF': 1,
                              'RT': 1}

                self.serial_conn = SerialDCM()
                self.serial_conn.send_params(param_dict)
                self.run_post_submit()

            if event == 'SUB-VVI':
                DCM.submit_parameters(self.username, values, param_keys, param_limits)

                param_dict = {'mode': 2,
                              'LRL': values['VVI-LRL'],
                              'URL': values['VOO-URL'],
                              'MSR': 1,
                              'FAD': 1,
                              'AA': 1,
                              'VA': values['VVI-VA'],
                              'APW': 1,
                              'VPW': values['VVI-VPW'],
                              'VRP': values['VVI-VRP'],
                              'ARP': 1,
                              'AT': 'Low',
                              'REAT': 1,
                              'RF': 1,
                              'RT': 1}

                self.serial_conn = SerialDCM()
                self.serial_conn.send_params(param_dict)
                self.run_post_submit()

            if event == 'SUB-AOO':
                DCM.submit_parameters(self.username, values, param_keys, param_limits)

                param_dict = {'mode': 3,
                              'LRL': values['AOO-LRL'],
                              'URL': values['AOO-URL'],
                              'MSR': 1,
                              'FAD': 1,
                              'AA': values['AOO-AA'],
                              'VA': 1,
                              'APW': values['AOO-APW'],
                              'VPW': 1,
                              'VRP': 1,
                              'ARP': 1,
                              'AT': 'Low',
                              'REAT': 1,
                              'RF': 1,
                              'RT': 1}

                self.serial_conn = SerialDCM()
                self.serial_conn.send_params(param_dict)
                self.run_post_submit()

            if event == 'SUB-AAI':
                DCM.submit_parameters(self.username, values, param_keys, param_limits)

                param_dict = {'mode': 4,
                              'LRL': values['AAI-LRL'],
                              'URL': values['AAI-URL'],
                              'MSR': 1,
                              'FAD': 1,
                              'AA': values['AAI-AA'],
                              'VA': 1,
                              'APW': values['AAI-APW'],
                              'VPW': 1,
                              'VRP': 1,
                              'ARP': values['AAI-ARP'],
                              'AT': 'Low',
                              'REAT': 1,
                              'RF': 1,
                              'RT': 1}

                self.serial_conn = SerialDCM()
                self.serial_conn.send_params(param_dict)
                self.run_post_submit()

            if event == 'SUB-DOO':
                DCM.submit_parameters(self.username, values, param_keys, param_limits)

                param_dict = {'mode': 5,
                              'LRL': values['DOO-LRL'],
                              'URL': values['DOO-URL'],
                              'MSR': 1,
                              'FAD': values['DOO-FAD'],
                              'AA': values['DOO-AA'],
                              'VA': values['DOO-VA'],
                              'APW': values['DOO-APW'],
                              'VPW': values['DOO-VPW'],
                              'VRP': 1,
                              'ARP': 1,
                              'AT': 'Low',
                              'REAT': 1,
                              'RF': 1,
                              'RT': 1}

                self.serial_conn = SerialDCM()
                self.serial_conn.send_params(param_dict)
                self.run_post_submit()

            if event == 'SUB-VOOR':
                DCM.submit_parameters(self.username, values, param_keys, param_limits)

                param_dict = {'mode': 6,
                              'LRL': values['VOOR-LRL'],
                              'URL': values['VOOR-URL'],
                              'MSR': values['VOOR-MSR'],
                              'FAD': 1,
                              'AA': 1,
                              'VA': values['VOOR-VA'],
                              'APW': 1,
                              'VPW': values['VOOR-VPW'],
                              'VRP': 1,
                              'ARP': 1,
                              'AT': values['VOOR-AT'],
                              'REAT': values['VOOR-REAT'],
                              'RF': values['VOOR-RF'],
                              'RT': values['VOOR-RT']}

                self.serial_conn = SerialDCM()
                self.serial_conn.send_params(param_dict)
                self.run_post_submit()

            if event == 'SUB-VVIR':
                DCM.submit_parameters(self.username, values, param_keys, param_limits)

                param_dict = {'mode': 7,
                              'LRL': values['VVIR-LRL'],
                              'URL': values['VVIR-URL'],
                              'MSR': values['VVIR-MSR'],
                              'FAD': 1,
                              'AA': 1,
                              'VA': values['VVIR-VA'],
                              'APW': 1,
                              'VPW': values['VVIR-VPW'],
                              'VRP': values['VVIR-VRP'],
                              'ARP': 1,
                              'AT': values['VVIR-AT'],
                              'REAT': values['VVIR-REAT'],
                              'RF': values['VVIR-RF'],
                              'RT': values['VVIR-RT']}

                self.serial_conn = SerialDCM()
                self.serial_conn.send_params(param_dict)
                self.run_post_submit()

            if event == 'SUB-AOOR':
                DCM.submit_parameters(self.username, values, param_keys, param_limits)

                param_dict = {'mode': 8,
                              'LRL': values['AOOR-LRL'],
                              'URL': values['AOOR-URL'],
                              'MSR': values['AOOR-MSR'],
                              'FAD': 1,
                              'AA': values['AOOR-AA'],
                              'VA': 1,
                              'APW': values['AOOR-APW'],
                              'VPW': 1,
                              'VRP': 1,
                              'ARP': 1,
                              'AT': values['AOOR-AT'],
                              'REAT': values['AOOR-REAT'],
                              'RF': values['AOOR-RF'],
                              'RT': values['AOOR-RT']}

                self.serial_conn = SerialDCM()
                self.serial_conn.send_params(param_dict)
                self.run_post_submit()

            if event == 'SUB-AAIR':
                DCM.submit_parameters(self.username, values, param_keys, param_limits)

                param_dict = {'mode': 9,
                              'LRL': values['AAIR-LRL'],
                              'URL': values['AAIR-URL'],
                              'MSR': values['AAIR-MSR'],
                              'FAD': 1,
                              'AA': values['AAIR-AA'],
                              'VA': 1,
                              'APW': values['AAIR-APW'],
                              'VPW': 1,
                              'VRP': 1,
                              'ARP': values['AAIR-ARP'],
                              'AT': values['AAIR-AT'],
                              'REAT': values['AAIR-REAT'],
                              'RF': values['AAIR-RF'],
                              'RT': values['AAIR-RT']}

                self.serial_conn = SerialDCM()
                self.serial_conn.send_params(param_dict)
                self.run_post_submit()

            if event == 'SUB-DOOR':
                DCM.submit_parameters(self.username, values, param_keys, param_limits)

                param_dict = {'mode': 10,
                              'LRL': values['DOOR-LRL'],
                              'URL': values['DOOR-URL'],
                              'MSR': values['DOOR-MSR'],
                              'FAD': values['DOOR-FAD'],
                              'AA': values['DOOR-AA'],
                              'VA': values['DOOR-VA'],
                              'APW': values['DOOR-APW'],
                              'VPW': values['DOOR-VPW'],
                              'VRP': 1,
                              'ARP': 1,
                              'AT': values['DOOR-AT'],
                              'REAT': values['DOOR-REAT'],
                              'RF': values['DOOR-RF'],
                              'RT': values['DOOR-RT']}

                self.serial_conn = SerialDCM()
                self.serial_conn.send_params(param_dict)
                self.run_post_submit()
                
        self.window.close()

    def run_pacing_screen(self):

        # Initialize pacing window layout
        pace_lay = make_parameters(DCM.set_paramaters(self.username))
        self.window = sg.Window('Pacemaker DCM', pace_lay)

    def run_post_submit(self):

        self.window2 = make_post_submit_layout()
        while True:
            # Read in event and input values
            event, values = self.window2.read()

            if event == "Exit" or event == sg.WIN_CLOSED:
                break

            if event == 'VERIFY-PARAM-BUTTON':
                self.serial_conn.verify_params()

            if event == 'DISPLAY-BOTH-EGRAM':
                self.serial_conn.get_all_egram_data()

            if event == 'DISPLAY-A-EGRAM':
                self.serial_conn.get_a_egram_data()

            if event == 'DISPLAY-V-EGRAM':
                self.serial_conn.get_v_egram_data()

            if event == 'STOP-PACING-BUTTON':
                param_dict = {'mode': 0,
                              'LRL': 1,
                              'URL': 1,
                              'MSR': 1,
                              'FAD': 1,
                              'AA': 1,
                              'VA': 1,
                              'APW': 1,
                              'VPW': 1,
                              'VRP': 1,
                              'ARP': 1,
                              'AT': 'Low',
                              'REAT': 1,
                              'RF': 1,
                              'RT': 1}

                self.serial_conn = SerialDCM()
                self.serial_conn.send_params(param_dict)

        self.window2.close()

    # This method authenticates the user login
    @staticmethod
    def verify(name, password):
        for line in open("user_data.txt", "r").readlines():
            user = line.split()
            if not user:
                return False
            if name == user[0] and password == user[1]:
                return True
        return False

    # This method authenticates the user login
    @staticmethod
    def existing_name(name):
        for line in open("user_data.txt", "r").readlines():
            user = line.split()
            if not user:
                return False
            if name == user[0]:
                return True
        return False

    # This method checks if db at full capacity
    @staticmethod
    def is_db_full():
        if sum(1 for line in open('user_data.txt')) == 10:
            return True
        return False

    # This method registers new users by writing it to the database(txt file)
    @staticmethod
    def register(name, password):
        file = open("user_data.txt", "a")
        file.write(name)
        file.write(" ")
        file.write(password)
        file.write("\n")
        file.close()

    #This method is for giving a new registered user default parameters
    @staticmethod
    def default_paramaters(name, param_keys, param_limits):
        count=0
        file = open("user_data.txt", "r")
        list_of_lines = file.readlines()

        for line in list_of_lines:
            user = line.split()
            if user:
                if name == user[0]:
                    file.close()
                    break
            count +=1

        default_params = ''
        for param in param_keys:
            default_params += str(param_limits[param.split('-')[1]]['nominal']) + ' '
        default_params += '\n'

        list_of_lines[count]= list_of_lines[count].replace("\n"," ") + default_params

        a_file = open("user_data.txt", "w")
        a_file.writelines(list_of_lines)
        a_file.close()

    #This method sends the inputed values to the text file with all the data
    @staticmethod
    def submit_parameters(name, values, param_keys, param_limits):
        invalid_value_flag = False
        count = 0
        
        a_file = open("user_data.txt", "r")
        list_of_lines = a_file.readlines()

        for line in list_of_lines:
            user = line.split()
            if name == user[0]:
                a_file.close()
                break
            count +=1
        user = list_of_lines[count].split()
        for x in range(len(user)):
            if(x==0 or x==1):
                continue
            curr_key = param_keys[x-2]
            valid_params = [str(x) for x in param_limits[curr_key.split('-')[1]]['valid']]

            if values[curr_key] in valid_params:
                user[x] = values[curr_key]
            else:
                sg.popup("Parameter out of bounds: {}".format(curr_key))
                invalid_value_flag = True

        if not invalid_value_flag:
            list_of_lines[count]= " ".join(user) + "\n"
            a_file = open("user_data.txt", "w")
            a_file.writelines(list_of_lines)
            a_file.close()

    #This method is used for gathering the saved values the user had submitted previously
    @staticmethod
    def set_paramaters(name):
        count = 0
        a_file = open("user_data.txt", "r")
        list_of_lines = a_file.readlines()
        for line in list_of_lines:
            user = line.split()
            if name == user[0]:
                a_file.close()
                break
            count +=1
        data = []
        user = list_of_lines[count].split()
        for x in range(len(user)):
            if(x==0 or x==1):
                continue
            data.append(user[x])
        return data
            
# Run module
program = DCM()