import random

name = input("What is your name? ")
print("Welcome, ", name,'!')

words = ['python', 'programming', 'coding', 'javascript', 'learning', 'achievement']

word = random.choice(words)
# print(word)

right = []
wrong = []

while True:
  print("=====================================================")
  guess = input("Guess the letter: ").lower()

  if guess in word:
    right.append(guess)
    print("Right letter: ", right)
  else:
    wrong.append(guess)
    print("Wrong letter: ", guess)