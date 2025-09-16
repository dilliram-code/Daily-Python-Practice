import random

while True:
  choice = input("Rolling a dice! (y/n) :").lower()
  if choice == 'y':
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    print(f"({die1}, {die2})")
    
  elif choice == 'n':
    print("Thank you!")
    break
  else:
    print("Invalid choice!")
    
    
    
# Optional enhancemnet
'''
- Modify the program so the user can specify how many dice they want to roll
- Add a feature that keeps track of how many times the user has rolled the dice during session.
'''