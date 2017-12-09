#!/bin/python

import json
import string
import gzip
import binascii
import base64

def tlMap(layer):
    mapTo   = layer["mapTo"]
    content = layer["content"]
    mapFrom = layer["mapFrom"]
    trtable = str.maketrans(mapFrom, mapTo)
    return content.translate(trtable)

def unGzip(layer):
    content = layer["content"]
    data = binascii.a2b_base64(content)
    return gzip.decompress(data)

def unBase64(layer):
    content = layer["content"]
    return base64.b64decode(content)

def doNothing(layer):
    content = layer["content"]
    return content

def xor(b, mask):
    b = bytearray(b)
    for i in range(0, len(b)):
        b[i] = b[i] ^ mask[i % len(mask)]

    return bytes(b)

def xorMask(layer):
    content = binascii.a2b_base64(layer["content"])
    mask    = binascii.a2b_base64(layer["mask"])
    return xor(content, mask).decode()

def reverseContent(layer):
    content = layer["content"]
    return content[::-1]

def printFlag(layer):
    content = layer["content"]
    print(content)

opDict = {
    "map"   : tlMap,
    "gzip"  : unGzip,
    "b64"   : unBase64,
    "nul"   : doNothing,
    "xor"   : xorMask,
    "rev"   : reverseContent,
    "flag"  : printFlag
}

def peel(layer, ctr):
    op      = layer["op"]
    opDone  = opDict[op](layer)
    ind = 0
    if ctr == 73: # cheeky little fucker put one last trick in there
        ind = 1
    if opDone != None:
        return [op, json.loads(opDone)[ind]]
    else:
        return [op]

with open("jsonion.json", "r") as f:
    orig = f.read()

p1 = json.loads(orig)
p2 = p1[0] # mapping instruction

curLayer = p2
ctr = 1
while type(curLayer) == dict and "op" in curLayer.keys():
    if curLayer["op"] not in opDict:
        print("Layer %i: UNKNOWN OP '%s'" % (ctr, curLayer["op"]))
        break
    res = peel(curLayer, ctr)
    print("Layer %i: %s" % (ctr, res[0]))
    if len(res) > 1:
        curLayer = res[1]
        ctr += 1
    else:
        break
