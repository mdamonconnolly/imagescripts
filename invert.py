import os
import PIL
from PIL import Image, ImageOps

def checkDir():
    saveToDir = input("Save to new folder ('Y) or save to current directory ('N')?")
    if saveToDir == 'Y' or saveToDir == 'y':
        if os.path.isdir('\InvertedImages'):
            pass
        else:
            newDir = os.mkdir('InvertedImages')

def invert():
    imageExt = ".png", ".jpg"
    promptInput = input("Overwrite existing images? If 'N' selected, the inverted images will be saved as new files: \n Y | N\n")

    checkDir()

    for file in os.listdir("."):
        if file.endswith(imageExt):
            img = Image.open(file)
            invertColours = PIL.ImageOps.invert(img)

            if promptInput == 'N' or promptInput == 'n':
                invertColours.save(str(checkDir.newDir) + '\_Inverted_' + file)
                
                print('Did not overwrite - saved copies')

            elif promptInput == 'Y' or promptInput == 'y':
                print(os.getcwd)
                invertColours.save(str(checkDir.newDir) + '\_Inverted_' + file)
                #os.remove(file)
                print('Original files were overwritten with inverted version')

        else:
            print("file skipped")
            pass

if __name__=='__main__':
    invert()
