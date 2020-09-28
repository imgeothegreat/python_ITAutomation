#!/usr/bin/env python3

from PIL import Image
import os

files = os.listdir(".")

for file in files:
   if file[0] != '.' and file != 'pil_script.py':
       name,extension = os.path.splitext(file)
       jpeg_file = name + ".png"


       with Image.open(file) as im:
           im.convert("RGB").rotate(90).resize((128,128)).save("/opt/icons/"+jpeg_file)
