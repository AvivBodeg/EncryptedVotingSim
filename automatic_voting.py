import encryption_methods
from Objects.cyclic_group import CyclicGroup
from Objects.cipher_message import CipherMessage
from Objects.key import Key
import random
import os
from datetime import datetime


def create_file_name():
    current_time = datetime.now()
    formatted_time = current_time.strftime("results_%Y-%m-%d_T%H%M%S")
    f_name = formatted_time + ".txt"
    if os.path.exists(f_name):
        os.remove(f_name)
    return f_name


def input_vote_amounts():
    num_voters = input("How many voters")
    while not num_voters.isdigit() or int(num_voters) < 1:
        num_voters = input("enter a valid number (positive int)")
    num_voters = int(num_voters)
    opt1_votes = input("How many votes for opt1?")
    while not opt1_votes.isdigit() or int(opt1_votes) > num_voters:
        opt1_votes = input(f"enter a valid number (int between 1 and {num_voters})")

    opt1_votes = int(opt1_votes)
    return num_voters, opt1_votes


def voting(c_group: CyclicGroup, num_voters: int, opt1_votes: int, f_name, TTP_key):
    f = open(f_name, "a")
    encrypted_dot_product = CipherMessage(1, 1)

    # generate a shuffled list of 1s and 0s (with opt1_votes 1s)
    votes = [1] * opt1_votes + [0] * (num_voters - opt1_votes)
    random.shuffle(votes)

    # write votes
    for i in range(0, num_voters):
        cur_key = Key(c_group)
        vote = votes[i]
        # encryption
        e_vote = encryption_methods.encrypt(c_group, vote, TTP_key, cur_key)
        f.write(f"vote={vote}   p_key={e_vote.p_key}    encrypted_message={e_vote.ciphertext}\n")
        encrypted_dot_product = encryption_methods.multi_vote_encryption(c_group, encrypted_dot_product, e_vote)

    f.close()
    return encrypted_dot_product


def automatic_voting():
    num_voters, opt1_votes = input_vote_amounts()
    c_group = CyclicGroup(num_voters)

    f_name = create_file_name()
    # create file and add header
    print(f"creating file named {f_name}")
    f = open(f_name, "x")
    f.write("Amount of voters: " + str(num_voters) + "\n")
    f.write("version 1.0\n")
    f.close()

    # encryption
    TTP_key = Key(c_group)
    encrypted_dot_product = voting(c_group, num_voters, opt1_votes, f_name, TTP_key.p_key)

    # decryption
    actual_opt1_votes = encryption_methods.multi_vote_decryption(c_group, encrypted_dot_product, TTP_key.s_key,
                                                                 num_voters)

    f = open(f_name, "a")
    f.write(f"encrypted dot product= ({encrypted_dot_product.p_key},{encrypted_dot_product.ciphertext})\n")
    f.write(f"votes for opt1: {actual_opt1_votes}, expected votes for opt1: {opt1_votes}\n")


automatic_voting()
