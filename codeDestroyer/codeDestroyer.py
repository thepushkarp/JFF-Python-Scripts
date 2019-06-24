""" 
codeDestroyer.py - Replaces semicolon(;) in files with Greek
Question Mark(;) that looks alike but shows syntax errors,
(since it is a different character) leaving the programmer
scratching their heads in confusion. ;-)

Usage: Put the file in the same folder as this script and run
"python3 codeDestroyer.py". Enter the full filename
(like helloWorld.c) in the prompt that follows. 
"""

import sys
import os
import re

# Unicode symbols for semicolon and the Greek Question mark
semicolon = u'\u003b'
greekQmark = u'\u037e'

# Name of file
fileName = input("Enter the file name (like helloWorld.c):\n")
filename = os.path.abspath(fileName)
if (not os.path.exists(fileName)) or os.path.islink(fileName):
	print("\nThe filename you entered is not valid. Please enter a valid filename.")
	sys.exit()
else:
	# Open the file to be destroyed
	destroyFile = open(fileName, 'r+')

	# Replace the characters in contents
	contents = destroyFile.read()
	contents = re.sub(semicolon, greekQmark, contents)

	# Overwrite on the original file
	destroyFile.seek(0, 0)
	destroyFile.write(contents)
	destroyFile.close()
	print("\n" + fileName + " destroyed syccessfully XD.")
