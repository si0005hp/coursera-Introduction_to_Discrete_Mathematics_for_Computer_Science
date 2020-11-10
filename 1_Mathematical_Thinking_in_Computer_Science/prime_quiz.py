from sympy import isprime

for i in range(2, 1000000):
  n = i * i + i + 41
  if not (isprime(n)):
    print(i)
