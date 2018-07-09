#!/usr/bin/env python
import glob
from PIL import Image

names = glob.glob('*.png')
for name in names:
    im = Image.open(name)
    rgb_im = im.convert('RGB')
    rgb_im.save(name+'.jpg')
