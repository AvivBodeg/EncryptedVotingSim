import PySimpleGUI as sg
from Objects.question_info import QuestionInfo


def create_results_window(question_info: QuestionInfo, sum_opt1, sum_opt2):
    winner = question_info.opt1 if sum_opt1 >= sum_opt2 else question_info.opt2
    layout = [
        [sg.Push(), sg.Text(question_info.question, font=("Helvetica", 18)), sg.Push()],
        [sg.Push(), sg.Text(winner + " was chosen", font=("Helvetica", 18)), sg.Push()]
    ]

    window = sg.Window("Project", layout)
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        window.close()
        return -1
