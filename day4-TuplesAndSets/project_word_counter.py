'''-----------------PROJECT: UNIQUE WORD COUNTER----------------'''

paragraph = input("Write a paragraph: ")
def word_counter(text):
  sentence = text
  words = sentence.lower().split()
  word_set = set(words)                   # removes duplicates
  words_number = len(word_set)            # length of the set: words number
  return words_number

result = word_counter(paragraph)
print(result)