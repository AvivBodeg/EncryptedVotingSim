import PySimpleGUI as sg
from Windows import vote_window, intermission_window, results_window, setup_window

sg.theme("DarkBlue14")


def main():
    counter = 0
    vote_settings = setup_window.create_setup_window()
    if vote_settings == -1:
        exit()
    for i in range(1, vote_settings.num_voters):
        vote = vote_window.create_vote_window(vote_settings.question_information, i)
        if vote == -1:
            exit()
        counter += vote
        intermission = intermission_window.create_intermission_window(i, "yes")
        if intermission == -1:
            exit()

    end = results_window.create_results_window(vote_settings.question_information, counter, 0)
    if end == -1:
        exit()


if __name__ == "__main__":
    main()
