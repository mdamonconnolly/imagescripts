import os, glob
from PIL import Image
import filetype

def determine_ownership():
    dir = os.getcwd()

    for filename in glob.glob("*.JPG"):
        img = Image.open(filename)
        img.save('_MINE_' + str(filename))

def renameFiles(checkFile.fType):
    
    for filename in os.listdir(os.getcwd()):
        #os.rename(filename, '__MINE__' + filename)
        print(filename)

def checkFile():
    fType = filetype.guess('bird.jpg')

    if fType is None:
        print('Error: File type is None')
        return
    print('File type: ' + fType.extension)


if __name__=='__main__':
    checkFile()

##working on 1 format
# TODO
# instead of copying have the file rename existing files
# work on multiple formats
