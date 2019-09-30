import os, glob
from PIL import Image

def determine_ownership():
    dir = os.getcwd()

    for filename in glob.glob("*.JPG"):
        img = Image.open(filename)
        img.save('_MINE_' + str(filename))

if __name__=='__main__':
    determine_ownership()
##working on 1 format
# TODO
# instead of copying have the file rename existing files
# work on multiple formats
