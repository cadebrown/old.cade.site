#!python3
""" make-img-lowres.py - Create 'img-lowres/' directory with low resolution copies of 'img/' images.

$ pip3 install pillow

@author: Cade Brown <me@cade.site>
"""


import argparse
import os
import PIL.Image


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--input', type=str, default='./img', help='Directory containing images to convert')
parser.add_argument('--output', type=str, default='./img-lowres', help='Directory to output low resolution images to')

parser.add_argument('--size', type=int, default=2400, help='Maximum dimension of output images')

args = parser.parse_args()


# remove output!!
def rrmdir(path):
    for entry in os.scandir(path):
        if entry.is_dir():
            rrmdir(entry)
        else:
            os.remove(entry)
    os.rmdir(path)
rrmdir(args.output)

# create output
os.makedirs(args.output, exist_ok=True)


def resize(fi, fo):
    img = PIL.Image.open(fi)
    sz = img.size

    # cap out maximum size
    if sz[0] > args.size or sz[1] > args.size:
        if sz[0] > sz[1]:
            img = img.resize((args.size, int(args.size * sz[1] / sz[0])))
        else:
            img = img.resize((int(args.size * sz[0] / sz[1]), args.size), PIL.Image.Resampling.LANCZOS)
    
        # output
        print(f"$ {fi} -> {fo}")
        os.makedirs(os.path.dirname(fo), exist_ok=True)
        img.save(fo)


for path, dirs, files in os.walk(args.input):
    for f in files:
        if f.split('.')[-1] in ['png', 'jpg', 'jpeg', 'webp']:
            # create output path
            fi = os.path.join(path, f)
            fo = os.path.join(args.output, os.path.relpath(os.path.join(path, f), args.input))

            # create output directory
            resize(fi, fo)

            # convert image
            #print(f'$ ')
            #resize()
            #os.system('convert -resize %dx%d "%s" "%s"' % (args.size, args.size, os.path.join(path, f), opath))
