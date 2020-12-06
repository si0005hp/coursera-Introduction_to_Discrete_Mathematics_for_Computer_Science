# calculate b^(2^k) mod m
def ModularExponentiation(b, k, m):
    if k < 2:
        return b**(2**k) % m

    n = ModularExponentiation(b, k - 1, m)
    return n**2 % m


def test():
    print(ModularExponentiation(3, 2, 7))
    print(ModularExponentiation(7, 5, 11))
