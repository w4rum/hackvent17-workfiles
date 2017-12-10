#!/bin/python22

from pwn import *
import re

def connect(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s

def sendChoices(s, choices, expectWin=False):
    output = ""
    for i, c in enumerate(choices):
        s.send(str(c) + '\n')
        if i < len(choices) - 1 or not expectWin:
            output = s.readuntil("Field:")
            state   = readState(output)
            printState(state)
        else:
            output = s.readuntil("start again")
    return output

def readState(response):
    m = re.compile("( X | \* | O )").findall(response)
    return [x[1] for x in m[-9:]]

def printState(state):
    output = ""
    for i, s in enumerate(state):
        output += s
        if i % 3 == 2 and i > 0 and i < 9:
            output += '\n'
    print(output)

HOST    = "challenges.hackvent.hacking-lab.com"
PORT    = 1037
s       = remote(HOST, PORT)

# title screen
print(s.readuntil("start the game"))
s.send('\n')
resp = s.readuntil("Field:")

# Level 1
level       = 1
followUp    = {
    "*********" : [1, False],

    "X***O****" : [9, False],
    "X*O*O***X" : [7, False],
    "X*O*O*XOX" : [4, True],

    "XOO*O*X*X" : [4, True],

    "XO**O***X" : [8, False],
    "XO**O*OXX" : [3, False],
    "XOX*OOOXX" : [4, True],

    "XOXOO*OXX" : [6, True],

    "XOO*O**XX" : [7, True],

    "XO*******" : [5, False],
    "XO**X***O" : [7, False],
    "XO*OX*X*O" : [3, True],

    "XOO*X****" : [9, True],

    "XOO*X*X*O" : [6, False],
    "XOOOXXX*O" : [8, True],
}

while level <= 100:
    print("Level %i" % level)
    state = readState(resp)
    stateStr = "".join(state)
    if stateStr in followUp:
        resp = sendChoices(s, [followUp[stateStr][0]], followUp[stateStr][1])
    else:
        print("Problem:")
        printState(state)
        s.interactive()
        break
    if "start again" in resp:
        if "Congratulations you won!" in resp:
            if level < 99:
                level += 1
            else:
                break
        s.send('\n')
        resp = s.readuntil("Field:")
s.interactive()
