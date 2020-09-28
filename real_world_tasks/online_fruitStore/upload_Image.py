#!/usr/bin/env python3

import os
import requests

BASEPATH = 'supplier-data/images/'

folder = os.listdir(BASEPATH)
url = "http://localhost/upload/"

for image in folder:
    if ".jpeg" in image:
        with open(BASEPATH+image, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
