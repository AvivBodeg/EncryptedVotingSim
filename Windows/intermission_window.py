import PySimpleGUI as sg


def create_intermission_window(current_voter, ciphertext):
    layout = [
        [sg.Push(), sg.Text("Encrypted vote: " + ciphertext), sg.Push()],
        [sg.Push(), sg.Button("Next"), sg.Push()]
    ]

    window = sg.Window("Voter #" + str(current_voter), layout)
    event, values = window.read()

    if event == "Next":
        window.close()
        return 0
    elif event == sg.WIN_CLOSED:
        window.close()
        return -1
