
def count_common_phrases(text_file_path):
  words = open(text_file_path).read().lower().split()
  common_phrase_dict = {}
  counter = 0
  while counter < len(words):
    sections = slice(counter, (counter+3))
    phrase = words[sections]
    new_phrase = ' '.join(phrase)
    if not new_phrase in common_phrase_dict:
      common_phrase_dict[new_phrase] = 1
    else:
      common_phrase_dict[new_phrase] += 1
    counter += 1
  print common_phrase_dict


count_common_phrases('../moby_dick.txt')

# import pdb; pdb.set_trace()