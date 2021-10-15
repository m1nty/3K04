import PySimpleGUI as sg
import os.path

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
AOO_layout = [  [sg.Text('Pacing Mode - AOO', font=("Helvetica", 20))],
                [sg.Graph((500, 250), (0,0), (500, 250), background_color='white', key="-GRAPH-")],
                [sg.Text('Enter Parameters:', font=("Helvetica", 16))],
                [sg.Text('Lower Rate Limit', size=(16,1)), sg.InputText('1', key='AOO-LRL')],
                [sg.Text('Upper Rate Limit', size=(16,1)), sg.InputText('1', key='AOO-URL')],
                [sg.Text('Atrial Amplitude', size=(16,1)), sg.InputText('1', key='AOO-AA')],
                [sg.Text('Atrial Pulse Width', size=(16,1)), sg.InputText('1', key='AOO-APW')],
                [sg.Button('Submit')] ]

VOO_layout = [  [sg.Text('Pacing Mode - VOO', font=("Helvetica", 20))],
                [sg.Graph((500, 250), (0,0), (500, 250), background_color='white')],
                [sg.Text('Enter Parameters:', font=("Helvetica", 16))],
                [sg.Text('Lower Rate Limit', size=(16,1)), sg.InputText('1', key='VOO-LRL')],
                [sg.Text('Upper Rate Limit', size=(16,1)), sg.InputText('1', key='VOO-URL')],
                [sg.Text('Ventrical Amplitude', size=(16,1)), sg.InputText('1', key='VOO-VA')],
                [sg.Text('Ventrical Pulse Width', size=(16,1)), sg.InputText('1', key='VOO-VPW')],
                [sg.Button('Submit')] ]

AAI_layout = [  [sg.Text('Pacing Mode - AAI', font=("Helvetica", 20))],
                [sg.Graph((500, 250), (0,0), (500, 250), background_color='white')],
                [sg.Text('Enter Parameters:', font=("Helvetica", 16))],
                [sg.Text('Lower Rate Limit', size=(16,1)), sg.InputText('1', key='AAI-LRL')],
                [sg.Text('Upper Rate Limit', size=(16,1)), sg.InputText('1', key='AAI-URL')],
                [sg.Text('Atrial Amplitude', size=(16,1)), sg.InputText('1', key='AAI-AA')],
                [sg.Text('Atrial Pulse Width', size=(16,1)), sg.InputText('1', key='AAI-APW')],
                [sg.Text('Atrial Sensitivity', size=(16,1)), sg.InputText('1', key='AAI-AS')],
                [sg.Text('ARP', size=(16,1)), sg.InputText('1', key='AAI-ARP')],
                [sg.Text('PVARP', size=(16,1)), sg.InputText('1', key='AAI-PVARP')],
                [sg.Text('Hysteresis', size=(16,1)), sg.InputText('1', key='AAI-H')],
                [sg.Text('Rate Smoothing', size=(16,1)), sg.InputText('1', key='AAI-RS')],
                [sg.Button('Submit')] ]

VVI_layout = [  [sg.Text('Pacing Mode - VVI', font=("Helvetica", 20))],
                [sg.Graph((500, 250), (0,0), (500, 250), background_color='white')],
                [sg.Text('Enter Parameters:', font=("Helvetica", 16))],
                [sg.Text('Lower Rate Limit', size=(16,1)), sg.InputText('1', key='VVI-LRL')],
                [sg.Text('Upper Rate Limit', size=(16,1)), sg.InputText('1', key='VVI-URL')],
                [sg.Text('Ventrical Amplitude', size=(16,1)), sg.InputText('1', key='VVI-VA')],
                [sg.Text('Ventrical Pulse Width', size=(16,1)), sg.InputText('1', key='VVI-VPW')],
                [sg.Text('Ventrical Sensitivity', size=(16,1)), sg.InputText('1', key='VVI-VS')],
                [sg.Text('VRP', size=(16,1)), sg.InputText('1', key='VVI-VRP')],
                [sg.Text('Hysteresis', size=(16,1)), sg.InputText('1', key='VVI-H')],
                [sg.Text('Rate Smoothing', size=(16,1)), sg.InputText('1', key='VVI-RS')],
                [sg.Button('Submit')] ]

welcome_column = [
    [sg.Text("Welcome to the Pacemaker DCM")],
]

log_in_column = [
    [
        sg.Text("Please login or register."),
    ],
    [
        sg.Text("Name"), sg.In(size=(25, 1), enable_events=True, key="-name-"),
        sg.Text("Password"), sg.In(size=(25, 1), enable_events=True, key="-password-", password_char='*'),
    ],
    [sg.Button("Login"), sg.Button("Register")],
]

layout = [
    [
        sg.Column(welcome_column),
        sg.VSeperator(),
        sg.Column(log_in_column),
    ]
]

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

# Create the Window
window = sg.Window('Pacemaker DCM', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    if event == "Login":
        if verify(values["-name-"], values["-password-"]):
            window.close()
            layout = [ [sg.TabGroup([[sg.Tab('AOO', AOO_layout), sg.Tab('VOO', VOO_layout), sg.Tab('AAI', AAI_layout), sg.Tab('VVI', VVI_layout)]])] ]
            window = sg.Window('Pacemaker DCM', layout)
        else:
            sg.popup("User doesn't exist. Please register.")

    elif event == "Register":
        if not values["-name-"] and not values["-password-"]:
            sg.popup("Credentials cannot be empty.")
        elif verify(values["-name-"], values["-password-"]):
            sg.popup("User already exists.")
        else:
            register(values["-name-"], values["-password-"])
            sg.popup("User successfully registered.")

window.close()