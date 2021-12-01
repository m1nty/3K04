# Imports
import PySimpleGUI as sg


# Set theme of GUI
sg.theme('Dark')

#method so that the pacemaker screens can access data
def make_parameters(data):
    AOO_layout = [  [sg.Text('Pacing Mode - AOO', font=("Helvetica", 20))],
                    [sg.Text('Enter Parameters:', font=("Helvetica", 16))],
                    [sg.Text('Lower Rate Limit', size=(16,1)), sg.InputText(data[0], key='AOO-LRL')],
                    [sg.Text('Upper Rate Limit', size=(16,1)), sg.InputText(data[1], key='AOO-URL')],
                    [sg.Text('Atrial Amplitude', size=(16,1)), sg.InputText(data[2], key='AOO-AA')],
                    [sg.Text('Atrial Pulse Width', size=(16,1)), sg.InputText(data[3], key='AOO-APW')],
                    [sg.Button('Submit', key='SUB-AOO')] ]

    VOO_layout = [  [sg.Text('Pacing Mode - VOO', font=("Helvetica", 20))],
                    [sg.Text('Enter Parameters:', font=("Helvetica", 16))],
                    [sg.Text('Lower Rate Limit', size=(16,1)), sg.InputText(data[4], key='VOO-LRL')],
                    [sg.Text('Upper Rate Limit', size=(16,1)), sg.InputText(data[5], key='VOO-URL')],
                    [sg.Text('Ventrical Amplitude', size=(16,1)), sg.InputText(data[6], key='VOO-VA')],
                    [sg.Text('Ventrical Pulse Width', size=(16,1)), sg.InputText(data[7], key='VOO-VPW')],
                    [sg.Button('Submit', key='SUB-VOO')] ]

    AAI_layout = [  [sg.Text('Pacing Mode - AAI', font=("Helvetica", 20))],
                    [sg.Text('Enter Parameters:', font=("Helvetica", 16))],
                    [sg.Text('Lower Rate Limit', size=(16,1)), sg.InputText(data[8], key='AAI-LRL')],
                    [sg.Text('Upper Rate Limit', size=(16,1)), sg.InputText(data[9], key='AAI-URL')],
                    [sg.Text('Atrial Amplitude', size=(16,1)), sg.InputText(data[10], key='AAI-AA')],
                    [sg.Text('Atrial Pulse Width', size=(16,1)), sg.InputText(data[11], key='AAI-APW')],
                    [sg.Text('ARP', size=(16,1)), sg.InputText(data[12], key='AAI-ARP')],
                    [sg.Button('Submit', key='SUB-AAI')] ]

    VVI_layout = [  [sg.Text('Pacing Mode - VVI', font=("Helvetica", 20))],
                    [sg.Text('Enter Parameters:', font=("Helvetica", 16))],
                    [sg.Text('Lower Rate Limit', size=(16,1)), sg.InputText(data[13], key='VVI-LRL')],
                    [sg.Text('Upper Rate Limit', size=(16,1)), sg.InputText(data[14], key='VVI-URL')],
                    [sg.Text('Ventrical Amplitude', size=(16,1)), sg.InputText(data[15], key='VVI-VA')],
                    [sg.Text('Ventrical Pulse Width', size=(16,1)), sg.InputText(data[16], key='VVI-VPW')],
                    [sg.Text('VRP', size=(16,1)), sg.InputText(data[17], key='VVI-VRP')],
                    [sg.Button('Submit', key='SUB-VVI')] ]

    DOO_layout = [  [sg.Text('Pacing Mode - DOO', font=("Helvetica", 20))],
                    [sg.Text('Enter Parameters:', font=("Helvetica", 16))],
                    [sg.Text('Lower Rate Limit', size=(16,1)), sg.InputText(data[18], key='DOO-LRL')],
                    [sg.Text('Upper Rate Limit', size=(16,1)), sg.InputText(data[19], key='DOO-URL')],
                    [sg.Text('Fixed AV Delay', size=(16,1)), sg.InputText(data[20], key='DOO-FAD')],
                    [sg.Text('Ventrical Amplitude', size=(16,1)), sg.InputText(data[21], key='DOO-VA')],
                    [sg.Text('Ventrical Pulse Width', size=(16,1)), sg.InputText(data[22], key='DOO-VPW')],
                    [sg.Text('Atrial Amplitude', size=(16,1)), sg.InputText(data[23], key='DOO-AA')],
                    [sg.Text('Atrial Pulse Width', size=(16,1)), sg.InputText(data[24], key='DOO-APW')],
                    [sg.Button('Submit', key='SUB-DOO')] ]

    AOOR_layout = [  [sg.Text('Pacing Mode - AOOR', font=("Helvetica", 20))],
                     [sg.Text('Enter Parameters:', font=("Helvetica", 16))],
                     [sg.Text('Lower Rate Limit', size=(16,1)), sg.InputText(data[25], key='AOOR-LRL')],
                     [sg.Text('Upper Rate Limit', size=(16,1)), sg.InputText(data[26], key='AOOR-URL')],
                     [sg.Text('Maximum Sensor Rate', size=(16,1)), sg.InputText(data[27], key='AOOR-MSR')],
                     [sg.Text('Atrial Amplitude', size=(16,1)), sg.InputText(data[28], key='AOOR-AA')],
                     [sg.Text('Atrial Pulse Width', size=(16,1)), sg.InputText(data[29], key='AOOR-APW')],
                     [sg.Text('Activity Threshold', size=(16,1)), sg.InputText(data[30], key='AOOR-AT')],
                     [sg.Text('Reaction Time', size=(16,1)), sg.InputText(data[31], key='AOOR-REAT')],
                     [sg.Text('Response Factor', size=(16,1)), sg.InputText(data[32], key='AOOR-RF')],
                     [sg.Text('Recovery Time', size=(16,1)), sg.InputText(data[33], key='AOOR-RT')],
                     [sg.Button('Submit', key='SUB-AOOR')] ]

    VOOR_layout = [  [sg.Text('Pacing Mode - VOOR', font=("Helvetica", 20))],
                     [sg.Text('Enter Parameters:', font=("Helvetica", 16))],
                     [sg.Text('Lower Rate Limit', size=(16,1)), sg.InputText(data[34], key='VOOR-LRL')],
                     [sg.Text('Upper Rate Limit', size=(16,1)), sg.InputText(data[35], key='VOOR-URL')],
                     [sg.Text('Maximum Sensor Rate', size=(16,1)), sg.InputText(data[36], key='VOOR-MSR')],
                     [sg.Text('Ventrical Amplitude', size=(16,1)), sg.InputText(data[37], key='VOOR-VA')],
                     [sg.Text('Ventrical Pulse Width', size=(16,1)), sg.InputText(data[38], key='VOOR-VPW')],
                     [sg.Text('Activity Threshold', size=(16,1)), sg.InputText(data[39], key='VOOR-AT')],
                     [sg.Text('Reaction Time', size=(16,1)), sg.InputText(data[40], key='VOOR-REAT')],
                     [sg.Text('Response Factor', size=(16,1)), sg.InputText(data[41], key='VOOR-RF')],
                     [sg.Text('Recovery Time', size=(16,1)), sg.InputText(data[42], key='VOOR-RT')],
                     [sg.Button('Submit', key='SUB-VOOR')] ]

    AAIR_layout = [  [sg.Text('Pacing Mode - AAIR', font=("Helvetica", 20))],
                     [sg.Text('Enter Parameters:', font=("Helvetica", 16))],
                     [sg.Text('Lower Rate Limit', size=(16,1)), sg.InputText(data[43], key='AAIR-LRL')],
                     [sg.Text('Upper Rate Limit', size=(16,1)), sg.InputText(data[44], key='AAIR-URL')],
                     [sg.Text('Maximum Sensor Rate', size=(16,1)), sg.InputText(data[45], key='AAIR-MSR')],
                     [sg.Text('Atrial Amplitude', size=(16,1)), sg.InputText(data[46], key='AAIR-AA')],
                     [sg.Text('Atrial Pulse Width', size=(16,1)), sg.InputText(data[47], key='AAIR-APW')],
                     [sg.Text('ARP', size=(16,1)), sg.InputText(data[48], key='AAIR-ARP')],
                     [sg.Text('Activity Threshold', size=(16,1)), sg.InputText(data[49], key='AAIR-AT')],
                     [sg.Text('Reaction Time', size=(16,1)), sg.InputText(data[50], key='AAIR-REAT')],
                     [sg.Text('Response Factor', size=(16,1)), sg.InputText(data[51], key='AAIR-RF')],
                     [sg.Text('Recovery Time', size=(16,1)), sg.InputText(data[52], key='AAIR-RT')],
                     [sg.Button('Submit', key='SUB-AAIR')] ]

    VVIR_layout = [  [sg.Text('Pacing Mode - VVIR', font=("Helvetica", 20))],
                     [sg.Text('Enter Parameters:', font=("Helvetica", 16))],
                     [sg.Text('Lower Rate Limit', size=(16,1)), sg.InputText(data[53], key='VVIR-LRL')],
                     [sg.Text('Upper Rate Limit', size=(16,1)), sg.InputText(data[54], key='VVIR-URL')],
                     [sg.Text('Maximum Sensor Rate', size=(16,1)), sg.InputText(data[55], key='VVIR-MSR')],
                     [sg.Text('Ventrical Amplitude', size=(16,1)), sg.InputText(data[56], key='VVIR-VA')],
                     [sg.Text('Ventrical Pulse Width', size=(16,1)), sg.InputText(data[57], key='VVIR-VPW')],
                     [sg.Text('VRP', size=(16,1)), sg.InputText(data[58], key='VVIR-VRP')],
                     [sg.Text('Activity Threshold', size=(16,1)), sg.InputText(data[59], key='VVIR-AT')],
                     [sg.Text('Reaction Time', size=(16,1)), sg.InputText(data[60], key='VVIR-REAT')],
                     [sg.Text('Response Factor', size=(16,1)), sg.InputText(data[61], key='VVIR-RF')],
                     [sg.Text('Recovery Time', size=(16,1)), sg.InputText(data[62], key='VVIR-RT')],
                     [sg.Button('Submit', key='SUB-VVIR')] ]

    DOOR_layout = [  [sg.Text('Pacing Mode - DOOR', font=("Helvetica", 20))],
                     [sg.Text('Enter Parameters:', font=("Helvetica", 16))],
                     [sg.Text('Lower Rate Limit', size=(16,1)), sg.InputText(data[63], key='DOOR-LRL')],
                     [sg.Text('Upper Rate Limit', size=(16,1)), sg.InputText(data[64], key='DOOR-URL')],
                     [sg.Text('Maximum Sensor Rate', size=(16,1)), sg.InputText(data[65], key='DOOR-MSR')],
                     [sg.Text('Fixed AV Delay', size=(16,1)), sg.InputText(data[66], key='DOOR-FAD')],
                     [sg.Text('Atrial Amplitude', size=(16,1)), sg.InputText(data[67], key='DOOR-AA')],
                     [sg.Text('Atrial Pulse Width', size=(16,1)), sg.InputText(data[68], key='DOOR-APW')],
                     [sg.Text('Ventrical Amplitude', size=(16,1)), sg.InputText(data[69], key='DOOR-VA')],
                     [sg.Text('Ventrical Pulse Width', size=(16,1)), sg.InputText(data[70], key='DOOR-VPW')],
                     [sg.Text('Activity Threshold', size=(16,1)), sg.InputText(data[71], key='DOOR-AT')],
                     [sg.Text('Reaction Time', size=(16,1)), sg.InputText(data[72], key='DOOR-REAT')],
                     [sg.Text('Response Factor', size=(16,1)), sg.InputText(data[73], key='DOOR-RF')],
                     [sg.Text('Recovery Time', size=(16,1)), sg.InputText(data[74], key='DOOR-RT')],
                     [sg.Button('Submit', key='SUB-DOOR')] ]

    pacing_layout = [ 
        [
            sg.TabGroup
            (
                [
                    [
                        sg.Tab('AOO', AOO_layout),
                        sg.Tab('VOO', VOO_layout),
                        sg.Tab('AAI', AAI_layout), 
                        sg.Tab('VVI', VVI_layout),
                        sg.Tab('DOO', DOO_layout),
                        sg.Tab('AOOR', AOOR_layout),
                        sg.Tab('VOOR', VOOR_layout),
                        sg.Tab('AAIR', AAIR_layout),
                        sg.Tab('VVIR', VVIR_layout),
                        sg.Tab('DOOR', DOOR_layout)
                    ]
                ]
            )
        ]
    ]
    return pacing_layout

def make_post_submit_layout():
    post_submit_layout = [
        [sg.Button('View Atrial E-GRAM data', key='DISPLAY-A-EGRAM')],
        [sg.Button('View Ventrical E-GRAM data', key='DISPLAY-V-EGRAM')],
        [sg.Button('View Atrial & Ventrical E-GRAM data', key='DISPLAY-BOTH-EGRAM')],
        [sg.Button('Verify Parameters', key='VERIFY-PARAM-BUTTON')],
        [sg.Button('Stop Pacing', key='STOP-PACING-BUTTON')]
    ] 

    return sg.Window('Pacemaker DCM', post_submit_layout)

def make_v_egram_layout():
    v_egram_layout = [
        [sg.Graph((800, 255), (0, -6), (800, 6), background_color='white', key="V-GRAPH")],
    ] 

    return sg.Window('Ventrical E-GRAM', v_egram_layout)

def make_a_egram_layout():
    a_egram_layout = [
        [sg.Graph((800, 255), (0, -6), (800, 6), background_color='white', key="A-GRAPH")],
    ] 

    return sg.Window('Atrial E-GRAM', a_egram_layout)

def make_a_v_egram_layout():
    a_v_egram_layout = [
        [sg.Text("Atrial", font=("Helvetica", 20))],
        [sg.Graph((800, 255), (0, 124), (800, 136), background_color='white', key="A-GRAPH")],
        [sg.Text("Ventrical", font=("Helvetica", 20))],
        [sg.Graph((800, 255), (0, -6), (800, 6), background_color='white', key="V-GRAPH")]
    ] 

    return sg.Window('Atrial & Ventrical E-GRAM', a_v_egram_layout)

# Set up the columns for the welcome/login screen
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

# Setup the layout for the welcome/login screen 
landing_layout = [
    [
        sg.Column(welcome_column),
        sg.VSeperator(),
        sg.Column(log_in_column),
    ]
]

