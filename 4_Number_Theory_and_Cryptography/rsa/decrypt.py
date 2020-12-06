from util import PowMod
from util import ConvertToStr
from util import InvertModulo
from encrypt import Encrypt


def Decrypt(ciphertext, p, q, exponent):
    n = p * q
    d = InvertModulo(exponent, (p - 1) * (q - 1))
    m = PowMod(ciphertext, d, n)
    return ConvertToStr(m)


def test():
    a = 3
    b = 7
    c = InvertModulo(a, b)
    print(c)

    p = 1000000007
    q = 1000000009
    exponent = 23917
    modulo = p * q
    ciphertext = Encrypt("attack", modulo, exponent)
    message = Decrypt(ciphertext, p, q, exponent)
    print(message)
