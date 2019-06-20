<h1 align = 'center'> JFF-Python-Scripts </h1>

<h3 align = 'center'> A collection of Python Scripts made for fun, while exploring Python 🐍</h3>

### Inspiration 💡

Some of the programs in this repository are inspired from the projects given in [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) by Al Sweigart and some other are born out of redundant curiosity of a boring mind during lazy afternoons.

This repository would contain python scripts, some of which might come of use occasionally. The purpose of creating this is to explore the various modules and implementations of the language through creating programs that are as much fun to use as they are to make.

## How to Use? 😀

- Clone the repository `$ git clone https://github.com/thepushkarp/JFF-Python-Scripts.git`
- Create a virtual environment ([click here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) to learn abou Virtual Environment)

```sh
python3 -m venv env
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

- Contents
	- [Code Destroyer](#Code-Destroyer)
	- [Phone Number and Email Extractor](#Phone_Number-and-Email-Extractor)

- [License](LICENSE)

### Code Destroyer

This program, inspired by [benbjohnson](https://github.com/benbjohnson)'s [tweet](https://twitter.com/benbjohnson/status/533848879423578112?lang=en) replaces semicolon ";" (U+003B) in files with a Greek Question Mark ";" (U+037E), that looks alike, but shows syntax errors (since it is a different character) leaving the programmer scratching their heads in confusion. ;-)

#### Usage:

Put the file to be destroyed in the same folder as this script and run:

```py3
python3 codeDestroyer.py
```

Enter the full filename (like helloWorld.c) in the prompt that follows.

 __Disclaimer: Do not use this to prank on someone's hard-work. You know how frustating that feels.__

### Phone Number and Email Extractor

This program takes in the text from your clipboard and saves the Phone Numbers and Email Addresses found in it to .txt files. It searches for Indian Mobile Phone Numbers, Toll-Free Numbers, Telephone Numbers and Emails using Regular Expressions.

#### Usage:

```py3
python3 phoneAndEmail.py
```

Two files, `emails.txt` and `phoneNumbers.txt` would be created in the same directory containing the emails and phone numbers from the copied text.

---

File Templates taken from [awesome-bashrc](https://github.com/aashutoshrathi/awesome-bashrc) and [HackerRank-Test-Case-Generator](https://github.com/aashutoshrathi/HackerRank-Test-Case-Generator/).

<p align="center"> Made with ❤ by <a href="https://github.com/thepushkarp">Pushkar Patel</a></p>
