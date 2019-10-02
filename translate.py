import os
from PIL import Image
import argparse


class Translate():

    def __init__(self):
        
        self.angle = 45
        self.imageExt = ".png", ".jpg"

        parser = argparse.ArgumentParser()
        parser.add_argument('--s', help='resize image to 0.25 original size', type=str)
        parser.add_argument('--h', help='flip image horizontally', type=str)
        parser.add_argument('--v', help='flip image vertically', type=str)
        parser.add_argument('--r', help='rotate by {0}'.format(self.angle), type=str)

        for self.file in os.listdir("."):
            if self.file.endswith(self.imageExt):
                self.img = Image.open(self.file)
                #invertColours = PIL.ImageOps.invert(img)

        self.u = input('Test input: ')
        self.openFile()
        



    def openFile(self):
        print(self.u, self.file)

    def scale():
        pass

    def flipHorizontal():
        pass

    def flipVertical():
        pass

    def rotate():
        pass

if __name__=='__main__':
    init = Translate()

# TODO
# angle for rotation to be user-defined
# scale to be user-defined - either by height/width or percentage
