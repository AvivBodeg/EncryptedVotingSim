import PySimpleGUI as sg
from Objects.question_info import QuestionInfo


def create_results_window(question_info: QuestionInfo, opt1_votes, opt2_votes):
    if opt1_votes == opt2_votes:
        return create_tie_window(question_info, opt1_votes, opt2_votes)
    else:
        return create_winner_window(question_info, opt1_votes, opt2_votes)


def create_winner_window(question_info: QuestionInfo, opt1_votes, opt2_votes):
    winning_opt = question_info.opt1 if opt1_votes >= opt2_votes else question_info.opt2
    layout = [
        [sg.Push(), sg.Text(question_info.question, font=("Helvetica", 18)), sg.Push()],
        [sg.Push(), sg.Text(str(opt1_votes) + " people voted for " + question_info.opt1, font=("Helvetica", 18)),
         sg.Push()],
        [sg.Push(), sg.Text(str(opt2_votes) + " people voted for " + question_info.opt2, font=("Helvetica", 18)),
         sg.Push()],
        [sg.Push(), sg.Text(" ")],
        [sg.Push(), sg.Text("The people chose " + winning_opt + "!", font=("Helvetica", 22), text_color="yellow"), sg.Push()],
        [sg.Push(), sg.Button("Done", font=("Helvetica", 18)), sg.Push()]
    ]
    window = sg.Window("Results", layout)
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Done":
        window.close()
        return 0


def create_tie_window(question_info: QuestionInfo, opt1_votes, opt2_votes):
    layout = [
        [sg.Push(), sg.Text(question_info.question, font=("Helvetica", 18)), sg.Push()],
        [sg.Push(), sg.Text(str(opt1_votes) + " people voted for " + question_info.opt1, font=("Helvetica", 18)),
         sg.Push()],
        [sg.Push(), sg.Text(str(opt2_votes) + " people voted for " + question_info.opt2, font=("Helvetica", 18)),
         sg.Push()],
        [sg.Push(), sg.Text(" ")],
        [sg.Push(), sg.Text("It's a tie!", font=("Helvetica", 22), text_color="yellow"), sg.Push()],
        [sg.Push(), sg.Button("Done", font=("Helvetica", 18)), sg.Push()]
    ]
    window = sg.Window("Results", layout)
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Done":
        window.close()
        return 0
