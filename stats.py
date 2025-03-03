def get_word_count(text):
  contents = text.split()
  count = len(contents)
  # print(f"{count} words found in the document")
  return count

def get_character_count(text):
  char_count = {}
  contents = text.split()
  for char in text:
    lowercased = char.lower()
    try:
      char_count[lowercased] += 1
    except KeyError:
      char_count[lowercased] = 1
  # print(char_count)
  return char_count