def get_book_text(file_to_read):
  with open(file_to_read) as f:
    contents = f.read().split()
    count = len(contents)
    print(f"{count} words found in the document")