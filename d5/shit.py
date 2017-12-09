#!/bin/python
from fractions import gcd

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def totient(n):
    amount = 0
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1
    return amount

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)

    for n_i, a_i in zip(n, a):
        p = prod / n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a / b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

values  = [0x69355f71,
          0xc2c8c11c,
          0xdf45873c,
          0x9d26aaff,
          0xb1b827f4,
          0x97d1acf4]

hint    = [0xFE8F9017,
           0x13371337]

primes = [0x1337, 0x10001]

#primes = [61, 53]
n = primes[0] * primes[1]
print(hex(n))
tot = lcm(primes[0]-1, primes[1]-1)
print(hex(tot))
"""for e in range(65538):
    print("============")
    print("e = %i" % e)
    try:
        d = modinv(e, tot)
    except Exception:
        print("modinv does not exist")
        continue
    print("d = %x" % d)
    plain = pow(values[0], d, n)
    if plain == 0x48563137:
        print("============")
        print("============")
        print("============")
        print(plain)
        print("============")
        print("============")
        print("============")
"""
c = 0
"""for d in range(0xffffffff):
    if c == 100000:
        print("d = %x" % d)
        c = 0
    plain = pow(values[0], d, n)
    c += 1
    if plain == 0x48563137:
        print("============")
        print("============")
        print("============")
        print(plain)
        print("============")
        print("============")
        print("============")
plain = [hex(pow(x, d, n)) for x in values]
#plain = hex(pow(values[0], primes[1], primes[0]))
print(plain)
"""

test = values + hint
"""for i in test:
    for j in test:
        print("0x%x and 0x%x: 0x%x"% (i, j, gcd(i, j)))
"""

target = 0x48563137
print(hex(values[0] ^ 0x6471c925))
"""for d in range(target , 0xffffffff):
    if c == 1000000:
        print("d = %x" % d)
        c = 0
    plain = (values[0]) % d
    c += 1
    if plain == target:
        print("============")
        print("============")
        print("============")
        print(plain)
        print("============")
        print("============")
        print("============")

"""
