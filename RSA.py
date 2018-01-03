from os import urandom as random

p, q = 61, 53
KEY_BIT_LENGTH = 2048
e = 2 ** 16 + 1


def generate_new_binary(bit_length):
    string = ""
    bits = random(bit_length)
    for byte in bits:
        string += str(int(byte % 2))
    return string


def generate_int(l):
    k = generate_new_binary(l)
    i = sum([int(k[j]) * 2 ** j for j in range(len(k))])
    return i

def totient(x, y):
    return (x - 1) * (y - 1)


def encrypt(message):
    pass


def decrypt(message):
    pass


def is_prime(number):
    pass


def _generate_pq(key_length=KEY_BIT_LENGTH):
    p, q = generate_int(KEY_BIT_LENGTH), generate_int(KEY_BIT_LENGTH)

    while not is_prime(p):
        p = generate_int(KEY_BIT_LENGTH)

    while not is_prime(q):
        q = generate_int(KEY_BIT_LENGTH)

    return p, q


def generate_new_keys():
    p, q = _generate_pq()
    n = totient(p, q)
    d = pow(e, n - 2, n)
    return n, d

print(generate_new_keys())
