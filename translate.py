import os
from PIL import Image
import argparse

def initializeTranslate():
    parser = argparse.ArgumentParser()
    parser.add_argument('--s', help='resize image to 0.25 original size', type=str)
    parser.add_argument('--h', help='flip image horizontally', type=str)
    parser.add_argument('--v', help='flip image vertically', type=str)
    parser.add_argument('--r', help='rotate by {0}'.format(angle), type=str)

    angle = 45
    imageExt = ".png", ".jpg"



    for file in os.listdir("."):
        if file.endswith(imageExt):
            img = Image.open(file)
            #invertColours = PIL.ImageOps.invert(img)
            #print('worked - opened {0}'.format(openFile))

def scale():
    pass

def flipHorizontal():
    pass

def flipVertical():
    pass

def rotate():
    pass

if __name__=='__main__':
    initializeTranslate()
