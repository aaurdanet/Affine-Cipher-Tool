alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain, a, b):
    charsec = ""
    num_res = 0
    for x in plain:
        if x in alphabet:
            num_res = (a * alphabet.index(x) + b) % 26
            charsec += alphabet[num_res]
    return "Ciphertext = " + charsec


def decrypt(cipher, a, b):
    ans = ""
    numval = 0

    modinv = get_mod_inverse(a, 26)

    for x in cipher:
        # get numeric value
        numval = ord(x)
        # scale to be 0 to 25
        numval = numval - ord('A')
        # get numeric plain text
        numletter = modinv * (numval - b) % 26
        # to map back to a character add to ascii value of 'A' then convert
        # to character
        ans += chr(numletter + ord('A')).lower()

    return ans


def brute_force_attack(cipher):
    alphas = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    betas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

    for i in range(0, len(alphas)):
        a = alphas[i]
        for j in range(0, len(betas)):
            b = betas[j]
            print(f"|| Current keys: Alpha: {a} Beta: {b} ||")
            # for k in cipher:
            print(f"{decrypt(cipher=cipher, a=a, b=b)}\n")


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def get_mod_inverse(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


selection = input("Would you like to 'encode' or 'decode'?\n").lower()

if selection == "decode":
    brute_force = input("Type 'yes' or 'no' if you would like to brute force to decode?\n").lower()
    if brute_force == 'yes':
        cipher = input("What would you like to decode?\n").upper()
        brute_force_attack(cipher)
    else:
        cipher = input("What would you like to decode?\n").upper()
        alpha = int(input("What is you alpha key?\n"))
        beta = int(input("What is your beta key?\n"))
        print(f"Decrypted text = " + decrypt(cipher, a=alpha, b=beta))



elif selection == 'encode':
    plain = input("What would you like to encode?\n").lower()
    alpha = int(input("What is you alpha key?\n"))
    beta = int(input("What is your beta key?\n"))

    print(f"Encrypted text = " + encrypt(plain, a=alpha, b=beta))
