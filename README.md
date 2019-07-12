<h1 align = 'center'> JFF-Python-Scripts </h1>

<h3 align = 'center'> A collection of Python Scripts made for fun, while exploring Python 🐍</h3>

### Inspiration 💡

Many of the programs in this repository are inspired from the projects given in [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) by [Al Sweigart](https://github.com/asweigart) and some other are born out of redundant curiosity of a boring mind during lazy afternoons.

This repository would contain python scripts, some of which might come of use occasionally. The purpose of creating this is to explore the various modules and implementations of the language through creating programs that are as much fun to use as they are to make.

## How to Use? 😀

- Clone the repository `$ git clone https://github.com/thepushkarp/JFF-Python-Scripts.git`
- Create a virtual environment ([click here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) to learn about Virtual Environment)

```sh
virtualenv env
```

- Activate virtual environment (On macOS and Linux)

```sh
source env/bin/activate
```

- Activate virtual environment (On Windows)

```sh
.\env\Scripts\activate
```

- Install requirements

```sh
pip install -r requirements.txt
```

- Run and explore the scripts!

## Contents 📄

- [Code Destroyer](#Code-Destroyer)
- [Extract Phone Number and Email](#Extract-Phone-Number-and-Email)
- [Search files based on size](#Search-files-based-on-size)
- [Fill gaps in naming](#Fill-gaps-in-naming)
- [Combine PDF files](#Combine-PDF-files)
- [Add Watermark to PDF](#Add-Watermark-to-PDF)
- [Encrypt or Decrypt a PDF](#Encrypt-or-Decrypt-a-PDF)
- [Add Logo to Images](#Add-Logo-to-Images)

### Code Destroyer

Code Destroyer, inspired by a [tweet](https://twitter.com/benbjohnson/status/533848879423578112?lang=en) by Ben Johnson, replaces semicolon ";" (U+003B) in files with a Greek Question Mark ";" (U+037E), that looks alike, but shows syntax errors (since it is a different character) leaving the programmer scratching their heads in confusion. ;-)

#### Usage:

Put the file to be destroyed in the same folder as this script and run:

```py3
python3 codeDestroyer.py
```

Enter the full filename (like helloWorld.c) in the prompt that follows.

 __Disclaimer: Do not use this to prank on someone's hard-work. You know how frustating that feels.__

### Extract Phone Number and Email

Takes in the text from your clipboard and saves the Phone Numbers and Email Addresses found in it to .txt files. It searches for Indian Mobile Phone Numbers, Toll-Free Numbers, Telephone Numbers and Emails using Regular Expressions.

_Useful if you have a large text data (like a website) and you are searching for phone numbers of emails in that text._

#### Usage:

```py3
python3 phoneAndEmail.py
```

Two files, `emails.txt` and `phoneNumbers.txt` would be created in the same directory containing the emails and phone numbers from the copied text.

### Search files based on size

Lets you search through a folder based on file size. Asks user for folder path and size. Files and subfolders inside the folder, greater than or equal to the input size would be displayed.

_Useful if you want to find large files and folders taking up space and wish to delete them._

#### Usage:

```py3
python3 searchSize.py
```

When prompted, enter the minimum size (in bytes) and the folder where files are to be searched. If the path entered is correct, the files, above and equal the size entered would be displayed.

### Fill gaps in naming

Finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on, in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt) and reanames all the files to close this gap.

_Useful if you have a number of files with same prefix and numbering after it and by some case, there is irregularity in numbering (like after deleting unnecessary images from a camera) and you wish to get a ragular naming in those files._

#### Usage:

```py3
python3 fillGap.py
```

Enter the file prefix, extesion name and taret folder in the prompt that appears. The files would be named in
order, closing gaps, if any.

### Combine PDF files

Combines all the PDFs in the current working directory into
a single PDF. The program also prompts user if they want to include the cover page of all the PDFs that are being merged.

It is recommended to rename files so that they are lexographically in the same order as they are to be combined and put them in the same directory as the script.
The combined PDF would be saved as the name of the first file in the lexographic order prepended with 'combined'. 

_Useful if you have many PDF and you want to read them all one after the another (like PDFs of a professor's slides that you wish to read before exams). You won't need to go from one PDF to another._

__Ensure that none of the PDFs are encrypted.__

#### Usage:

```py3
python3 combinePDF.py
```

Choose whether you want to include the cover page of each individual PDF by entering `y` or `n`.

### Add Watermark to PDF

Add watermark to every page of a PDF document.

The watermark file should be a PDF too. If you want to make an image or text as a watermark, put them in a word file and stylize as per you want it to appear as the watermark and then export the file as PDF. This file would be the watermark file.

_The usefullness of this script is straightforward - To add watermark to PDF files to prove its originality, make it harder to copy, and add authorship._

__Ensure that none of the PDFs are encrypted.__

#### Usage:

```py3
python3 addWatermarkPDF.py
```

Enter the filenames of the PDF to be watermarked and then of the watermark PDF.

### Encrypt or Decrypt a PDF

Encrypt an unencrypted PDF file with a password or decrypt a password-protected PDF and save as an unencrypted file.

_The usefullness of this script too is pretty straightforward - To add or remove privacy to PDF files._

#### Usage:

```py3
python3 encryptDecryptPDF.py
```

Choose whether you want to encrypt or decrypt a PDF and then enter the name of the file. You would be prompted to enter the password either to encrypt the PDF or decrypt it, as selected earlier.

### Add Logo to Images

Adds logo to the lower-right corner of all the pngs, jpgs and jpegs in the directory.

_Useful to add logos to imagesto prove their originality, make them harder to copy, and add authorship._
#### Usage:

```py3
python3 addLogo.py
```

Enter the location of the logo file in the prompt that follows. All the images with added logo would be saved in the 'withLogo' directory.


## License

[MIT License](LICENSE)

---

File Templates taken from [awesome-bashrc](https://github.com/aashutoshrathi/awesome-bashrc) and [HackerRank-Test-Case-Generator](https://github.com/aashutoshrathi/HackerRank-Test-Case-Generator/).

<p align="center"> Made with ❤ by <a href="https://github.com/thepushkarp">Pushkar Patel</a></p>
