from encrypt import Encrypt
from decrypt import Decrypt
from util import IntSqrt


def DecipherSmallDiff(ciphertext, modulo, exponent):
    for i in range(1, 1000):
        if is_exact_square(modulo + i**2):
            x = IntSqrt(modulo + i**2)
            big_prime = x + i
            small_prime = x - i
            return Decrypt(ciphertext, small_prime, big_prime, exponent)

    return "don't know"


def is_exact_square(n):
    if IntSqrt(n)**2 == n:
        return True
    return False


def test():
    p = 1000000007
    q = 1000000009
    n = p * q
    e = 239
    ciphertext = Encrypt("attack", n, e)
    message = DecipherSmallDiff(ciphertext, n, e)
    print(ciphertext)
    print(message)
