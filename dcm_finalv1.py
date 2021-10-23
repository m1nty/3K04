import PySimpleGUI as sg
#definitly not final btw
#still need to add the parameter screens
#
sg.theme('TealMono')#hospital vibes

def make_welc_win():
    layout = [[sg.Text('Welcome to the PACEMAKER 9000')],
              [sg.Button('Enter'), sg.Button('Exit')]]
    return sg.Window('Welcome Window', layout, finalize=True)
def make_login():
    layout = [[sg.Text('Please enter your username and password')],
              [sg.Text('Username'),sg.Input(key='-username-', enable_events=True)],
              [sg.Text('Password'),sg.Input(key='-password-',enable_events=True)],
              [sg.Button('Login'),sg.Button('Register')]]
    return sg.Window('Login/Registration Window', layout, finalize=True)
#stole the verify and register functions from m1nts
#thank you m1nts
def verify(name, password):
    for line in open("user_data.txt", "r").readlines():
        user = line.split()
        if name == user[0] and password == user[1]:
            return True
    return False


def register(name, password):
    file = open("user_data.txt", "a")
    file.write(name)
    file.write(" ")
    file.write(password)
    file.write("\n")
    file.close()

window= make_welc_win()        # start off with 1 window open

while True: #EVENT LOOP
    window,event,values = sg.read_all_windows()
    if window == sg.WIN_CLOSED:
        break
    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()

    if event == 'Enter':
        window.close()
        window = make_login()
    #logging in
    if event == 'Login':
        if verify(values["-username-"], values["-password-"]):
            window.close()
            sg.popup("YOU HAVE SUCCESFULLY LOGGED IN. WORK IN PROGRESS WOOPSIES")
            #this will make a new window open up with all the data
        else:
            sg.popup("This user does not exist try again")
    #registering user
    elif event =='Register':

        if not values["-username-"] and not values["-password-"]:
            sg.popup("Input cannot be empty")

        elif verify(values["-username-"], values["-password-"]):
            sg.popup("This user already exists, try a new name")
        else:
            register(values["-username-"], values["-password-"])
            sg.popup("User has been registered.")
        


