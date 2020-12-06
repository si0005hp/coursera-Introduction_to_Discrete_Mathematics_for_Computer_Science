from encrypt import Encrypt
from decrypt import Decrypt
from util import GCD


def DecipherCommonDivisor(first_ciphertext, first_modulo, first_exponent, second_ciphertext, second_modulo,
                          second_exponent):
    common_prime = GCD(first_modulo, second_modulo)
    q1 = first_modulo // common_prime
    q2 = second_modulo // common_prime
    return (Decrypt(first_ciphertext, common_prime, q1,
                    first_exponent), Decrypt(second_ciphertext, common_prime, q2, second_exponent))


def test():
    # Example usage with common prime p and different second primes q1 and q2
    p = 101
    q1 = 1829897073254110
    q2 = 1000000007
    first_modulo = p * q1
    second_modulo = p * q2
    first_exponent = 239
    second_exponent = 17
    first_ciphertext = Encrypt("attack", first_modulo, first_exponent)
    second_ciphertext = Encrypt("wait", second_modulo, second_exponent)
    print(DecipherCommonDivisor(first_ciphertext, first_modulo, first_exponent, second_ciphertext, second_modulo,
                                second_exponent))
