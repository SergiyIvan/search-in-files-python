# Search for certain words in all files in the directory

Simple Python 3 script that allows you to get the count of specific words in all files in the certain directory and all its subdirectories.

## Prerequisites
* Python 3

## Preparation
* Install Python 3
* Run `pip install pathlib`. This library is used to retrieve all files in the directory
* Clone this repository: `git clone https://github.com/SergiyIvan/search-in-files-python.git`

After that open the `words.py` file. Specify **absolute** path to the directory in the `directory` variable (few lines below the beginning of `main` method):
```
directory = '/path/to/directory'
OR
directory = 'D:\path\to\directory
```
Script will perform search in the indicated diectory and all its subdirectories recursively.
Text file with words has to be in the same directory as .py file. Fill this file with a single word per line:
```
word1
word2
```

## Running
To run the script, just use this command:
```
python words.py
```

## Notes
This application outputs the count of entries of all words from the text file in the files in specific directory and all its subdirectories. You can sort the output by filenames, words (in alphabetical order) or by count of entries.
