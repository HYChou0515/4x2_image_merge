#!/usr/bin/env python
from PIL import Image
import glob
import numpy as np

WIDTH=569
HEIGHT=414
xborder=3
yborder=4
yspace = 140
xspace = 120

BIGW=1381 #WIDTH*2+x+2xspace
BIGH=1948 #HEIGHT*4+3y+2yspace

names = np.array(glob.glob('*.jpg'))
names = names.reshape(int(len(names)/8),8)
imid=0
for name in names:
    new_im = Image.new('RGB', (BIGW,BIGH), 'WHITE')
    images = map(Image.open, name)
    x_offset = xspace
    y_offset = yspace
    count = 0
    for im in images:
        if im.size != (WIDTH,HEIGHT):
            print('SIZE ERROR')
        if count == 4:
            x_offset += WIDTH+xborder
            y_offset = yspace
        new_im.paste(im, (x_offset,y_offset))
        y_offset += HEIGHT+yborder
        count+=1
    new_im.save('t'+str(imid)+'.jpg')
    imid+=1
