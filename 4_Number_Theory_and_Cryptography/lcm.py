def gcd(a, b):
    assert a >= b and b >= 0 and a + b > 0
    return gcd(b, a % b) if b > 0 else a


def lcm(a, b):
    assert a > 0 and b > 0
    d = gcd(a, b) if a >= b else gcd(b, a)

    return a * b // d


print(lcm(2, 3))
print(lcm(35, 70))
print(lcm(1849639579327, 790933790547))
