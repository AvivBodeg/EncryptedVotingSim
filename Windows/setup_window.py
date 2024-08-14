import PySimpleGUI as sg

from Objects.vote_settings import VoteSettings


def create_setup_window():
    layout_intro = [
        [sg.Push(), sg.Text("Enter question: ", font=("Helvetica", 18)), sg.Push()],
        [sg.Push(), sg.Multiline(k="-QUESTION-", font=("Helvetica", 18), size=(35, 3), no_scrollbar=True), sg.Push()],
        [sg.Push(), sg.InputText(k="-OPTION_1-", default_text="Option 1", font=("Helvetica", 18), size=(15, 1)),
         sg.InputText(k="-OPTION_2-", default_text="Option 2", font=("Helvetica", 18), size=(15, 1)), sg.Push()],
        [sg.VPush()],
        [sg.vbottom(sg.Text("Num. of voters: ", size=(13, 1))),
         sg.Slider((1, 100), 5, orientation="h", k="-NUM_VOTERS-")],
        [sg.VPush()],
        [sg.Push(), sg.Button("START", font=("Helvetica", 18), expand_x=True), sg.Push()],
        # [sg.Push(), sg.Checkbox("Auto mode?", k="-AUTO-")]
    ]

    window = sg.Window("Project", layout_intro)

    event, values = window.read()
    if event == sg.WIN_CLOSED:
        window.close()
        return -1
    elif event == "START":
        question = values["-QUESTION-"] if values["-QUESTION-"] != "" else "Question?"
        num_voters = int(values["-NUM_VOTERS-"])
        # auto = values["-AUTO-"]
        option1 = values["-OPTION_1-"] if values["-OPTION_1-"] != "" else "Option 1"
        option2 = values["-OPTION_2-"] if values["-OPTION_2-"] != "" else "Option 2"

        window.close()
        return VoteSettings(question, option1, option2, num_voters)


create_setup_window()