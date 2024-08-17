# EncryptedVotingSim

EncryptedVotingSim is a simulation of a two-choice online voting system using ElGamal encryption. This project was developed as the final project for the Computer Science Research Colloquium course. The simulation demonstrates the principles of secure voting, ensuring voter privacy and vote integrity using cryptographic techniques.


## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)
- [ElGamal Encryption](#elgamal-encryption)


## Introduction

In the digital age, ensuring the integrity and privacy of votes in an online voting system is a critical challenge. EncryptedVotingSim addresses this challenge by simulating a voting system where each vote is securely encrypted using the ElGamal encryption algorithm. This ensures that votes remain confidential while allowing the tallying of votes without revealing individual choices.


## Features

•	Secure Voting: Utilizes ElGamal encryption to ensure that votes are confidential.

•	Two-Choice Voting: Simulates a voting system where voters can choose between two options.

•	End-to-End Encryption: Demonstrates the complete process from encryption to decryption.

•	Automatic mode: Simulates a large amount of votes with minimal input (total amount of votes and how many voted for one of the options).

•	Python Implementation: The project is implemented entirely in Python, making it easy to understand.


## Usage

•	For manual voting run the `main.py` file

•	For an automatic simulation run the `automatic_vote.py` file


## ElGamal Encryption

ElGamal encryption is a public-key cryptosystem that provides semantic security. In the context of voting, it allows each vote to be encrypted in such a way that the content of the vote remains confidential, but the total number of votes for each option can still be counted.

The encryption process involves the following steps:


1.	**Key Generation:** A public-private key pair is generated.
2.	**Encryption:** The voter’s choice is encrypted using the public key.
3.	**Decryption:** After the voting process, the votes are decrypted using the private key to reveal the final tally.

```
EncryptedVotingSim/
├── README.md
├── .gitignore
├── requirements.txt
├── setup.py
├── src/
│   ├── init.py
│   ├── main.py
│   ├── encryption.py
│   └── voting.py
├── tests/
│   ├── init.py
│   └── test_voting.py
└── docs/
└── design.md
```
