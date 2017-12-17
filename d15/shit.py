#!/bin/python

from base64 import b64encode, b64decode
from pprint import pprint
from itertools import permutations
from math import factorial
from fuzzywuzzy import fuzz
from bs4 import BeautifulSoup
from urllib import request
import hashlib
import re

def readAccounts(filepath):
    with open(filepath, "r") as f:
        accounts = []
        headers = f.readline().rstrip().split(",")
        content = f.read().split("\n")
        for user in content:
            if user.strip() == "":
                continue
            userData = {
                headers[i]: value
                for i, value in enumerate(user.split(","))
            }
            accounts.append(userData)
        return accounts

def checkUser(u):
    URL_PREFIX   = "http://challenges.hackvent.hacking-lab.com:3958/gallery/"
    KNOWN_TITLES = ["Tunnel", "Traffic", "Sky", "Rocks", "Rails", "Park",
                   "Coast", "Bridge", "Benches"]

    email = u["email"]
    url = URL_PREFIX + toGalleryToken(email)
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    for a in soup.find_all('a'):
        title = a.img['alt']
        if title not in KNOWN_TITLES:
            print("Unknown Title %s on\n%s" % (title, url))

accounts = readAccounts("accounts.csv")

target      = b64decode("bncqYuhdQVey9omKA6tAFi4rep1FDRtD4H8ftWiw")
"""
possUsers   = []
for user in accounts:
    if user["prename"] == "Danny":
        possUsers.append(user)

hashAlgos = hashlib.algorithms_available

# strip out keys
for i, user in enumerate(possUsers):
    nUser = []
    for key in user:
        nUser.append(user[key])
    possUsers[i] = nUser


bestRat = 0
bestConfig = []
ctr = 1
maxCtr = len(hashAlgos) * len(accounts[0].keys()) * len(possUsers)
def findAlgo():
    for hashAlg in enumerate(hashAlgos):
            for user in possUsers:
                for val in user:
                    global ctr
                    hF = hashlib.new(hashF)
                    if ctr % 10 == 0:
                        print("%i / %i = %f%%" % (ctr, maxCtr, ctr / maxCtr * 100))
                        print(hF)
                    hF.update(val.encode())
                    h = hF.digest()
                    global bestScore
                    global bestConfig
                    score = fuzz.ratio(h, target)
                    if score > bestScore:
                        bestScore = score
                        bestConfig = [b, val, hF, h]
                    ctr += 1
findAlgo()
"""

# Found algo: sha256 with all non-alphanumeric chars cut out
hashAlg     = 'sha256'
postproc    = lambda h: re.sub("[^a-zA-Z0-9]", "", b64encode(h).decode())

def toGalleryToken(email):
    m = hashlib.new(hashAlg)
    m.update(email.encode())
    return postproc(m.digest())

possUsers   = []
for user in accounts:
    if user["prename"] == "Thumper" \
            and user["state"] == "active":
        possUsers.append(user)

for u in possUsers:
    checkUser(u)
