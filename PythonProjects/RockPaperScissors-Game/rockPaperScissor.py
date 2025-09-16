import random

choices = ('r', 'p', 's')
emojis = {
  "r": "⬛",
  "p":"📄",
  "s": "✂"
}

computer_choice = random.choice(choices)



while True:
  user_choice = input("Enter your choice (r/p/s): ").lower()
  if user_choice not in choices:
    print("Invalid choice!")
    continue
  
  print(f"Your chose {emojis[user_choice]}")
  print(f"Computer choice: {emojis[computer_choice]}")

  if computer_choice == user_choice:
    print("Tie!")

  elif ((user_choice == "r" and computer_choice == "s") or 
        (user_choice == "s" and computer_choice == "p") or
        (user_choice == "p" and computer_choice == "r")):
    print("Win!")
  else:
    print("Lose!")


  should_continue = input("Continue? (y/n) :").lower()
  if should_continue == "n":
    break