import os, glob
from PIL import Image
import filetype
import pathlib

"""
def determine_ownership():
    dir = os.getcwd()

    for filename in glob.glob("*.JPG"):
        img = Image.open(filename)
        img.save('_MINE_' + str(filename))

"""

dir = os.listdir(os.getcwd())

def checkFile():

    for files in dir:
        #ext = files[-3:]
        ext = files.split('.')[1]

        if ext == 'png' or ext == 'jpg':
            print('theoretically renamed: {0}'.format(files))
        else:
            print("{0} ignored".format(files))


if __name__=='__main__':
    checkFile()

##working on 1 format
# TODO
# instead of copying have the file rename existing files
# work on multiple formats

#- browse the current directory (dir)
#- check file extension
#- if file extension type jpg or png
#- operate on filenames and rename them.
