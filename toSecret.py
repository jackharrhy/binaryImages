from PIL import Image
import numpy as np
import sys

debug = True

if debug:
    print(sys.argv)

try:
    text = sys.argv[1]
except:
    print('Please pass a string to hide!')
    sys.exit(1)

type = None

try:
    sys.argv[2]
except:
    print('Processing pure image secret...')
    pixels = np.zeros((len(text),7,4), dtype=np.uint8)

    type = 'generate'
else:
    print('Processing modded image with secret...')
    im = Image.open(sys.argv[2])
    row,col =  im.size
    data = np.zeros([row, col])
    pixels = im.load()
    row -= 1
    col -= 1

    for r in range(row):
        if r >= col + 1:
            break
        for c in range(col):
            if pixels[c,r] == (255,255,255):
                pixels[c,r] = (254,254,254,255)
                pixels[x,y] = (255,200,125,255)

    type = 'image'

for x in range(len(text)):
    binary = format(ord(text[x]), 'b')

    if debug:
        print(x, len(binary),  binary)
    for y in range(len(binary)):
        if type == 'image':
            if int(binary[y]) == 1:
                pixels[y,x] = (255,255,255,255)

        else:
            if int(binary[y]) == 1:
                pixels[x,y] = [255,255,255,255]

            else:
                pixels[x,y] = [255,200,125,255]

if type == 'image':
    im.save('secret.png')

else:
    img = Image.fromarray(pixels, 'RGBA')
    img.save('secret.png')

if debug:
    from subprocess import call
    call(['feh','--force-aliasing','secret.png','-Z'])
