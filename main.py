import os
from PIL import Image


def check_and_rename():

    for file in os.listdir("."):
        ext = file.split('.')[1]
        newName = '__MINE__'+file

        if file.endswith(".png") or file.endswith(".jpg"):
            os.rename(file, newName)
            print(file)
        else:
            print("|")

if __name__=='__main__':
    check_and_rename()

# TODO
# instead of copying have the file rename existing files

#- browse the current directory (dir)
#- check file extension
#- if file extension type jpg or png
#- operate on filenames and rename them.
