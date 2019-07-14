"""
addLogo.py - Adds logo to the lower-right corner of all the pngs, jpgs and
jpegs in the directory. The size of logo is approximately 1/10 th of the size
of the image and has a padding of 1/25 th to the right and bottom of the logo
is added.

Usage: run "python3 addLogo.py" and enter the name of the logo to be inserted.
All the images with added logo would be saved in 'withLogo' directory.
"""

import os
import sys
from PIL import Image

logoName = input('Enter the name of the logo image:\n')
logoName = os.path.abspath(logoName)

# If logo file does not ecists or is not a supported image file
if not os.path.exists(logoName):
	print(f'The filename {logoName}  does not exists.')
	sys.exit()
elif not (logoName.lower().endswith('.png') or \
	logoName.lower().endswith('.jpg') or logoName.lower().endswith('.jpeg')):
	print(f'The filename {logoName} is not a supported image file.')
	sys.exit()

logoIm = Image.open(logoName).convert("RGBA")
logoWidth, logoHeight = logoIm.size
os.makedirs('withLogo', exist_ok = True)

# Loop over all files in the working directory
for fileName in os.listdir('.'):
	if not (fileName.lower().endswith('.png') or \
		fileName.lower().endswith('.jpg') or \
		fileName.lower().endswith('.jpeg')) or \
		os.path.abspath(fileName) == logoName:
		continue # skip non-image files and the logo file itself

	im = Image.open(fileName)
	width, height = im.size

	# Resizes the largest dimention of logo to 1/10th of smallest dimension
	# of the image file and padding to 1/25th.
	if height < width:
		if logoWidth > logoHeight:
			logoHeight = int((logoHeight / logoWidth) * int(height/10))
			logoWidth = int(height/10)
		else:
			logoWidth = int((logoWidth / logoHeight) * int(height/10))
			logoHeight = int(height/10)
		pad = int(height/25)
	else:
		if logoWidth > logoHeight:
			logoHeight = int((logoHeight / logoWidth) * int(width/10))
			logoWidth = int(width/10)
		else:
			logoWidth = int((logoWidth / logoHeight) * int(width/10))
			logoHeight = int(width/10)
		pad = int(height/25)

	# Resize the logo
	logoIm = logoIm.resize((logoWidth, logoHeight), Image.ANTIALIAS)

	# Add logo
	print(f'\nAdding logo to {fileName}...')
	im.paste(logoIm, (width - logoWidth - pad, height - logoHeight - pad), \
		logoIm)

	# Save the image with added logo
	im.save(os.path.join('withLogo', fileName), quality = 100)
	print(f'Saved {fileName} with added logo')
