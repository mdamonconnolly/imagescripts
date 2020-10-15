"""
Converters.py
Contains the functions for converting between formats.
"""

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
