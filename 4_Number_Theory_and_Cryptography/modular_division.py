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


def divide(a, b, n):
    assert n > 1 and a > 0

    if a >= n:
        (d, s, t) = extended_gcd(a, n)
    else:
        (d, t, s) = extended_gcd(n, a)
    assert d == 1

    multiplicative_inverse_of_a_mod_n = s % n
    x = (b * multiplicative_inverse_of_a_mod_n) % n
    assert 0 <= x and x <= n - 1.

    return x


print(divide(2, 7, 9))
print(divide(3, 5, 7))
