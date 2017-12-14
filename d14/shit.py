#!/bin/python

from fractions import gcd
from binascii import unhexlify

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

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

flag= 0x7A9FDCA5BB061D0D638BE1442586F3488B536399BA05A14FCAE3F0A2E5F268F2F3142D1956769497AE677A12E4D44EC727E255B391005B9ADCF53B4A74FFC34C
n   = 0xF66EB887F2B8A620FD03C7D0633791CB4804739CE7FE001C81E6E02783737CA21DB2A0D8AF2D10B200006D10737A0872C667AD142F90407132EFABF8E5D6BD51
# prime factors found on factordb.com
p   = 18132985757038135691
q   = 711781150511215724435363874088486910075853913118425049972912826148221297483065007967192431613422409694054064755658564243721555532535827
e   = 65537
tot = lcm(p-1, q-1)
d   = modinv(e, tot)

flagPlain = pow(flag, d, n)
print(unhexlify(hex(flagPlain)[2:]).decode())
