"""
operations.py
Contains all of the transfomation and overlays etc
"""

#TODO: Complete re-write of every function. 
#TODO: Create "generate imageID" function. Generates ID from the date, image type and commissioner name. 
#TODO: Add Watermark function.


def flip(image, h = False, v = False):
	"""
	Flips the input image
	:param image: The image to be flipped.
	:param h: Flip horizontally.
	:param v: Flip vertically.
	"""
	return


def invert(image, **kwargs):
	"""
	Inverts the image. Inverts in black/white if no arguments are provided.
	:param image: The image to be inverted.
	:param kwargs: "R", "G" or "B" to flip a specific channel.  
	"""
	return


def atlas(images, keepSquare=False):
	"""
	Atlases a bunch of images into 1 larger image.
	:param images: The images to be atlased together.
	:param keepSquare: If True, the function will crop images to keep it square.
	"""
	return


def watermark(image, watermark, scale=0.5, offset=(0, 0), tiled=False):
	"""
	Watermarks an image.
	:param image: The image to apply the watermark to.
	:param watermark: The watermark to apply to the image.
	:param scale: The scale of the watermark. 1.0 would be covering the entire image.
	:param offset: For non-tiled. Offset the watermark in x or y axis.
	:param tiled: If True, the watermark will be tiled across the image. Offset will be ignored.
	"""
	return
