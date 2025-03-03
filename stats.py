def get_word_count(text):
  contents = text.split()
  count = len(contents)
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
  return char_count

def sorted_dictionary(dict_input):
  filtered_dict = {k: v for k, v in dict_input.items() if k.isalpha()}
  sorted_dict = dict(sorted(filtered_dict.items(), key=lambda item: item[1], reverse=True))
  return sorted_dict