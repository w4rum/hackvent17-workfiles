#!/bin/python

import zbarlight
from PIL import Image
import urllib.request
from datetime import datetime
import os
import sys

def readQR(filename):
    with open(filename, 'rb') as f:
        image = Image.open(f)
        image.load()
        data = zbarlight.scan_codes('qrcode', image)
    return data

def downloadNext():
    targetDir = "download"
    if not os.path.isdir(targetDir):
        os.mkdir(targetDir)
    targetFilename = "qr-code-%s.png" % \
        datetime.now().strftime('%Y-%b-%d--%H-%M-%S-%f')
    targetPath = targetDir + "/" + targetFilename
    targetURL = "http://challenges.hackvent.hacking-lab.com:4200/"
    urllib.request.urlretrieve(targetURL, targetPath)
    return targetPath

while True:
    print(readQR(downloadNext()))

