import PySimpleGUI as sg
from Objects.VoteSettings import VoteSettings


def create_window_intro():
    width, height = sg.Window.get_screen_size()
    layout_intro = [
        [sg.Push(), sg.Text("Enter question: "), sg.Push()],
        [sg.Push(), sg.InputText(size=(40, 1), k="-QUESTION-"), sg.Push()],
        [sg.Push(), sg.InputText(size=(15, 1), k="-OPTION_1-", default_text="Option 1"),
         sg.InputText(size=(15, 1), k="-OPTION_2-", default_text="Option 2"), sg.Push()],
        [sg.VPush()],
        [sg.vbottom(sg.Text("Num. of voters: ", size=(13, 1))),
         sg.Slider((1, 100), 5, orientation="h", k="-NUM_VOTERS-")],
        [sg.VPush()],
        [sg.Push(), sg.Button("OK"), sg.Push()],
        [sg.Push(), sg.Checkbox("Auto mode?", k="-AUTO-")]
    ]

    window = sg.Window("Project", layout_intro, size=(int(width*0.5), int(height*0.5)))

    event, values = window.read()
    if event == sg.WIN_CLOSED:
        window.close()
        return -1
    elif event == "OK":
        question = values["-QUESTION-"] if values["-QUESTION-"] != "" else "Question?"
        num_voters = int(values["-NUM_VOTERS-"])
        auto = values["-AUTO-"]
        option1 = values["-OPTION_1-"] if values["-OPTION_1-"] != "" else "Option 1"
        option2 = values["-OPTION_2-"] if values["-OPTION_2-"] != "" else "Option 2"

        window.close()
        return VoteSettings(question, option1, option2, num_voters)
