import os
from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--s', help='resize image to 0.25 original size', type=str, action="store_true")
parser.add_argument('--r', help='rotate by 45 degrees', type=str, action="store_true")
parser.add_argument('--h', help='flip image horizontally', type=str, action="store_true")
parser.add_argument('--v', help='flip image vertically', type=str, action="store_true")
args = parser.parse_args()

class Translate():

    def __init__(self, args):
        
        self.angle = 45
        self.imageExt = ".png", ".jpg"
        self.openFile()
    
    def openFile(self):
        for self.file in os.listdir("."):
            if self.file.endswith(self.imageExt):
                self.img = Image.open(self.file)

        if self.args.s:
            self.scale()
        elif self.args.r:
            self.rotate()
        elif self.args.h:
            self.flipHorizontal()
        elif self.args.v:
            self.flipVertical()
        else:
            print('Error: invalid argument selected')

                
    def scale(self):
        self.openFile()
        width, height = img.size
        img.scale((width/4), (height/4))
        img.save('_25%_'+file)
        print('Successfully resized {0}'.format(file) + ' to 25%. ')

    
    def rotate():
        print('Rotate (empty)')

    def flipHorizontal():
        print('Flip horizontal (empty)')

    def flipVertical():
        print('Flip vertical (empty)')




if __name__=='__main__':
    init = Translate()

# TODO
# angle for rotation to be user-defined
# scale to be user-defined - either by height/width or percentage
