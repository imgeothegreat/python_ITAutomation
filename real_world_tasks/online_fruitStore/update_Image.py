#!/usr/bin/env python3
import os
from PIL import Image

BASEPATH = 'supplier-data/images/'

image_folder = os.listdir(BASEPATH)


for image in image_folder:
    if ".tiff" in image:
      name, extension = os.path.splitext(image)
      jpeg_file = name + ".jpeg"

      with Image.open(BASEPATH + image) as im:
          im.convert("RGB").resize((600,400)).save(BASEPATH+jpeg_file)
