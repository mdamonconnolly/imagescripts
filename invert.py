import os
import PIL
from PIL import Image, ImageOps

imageExt = ".png", ".jpg"

def invert():
    for file in os.listdir("."):
        if file.endswith(imageExt):
            img = Image.open(file)
            invertColours = PIL.ImageOps.invert(img)
            invertColours.save('_Inverted_' + file)
            print('inverted')
        else:
            print('Error')

if __name__=='__main__':
    invert()
