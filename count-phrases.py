
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
  most_frequent_phrases = sorted(common_phrase_dict.items(), key=lambda x: x[1], reverse=True)
  return most_frequent_phrases[:100]

def makes_pretty(text_file_path):
  popular_phrase = count_common_phrases(text_file_path)
  for pair in popular_phrase:
    print "{} -{}".format(pair[0], pair[1])


makes_pretty('../moby_dick.txt')
