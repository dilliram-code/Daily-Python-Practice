import random

randomNumber = random.randint(1,100)


while True:
  
  try:
    guess = int(input("Guess a number between 1 and 100 :"))
    if guess > randomNumber:
      print("Too high!")
    elif guess < randomNumber:
      print("Too low!")
    else:
      print("Congratulatins!")
      break
  except ValueError:
    print("Invalid input!")