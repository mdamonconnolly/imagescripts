import os
import PIL
from PIL import Image, ImageOps
 
def invert():
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

if __name__=='__main__':
    invert()


#TODO
# check if inverted or original already prefixed to name - if so, swap them
# refactor


