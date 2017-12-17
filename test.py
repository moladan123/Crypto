from math import floor, ceil
from os import urandom as random
import hashlib

PUBLIC_KEY_LENGTH = 2048
PRIVATE_KEY_LENGTH = 256

BIG_PRIME = 32317006071311007300714876688669951960444102669715484032130345427524655138867890893197201411522913463688717960921898019494119559150490921095088152386448283120630877367300996091750197750389652106796057638384067568276792218642619756161838094338476170470581645852036305042887575891541065808607552399123930385521914333389668342420684974786564569494856176035326322058077805659331026192708460314150258592864177116725943603718461857357598351152301645904403697613233287231227125684710820209725157101726931323469678542580656697935045997268352998638215525166389437335543602135433229604645318478604952148193555853611059596232273
SMALL_PRIME = 115792089237316195423570985008687907853269984665640564039457584007913129641017

powers = dict()
def fast_exp(x, pow, mod):
    powers = dict()
    return _fast_exp(x, pow, mod)


def _fast_exp(x, pow, mod):
    if pow in powers:
        return powers[pow]
    if pow == 0:
        return 1
    if pow == 1:
        return x % mod
    else:
        powers[int(floor(pow / 2.0))] = _fast_exp(x, int(floor(pow / 2.0)), mod)
        powers[int(ceil(pow / 2.0))] = _fast_exp(x, int(ceil(pow / 2.0)), mod)

        return (powers[int(floor(pow / 2.0))]) * (powers[int(ceil(pow / 2.0))]) % mod


def encrypt(message):
    " (str) -> str "
    for i in range(len()):
        generate_new_key


def generate_new_key(length):
    string = ""
    bits = random(length)
    for byte in bits:
        string += str(int(byte % 2))
    return string




def generate_key_pair():
    pass


if __name__ == "__main__":

    print(fast_exp(3, 1000000000000000000000, 1000000000000000000000000000000000007))

    print(hashlib.algorithms_guaranteed)

    print(generate_new_key(2048))
