"""
phoneAndEmail.py - Finds Indian phone numbers and email addresses
from the clipboard and saves them to a file.

Usage: Copy the text from where phone numbers and emails are to be
extracted, to the clipboard and run "python3 phoneAndEmail.py".
The phone numbers and emails from the text would be saved in
phoneNumbers.txt and emails.txt files respectively.
"""

import re
import pyperclip

# Mobile phone number regex
# Pata nahi log ek universal mobile number format kyu nahi follow
# karte ¯\_(ツ)_/¯ The number could be in the form of AAA-BBB-CCCC,
# AAAAA-BBBBB, AAAA-BBBBBB or AA-BBB-CCCCC, AAAAAAAAAA or maybe
# something else (╯°□°）╯︵ ┻━┻. However, this regex checks for the
# form of AAAA-BBBBBB and AAAAAAAAAA, as given on
# https://en.wikipedia.org/wiki/Telephone_numbers_in_India#mobile_numbers
mobileRegex = re.compile(r'''(
	(?:				# prefixes
		(?:
			(?:\+|0{0,2})		# +/zeros before country code
			91					# country code
			(?:[ -]?)			# separator
		)
		|(?:[0]{0,2}[ -]?)	# zero and separator before number
	)?				
	([6-9]\d{3})	# first 4 digits
	(?:[ -]?)		# separator
	(\d{6})			# last 6 digits
)''',re.VERBOSE)

# Toll-free/local-rate phone number regex
tollFreeRegex = re.compile(r'''(
	(1|000)			# 1 or 000
	(?:[ -]?)		# separator
	(800|860)		# toll-free/local-rate numbers
	(?:[ -]?)		# separator
	(\d{3})			# next 3 digits
	(?:[ -]?)		# separator
	(\d{3,4})		# last 3 or 4 digits
)''',re.VERBOSE)

# Telephone number Regex
telRegex = re.compile(r'''(
	(?:				# prefixes
		(?:
			(?:\+|0{0,2})		# +/zeros before country code
			91					# country code
			(?:[ -]?)			# separator
		)
		|(?:[0]{0,2}[ -]?)	# zero and separator before number
	)?				
	(?:					
		(						# Tier-1 cities
			([1-8]\d{1})		# STD code
			(?:[ -]?)			# separator
			([2-7]\d{7})		# number
		)
		|(						# Tier-2 cities
			([1-8]\d{2})		# STD code
			(?:[ -]?)			# separator
			([2-7]\d{6})		# number
		)
		|(						# Tier-3 cities
			([1-8]\d{3})		# STD Code
			(?:[ -]?)			# separator
			([2-7]\d{5})		# number
		)
	)
)''',re.VERBOSE)

# Email regex
emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+	# username
	@					# @ symbol
	[a-zA-Z0-9.-]+		# domain name
	(\.[a-zA-Z]{2,4})	# dot-something
)''', re.VERBOSE)

# Find matches in clipboard text
text = str(pyperclip.paste())
mobileMatches = []
tollFreeMatches = []
telMatches = []
emailMatches = []

for groups in mobileRegex.findall(text):
	mobNum = ''.join([groups[1], groups[2]])
	mobileMatches.append(mobNum)

for groups in tollFreeRegex.findall(text):
	tollFreeNum = ''.join([groups[1], groups[2], groups[3], groups[4]])
	tollFreeMatches.append(tollFreeNum)

for groups in telRegex.findall(text):
	if groups[1] != '':
		telNum = ''.join([groups[2], groups[3]])
		if telNum not in mobileMatches:
			if telNum not in tollFreeMatches:
				telMatches.append('0'+ groups[1])
	if groups[4] != '':
		telNum = ''.join([groups[5], groups[6]])
		if telNum not in mobileMatches:
			if telNum not in tollFreeMatches:
				telMatches.append('0'+ groups[4])
	if groups[7] != '':
		telNum = ''.join([groups[8], groups[9]])
		if telNum not in mobileMatches:
			if telNum not in tollFreeMatches:
				telMatches.append('0'+ groups[7])

for groups in emailRegex.findall(text):
	emailMatches.append(groups[0])

# Save results in .txt files
phoneNumbers = open('phoneNumbers.txt', 'w')

phoneNumbers.write('Mobile Phone Numbers:\n')
if mobileMatches == []:
	phoneNumbers.write('No Mobile Phone Numbers Found')
else:
	phoneNumbers.write('\n'.join(mobileMatches))
phoneNumbers.write('\n\n')

phoneNumbers.write('Toll-Free/LocalRate Phone Numbers:\n')
if tollFreeMatches == []:
	phoneNumbers.write('No Toll-Free/Local-Rate Phone Numbers Found')
else:
	phoneNumbers.write('\n'.join(tollFreeMatches))
phoneNumbers.write('\n\n')

phoneNumbers.write('Telephone Numbers:\n')
if telMatches == []:
	phoneNumbers.write('No Telephone Numbers Found')
else:
	phoneNumbers.write('\n'.join(telMatches))
phoneNumbers.write('\n')

emails = open('emails.txt', 'w')
emails.write('Emails:\n')
if emailMatches == []:
	emails.write('No Emails Found')
else:
	emails.write('\n'.join(emailMatches))
emails.write('\n')

phoneNumbers.close()
emails.close()
print('Phone Numbers and Emails saved to phoneNumbers.txt and emails.txt')
