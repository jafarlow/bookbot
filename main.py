import sys
from stats import get_word_count
from stats import get_character_count
from stats import sorted_dictionary

def main():
  if len(sys.argv) != 2:
    print("Input requires relative path to the book you would like to analyze \n", 
          "USAGE: python3 main.py <path_to_book> \n", 
          f"Expected 2 inputs, but received {len(sys.argv)}")
    sys.exit(1)
  else:
    path = sys.argv[1]
    text = get_book_text(path)
    count = get_character_count(text)
    letters = sorted_dictionary(count)
    report(text, path, letters)

def get_book_text(path):
  with open(path) as f:
    return f.read()
    
def report(text_input, path_to_text, characters):
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {path_to_text}...")
  print("----------- Word Count ----------")
  count = get_word_count(text_input)
  print(f"Found {count} total words")
  print("--------- Character Count -------")
  for k, v in characters.items():
    print(f"{k}: {v}")
  print("============= END ===============")

main()