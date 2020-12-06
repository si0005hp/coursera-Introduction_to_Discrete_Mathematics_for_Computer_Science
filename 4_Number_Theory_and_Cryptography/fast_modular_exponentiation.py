from modular_exponentiation import ModularExponentiation


# calculate b^e mod m
def FastModularExponentiation(b, e, m):
    e_bin = format(e, 'b')
    mod_ms = [ModularExponentiation(b, k, m) for k, digit in enumerate(reversed(list(e_bin))) if digit == '1']

    res = 1
    for mod_m in mod_ms:
        res = res * mod_m % m

    return res


def test():
    print(FastModularExponentiation(7, 13, 11))
    print(FastModularExponentiation(7, 32, 11))
