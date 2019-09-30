import os
#from PIL import Image

def check_and_rename():
    for file in os.listdir("."):
        newName = '__MINE__' + file

        if file.endswith(".png") or file.endswith(".jpg"):
            os.rename(file, newName)

if __name__=='__main__':
    check_and_rename()
