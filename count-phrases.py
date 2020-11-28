import sys

def get_words_from_files(text_file_path):
  words = []
  if not sys.stdin.isatty():
    words = sys.stdin.read().lower().split()
  else:
    for files in text_file_path:
      words += open(files).read().lower().split()
  return words

def count_common_phrases(text_file_path):
  words = get_words_from_files(text_file_path)
  common_phrase_dict = {}
  counter = 0
  while counter < len(words):
    sections = slice(counter, (counter+3))
    phrase = words[sections]
    three_word_sequence = ' '.join(phrase)
    if not three_word_sequence in common_phrase_dict:
      common_phrase_dict[three_word_sequence] = 1
    else:
      common_phrase_dict[three_word_sequence] += 1
    counter += 1
  most_frequent_phrases = sorted(common_phrase_dict.items(), key=lambda x: x[1], reverse=True)
  return most_frequent_phrases[:100]

def formats_output(text_file_path):
  popular_phrase = count_common_phrases(text_file_path)
  for pair in popular_phrase:
    print "{} - {}".format(pair[0], pair[1])

if not sys.stdin.isatty():
  stdin_file = sys.stdin
  formats_output(stdin_file)

# formats_output(['../origin_of_species.txt', '../moby_dick.txt'])
# formats_output(['../moby_dick.txt'])

# species length = 209750
# moby length = 215830
# import pdb; pdb.set_trace()

# cat ../moby_dick.txt | python ./count-phrases.py