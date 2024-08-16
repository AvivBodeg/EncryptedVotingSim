# EncryptedVotingSim

EncryptedVotingSim is a simulation of a two-choice online voting system using ElGamal encryption. This project was developed as the final project for the Computer Science Research Colloquium course. The simulation demonstrates the principles of secure voting, ensuring voter privacy and vote integrity using cryptographic techniques.

# ElGamal Encryption

ElGamal encryption is a public-key cryptosystem that provides semantic security. In the context of voting, it allows each vote to be encrypted in such a way that the content of the vote remains confidential, but the total number of votes for each option can still be counted.

The encryption process involves the following steps:


1.	**Key Generation:** A public-private key pair is generated.
2.	**Encryption:** The voter’s choice is encrypted using the public key.
3.	**Decryption:** After the voting process, the votes are decrypted using the private key to reveal the final tally.
