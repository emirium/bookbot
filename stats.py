def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

def get_num_words(words):
  words_list = words.split()
  return len(words_list)

def get_num_chars(words):
  words_list = words.split()
  all_chars_count = {}
  
  for word in words_list:
    word_lowercase = word.lower()
    word_characters_list = word_lowercase.split()[0]

    for character in word_characters_list:
      if character in all_chars_count:
        all_chars_count[character] = all_chars_count[character] + 1
      else:
        all_chars_count[character] = 1
  
  return all_chars_count

def sort_on(items):
  return items["num"]

def get_chars_num_list(chars_dictionary):
  chars_num_list = []

  for key in chars_dictionary:
    if not key.isalpha():
      continue
    chars_num_list.append({"char": key, "num": chars_dictionary[key]})

  chars_num_list.sort(reverse=True, key=sort_on)
  return chars_num_list




def print_book_report(book_filepath):
  book_text = get_book_text(book_filepath)
  num_words = get_num_words(book_text)
  num_chars = get_num_chars(book_text)
  chars_num_list = get_chars_num_list(num_chars)

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_filepath}...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  for item in chars_num_list:
    print(f"{item['char']}: {item['num']}")
  print("============= END ===============")
