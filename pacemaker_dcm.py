# Imports
import PySimpleGUI as sg
from dcm_layouts import landing_layout, pacing_layout

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

                    # If login is successful, proceed to pacing screens
                    self.window.close()
                    self.run_pacing_screen()
                else:
                    sg.popup("User doesn't exist. Please register.")

            # Registration process
            elif event == "Register":

                # Ensure the fields are not empty
                if not values["-name-"] and not values["-password-"]:
                    sg.popup("Credentials cannot be empty.")

                # Avoid duplicate users
                elif DCM.verify(values["-name-"], values["-password-"]):
                    sg.popup("User already exists.")

                # Successful registration
                else:
                    DCM.register(values["-name-"], values["-password-"])
                    sg.popup("User successfully registered.")

        self.window.close()

    def run_pacing_screen(self):

        # Initialize pacing window layout
        self.window = sg.Window('Pacemaker DCM', pacing_layout)

    # This method authenticates the user login
    @staticmethod
    def verify(name, password):
        for line in open("user_data.txt", "r").readlines():
            user = line.split()
            if name == user[0] and password == user[1]:
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

# Run module
program = DCM()