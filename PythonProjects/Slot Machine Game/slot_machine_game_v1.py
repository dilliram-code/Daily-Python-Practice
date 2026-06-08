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

# logic to display reels
def display_reels(reels):
  print(f'{reels[0]} | {reels[1]} | {reels[2]}')

# logic to calculate pay
def calculate_pay(reels, bet):
  if reels[0] == reels[1] == reels[3]:
    return bet * 10
  if reels[0] == reels[1] or reels[1]==reels[2] or reels[0]==reels[2]:
    return bet * 2
  return 0

def main():
  balance = get_starting_balance()

  print('Welcome you in slot machine game!')
  print(f'start playing with the balance {balance}. \n')


  while balance > 0:
    print(f'Your current balance is $ {balance}.')
    
    # get the bet amount
    bet = get_bet_amount(balance)
    reels = spin_reels()
    display_reels(reels)
    payout = calculate_pay(reels, bet)
    
    if payout > 0:
      print(f'You won ${payout}!')
    else:
      print('You lost!')

    balance += payout - bet 
    if balance <= 0:
      print('You are out of money. Game over!')
      break 
    
    play_again = input('Do you want to play again? (y/n): ').lower()
    if play_again != 'y':
      print(f'You walk away with $ {balance}.')
      break 




if __name__ == "__main__":
  main()