import encryption_methods
from Windows import dot_product_window, intermission_window, results_window, setup_window, vote_window
from Objects.cyclic_group import CyclicGroup
from Objects.vote_settings import VoteSettings
from Objects.cipher_message import CipherMessage
from Objects.key import Key


def main():
    status, vote_settings = setup_window.create_setup_window()
    if status == -1 or vote_settings is None:
        print("ERROR: someone existed the program")
        exit(1)

    # creates cyclic group
    c_group = CyclicGroup(vote_settings.num_voters)

    TTP_key = Key(c_group)
    encrypted_dot_product = CipherMessage(1, 1)

    for i in range(1, vote_settings.num_voters + 1):
        cur_voter_key = Key(c_group)
        vote = vote_window.create_vote_window(vote_settings.question_information, i, cur_voter_key.p_key)
        if vote is None or vote == -1:
            print("ERROR: someone existed the program")
            exit(2)

        # encryption:
        encrypted_vote = encryption_methods.encrypt(c_group, vote, TTP_key.p_key, cur_voter_key)
        encrypted_dot_product = encryption_methods.multi_vote_encryption(c_group, encrypted_dot_product, encrypted_vote)
        status = intermission_window.create_intermission_window(i, encrypted_vote)


if __name__ == "__main__":
    main()
