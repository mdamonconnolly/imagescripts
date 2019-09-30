import os, glob
from PIL import Image
import filetype
import pathlib

dir = os.listdir(os.getcwd())

def checkFile():

    for file in os.listdir("."):
        ext = file.split('.')[1]
        newName = '__MINE__'+file

        if ext == 'png' or ext == 'jpg':
            os.rename(file, file.replace(newName, '', 1))
            print(file)
        else:
            print("|")
    print(newName)


if __name__=='__main__':
    checkFile()

# TODO
# instead of copying have the file rename existing files

#- browse the current directory (dir)
#- check file extension
#- if file extension type jpg or png
#- operate on filenames and rename them.
