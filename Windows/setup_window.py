import PySimpleGUI as sg

from Objects.vote_settings import VoteSettings


def create_setup_window():
    layout_intro = [
        [sg.Push(), sg.Text("Enter question: ", font=("Helvetica", 18)), sg.Push()],
        [sg.Push(), sg.Multiline(k="-QUESTION-", font=("Helvetica", 18), size=(35, 3), no_scrollbar=True), sg.Push()],
        [sg.Text("Option 1:", font=("Helvetica", 18)),
         sg.InputText(k="-OPTION_1-", font=("Helvetica", 18), size=(18, 1)), sg.Push()],
        [sg.Text("Option 2:", font=("Helvetica", 18)),
         sg.InputText(k="-OPTION_2-", font=("Helvetica", 18), size=(18, 1)), sg.Push()],
        [sg.Text("Number of Voters: ", font=("Helvetica", 18)),
         sg.Input(key='-NUM_VOTERS-', font=("Helvetica", 20), enable_events=True, size=(10, 1))],
        [sg.Push(), sg.Button("START", font=("Helvetica", 18), expand_x=True), sg.Push()]
        # [sg.Push(), sg.Checkbox("Auto mode?", k="-AUTO-")]
    ]

    window = sg.Window("Project", layout_intro)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            window.close()
            return -1

        if event == '-NUM_VOTERS-':
            input_value = values['-NUM_VOTERS-']

            # Allow only integer input: digits and a leading negative sign
            if input_value and not (
                    input_value.isdigit() or (input_value.startswith('-') and input_value[1:].isdigit())):
                # If the input is not a valid integer, revert to the previous value
                window['-NUM_VOTERS-'].update(input_value[:-1])

        elif event == "START" and values['-NUM_VOTERS-'] != "":
            question = values["-QUESTION-"] if values["-QUESTION-"] != "" else "Question?"
            num_voters = int(values["-NUM_VOTERS-"])
            option1 = values["-OPTION_1-"] if values["-OPTION_1-"] != "" else "Option 1"
            option2 = values["-OPTION_2-"] if values["-OPTION_2-"] != "" else "Option 2"
            # auto = values["-AUTO-"]
            window.close()
            return VoteSettings(question, option1, option2, num_voters)
