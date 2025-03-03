def get_book_text(file_to_read):
  with open(file_to_read) as f:
    contents = f.read().split()
    count = len(contents)
    print(f"{count} words found in the document")

def get_character_count(file_to_read):
  char_count = {}
  with open(file_to_read) as f:
    contents = f.read().split()
    for word in contents:
      lowercased = word.lower()
      chars = list(lowercased)
      for char in chars:
        try:
          char_count[char] += 1
        except KeyError:
          char_count[char] = 1
  print(char_count)