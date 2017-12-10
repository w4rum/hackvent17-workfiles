#!/bin/python

c = 0x423EDCDCDCD928DD43EAEEBFE210E694303C695C20F42A27F10284215E90
p = 0xB1FF12FF85A3E45F722B01BF3135ED70A552251030B114B422E390471633
b = 0x88589F79D4129AB83923722E4FB6DD5E20C88FDD283AE5724F6A3697DD97

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

# c     =_p (ab)
# c/b   =_p a

d = c * modinv(b, p)
