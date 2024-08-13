import PySimpleGUI as sg
from Windows import window_intro, window_intermission, window_end, window_voting

sg.theme("DarkBlue14")


def main():
    counter = 0
    vote_settings = window_intro.create_window_intro()
    if vote_settings == -1:
        exit()
    for i in range(1, vote_settings.num_voters):
        vote = window_voting.create_window_voting(vote_settings.question_info, i)
        if vote == -1:
            exit()
        counter += vote
        intermission = window_intermission.create_window_intermission(i, "yes")
        if intermission == -1:
            exit()

    end = window_end.create_window_end(vote_settings.question_info, counter, 0)
    if end == -1:
        exit()


if __name__ == "__main__":
    main()
