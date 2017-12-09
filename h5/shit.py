#!/bin/python

import telnetlib
import time
import sys

HOST = "challenges.hackvent.hacking-lab.com"

tn = telnetlib.Telnet(HOST)

while True:
    with open("output", "a") as f:
        text = tn.read_some().decode()
        f.write(text)
        sys.stdout.write(text)
