"""
operations.py
Contains all of the transfomation and overlays etc
"""

#TODO: Complete re-write of every function. 
#TODO: Create "generate imageID" function. Generates ID from the date, image type and commissioner name. 
#TODO: Add Watermark function.
#TODO: Add Atlas function.

def check_and_rename():
	"""
	Renames a selection of images.
	TODO: Possibly add more options for tagging and so on.
	"""
	for file in os.listdir("."):
		newName = '__MINE__' + file

		if file.endswith(".png") or file.endswith(".jpg"):
			os.rename(file, newName)


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
