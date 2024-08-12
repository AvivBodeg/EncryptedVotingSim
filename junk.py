# def __generator_finder(self):
#     """Finds a suitable generator that can generate the cyclic group with
#     returns -1 if a generator cannot be found
#     """
#     for i in range(2, self.mod - 1):
#         if math.gcd(i, self.mod - 1) == 1:
#     return -1
#             return i


# def encrypt_single_msg(cyclic_group: CyclicGroup, plaintext, TTP_key):
#     key = Key(cyclic_group)
#     h = pow(TTP_key, key.s_key, mod=cyclic_group.mod)
#     ciphertext = (plaintext * h) % cyclic_group.mod
#     message = CipherMessage(key.p_key, ciphertext)
#     return message
#
#
# def decrypt_single_msg(cyclic_group: CyclicGroup, cipher_message: CipherMessage, s_key):
#     power_canceler = pow(cipher_message.p_key, -s_key, mod=cyclic_group.mod)
#     decrypted_message = (cipher_message.ciphertext * power_canceler) % cyclic_group.mod
#     return decrypted_message
