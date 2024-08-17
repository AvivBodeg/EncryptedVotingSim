import encryption_methods
from Objects.cyclic_group import CyclicGroup
from Objects.cipher_message import CipherMessage
from Objects.key import Key
import os
from datetime import datetime


def create_file_name():
    current_time = datetime.now()
    formatted_time = current_time.strftime("results_%Y-%m-%d_T%H%M%S")
    f_name = formatted_time + ".txt"
    if os.path.exists(f_name):
        os.remove(f_name)
    return f_name


def automatic_voting():
    num_voters = int(input("How many voters"))
    c_group = CyclicGroup(num_voters)
    f_name = create_file_name()
    # create file and add header
    f = open(f_name, "x")
    f.write("Amount of voters: " + str(num_voters) + "\n")
    f.write("version 1.0\n")
    f.close()


automatic_voting()
