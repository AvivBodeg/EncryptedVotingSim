from Objects.cyclic_group import CyclicGroup
from Objects.key import Key
from Objects.cipher_message import CipherMessage


def multi_vote_encryption(cyclic_group: CyclicGroup, encrypted_voting_product: CipherMessage,
                          encrypted_vote: CipherMessage):
    """ Gets the current vote and encrypts it into the given voting product using ElGamal encryption method and dot
    product"""
    key_product = (encrypted_voting_product.p_key * encrypted_vote.p_key) % cyclic_group.mod
    message = (encrypted_voting_product.ciphertext * encrypted_vote.ciphertext) % cyclic_group.mod
    new_voting_product: CipherMessage = CipherMessage(key_product, message)
    return new_voting_product


def encrypt(cyclic_group: CyclicGroup, vote, TTP_key: Key, self_key: Key):
    """ Encrypts the vote as a power of cyclic_group.generator using ElGamal encryption method"""
    key = self_key  # Key(cyclic_group)
    h = pow(TTP_key, key.s_key, mod=cyclic_group.mod)
    ciphertext = (pow(cyclic_group.generator, vote) * h) % cyclic_group.mod
    cipher_message: CipherMessage = CipherMessage(key.p_key, ciphertext)
    return cipher_message


def multi_vote_decryption(cyclic_group: CyclicGroup, voting_product: CipherMessage, s_key, num_voters):
    """ Decrypts the dot product using ElGamal encryption method and the properties of multiplications of powers"""
    power_canceler = pow(voting_product.p_key, -s_key, mod=cyclic_group.mod)
    voting_result = (voting_product.ciphertext * power_canceler) % cyclic_group.mod
    return find_voting_result(cyclic_group, num_voters, voting_result)


def find_voting_result(cyclic_group: CyclicGroup, num_voters, result_as_power):
    """ Finds the power (between 0 and num_voters) of cyclic_group.generator that gives result_as_power,
    that value is the amount of people who voted for opt1"""
    for i in range(num_voters + 1):
        if pow(cyclic_group.generator, i, mod=cyclic_group.mod) == result_as_power:
            return i
    return -1


# def main():
#     group = CyclicGroup(10)
#     TTP_key = Key(group)
#     st_vote = "1110111101"
#     vote_product: CipherMessage = CipherMessage(1, 1)
#     for i in range(10):
#         vote = int(st_vote[i])
#         self_key = Key(group)
#         e_vote = encrypt(group, vote, TTP_key.p_key, self_key)
#         vote_product = multi_vote_encryption(group, vote_product, e_vote)
#         print("p_key product=", vote_product.ciphertext, ", ciphertext product=", vote_product.ciphertext)
#     res = multi_vote_decryption(group, vote_product, TTP_key.s_key, 10)
#     print(res, " people voted for")
#
#
# if __name__ == "__main__":
#     main()