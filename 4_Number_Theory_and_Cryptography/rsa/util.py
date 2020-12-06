import sys
sys.path.append('..')
import hashlib
from fast_modular_exponentiation import FastModularExponentiation
from gcd_euclid_extended import extended_gcd
import math
from chinese_remainder_theorem import ChineseRemainderTheorem as _ChineseRemainderTheorem


def ConvertToInt(message):
    res = ''.join(format(ord(i), 'b') for i in message)
    return int(res, 2)


def PowMod(b, e, m):
    return FastModularExponentiation(b, e, m)


def ConvertToStr(message_i):
    bin_data = format(message_i, "b")

    str_data = ''
    for i in range(0, len(bin_data), 7):
        temp_data = bin_data[i:i + 7]
        decimal_data = int(temp_data, 2)
        str_data = str_data + chr(decimal_data)

    return str_data


# returns integer b such that ab ≡ 1 mod n
def InvertModulo(a, n):
    if a >= n:
        d, x, y = extended_gcd(a, n)
    else:
        d, y, x = extended_gcd(n, a)

    return x % n


# takes integer n and returns the largest integer x such that x^2 ≦ n
def IntSqrt(n):
    return int(math.sqrt(n))


def GCD(a, b):
    if a >= b:
        d, _, _ = extended_gcd(a, b)
    else:
        d, _, _ = extended_gcd(b, a)
    return d


def ChineseRemainderTheorem(a, ra, b, rb):
    return _ChineseRemainderTheorem(a, ra, b, rb)
