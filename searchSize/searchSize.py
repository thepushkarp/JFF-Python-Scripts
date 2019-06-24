"""
searchSize.py - Lets you search through a folder based on file size.
Files and subfolders greater than or equal to the size entered, would
be displayed.

Usage: run "python3 searchSize.py". When prompted, enter the minimum
size (in bytes) and the folder where files are to be searched.
If the path entered is correct, the files, above and equal the size
entered would be displayed.
"""

import os
import sys

# Dictionary to save large files/folders with path as key ad size as
# value
large = {}

# Get size of folder and save path of files and folders greater than
# input size to the dict. large
def getSize(folPath):
	totalSize = 0
	for folderName, subfolders, fileNames in os.walk(folPath):
		for subfolder in subfolders:
			subfolderPath = os.path.join(folderName, subfolder)
			subfolderSize = getSize(subfolderPath)
			if subfolderSize >= size:
				large[subfolderPath] = subfolderSize
			totalSize += subfolderSize

		for fileName in fileNames:
			filePath = os.path.join(folderName, fileName)
			if not os.path.islink(filePath): # Skip if symbolic link
				fileSize = os.path.getsize(filePath)
				if fileSize >= size:
					large[filePath] = fileSize
				totalSize += fileSize
	return totalSize

# Input minimum size
size = int(input("Enter the minimum size (in bytes)\n"))

# Input folder name
folder = input("Enter the path of the folder to search\n")
folder = os.path.abspath(folder) # Absolute path

# Verify if folder name and path exists
if not os.path.exists(folder):
	print("The folder path entered does not exists.")
	sys.exit()
else:
	folderSize = getSize(folder)

	# If no files/folders found
	if large == {}:
		print(f"There are no files or folders with size greater than {size} bytes.")

	#  Print paths with size
	else:
		print(f"The files and folders with size greater than {size} are:")
		for path in large.keys():
			if os.path.isfile(path):
				print(f"The size of the file {path} is: {large[path]} bytes.")
			elif os.path.isdir(path):
				print(f"The size of the folder {path} is: {large[path]} bytes.")
