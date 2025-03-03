from stats import get_book_text
from stats import get_character_count

def main(book):
  get_book_text(book)
  get_character_count(book)

main("./books/frankenstein.txt")