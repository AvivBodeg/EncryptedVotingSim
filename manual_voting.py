import encryption_methods
from Windows import dot_product_window, intermission_window, results_window, setup_window, vote_window
from Objects.cyclic_group import CyclicGroup
from Objects.vote_settings import VoteSettings
from Objects.cipher_message import CipherMessage
from Objects.key import Key


def manual_voting():
    status, vote_settings = setup_window.create_setup_window()
    if status == -1 or vote_settings is None:
        exit("Error: someone existed the program during setup_window")

    # creates cyclic group
    c_group = CyclicGroup(vote_settings.num_voters)

    TTP_key = Key(c_group)
    encrypted_dot_product = CipherMessage(1, 1)

    # Voting:
    for i in range(1, vote_settings.num_voters + 1):
        cur_voter_key = Key(c_group)
        vote = vote_window.create_vote_window(vote_settings.question_information, i, cur_voter_key.p_key)
        if vote is None or vote == -1:
            exit("Error: someone existed the program during vote_window")

        # encryption:
        encrypted_vote = encryption_methods.encrypt(c_group, vote, TTP_key.p_key, cur_voter_key)
        encrypted_dot_product = encryption_methods.multi_vote_encryption(c_group, encrypted_dot_product, encrypted_vote)

        status = intermission_window.create_intermission_window(i, encrypted_vote)
        if status == -1:
            exit("Error: someone existed the program during intermission_window")

    status = dot_product_window.create_dot_product_window(encrypted_dot_product)
    if status == -1:
        exit("Error: someone existed the program during dot_product_window")

    # decryption
    opt1_votes = encryption_methods.multi_vote_decryption(c_group, encrypted_dot_product, TTP_key.s_key,
                                                          vote_settings.num_voters)
    if opt1_votes == -1 or opt1_votes > vote_settings.num_voters:
        exit("Error: decryption failed")

    opt2_votes = vote_settings.num_voters - opt1_votes

    results_window.create_results_window(vote_settings.question_information, opt1_votes, opt2_votes)


manual_voting()
