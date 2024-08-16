import PySimpleGUI as sg
from Objects.cipher_message import CipherMessage


def create_dot_product_window(dot_product_message: CipherMessage):
    layout = [
        [sg.Push(), sg.Text("The dot product of public keys is " + str(dot_product_message.p_key),
                            font=("Helvetica", 18)), sg.Push()],
        [sg.Push(), sg.Text("The dot product of the votes is " + str(dot_product_message.ciphertext),
                            font=("Helvetica", 18)), sg.Push()],
        [sg.Text("")],
        [sg.Text("")],
        [sg.Push(), sg.Button("Ok", font=("Helvetica", 18)), sg.Push()]
    ]
    window = sg.Window("Encrypted Dot Product", layout)
    event, values = window.read()

    if event == "Ok":
        window.close()
        return 0
    elif event == sg.WIN_CLOSED:
        window.close()
        return -1


c = CipherMessage(12112, 1217821)
create_dot_product_window(c)
