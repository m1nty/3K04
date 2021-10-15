import PySimpleGUI as sg
import os.path

sg.theme("DarkAmber")

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

window = sg.Window("DCM", layout)


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


while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    if event == "Login":
        if verify(values["-name-"], values["-password-"]):
            sg.popup("Welcome!")
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
