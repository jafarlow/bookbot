# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project! This was written in python, and requires python 3 to be installed in order to run properly.

## How to test:
* Clone the repo locally
* Download a text file version of a book from [Gutenberg](https://www.gutenberg.org)
  * Search for the book you want, and select "Plain Text UTF-8"
  * Copy all the text from the new tab which should have opened into a local text file and save with .txt file extension
* Navigate to the cloned repo in your terminal and execute the command (requires python 3 to be installed on your computer):
  * `python3 main.py <relative-path-to-book-file>`
* Celebrate that you now have tested this small starter project!

## What to expect in the terminal output for a successful execution:
* Where the book was "found", aka the file path
* How many words there are
* A list of characters and their counts, sorted in descending order (most-to-least)
  * Punctuation and numbers are excluded from the output

## Caveats:
* This is a starter python project, and edge case handling is minimal or non-existent
  * Presently, this only supports analysis of txt files. Other file extensions are not guaranteed to work, and no error messaging has been written to account for improper input, other than if more (or fewer) than 2 arguments are supplied to the `python3` command.
  * There is no error handling for when a user submits the expected number of inputs, but there's a typo or the file doesn't exist