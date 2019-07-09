"""
combinePDF.py - Combines all the PDFs in the current working directory into
a single PDF.

Usage: run "python3 combinePDF.py" and choose whether you want to include the
cover page of each individual PDF by entering y or n.
"""

import os
import PyPDF3

# Get all the PDF filenames
pdfFiles = []
for filename in os.listdir('.'):
	if filename.endswith('.pdf'):
		pdfFiles.append(filename)
pdfFiles.sort()

pdfWriter = PyPDF3.PdfFileWriter()

print('Combining PDFs...')

# Loop through all the PDF files
for filename in pdfFiles:
	pdfFileObj = open(filename, 'rb')
	pdfReader = PyPDF3.PdfFileReader(pdfFileObj)

	# Loop through the pages and add them
	start = 0
	if pdfReader.numPages > 1:
		ans = input('Do you want to include the cover page of ' + filename\
		+ ' ? (y/n): ')
		start = 0 if ans.lower() == 'y' else 1
	for pageNum in range(start, pdfReader.numPages):
		pageObj = pdfReader.getPage(pageNum)
		pdfWriter.addPage(pageObj)

# Save the resulting PDF to a file
os.makedirs('combinedPDFs', exist_ok = True)
pdfOutput = open(os.path.join('combinedPDFs', 'combined' + pdfFiles[0]), 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()

print('Combined PDF saved as ' + 'combined' + pdfFiles[0])
