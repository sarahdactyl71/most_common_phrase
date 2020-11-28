from nose.tools import *
from count_phrases import *

#testing for method get_words_from_files
def test_first_ten_words_from_files():
  file = ['origin_of_species.txt']
  large_file = get_words_from_files(file)
  first_ten = large_file[:10]
  assert_equal(first_ten, ['\xef\xbb\xbfthe','project','gutenberg','ebook','of','on','the','origin','of','species,'])

def test_last_ten_words_from_files():
  file = ['origin_of_species.txt']
  large_file = get_words_from_files(file)
  first_ten = large_file[-10:]
  assert_equal(first_ten, ['subscribe','to','our', 'email','newsletter', 'to','hear','about','new','ebooks.'])

#testing for cleaned_word_list
def test_cleaned_words_from_given_list():
  words = ["adventure-time", "c'mon", "grab", "your", "friends", " ", "*", ""]
  new_list = clean_word_list(words)
  assert_equal(new_list, ['adventure', 'time', "c'mon", 'grab', 'your', 'friends'])

def test_cleaned_words_from_given_list_puntuation():
  words = ["hello.", "my,", "name is", "finn!", "the", "human*"]
  new_list = clean_word_list(words)
  assert_equal(new_list, ['hello', 'my', 'name', 'is', 'finn', 'the', 'human'])

def test_cleaned_words_from_file_one():
  file = ['origin_of_species.txt']
  large_file = get_words_from_files(file)
  random_section = large_file[560:580]
  cleaned_list =  clean_word_list(random_section)
  assert_equal(cleaned_list, ['adaptation','to','an','end','wheresoever','therefore','all','things','together','that','is','all','the','parts','of','one','whole','happened','like','as'])

def test_cleaned_words_from_file_two():
  file = ['origin_of_species.txt']
  large_file = get_words_from_files(file)
  random_section = large_file[776:786]
  cleaned_list =  clean_word_list(random_section)
  assert_equal(cleaned_list, ['inorganic','world','being','the','result','of','law','and','not','of'])

#testing for count_common_phrases
def test_count_common_phrases_from_given_list():
  phrases = ["i", "like", "dogs", "animals", "sushi", "is", "tasty", "finn", "i", "like", "dogs","i", "like", "dogs", "octopus", "i", "like", "dogs", "corgi", "sushi", "is", "tasty"]
  common_phrases = count_common_phrases(phrases)
  assert_equal(common_phrases[0], ('i like dogs', 4))
  assert_equal(common_phrases[1], ('sushi is tasty', 2))

def test_count_common_phrases_from_file():
  file = ['origin_of_species.txt']
  large_file = get_words_from_files(file)
  cleaned_list =  clean_word_list(large_file)
  phrase = count_common_phrases(cleaned_list)
  assert_equal(phrase[0], ('of the same', 320))
  assert_equal(phrase[1], ('the same species', 130))
  assert_equal(phrase[2], ('conditions of life', 125))
  assert_equal(phrase[3], ('in the same', 117))

