"""
addWatermarkPDF.py - Add watermark to every page of a PDF document

Usage: run "python3 addWatermarkPDF.py" and enter the filenames of
the PDF to be watermarked and the watermark PDF.
"""

from os import path
import sys
import PyPDF3

# PDF filenames
baseFileName = input('Enter the name of the PDF file to be watermarked:\n')
baseFileName = path.abspath(baseFileName)
watermarkName = input('Enter the name of watermark PDF:\n')
watermarkName = path.abspath(watermarkName)

# Check if entered filenames are valid
if not path.exists(baseFileName) or baseFileName[-4:].lower() != '.pdf':
	print(f'The filename {baseFileName} is not a PDF.')
	sys.exit()

elif not path.exists(watermarkName) or watermarkName[-4:].lower() != '.pdf':
	print(f'The filename {watermarkName} is not a PDF.')
	sys.exit()

else:
	print('Adding Watermark...')

	baseFile = open(baseFileName, 'rb')
	pdfReader = PyPDF3.PdfFileReader(baseFile)
	pdfWatermarkReader = PyPDF3.PdfFileReader(open(watermarkName, 'rb'))
	pdfWriter = PyPDF3.PdfFileWriter()

	# Merge watermark to each page of PDF
	for pageNum in range(pdfReader.numPages):
		pageObj = pdfReader.getPage(pageNum)
		pageObj.mergePage(pdfWatermarkReader.getPage(0))
		pdfWriter.addPage(pageObj)

	# Save the resulting PDF to a file
	markedPdfFile = open('watermarked' + path.basename(baseFileName), 'wb')
	pdfWriter.write(markedPdfFile)
	baseFile.close()
	markedPdfFile.close()

	print(f'Watermarked file saved as watermarked{path.basename(baseFileName)}')
