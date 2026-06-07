'''Game Flow'''
# Ask the user for the starting balance
# Validate the balance
#   Positive number
# Loop (while balance>0)
#   print the current balance
#   Ask the user to bet
#   Validate the bet
#     bet > 0
#     bet > balance
#   Spin reels
#     generate three random symbols
#   Display the reels
#   Calculate the payout
#     If three symbols match, payout = bet x 10
#     If two symbols match, payout = bet x 2
#     Else, payout = 0
#   Recalculate the balance
#     balance += balance + payout - bet
#   If balance < 0
#       print message
#       break
#   Else
#       ask the user if they want to playing continue
#       If not
#             break out of the loop
import random
def get_starting_balance():
  while True:
    try:
      balance = int(input("Enter starting balance: $"))
      if balance <= 0:
        print("Balance must be a positive number.")
      else:
        return balance
    except ValueError:
      print("Please enter a valid number.")
  
def get_bet_amount(balance):
  while True: 
      try: 
        bet = int(input('Enter your bet amount: \n'))
        if bet > balance or bet <= 0:
          print(f"Invalid bet amount. You can bet between $1 and ${balance}")
        else:
          return bet
      except ValueError:
        print('Please enter a valid number for bet amount.')

# ===========================SPIN WHEELS========================= #
def spin_reels():
  symbols = ['🍒', '🍋', '🔔', '⭐️', '🍉']
  
  # reels = []
  # for _ in range(3):
  #   reels.append(random.choice(symbols))
  # return reels
  
  # [expression for item in iterable]
  return [random.choice(symbols) for _ in symbols]


def main():
  balance = get_starting_balance()

  print('Welcome you in slot machine game!')
  print(f'start playing with the balance {balance}. \n')


  while balance > 0:
    print(f'Your current balance is $ {balance}.')
    
    # get the bet amount
    bet = get_bet_amount(balance)
    reels = spin_reels()





if __name__ == "__main__":
  main()