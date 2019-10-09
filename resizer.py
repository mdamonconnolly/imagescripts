import os
from PIL import Image

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
        print('Successfully resized {0}'.format(file))

