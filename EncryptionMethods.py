from CyclicGroup import CyclicGroup
from Key import Key
from CipherMessage import CipherMessage


def encrypt(cyclic_group: CyclicGroup, plaintext, TTP_key):
    key = Key(cyclic_group)
    h = pow(TTP_key, key.s_key, mod=cyclic_group.mod)
    ciphertext = (plaintext * h) % cyclic_group.mod
    message = CipherMessage(key.p_key, ciphertext)
    return message


def decrypt(cyclic_group: CyclicGroup, cipher_message: CipherMessage, s_key):
    power_canceler = pow(cipher_message.p_key, -s_key, mod=cyclic_group.mod)
    decrypted_message = (cipher_message.ciphertext * power_canceler) % cyclic_group.mod
    return decrypted_message



def main():
    group = CyclicGroup(1000)
    vote = input("Enter 0 to vote against and 1 to vote for")
    plaintext = pow(group.generator, int(vote), mod=group.mod)
    print("your plaintext is:", plaintext)
    TTP_key = Key(group)
    print("your given key is:", TTP_key.p_key)
    encrypted_message = encrypt(group, plaintext, TTP_key.p_key)
    print("your encrypted message is:", encrypted_message.ciphertext)
    decrypted_message = decrypt(group, encrypted_message, TTP_key.s_key)
    print("your decrypted message is:", decrypted_message)
    if decrypted_message == group.generator:
        print("you voted for!")
    elif decrypted_message == 1:
        print("you voted against")
    else:
        print("invalid or i fucked up")

if __name__ == '__main__':
    main()