from stats import get_word_count
from stats import get_character_count

def main(book):
  text = get_book_text(book)
  get_word_count(text)
  get_character_count(text)

def get_book_text(path):
  with open(path) as f:
    return f.read()
    
main("./books/frankenstein.txt")