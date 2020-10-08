import os, PIL, argparse
from PIL import Image, ImageOps
from moviepy.editor import *

"""
A collection of image scripts.
TODO: Add argparse for main and use the arguments for all of the functions, not just some.
TODO: General cleanup so that all of the functions work in a similar way.
"""

def check_and_rename():
    """
    Renames a selection of images.
    TODO: Possibly add more options for tagging and so on.
    """
    for file in os.listdir("."):
        newName = '__MINE__' + file

        if file.endswith(".png") or file.endswith(".jpg"):
            os.rename(file, newName)


class Translate():

    """
    Image translator.
    """

    def __init__(self, args):
        
        self.angle = 45
        self.imageExt = ".png", ".jpg"
        self.openFile()
        self.args = args
    
    def openFile(self):
        for self.file in os.listdir("."):
            if self.file.endswith(self.imageExt):
                self.img = Image.open(self.file)

        if self.args.scale:
            self.scale()
        elif self.args.rotate:
            self.rotate()
        elif self.args.horizontal:
            self.flipHorizontal()
        elif self.args.vertical:
            self.flipVertical()
        else:
            print('Error: invalid argument selected')

                
    def scale(self):
        self.openFile()
        width, height = img.size
        img.scale((width/4), (height/4))
        img.save('_25%_'+file)
        print('Successfully resized {0}'.format(file) + ' to 25%. ')

    
    def rotate(self):
        print('Rotate (empty)')

    def flipHorizontal(self):
        print('Flip horizontal (empty)')

    def flipVertical(self):
        print('Flip vertical (empty)')


def resize():
    """
    Resize a group of images.
    """
    rawPercent = int(input("Please enter desired percentage to scale to\n"))
    path = os.getcwd()
    percent = rawPercent/100

    for file in os.listdir("."):
        if file.endswith(".png") or file.endswith(".jpg"):
            newName = file.split('.')[0] + '_resized_{0}%.'.format(rawPercent) + file.split('.')[1]

            img = Image.open(path + '\\' + file)
            width = int(img.size[0] * percent)
            height = int(img.size[1] * percent)

            img.thumbnail((width, height), Image.ANTIALIAS)
            img.save(str(newName))
            print('Successfully resized {0} to {1}%'.format(file, rawPercent))

def invert():
    """
    Inverts an png/jpg image.
    TODO: Add arg to take image location rather than just doing it on all of the images in the selected folder
    """
    imageExt = ".png", ".jpg"
    overWriteQuery = input("Overwrite existing images? If 'N' selected, the inverted images will be saved as new files: \n Y | N\n")
    currentDir = os.curdir

    saveToDir = input("Save to new folder ('Y) or save to current directory (leave blank)?\n")
    if saveToDir == 'y':
        if os.path.isdir('InvertedImages'):
            print('Folder already exists')
        else:
            newDir = os.mkdir('InvertedImages')
            print("New Folder Created\n")


    for file in os.listdir("."):
        if file.endswith(imageExt):
            img = Image.open(file)
            invertColours = PIL.ImageOps.invert(img)
            newfile = '_inverted_' + file

            #check prefix

            for i in file:
                if '_inverted_' in file:
                    newfile = '_original_' + file[10:]


            if overWriteQuery == 'n':
                if saveToDir == 'y':
                    invertColours.save(os.path.join(currentDir + '/InvertedImages', newfile))
                else:
                    invertColours.save(newfile)
                print('Did not overwrite - saved copies')

            elif overWriteQuery == 'y':
                if saveToDir == 'y':
                    invertColours.save(os.path.join(currentDir + '/InvertedImages', newfile))
                    os.file.remove(file)
                else:
                    invertColours.save(newfile)
                    os.remove(file)
                    print('Original files were overwritten to this directory')


def vid2gif():
    """
    Converts a video file to a gif.
    """
	path = str(os.getcwd())

	for file in os.listdir("."):
		if file.endswith(".mp4") or file.endswith(".MP4") or file.endswith(".flv") or file.endswith(".avi"):
			vid = VideoFileClip(file)
			vid.write_gif(file.split('.')[0] + '_gif.gif')


		print("Successfully converted file(s) to gif format")
