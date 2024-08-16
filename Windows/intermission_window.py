import PySimpleGUI as sg
from Objects.cipher_message import CipherMessage


def create_intermission_window(current_voter, cipher_message: CipherMessage):
    layout = [
        [sg.Push(), sg.Text("Public Key: " + str(cipher_message.p_key), font=("Helvetica", 18)), sg.Push()],
        [sg.Push(), sg.Text("Encrypted vote: " + str(cipher_message.ciphertext), font=("Helvetica", 18)), sg.Push()],
        [sg.Push(), sg.Text(" ", font=40), sg.Push()],
        [sg.Push(), sg.Button("Next", expand_x=True, font=("Helvetica", 18)), sg.Push()]
    ]

    window = sg.Window("Voter #" + str(current_voter), layout)
    event, values = window.read()

    if event == "Next":
        window.close()
        return 0
    elif event == sg.WIN_CLOSED:
        window.close()
        return -1
