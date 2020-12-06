from util import PowMod
from util import ConvertToInt


def Encrypt(message, modulo, exponent):
    m = ConvertToInt(message)
    return PowMod(m, exponent, modulo)
