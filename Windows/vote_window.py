import PySimpleGUI as sg

from Objects.question_info import QuestionInfo


def create_vote_window(question_info: QuestionInfo, current_voter, p_key):
    layout_voting = [
        [sg.Push(), sg.Text(question_info.question, font=("Helvetica", 20)), sg.Push()],
        [sg.Text("(your public key is " + str(p_key) + ")", font=("Helvetica", 14))],
        [sg.Push(), sg.Text(" ", font=("Helvetica", 20)), sg.Push()],
        [sg.Button(question_info.opt1, font=("Helvetica", 18), expand_x=True),
         sg.Text(" ", font=("Helvetica", 18)),
         sg.Button(question_info.opt2, font=("Helvetica", 18), expand_x=True)]
    ]
    window = sg.Window("Voter #" + str(current_voter), layout_voting)
    event, values = window.read()

    if event == question_info.opt1:
        window.close()
        return 1
    elif event == question_info.opt2:
        window.close()
        return 0
    elif event == sg.WIN_CLOSED:
        window.close()
        return -1
