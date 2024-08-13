from Objects.cyclic_group import CyclicGroup
from Objects.key import Key
from Objects.cipher_message import CipherMessage


def multi_vote_encryption(cyclic_group: CyclicGroup, vote, voting_product: CipherMessage, TTP_key: Key):
    current_vote = encrypt(cyclic_group, vote, TTP_key)
    key_product = (voting_product.p_key * current_vote.p_key) % cyclic_group.mod
    message = (voting_product.ciphertext * current_vote.ciphertext) % cyclic_group.mod
    new_voting_product: CipherMessage = CipherMessage(key_product, message)
    return new_voting_product


def encrypt(cyclic_group: CyclicGroup, vote, TTP_key: Key):
    key = Key(cyclic_group)
    h = pow(TTP_key, key.s_key, mod=cyclic_group.mod)
    ciphertext = (pow(cyclic_group.generator, vote) * h) % cyclic_group.mod
    cipher_message: CipherMessage = CipherMessage(key.p_key, ciphertext)
    print("p_key", cipher_message.p_key, "message:", cipher_message.ciphertext)
    return cipher_message


def multi_vote_decryption(cyclic_group: CyclicGroup, voting_product: CipherMessage, s_key, num_voters):
    power_canceler = pow(voting_product.p_key, -s_key, mod=cyclic_group.mod)
    voting_result = (voting_product.ciphertext * power_canceler) % cyclic_group.mod
    return find_voting_result(cyclic_group, num_voters, voting_result)


def find_voting_result(cyclic_group: CyclicGroup, num_voters, result_as_power):
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
#         vote_product = multi_vote_encryption(group, vote, vote_product, TTP_key.p_key)
#         print("p_key product=", vote_product.ciphertext, ", ciphertext product=", vote_product.ciphertext)
#     res = multi_vote_decryption(group, vote_product, TTP_key.s_key, 10)
#     print(res, " people voted for")


if __name__ == "__main__":
    main()
