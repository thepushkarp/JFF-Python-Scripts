"""
encryptDecryptPDF.py - A program that can encrypt an unencrypted PDF file
with a password or decrypt an already password-protected PDF to an unencrypted
PDF.

Usage: run "python3 encryptDecryptPDF.py" and choose whether you want to
encrypt or decrypt a PDF and then enter the name of the file. You would be
prompted to enter the password either to encrypt the PDF or decrypt it, as
selected earlier.
"""

from os import path
import sys
import PyPDF3

# Encrypt
def encrypt():
	pdfName = input('Enter the name of PDF file to encrypt:\n')
	pdfName = path.abspath(pdfName)

	# Check if entered filename is valid
	if not path.exists(pdfName) or pdfName[-4:].lower() != '.pdf':
		print('The filename ' + pdfName + ' is not a PDF.')
		sys.exit()

	pdfFile = open(pdfName, 'rb')
	pdfReader = PyPDF3.PdfFileReader(pdfFile)
	pdfWriter = PyPDF3.PdfFileWriter()

	# Loop through the pages and add them to pdfWriter
	for pageNum in range(pdfReader.numPages):
		pdfWriter.addPage(pdfReader.getPage(pageNum))

	# Password for encryption
	password = input('Enter a password to encrypt the PDF: \n')
	pdfWriter.encrypt(password)

	# Save the resulting PDF to a file
	encryptedPdf = open('encrypted' + path.basename(pdfName), 'wb')
	pdfWriter.write(encryptedPdf)
	encryptedPdf.close()
	print('File encrypted and saved as encrypted' + path.basename(pdfName))

# Decrypt
def decrypt():
	pdfName = input('Enter the name of PDF file to decrypt:\n')
	pdfName = path.abspath(pdfName)

	# Check if entered filename is valid
	if not path.exists(pdfName) or pdfName[-4:].lower() != '.pdf':
		print('The filename ' + pdfName + ' is not a PDF.')
		sys.exit()

	pdfFile = open(pdfName, 'rb')
	pdfReader = PyPDF3.PdfFileReader(pdfFile)

	# Password for decryption
	password = input('Enter the password to decrypt the PDF: \n')
	pdfReader.decrypt(password)
	pdfWriter = PyPDF3.PdfFileWriter()

	# Loop through the pages and add them to pdfWriter
	for pageNum in range(pdfReader.numPages):
		pdfWriter.addPage(pdfReader.getPage(pageNum))

	# Save the resulting PDF to a file
	decryptedPdf = open('decrypted' + path.basename(pdfName), 'wb')
	pdfWriter.write(decryptedPdf)
	decryptedPdf.close()
	print('File decrypted and saved as decrypted' + path.basename(pdfName))

print('Enter the task to perform (1 or 2)\n1. Encrypt a PDF\n2. Decrypt a PDF')
response = int(input())

if response == 1:
	encrypt()

elif response ==2:
	decrypt()

else:
	print('You entered a wrong response.')
	sys.exit()
