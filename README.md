Affine Cipher Tool

This Python script implements an Affine Cipher, a type of substitution cipher that uses a mathematical function to encrypt and decrypt text. The script also includes a brute-force method to decode ciphertext when the keys are unknown.
Features

    Encryption: Converts plain text into ciphertext using the Affine Cipher.
    Decryption: Converts ciphertext back into plain text using known keys.
    Brute Force Attack: Attempts to decode ciphertext by trying all possible key combinations.

How It Works

The Affine Cipher works by transforming each letter in the plaintext using the formula:

scss

E(x) = (a * x + b) mod 26

Where:

    x is the position of the letter in the alphabet.
    a and b are keys.
    26 is the number of letters in the English alphabet.

For decryption, the formula used is:

scss

D(x) = a^-1 * (x - b) mod 26

Where a^-1 is the modular inverse of a mod 26.
Script Overview

    alphabet: A list containing the letters of the English alphabet repeated twice to handle wrap-around during encryption.
    encrypt(plain, a, b): Encrypts the plaintext using the provided a and b keys.
    decrypt(cipher, a, b): Decrypts the ciphertext using the provided a and b keys.
    brute_force_attack(cipher): Attempts to decrypt the ciphertext by trying all possible key combinations.
    egcd(a, b): Computes the Extended Euclidean Algorithm to find the greatest common divisor (GCD) and the coefficients.
    get_mod_inverse(a, m): Finds the modular inverse of a modulo m.

How to Use

    Run the script: Execute the main.py script.

    Choose an option: The script will prompt you to either 'encode' (encrypt) or 'decode' (decrypt) a message.

    Provide inputs:
        For encoding, input the plaintext, followed by the alpha and beta keys.
        For decoding, input the ciphertext, alpha and beta keys. Alternatively, choose the brute-force option to try all possible keys.

    View the result: The script will display the encrypted or decrypted text based on your selection.

Example Usage
Encoding:

vbnet

Would you like to 'encode' or 'decode'?
encode
What would you like to encode?
hello
What is your alpha key?
5
What is your beta key?
8
Encrypted text = mjqqt

Decoding:

vbnet

Would you like to 'encode' or 'decode'?
decode
Type 'yes' or 'no' if you would like to brute force to decode?
no
What would you like to decode?
mjqqt
What is your alpha key?
5
What is your beta key?
8
Decrypted text = hello

Brute Force Attack:

sql

Would you like to 'encode' or 'decode'?
decode
Type 'yes' or 'no' if you would like to brute force to decode?
yes
What would you like to decode?
mjqqt
|| Current keys: Alpha: 1 Beta: 0 ||
...

Requirements

    Python 3.x

Notes

    Ensure that the alpha key is coprime with 26 for the cipher to work correctly. The script includes a check for this when finding the modular inverse.
    The brute-force attack can be time-consuming depending on the length of the ciphertext.
