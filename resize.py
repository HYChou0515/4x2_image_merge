#!/usr/bin/env python
from PIL import Image
import glob
import numpy as np

WIDTH=569
HEIGHT=414
OUTPUT_DIR='merged'

names = np.array(glob.glob('*.jpg'))
imid=0
for name in names:
    image = Image.open(name)
    if image.size[0] < image.size[1]:
        image = image.rotate(90, expand=1)
    new_im = Image.new('RGB', (WIDTH, HEIGHT), 'WHITE')
    resizeRatio = min(WIDTH/image.size[0], HEIGHT/image.size[1])
    properSize = (int(image.size[0] * resizeRatio), int(image.size[1] * resizeRatio))
    print(properSize)
    image = image.resize(properSize)
    print((int((WIDTH-image.size[0])/2), int((HEIGHT-image.size[1])/2)))
    new_im.paste(image, (int((WIDTH-image.size[0])/2), int((HEIGHT-image.size[1])/2)))
    new_im.save("%s/s%02d.jpg" % (OUTPUT_DIR, imid))
    imid+=1
