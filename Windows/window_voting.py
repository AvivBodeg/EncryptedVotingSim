import PySimpleGUI as sg

from Objects.QuestionInfo import QuestionInfo


def create_window_voting(question_info: QuestionInfo, current_voter):
    layout_voting = [
        [sg.Push(), sg.Text(question_info.question), sg.Push()],
        [sg.Push(), sg.Button(question_info.opt1), sg.Button(question_info.opt2), sg.Push()]
    ]
    window_voting = sg.Window("Voter " + str(current_voter), layout_voting)
    event, values = window_voting.read()

    if event == question_info.opt1:
        window_voting.close()
        return 1
    elif event == question_info.opt2:
        window_voting.close()
        return 0
    elif event == sg.WIN_CLOSED:
        window_voting.close()
        return -1
