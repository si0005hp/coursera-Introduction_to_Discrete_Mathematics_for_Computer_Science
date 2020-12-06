def extended_gcd(a, b):
    assert a >= b and b >= 0 and a + b > 0

    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)

    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y
    return (d, x, y)


# return (x, y)
# which satisfies ax + by = c
def diophantine(a, b, c):
    if a >= b:
        (d, x, y) = extended_gcd(a, b)
    else:
        (d, y, x) = extended_gcd(b, a)

    assert c % d == 0
    assert c == a * x * (c // d) + b * y * (c // d)

    return (x * (c // d), y * (c // d))


print(diophantine(10, 6, 14))
print(diophantine(3, 6, 18))
