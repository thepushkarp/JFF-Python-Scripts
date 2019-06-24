"""
fillGap.py - A program that finds all files with a given prefix,
such as spam001.txt, spam002.txt, and so on, in a single folder
and locates any gaps in the numbering (such as if there is a
spam001.txt and spam003.txt but no spam002.txt) and reanames all the
files to close this gap.

Usage: run "python3 fillGap.py" and Enter the file prefix, estension
and taret folder in the prompt that appears. The files would be named
in order, closing gaps, if any.
"""

import os
import sys
import re
from math import log
import shutil

# Input file/folder name and extension
filename = input("Enter the name prefix for the files/folders\n")
print("\nEnter the extension after the dot in filenames (like txt in spam01.txt)")
print("Type \"folder\" (without the quotes) if the files are folders")
ext = input()

# Create filename regex
if ext == 'folder':
	nameSeq = re.compile(
		r'^' + re.escape(filename) + r'\d*' + r'$'
	)
else:
	nameSeq = re.compile(
		r'^' + re.escape(filename) + r'\d*' +
		r'[.]' + re.escape(ext) + r'$'
	)

# Put matching file/folder names in a list
path = input("\nEnter the path of folder containing the file/folder\n")
path = os.path.abspath(path)
print(path)
if not os.path.isdir(path):
	print("The path entered is not a valid folder.")
	sys.exit()
else:
	lst = []
	for entry in os.listdir(path):
		found = nameSeq.search(entry)
		if found:
			lst.append(found[0])

# Sort list and take size of list as padding
lst = sorted(lst)
padding = int(log(len(lst))//log(10)) + 1

# Rename files/folders
for i in range(len(lst)):
	if ext == 'folder':
		newName = filename + str(i).rjust(padding, '0')
		oldPath = os.path.join(path, lst[i])
		newPath = os.path.join(path, newName)
		shutil.move(oldPath, newPath)
	else:
		newName = filename + str(i).rjust(padding, '0') + '.' + ext
		oldPath = os.path.join(path, lst[i])
		newPath = os.path.join(path, newName)
		shutil.move(oldPath, newPath)
print("The files are renamed with gaps closed.")
