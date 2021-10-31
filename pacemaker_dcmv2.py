# Imports
import PySimpleGUI as sg
from dcm_layoutsv2 import landing_layout, make_parameters

# Set theme of GUI
sg.theme('Dark')

class DCM:
    def __init__(self):

        # Initialize landing window layout and run program
        self.window = sg.Window('Pacemaker DCM', landing_layout)
        self.run_welcome_screen()

    def run_welcome_screen(self):
        # Infinite loop so that the program stays running until the window is closed
        while True:
            # Read in event and input values
            event, values = self.window.read()
            # Termination
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
            
            # Login process
            if event == "Login":
                if DCM.verify(values["-name-"], values["-password-"]):
                    global username 
                    username = values["-name-"]
                    # If login is successful, proceed to pacing screens
                    self.window.close()
                    DCM.set_paramaters()
                    self.run_pacing_screen()

                else:
                    sg.popup("User doesn't exist. Please register.")

            # Registration process
            elif event == "Register":
                username = values["-name-"]
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
                    DCM.default_paramaters()
                    sg.popup("User successfully registered.")
                
            if event in ['SUB-AOO', 'SUB-VOO', 'SUB-AAI', 'SUB-VVI']:
                DCM.submit_parameters(username,values)


        self.window.close()

    def run_pacing_screen(self):

        # Initialize pacing window layout
        pace_lay = make_parameters(self.set_paramaters())
        self.window = sg.Window('Pacemaker DCM',pace_lay)

    # This method authenticates the user login
    @staticmethod
    def verify(name, password):
        for line in open("user_data.txt", "r").readlines():
            user = line.split()
            if name == user[0] and password == user[1]:
                return True
        return False

    # This method authenticates the user login
    @staticmethod
    def existing_name(name):
        for line in open("user_data.txt", "r").readlines():
            user = line.split()
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
    def default_paramaters():
        count=0
        file = open("user_data.txt", "r")
        list_of_lines = file.readlines()

        for line in list_of_lines:
            user = line.split()
            if username == user[0]:
                file.close()
                break
            count +=1

        list_of_lines[count]= list_of_lines[count].replace("\n","")+" 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25\n"

        a_file = open("user_data.txt", "w")
        a_file.writelines(list_of_lines)
        a_file.close()

    #This method sends the inputed values to the text file with all the data
    @staticmethod
    def submit_parameters(name,values):
        
        count = 0
        list_of_keys =['AOO-LRL','AOO-URL','AOO-AA','AOO-APW','VOO-LRL','VOO-URL','VOO-VA','VOO-VPW','AAI-LRL','AAI-URL','AAI-AA','AAI-APW','AAI-AS','AAI-ARP','AAI-PVARP','AAI-H','AAI-RS','VVI-LRL','VVI-URL','VVI-VA','VVI-VPW','VVI-VS','VVI-VRP','VVI-H','VVI-RS']
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

            user[x] = values[list_of_keys[x-2]]
        list_of_lines[count]= " ".join(user) + "\n"


        a_file = open("user_data.txt", "w")
        a_file.writelines(list_of_lines)
        a_file.close()

    #This method is used for gathering the saved values the user had submitted previously
    @staticmethod
    def set_paramaters():
        count = 0
        a_file = open("user_data.txt", "r")
        list_of_lines = a_file.readlines()
        for line in list_of_lines:
            user = line.split()
            if username == user[0]:
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