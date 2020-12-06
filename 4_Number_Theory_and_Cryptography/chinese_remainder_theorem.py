def ExtendedEuclid_Impl(a, b):
    assert a >= b and b >= 0 and a + b > 0

    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = ExtendedEuclid_Impl(b, a % b)
        x = q
        y = p - q * (a // b)

    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y
    return (d, x, y)


def ExtendedEuclid(a, b):
    if a >= b:
        d, x, y = ExtendedEuclid_Impl(a, b)
        return (x, y)
    else:
        d, x, y = ExtendedEuclid_Impl(b, a)
        return (y, x)


def ChineseRemainderTheorem(a, ra, b, rb):
    (x, y) = ExtendedEuclid(a, b)
    n = ra * b * y + rb * a * x
    r = n % (a * b)
    return r


def test():
    a = 3
    b = 5
    for i in range(0, a * b):
        ra = i % a
        rb = i % b
        print(ChineseRemainderTheorem(a, ra, b, rb))
